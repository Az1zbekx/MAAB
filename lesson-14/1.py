import numpy as np

def f_to_c(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
f_to_c_vec = np.vectorize(f_to_c)
temps_c = f_to_c_vec(temps_f)

print("Celsius:", temps_c)
