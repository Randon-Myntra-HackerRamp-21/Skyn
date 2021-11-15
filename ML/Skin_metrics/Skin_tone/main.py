from skin_detection import skin_detection
from skin_tone import skin_tone
from skin_tone_knn import skin_tone_knn
import numpy as np

image_dir = "public\\test images\\brendon_urie_3.jpeg"
mean_color_values = skin_detection(image_dir)

# B = img_final.reshape([-1, 3])[:, 0]
# G = img_final.reshape([-1, 3])[:, 1]
# R = img_final.reshape([-1, 3])[:, 2]
# mean_color_values = []
# mean_color_values.append(np.bincount(R[R[:] != 0]).argmax())
# mean_color_values.append(np.bincount(G[G[:] != 0]).argmax())
# mean_color_values.append(np.bincount(B[B[:] != 0]).argmax())

# print(R[R[:] != 0])
# print(mean_color_values)

skin_tone = skin_tone(mean_color_values)
skin_tone_knn = skin_tone_knn(mean_color_values)

print(skin_tone)
print(skin_tone_knn)
