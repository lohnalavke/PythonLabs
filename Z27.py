print((5-1)%3+1)

import numpy as np

sizes = [10,30,200]
mu = 1.0
sigma = 0.5

for n in sizes:
    vector = np.random.normal(mu, sigma, n)
    print(f"Вектор из {n} значений (mu = {mu}, sigma = {sigma})")
    print(vector)
