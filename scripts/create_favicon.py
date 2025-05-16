"""
Simple script to generate a placeholder favicon.
Run this once to create a favicon for the Chainlit app.
"""
import os
from PIL import Image, ImageDraw

def create_favicon():
    """Create a simple favicon for the app."""
    # Create a simple colored image
    img = Image.new('RGB', (32, 32), color=(79, 70, 229))
    
    # Add a simple design
    draw = ImageDraw.Draw(img)
    draw.rectangle([8, 8, 24, 24], fill=(255, 255, 255))
    draw.rectangle([12, 12, 20, 20], fill=(79, 70, 229))
    
    # Ensure directory exists
    os.makedirs('app/static', exist_ok=True)
    
    # Save the image
    img.save('app/static/favicon.ico')
    print("Favicon created at app/static/favicon.ico")

if __name__ == "__main__":
    create_favicon()
