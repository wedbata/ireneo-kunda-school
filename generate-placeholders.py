#!/usr/bin/env python3
"""
Generate placeholder images for Ireneo Kunda Complex Gallery
This creates professional-looking placeholder images with colors and text
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Create directories
os.makedirs('images/logo', exist_ok=True)
os.makedirs('images/gallery', exist_ok=True)

print("\n" + "="*70)
print("🎨 CREATING PLACEHOLDER IMAGES FOR GALLERY")
print("="*70 + "\n")

# Color scheme
colors = {
    'campus': '#2d8a5e',      # Green
    'classroom': '#4f46e5',    # Blue
    'activities': '#ff8c42',   # Orange
    'events': '#ec4899',       # Pink
    'sports': '#f59e0b'        # Amber
}

# Gallery items to create
gallery_items = [
    ('campus-building.jpg', 'campus', 'School Building'),
    ('campus-assembly.jpg', 'campus', 'School Assembly'),
    ('life-classroom.jpg', 'classroom', 'Classroom Learning'),
    ('students-group-1.jpg', 'activities', 'Student Activities'),
    ('students-group-2.jpg', 'activities', 'Group Learning'),
    ('hero-students.jpg', 'events', 'Student Achievements'),
    ('leader-portrait.jpg', 'events', 'School Leadership'),
    ('life-sports.jpg', 'sports', 'Sports Activities'),
]

# Create placeholder images
for filename, category, title in gallery_items:
    # Create image with category color
    img = Image.new('RGB', (800, 600), color=colors[category])
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fall back to default
    try:
        font_large = ImageFont.truetype("arial.ttf", 56)
        font_small = ImageFont.truetype("arial.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw title
    draw.text((50, 250), title, fill='white', font=font_large)

    # Draw category label
    draw.text((50, 520), f"Category: {category.upper()}", fill='white', font=font_small)

    # Save image
    path = f'images/gallery/{filename}'
    img.save(path, 'JPEG', quality=90)
    print(f"✓ Created {filename}")

print("\n✓ Creating logo placeholder...\n")

# Create logo
logo_img = Image.new('RGB', (300, 100), color='#2d8a5e')
logo_draw = ImageDraw.Draw(logo_img)

try:
    logo_font = ImageFont.truetype("arial.ttf", 48)
except:
    logo_font = ImageFont.load_default()

logo_draw.text((20, 20), 'IKC', fill='white', font=logo_font)
logo_path = 'images/logo/logo.png'
logo_img.save(logo_path, 'PNG')

print(f"✓ Created logo.png")

print("\n" + "="*70)
print("✅ SETUP COMPLETE!")
print("="*70 + "\n")

print("📊 Created:")
print(f"   • 1 Logo (logo.png)")
print(f"   • 8 Gallery Images")
print(f"   • Total: 9 assets\n")

print("📁 Locations:")
print(f"   • Logo: images/logo/logo.png")
print(f"   • Gallery: images/gallery/\n")

print("🎉 Your website is ready!")
print("   Open it in a browser to see the gallery and logo.\n")
print("="*70 + "\n")
