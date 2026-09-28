#!/usr/bin/env python3
"""
Generate placeholder images for the gallery
Run this script to create sample images for testing
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images/gallery', exist_ok=True)

# Define gallery categories with colors
categories = {
    'campus': '#2d8a5e',      # Green
    'classroom': '#4f46e5',    # Blue
    'activities': '#ff8c42',   # Orange
    'events': '#ec4899',       # Pink
    'sports': '#f59e0b'        # Amber
}

# Create 12 sample images (matching the gallery.json)
images_to_create = [
    ('campus-1.jpg', 'campus', 'School Main Building'),
    ('classroom-1.jpg', 'classroom', 'Primary Classroom'),
    ('classroom-2.jpg', 'classroom', 'Science Laboratory'),
    ('activities-1.jpg', 'activities', 'Art Class'),
    ('activities-2.jpg', 'activities', 'Music Class'),
    ('events-1.jpg', 'events', 'Graduation Ceremony'),
    ('events-2.jpg', 'events', 'Cultural Day'),
    ('sports-1.jpg', 'sports', 'Football Match'),
    ('sports-2.jpg', 'sports', 'Athletics Day'),
    ('campus-2.jpg', 'campus', 'School Library'),
    ('campus-3.jpg', 'campus', 'Computer Lab'),
    ('activities-3.jpg', 'activities', 'Drama Performance'),
]

print("🎨 Creating gallery placeholder images...")

for filename, category, title in images_to_create:
    # Create image
    img = Image.new('RGB', (800, 600), color=categories[category])
    draw = ImageDraw.Draw(img)

    # Add text to image
    try:
        font = ImageFont.truetype("arial.ttf", 48)
        small_font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Draw title
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (800 - text_width) // 2
    draw.text((text_x, 200), title, fill='white', font=font)

    # Draw category
    draw.text((50, 500), f"Category: {category.upper()}", fill='white', font=small_font)

    # Save image
    path = f'images/gallery/{filename}'
    img.save(path, 'JPEG', quality=95)
    print(f"✓ Created {filename}")

print("\n✅ Gallery placeholder images created successfully!")
print(f"📁 Location: images/gallery/")
print(f"📊 Total images: {len(images_to_create)}")
print("\n💡 Now open your gallery page to see the images!")
