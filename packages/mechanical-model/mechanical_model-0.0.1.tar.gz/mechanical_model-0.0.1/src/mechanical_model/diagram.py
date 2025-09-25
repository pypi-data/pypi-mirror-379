from abc import ABC, abstractmethod

class Diagram(ABC):
    """A diagram of one or more components in series or in parallel"""
    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def width(self):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    def __add__(self, other):
        """self and other in series"""
        return SeriesDiagram(self, other)

    def __mul__(self, other):
        """self and other in parallel"""
        return ParallelDiagram(self, other)

class DiagramLeaf(Diagram):
    """A single component in the diagram"""

    def __init__(self, s):
        """Initialize from a string that draws a component.
        The connecting wires must be on the second to last line"""
        lines_lengths =  list(map(len, s.splitlines()))
        maxl = max(lines_lengths)
        assert lines_lengths[-2] == maxl, """connection must be the longest line"""
        #add spaces on the right so that each line have the same length
        self.lines = [
            line.ljust(maxl)
            for line in s.splitlines()
        ]

    def __str__(self):
        return "\n".join(self.lines)

    @property
    def width(self):
        return len(self.lines[0])

    @property
    def height(self):
        return len(self.lines)

class Spring(DiagramLeaf):
    """A spring of modulus G."""
    def __init__(self, G='G'):
        DiagramLeaf.__init__(self, f"""

____╱╲  ╱╲  ╱╲  ___{'_'*len(G)}
      ╲╱  ╲╱  ╲╱ {G}
""")

class Dashpot(DiagramLeaf):
    """A dashpot of viscosity eta."""
    def __init__(self, eta='η'):
        DiagramLeaf.__init__(self, f"""
    ___
_____| |____{'_'*len(eta)}
    _|_| {eta}
""")

class Springpot(DiagramLeaf):
    """A springpot of exponent alpha and quasiproperty V."""
    def __init__(self, V='V', alpha='α'):
        DiagramLeaf.__init__(self, f"""

____╱╲____{'_'*(len(V)+len(alpha))}
    ╲╱ {V}, {alpha}
""")

class SeriesDiagram(Diagram):
    """Two or more elements in series"""
    def __init__(self, *args):
        assert(len(args)>1), f"Only {len(args)} elements were provided."
        self.children = []
        for child in args:
            if isinstance(child, SeriesDiagram):
                self.children += child.children
            else:
                self.children.append(child)
    @property
    def width(self):
        return sum(child.width for child in self.children)

    @property
    def height(self):
        return max(child.height for child in self.children)

    def __str__(self):
        ret = ['' for l in range(self.height)]
        for child in self.children:
            for l, line in enumerate(f'{child}'.splitlines()[::-1]):
                ret[len(ret)-l-1] += line
            for l in range(len(ret)-child.height):
                ret[l] += ' '*child.width
        return "\n".join(ret)

class ParallelDiagram(Diagram):
    """Two or more elements in parallel"""
    def __init__(self, *args):
        assert(len(args)>1), f"Only {len(args)} elements were provided."
        self.children = []
        for child in args:
            if isinstance(child, ParallelDiagram):
                self.children += child.children
            else:
                self.children.append(child)
    @property
    def width(self):
        return max(child.width for child in self.children)+8

    @property
    def height(self):
        return sum(child.height for child in self.children)

    def __str__(self):
        maxL = self.width-8
        ret = []
        lines = f'{self.children[0]}'.splitlines()
        for line in lines[:-2]:
            ret.append(line.center(maxL+8))
        ret.append(' '*4 + lines[-2].center(maxL, '_')+' '*4)
        ret.append('   |'+lines[-1].center(maxL)+'|   ')
        for child in self.children[1:-1]:
            lines = f'{self.child}'.splitlines()
            for line in lines[:-2]:
                ret.append('   |'+line.center(maxL)+'|   ')
            ret.append('   |'+lines[-2].center(maxL, '_')+'|   ')
            ret.append('   |'+lines[-1].center(maxL)+'|   ')
        lines = f'{self.children[-1]}'.splitlines()
        for line in lines[:-2]:
            ret.append('   |'+line.center(maxL)+'|   ')
        ret.append('___|'+lines[-2].center(maxL, '_')+'|___')
        ret.append(lines[-1].center(maxL+8))
        return '\n'.join(ret)
