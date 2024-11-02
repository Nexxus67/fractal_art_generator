import numpy as np
from PIL import Image
from cryptography.fernet import Fernet

def extract_message_from_image(image_path, message_length):
    image = Image.open(image_path)
    image_data = np.array(image)
    binary_message = ""
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            pixel = image_data[i, j]
            for k in range(3):
                binary_message += str(pixel[k] & 1)
                if len(binary_message) >= message_length * 8:
                    break
            if len(binary_message) >= message_length * 8:
                break
    message_bytes = [int(binary_message[i:i + 8], 2) for i in range(0, len(binary_message), 8)]
    return bytes(message_bytes)

with open("clave.key", "rb") as f:
    key = f.read()
cipher = Fernet(key)

encrypted_message = extract_message_from_image("imagen_esteganografica.png", message_length=len(open("mensaje_cifrado.bin", "rb").read()))
decrypted_message = cipher.decrypt(encrypted_message).decode()
print("Mensaje recuperado:", decrypted_message)

