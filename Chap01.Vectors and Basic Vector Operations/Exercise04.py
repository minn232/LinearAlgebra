import numpy as np

v = np.array(list(map(float, input().split())))
vector_norm = int(input())

# 동일 방향의 단위 벡터
v /= np.linalg.norm(v)


v *= vector_norm

print(v)