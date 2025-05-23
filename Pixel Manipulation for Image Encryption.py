from PIL import Image

def encrypt_image(input_path, output_path):
    image = Image.open(input_path)
    encrypted = Image.new("RGB", image.size)
    
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            encrypted.putpixel((x, y), (255 - r, 255 - g, 255 - b))  # Invert each channel

    encrypted.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path):
    
    encrypt_image(input_path, output_path)
    print(f"Decrypted image saved to {output_path}")


encrypt_image("original_image.jpg", "encrypted_image.png")
decrypt_image("encrypted_image.png", "decrypted_image.png")
