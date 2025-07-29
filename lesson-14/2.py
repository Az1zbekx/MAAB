def custom_pow(x, y):
    return x ** y

a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
pow_vec = np.vectorize(custom_pow)
result = pow_vec(a, b)

print("Power Result:", result)
