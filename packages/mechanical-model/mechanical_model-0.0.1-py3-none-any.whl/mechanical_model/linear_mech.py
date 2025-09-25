from abc import ABC, abstractmethod
import numpy as np
from scipy import constants as const
from scipy.special import gamma
import mpmath

from .diagram import Spring, Dashpot, Springpot

class LinearMechanicalModel(ABC):
    diagram = """No implemented diagram"""
    @abstractmethod
    def Laplace_G(self, s):
        """The modulus in the Laplace domain.

        In principle, only this method needs to be implemented as all other
        methods can be derived from the results of this one. However in practice,
        analytical simplified expressions of the other methods will be more
        efficient, in particular J(t) that implies inverse Laplace transform
        that is slow numerically."""
        pass

    @abstractmethod
    def __str__(self):
        pass

    def Gp(self, ω):
        """Elastic modulus function of pulsation ω"""
        return np.real(self.Laplace_G(1j * ω))

    def Gpp(self, ω):
        """Viscous modulus function of pulsation ω"""
        return np.imag(self.Laplace_G(1j * ω))

    def tandelta(self, ω):
        """Loss tangent function of pulsation ω"""
        G = self.Laplace_G(1j * ω)
        return np.imag(G) / np.real(G)

    def J(self, t):
        """Creep compilance function of time"""
        Laplace_J = lambda s: 1/s/self.self.Laplace_G(s)
        return np.array([
            mpmath.invertlaplace(Laplace_J, x)
            for x in t], float)

    def msd(self, t, T, a, d=3):
        """Mean square displacement function of time of a particle of radius a (m) immersed in the
        medium at temperature T (°C). Dimensionality is d."""
        return d*const.Boltzmann * const.convert_temperature(T, 'C', 'K') /(3*np.pi*a) * self.J(t)


class Elastic(LinearMechanicalModel):
    """Elastic solid of constant elasticity G (Pa)"""

    diagram = Spring('G')

    def __init__(self, G):
        self.G = G

    def __str__(self):
        return f"Elastic G={self.G:3.2f} Pa"

    def Laplace_G(self, s):
        return np.full_like(s, self.G)

    def Gp(self, ω):
        return np.full_like(ω, self.G)

    def Gpp(self, ω):
        return np.zeros_like(ω)

    def tandelta(self, ω):
        return np.zeros_like(ω)

    def J(self, t):
        return np.full_like(t, 1/self.G)


class Newtonian(LinearMechanicalModel):
    """Newtonian fluid of constant viscosity η (Pa.s)"""

    diagram = Dashpot('η')

    def __init__(self, η):
        self.η = η

    def __str__(self):
        return f"Viscous η={self.η:3.2f} Pa.s"

    def Laplace_G(self, s):
        return s * self.η

    def Gp(self, ω):
        return np.zeros_like(ω)

    def Gpp(self, ω):
        return ω * self.η

    def tandelta(self, ω):
        return np.full_like(ω, np.inf)

    def J(self, t):
        return t/self.η

class Maxwell(LinearMechanicalModel):
    """Maxwell model of an elasticity G (Pa) in series with a viscosity η (Pa.s). The characteristic time is τ (s)"""

    diagram = Spring('G') + Dashpot('η')

    def __init__(self, G=None, eta=None, tau=None):
        assert G is None or eta is None or tau is None, "G, η and τ are not independent. All three cannot be set."
        if G is not None:
            self.G = G
            if eta is not None:
                self.η = eta
                self.τ = eta / G
            elif tau is not None:
                self.τ = tau
                self.η = G * tau
            else:
                raise KeyError("Either η or τ must be defined")
        elif eta is not None and tau is not None:
            self.η = eta
            self.τ = tau
            self.G = eta / tau
        else:
            raise KeyError("Two among G, η or τ must be defined")

    def __str__(self):
        return f"Maxwell G={self.G:3.2f} Pa, η={self.η:3.2f} Pa.s, τ={self.τ:3.2f} s"

    def Laplace_G(self, s):
        return s * self.η / (1 + s*self.τ)

    def Gp(self, ω):
        return self.G * (
            self.τ**2 * ω**2
        )/(
            1 + self.τ**2 * ω**2
        )

    def Gpp(self, ω):
        return self.G * (
            self.τ * ω
        )/(
            1 + self.τ**2 * ω**2
        )

    def tandelta(self, ω):
        return 1/(self.τ * ω)

    def J(self, t):
        return 1/self.G + t/self.η

class KelvinVoigt(LinearMechanicalModel):
    """Kelvin-Voigt model of an elasticity G (Pa) in parallel to a viscosity η (Pa.s). The characteristic time is τ (s)"""

    diagram = Spring('G') * Dashpot('η')

    def __init__(self, G=None, eta=None, tau=None):
        assert G is None or eta is None or tau is None, "G, η and τ are not independent. All three cannot be set."
        if G is not None:
            self.G = G
            if eta is not None:
                self.η = eta
                self.τ = eta / G
            elif tau is not None:
                self.τ = tau
                self.η = G * tau
            else:
                raise KeyError("Either η or τ must be defined")
        elif eta is not None and tau is not None:
            self.η = eta
            self.τ = tau
            self.G = eta / tau
        else:
            raise KeyError("Two among G, η or τ must be defined")

    def __str__(self):
        return f"Kelvin-Voigt G={self.G:3.2f} Pa, η={self.η:3.2f} Pa.s, τ={self.τ:3.2f} s"

    def Laplace_G(self, s):
        return self.G + s * self.η

    def Gp(self, ω):
        return np.full_like(ω, self.G)

    def Gpp(self, ω):
        return ω * self.η

    def tandelta(self, ω):
        return self.η * ω / self.G

    def J(self, t):
        return (1 - np.exp(-t/self.τ)) / self.G

class JohnsonSegalman(Maxwell):
    """Johnson-Segalman model of a viscosity ηs (Pa.s) in parallel to a Maxwell of elasticity G (Pa) and viscosity η (Pa.s)."""

    diagram = Dashpot('ηs') * Maxwell.diagram

    def __init__(self, G, eta, eta_s):
            self.G = G
            self.η = eta
            self.ηs = eta_s

    def __str__(self):
        return f"Johnson-Segalman G={self.G:3.2f} Pa, η={self.η:3.2f} Pa.s, ηs={self.ηs:3.2f} Pa.s"

    def Laplace_G(self, s):
        return Maxwell.Laplace_G(self, s) + ω * self.ηs

    def Gpp(self, ω):
        return Maxwell.Gpp(self, ω) + ω * self.ηs

    def tandelta(self, ω):
        return Maxwell.tandelta(self, ω) + self.η * ω / Maxwell.Gpp(self, ω)

    def J(self, t):
        return t/(self.η + self.ηs) + 1/self.G * (self.η/(self.η + self.ηs))**2 * (1 - np.exp(-self.G * (1/self.η + 1/self.ηs)*t))

class PowerLaw(LinearMechanicalModel):
    """A springpot element of exponent α and pseudo-property V (Pa.s^α)"""

    diagram = Springpot('V', 'α')

    def __init__(self, V, alpha):
            self.V = V
            self.α = alpha

    def __str__(self):
        return f"power law V={self.V:3.2f} Pa.s^{self.α:.3f}"

    def Laplace_G(self, s):
        return self.V * s ** self.α

    def Gp(self, ω):
        return self.V * np.cos(π * self.α / 2) * ω**self.α

    def Gpp(self, ω):
        return self.V * np.sin(π * self.α / 2) * ω**self.α

    def tandelta(self, ω):
        return np.tan(π * self.α / 2)

    def J(self, t):
        return t**self.α / (self.V * gamma(1 + self.α))

class FractionalMaxwell(LinearMechanicalModel):
    """Two springpot elements in series of respective exponent α and β and
    respective pseudo-property V (Pa.s^α) and G (Pa.s^β)"""

    diagram = Springpot('V', 'α') + Springpot('G', 'β')

    def __init__(self, alpha, beta, V=None, G=None, tau=None):
        assert G is None or V is None or tau is None, "G, V and τ are not independent. All three cannot be set."
        self.α = alpha
        α = alpha
        self.β = beta
        β = beta
        if tau is not None:
            self.τ = tau
            if G is not None and V is None:
                self.G = G
                self.V = G * (np.sin(π*α/2) - np.cos(π*α/2)) / (np.cos(π*β/2) - np.sin(π*β/2)) * tau**(α-β)
            elif V is not None and G is None:
                self.V = V
                self.G = V * (np.cos(π*β/2) - np.sin(π*β/2)) / (np.sin(π*α/2) - np.cos(π*α/2)) * tau**(β-α)
            else:
                raise KeyError("Either V or G must be defined if τ is defined, but not both.")
        else:
            self.G = G
            self.V = V
            self.τ = (V/G * (np.cos(π*β/2) - np.sin(π*β/2)) / (np.sin(π*α/2) - np.cos(π*α/2)))**(1/(α-β))

    def __str__(self):
        return f"fractional Maxwell V={self.V:3.2f} Pa.s^{self.α:.3f}, G={self.V:3.2f} Pa.s^{self.β:.3f}"

    def Laplace_G(self, s):
        return self.V * self.G * s**(self.α + self.β) /(self.V * s**self.α + self.G * s**self.β)

    def Gp(self, ω):
        Go = G*ω**β
        Vo = V*ω**α
        return (
            Go**2 * Vo * np.cos(π * self.α/2) + Vo**2 * Go * np.cos(π * self.β/2)
        )/(
            Vo**2 + Go**2 + 2*Vo*Go*np.cos(π*(self.α-self.β)/2)
        )

    def Gpp(self, ω):
        Go = G*ω**β
        Vo = V*ω**α
        return (
            Go**2 * Vo * np.sin(π * self.α/2) + Vo**2 * Go * np.sin(π * self.β/2)
        )/(
            Vo**2 + Go**2 + 2*Vo*Go*np.cos(π*(self.α-self.β)/2)
        )

    def tandelta(self, ω):
        Go = G*ω**β
        Vo = V*ω**α
        return (
            Go * np.sin(π * self.α/2) + Vo * np.sin(π * self.β/2)
        )/(
            Go * np.cos(π * self.α/2) + Vo * np.cos(π * self.β/2)
        )

    def J(self, t):
        return t**self.α / (self.V*gamma(1+self.α)) + t**self.β/(self.G * gamma(1+self.β))
