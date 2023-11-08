import numpy as np

def nest(c, x):
    n = len(c) - 1
    result = c[n]
    for i in range(n - 1, -1, -1):
        result = result * x + c[i]
    return result

def test_feil(funk):
    c = np.ones(51)
    x = 1.00001
    Px = (x**51 - 1) / (x - 1)  # Ekvivalent uttrykk for polynom fra oppgavetekst, evaluert i x=1.00001
    error = abs(Px - funk(c, x))
    return error

# Test funksjonen test_feil med nest-funksjonen
test_feil(nest)

