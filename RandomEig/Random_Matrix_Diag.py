import numpy as np
import matplotlib.pyplot as plt

N = 2 # dim
reps = 100000

eigenvals = np.zeros((reps, N), dtype="complex")

for i in range(reps):
    M = 2 * np.random.random((N,N)) - 1
    #M = np.random.random((N,N))
    eigenvals[i,:] = np.linalg.eigvals(M)
    if np.abs(np.linalg.trace(M))>N:
        print(M)

data = eigenvals.flatten()
x = data.real
y = data.imag

plt.scatter(x, y, s=0.1, label="dim={}".format(N))
plt.xlabel("$Re \\lambda$")
plt.ylabel("$Im \\lambda$")
plt.legend()
plt.show()