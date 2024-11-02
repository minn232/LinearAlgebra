import numpy as np
import matplotlib.pyplot as plt

# 벡터 선언
v = np.array([1, 2])
w = np.array([4, -6])

# 벡터의 덧셈, 뺄셈
sum_vw = v + w
abstract_vw = v - w

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label = 'v')
plt.quiver(v[0], v[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='g', label = 'w')
plt.quiver(0, 0, sum_vw[0], sum_vw[1], angles='xy', scale_units='xy', scale=1, color='b', label = 'v+w')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.legend()
plt.title("v, w, v+w")

plt.subplot(1, 2, 2)
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label = 'v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='g', label = 'w')
plt.quiver(w[0], w[1], abstract_vw[0], abstract_vw[1], angles='xy', scale_units='xy', scale=1, color='b', label = 'v-w')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.legend()
plt.title("v, w, v+w")

plt.show()