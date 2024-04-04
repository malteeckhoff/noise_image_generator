from PIL import Image
import random

def create_noisy_image(base_color_hex, width, height):
    # Convert the hex color to RGB
    base_color = tuple(int(base_color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Create a new image
    image = Image.new('RGB', (width, height), base_color)
    pixels = image.load()
    
    # Introduce subtle noise
    for x in range(width):
        for y in range(height):
            # Generate a subtle variation (-2 to 2) for each color channel
            variation = tuple(random.randint(-2, 2) for _ in range(3))
            # Apply the variation and ensure values are within 0-255
            new_color = tuple(max(0, min(255, base_color[i] + variation[i])) for i in range(3))
            pixels[x, y] = new_color
    
    # Save or display the image
    image.save('noisy_image.png')

# Example usage
create_noisy_image("#ffffff", 1000, 1000)

