# Middeltemperaturer pr mnd i Skien 2005 - 2015

# Import av pakker
import numpy as np
import matplotlib.pyplot as plt

# Definisjonen av variable med tabellverdier:
mnd = np.array([1, 2, 3, 4, 5, 6, 
                7, 8, 9, 10, 11, 12]) # mnd nr
temp_C_array = np.array([-3, -2, 2, 7, 11, 15,
                17, 16, 12, 6, 2, -3]) # Grader C
temp_F_array = temp_C_array*(9/5) + 32

# Beregninger av middelverdi

mean_temp = np.mean(temp_F_array)

print("Middelverdi av alle månedstemp = ", mean_temp)

# Plotting av temperaturene:

plt.close("all")
plt.figure(1)
plt.plot(mnd, temp_F_array, "bo--", label = "temp")
plt.plot(mnd, temp_F_array*0 + mean_temp, "g", label = "middelverdi")
plt.legend()
plt.title("Midlere månedstemperatur i Skien 2005-2015")
plt.xlabel("Måned nr.")
plt.ylabel("Grader F")
plt.xlim(1, 12)
plt.grid()
plt.show()