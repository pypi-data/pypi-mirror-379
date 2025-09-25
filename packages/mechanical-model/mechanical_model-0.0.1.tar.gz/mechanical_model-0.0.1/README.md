# Mechanical models

A package to deal with mechanical models and their linear
response in oscillations, creep, microrheology, etc.

##Installation

- Clone from github
- `pip install -e .`

## Drawing diagrams in plain text

```python
from mechanical_model.diagram import Spring, Dashpot, Springpot
print(Spring() + Dashpot('ηs') * (Springpot('V', 'α') + Springpot('W', 'β')))
```

```

                                 ___                
                        __________| |___________    
                       |         _|_| ηs        |   
                       |                        |   
                       |                        |   
____╱╲  ╱╲  ╱╲  _______|____╱╲__________╱╲______|___
      ╲╱  ╲╱  ╲╱ G          ╲╱ V, α     ╲╱ W, β     
```

## Mechanical response in oscillations

```python
import numpy as np
from mechanical_model.linear_mech import Maxwell
from matplotlib import pyplot as plt

omega = np.logspace(-2,2)
fig, axs = plt.subplots(2,1, sharex=True, layout='constrained')
for m in [Maxwell(G=10, eta=1), Maxwell(G=1, tau=0.3)]:
    line, = axs[0].plot(omega, m.tandelta(omega), label=m)
    axs[1].plot(omega, m.Gp(omega), color=line.get_color())
    axs[1].plot(omega, m.Gpp(omega), ls='--', color=line.get_color())

axs[0].set_ylabel(r'$\tan\delta$')
axs[1].set_ylabel(r'$G^\prime,G^{\prime\prime}$')
axs[1].set_xlabel(r'$\omega$')
for ax in axs:
    ax.set_xscale('log')
    ax.set_yscale('log')

axs[0].legend()
```
