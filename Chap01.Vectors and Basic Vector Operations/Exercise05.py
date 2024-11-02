import numpy as np

v = np.array(list(map(int, input().split())))

v_T = list()
for idx in range(len(v)):
    v_T.append([int(v[idx])])

print(v_T)