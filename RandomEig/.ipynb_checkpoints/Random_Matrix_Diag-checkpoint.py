import numpy as np
import matplotlib.pyplot as plt

N = 50 # dim
reps = 50

eigenvals = np.zeros((reps, N), dtype="complex")

for i in range(reps):
    M = 2 * np.random.random((N,N)) - 1
    eigenvals[i,:] = np.linalg.eigvals(M)

data = eigenvals.flatten()
x = data.real
y = data.imag

print(x, y)

plt.scatter(x, y, s=0.1)
plt.xlabel("$Re \\lambda$")
plt.ylabel("$Im \\lambda$")
plt.show()