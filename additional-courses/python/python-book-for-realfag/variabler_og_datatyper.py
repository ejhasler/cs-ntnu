 # Funksjon
import numpy as np
x = 2.0
y = np.sqrt(x)

# Metode
L = [0, 1]
L.append(5)

# Formattering av tall i print()
x1 = x2 = x3 = x4 = x5 = x6 = x7 = 200/3
y2 = y4 = y6 = 100/3

print("x1 =", x1)
print("x2 = ", x2, "og y2 = ", y2)
print("x3 = ", f"{x3:.3f}")
print(f"x4 = {x4:.3f} og y4 = {y4:.1.f}")
print("x5 = %.3f" % x5)
print("x6 = %.3f og y6 = %.1f" % (x6, y6))
print(f"x7 = {x7:.2e}")

# Tekststrenger (strings)
print("1" + "2")
print("I don\'t know.")
print("Linje 1.\nLinje 2.")

# Fra tall til tekst og fra tekst til tall
vekt_float = 59.8 #Flyttall
info = "Hun veier " + str(vekt_float)  + "kg."
info

# print()-funksjonen aksepterer en miks av ulike datatyper
vekt_float = 59.8
print("Hun veier", vekt_float, "kg")

# Typekonvertering ifm. input()-funksjonen
x = float(input("Skriv inn tallet x: "))
x = 1.2
y = x + 3.4

# Logiske operatorer
A = True
B = False

C = A and B

A or B

not A

A and (not B)

# Liste
L1 = [0.1, 2.3, 4.5, 6.3]

L2 = ["null", "en", "to"]

L3 = [0.1, "en", [1.0, "to"]]
n = len(L1)

# Lese ett element i en liste
L = [0.1, 2.3, 4.5, 6.3]
L[1]

# Lese en serie av elementer i en liste
L = [0.1, 2.3, 4.5, 6.7]
L[0:2]
L[:2]

# Lese en serie av elementer til og med siste element i listen
L = [0.1, 2.3, 4.5, 6.7]
L[1:]

# Oppdatere ett element i en liste
L = [0.1, 2.3, 4.5, 6.7]
L[2] = -4.5

# Oppdatere en serie av elementer i en liste
L = [0.1, 2.3, 4.5, 6.7]
L[0:3] = [0.5, 2.5, 3.5]

# Utvidelse av liste
L = [0.1, 2.3, 4.5, 6.7]
L.extend([8.9])

# Fjerne elementer fra en liste
L = [0.1, 2.3, 4.5, 6.7]
del L[2]

# Listemanipulering med + og *
L = [10, 20, 30]
L1 = [40, 50, 60]

L + L1

L = [10, 20, 30]
L*3

# Dictionary
D = {} # Lager ett tomt dictionary
D["Lag"] = "Odd" # Legger til et dictionary-element
D["Poeng"] = 100 # Legger til enda et element

# Kovertering av liste til array
L = [0.1, 2.3, 4.5, 6.7]
A = np.array(L)

# Konvertering av liste til array
A = np.array([0.1, 2.3, 4.5, 6.7])
L = list(A)

# Array med fast inkrement mellom elemente
t_start = 0.0
t_stopp = 1.0
Ts = 0.1
n = int((t_stopp - t_start)/Ts) + 1 # int() gir heltall avrundet mot 0.
t = np.linspace(t_start, t_stopp, n)

# Bruk av arrange() til å lage en array av tidspunkter med fast tidskritt
t_start = 0.0
t_stopp = 1.0
Ts = 0.1
t = np.arrange(t_start, t_stopp, Ts)
n = len(t)

# Matrise (2D-array)
A = np.array([[0, 10, 20], [30, 40, 50]])

# Størrelsen av en array

b = np.array([1, 2, 3, 4])
n = len(b)

# Dimensjoner av et 2D-array, dvs. en matrise
A = ([1,2], [3, 4], [5, 6])
(m, n) = A.shape

# Skalarprodukt
a = np.array([[0, 1, 2]])
b = np.array([[3, 4, 5]])
p = a @ b.T

# Multiplikasjon av matrise og vektor
M = np.array([1, 0], [0, 2])
v = np.array([[3, 4]])
p = M @ v

# Et par eksempler på matrisefunksjoner i lineæralgebra
M = np.array([[1, 0], [0, 2]])
det_M = np.linalg.det(M)

x = np.array([0, 10, 20, 30, 40])
y = np.sqrt(x)

t_start = 0
t_stopp = 5.0
Ts = 1.0
n = int((t_stopp - t_start)/Ts + 1)
g = 9.81
t = np.linspace(t_start, t_stopp, n)
s = (1/2)*g*t*t