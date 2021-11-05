from skin_detection import skin_detection
from skin_tone import skin_tone
from skin_tone_knn import skin_tone_knn

image_dir = "public\\test images\Optimized-20191221_123814.jpg"
mean_color_values = skin_detection(image_dir)
skin_tone = skin_tone(mean_color_values)
skin_tone_knn = skin_tone_knn(mean_color_values)

print(skin_tone)
print(skin_tone_knn)