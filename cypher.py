from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
message = "soy un mensaje cifrado".encode()
encrypted_message = cipher.encrypt(message)

with open("mensaje_cifrado.bin", "wb") as f:
    f.write(encrypted_message)
with open("clave.key", "wb") as f:
    f.write(key)

print("Mensaje cifrado y guardado en 'mensaje_cifrado.bin'")
print("Clave de cifrado guardada en 'clave.key'")

