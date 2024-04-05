from PIL import Image
import random
import argparse

def create_noisy_image(base_color_hex, width, height, variation_range):
    # Convert the hex color to RGB
    base_color = tuple(int(base_color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Create a new image
    image = Image.new('RGB', (width, height), base_color)
    pixels = image.load()
    
    # Introduce subtle noise
    for x in range(width):
        for y in range(height):
            # Generate a subtle variation (-variation_range to variation_range) for each color channel
            variation = tuple(random.randint(-variation_range, variation_range) for _ in range(3))
            # Apply the variation and ensure values are within 0-255
            new_color = tuple(max(0, min(255, base_color[i] + variation[i])) for i in range(3))
            pixels[x, y] = new_color
    
    # Save or display the image
    image.save('noisy_image.png')

parser = argparse.ArgumentParser(description='Generate a noisy image.')
parser.add_argument('--base_color', type=str, default='#ffffff', help='Base color in hex format (default: #ffffff)')
parser.add_argument('--width', type=int, default=1000, help='Width of the image (default: 1000)')
parser.add_argument('--height', type=int, default=1000, help='Height of the image (default: 1000)')
parser.add_argument('--variation', type=int, default=2, help='Variation for each color channel (default: 2)')

args = parser.parse_args()

create_noisy_image(base_color_hex=args.base_color, width=args.width, height=args.height, variation_range=args.variation)
