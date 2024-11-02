import numpy as np

v = np.random.randint(-100, 100, size = (2, 1))
v_norm = np.sqrt(np.sum(v ** 2))
print(f'my_norm( v({v[0][0]}, {v[1][0]}) ) = {v_norm:.2f}')
print(f'np.linalg.norm( v ) = {np.linalg.norm(v):.2f}')