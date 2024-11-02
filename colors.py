import cv2
import numpy as np
from PIL import Image

def apply_psychedelic_colors(image_path):
    image = Image.open(image_path).convert("L")
    image = np.array(image)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    hsv_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
    hsv_image[..., 0] = (hsv_image[..., 0] + 50) % 180  # Ajuste de tono
    hsv_image[..., 1] = 255  # Saturación máxima
    colored_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    Image.fromarray(colored_image).save("fractal_psicodelico.png")
    print("Imagen psicodélica guardada como 'fractal_psicodelico.png'")

apply_psychedelic_colors("fractal_base.png")
apply_psychedelic_colors("fractal_burning_ship.png")

