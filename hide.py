import numpy as np
from PIL import Image

def hide_message_in_image(image_path, message_path, output_path):
    with open(message_path, "rb") as f:
        encrypted_message = f.read()

    image = Image.open(image_path)
    image_data = np.array(image)
    binary_message = ''.join(format(byte, '08b') for byte in encrypted_message)
    message_index = 0
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            pixel = list(image_data[i, j])
            for k in range(3):
                if message_index < len(binary_message):
                    pixel[k] = (pixel[k] & 0b11111110) | int(binary_message[message_index])
                    message_index += 1
            image_data[i, j] = tuple(pixel)
            if message_index >= len(binary_message):
                break
    Image.fromarray(image_data).save(output_path)
    print(f"Mensaje oculto en la imagen guardada como '{output_path}'")

hide_message_in_image("fractal_psicodelico.png", "mensaje_cifrado.bin", "imagen_esteganografica.png")

