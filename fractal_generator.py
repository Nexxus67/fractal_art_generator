import numpy as np
from PIL import Image
import random

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    fractal = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            x = x_min + (x_max - x_min) * i / width
            y = y_min + (y_max - y_min) * j / height
            zx, zy = x, y
            iteration = 0
            while zx * zx + zy * zy < 4 and iteration < max_iter:
                xtemp = zx * zx - zy * zy + x
                zy, zx = 2 * zx * zy + y, xtemp
                iteration += 1
            fractal[j, i] = iteration
    return fractal

def julia(width, height, x_min, x_max, y_min, y_max, max_iter, c_x, c_y):
    fractal = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            zx = x_min + (x_max - x_min) * i / width
            zy = y_min + (y_max - y_min) * j / height
            iteration = 0
            while zx * zx + zy * zy < 4 and iteration < max_iter:
                xtemp = zx * zx - zy * zy + c_x
                zy, zx = 2 * zx * zy + c_y, xtemp
                iteration += 1
            fractal[j, i] = iteration
    return fractal

def burning_ship(width, height, x_min, x_max, y_min, y_max, max_iter):
    fractal = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            x = x_min + (x_max - x_min) * i / width
            y = y_min + (y_max - y_min) * j / height
            zx, zy = x, y
            iteration = 0
            while zx * zx + zy * zy < 4 and iteration < max_iter:
                xtemp = abs(zx * zx - zy * zy + x)
                zy, zx = abs(2 * zx * zy + y), xtemp
                iteration += 1
            fractal[j, i] = iteration
    return fractal

def generate_fractal_choice():
    print("Seleccione el tipo de fractal a generar:")
    print("1: Mandelbrot")
    print("2: Julia")
    print("3: Burning Ship")
    
    choice = input("Ingrese el número de la opción (1/2/3): ")
    
    if choice == '1':
        fractal = mandelbrot(800, 800, -2.0, 1.0, -1.5, 1.5, 256)
        filename = "fractal_mandelbrot.png"
    elif choice == '2':
        c_x, c_y = random.uniform(-1, 1), random.uniform(-1, 1)
        fractal = julia(800, 800, -2.0, 1.0, -1.5, 1.5, 256, c_x, c_y)
        filename = "fractal_julia.png"
    elif choice == '3':
        fractal = burning_ship(800, 800, -2.0, 1.0, -1.5, 1.5, 256)
        filename = "fractal_burning_ship.png"
    else:
        print("Opción inválida, generando fractal Mandelbrot por defecto.")
        fractal = mandelbrot(800, 800, -2.0, 1.0, -1.5, 1.5, 256)
        filename = "fractal_mandelbrot.png"

    fractal_image = Image.fromarray(np.uint8(fractal * 255 / fractal.max()))
    fractal_image.save(filename)
    print(f"Imagen fractal generada y guardada como '{filename}'")

generate_fractal_choice()

