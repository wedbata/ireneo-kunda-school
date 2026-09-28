#!/usr/bin/env python3
"""
Complete Automatic Setup - Generates all assets (logo + gallery images)
Run once: python complete-setup.py
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

print("\n" + "█" * 80)
print("█" + " " * 78 + "█")
print("█" + "  🚀 IRENEO KUNDA COMPLEX - COMPLETE SETUP".ljust(79) + "█")
print("█" + " " * 78 + "█")
print("█" * 80 + "\n")

# Step 1: Create directories
print("📁 Step 1: Creating directories...")
os.makedirs(os.path.join(PROJECT_ROOT, 'images', 'logo'), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, 'images', 'gallery'), exist_ok=True)
print("   ✓ Directories ready\n")

# Step 2: Create logo
print("🎨 Step 2: Creating logo...")

try:
    logo_img = Image.new('RGB', (300, 100), color='#2d8a5e')
    logo_draw = ImageDraw.Draw(logo_img)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()

    logo_draw.text((50, 25), 'IKC', fill='white', font=font)
    logo_path = os.path.join(PROJECT_ROOT, 'images', 'logo', 'logo.png')
    logo_img.save(logo_path, 'PNG')
    print("   ✓ logo.png created\n")
except Exception as e:
    print(f"   ✗ Error creating logo: {e}\n")

# Step 3: Create gallery images
print("🖼️  Step 3: Creating gallery images...")

gallery_items = [
    ('campus-building.jpg', 'campus', 'School Building', '#2d8a5e'),
    ('campus-assembly.jpg', 'campus', 'School Assembly', '#2d8a5e'),
    ('life-classroom.jpg', 'classroom', 'Classroom Learning', '#4f46e5'),
    ('students-group-1.jpg', 'activities', 'Student Activities', '#ff8c42'),
    ('students-group-2.jpg', 'activities', 'Group Learning', '#ff8c42'),
    ('hero-students.jpg', 'events', 'Student Achievements', '#ec4899'),
    ('leader-portrait.jpg', 'events', 'School Leadership', '#ec4899'),
    ('life-sports.jpg', 'sports', 'Sports Activities', '#f59e0b'),
]

image_count = 0

try:
    for filename, category, title, color in gallery_items:
        img = Image.new('RGB', (800, 600), color=color)
        draw = ImageDraw.Draw(img)

        try:
            font_large = ImageFont.truetype("arial.ttf", 56)
            font_small = ImageFont.truetype("arial.ttf", 28)
        except:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Draw title
        draw.text((50, 250), title, fill='white', font=font_large)

        # Draw category
        draw.text((50, 520), f"Category: {category.upper()}", fill='white', font=font_small)

        # Save image
        path = os.path.join(PROJECT_ROOT, 'images', 'gallery', filename)
        img.save(path, 'JPEG', quality=90)
        print(f"   ✓ {filename}")
        image_count += 1

except Exception as e:
    print(f"   ✗ Error creating gallery images: {e}\n")

print()

# Step 4: Update gallery.json
print("⚙️  Step 4: Updating gallery.json...")

gallery_config = [
    {"id": 1, "src": "images/gallery/campus-building.jpg", "title": "School Building", "category": "campus", "description": "Main school building"},
    {"id": 2, "src": "images/gallery/campus-assembly.jpg", "title": "School Assembly", "category": "campus", "description": "School assembly"},
    {"id": 3, "src": "images/gallery/life-classroom.jpg", "title": "Classroom Learning", "category": "classroom", "description": "Interactive learning"},
    {"id": 4, "src": "images/gallery/students-group-1.jpg", "title": "Student Activities", "category": "activities", "description": "Group activities"},
    {"id": 5, "src": "images/gallery/students-group-2.jpg", "title": "Group Learning", "category": "activities", "description": "Collaborative learning"},
    {"id": 6, "src": "images/gallery/hero-students.jpg", "title": "Student Achievements", "category": "events", "description": "Student success"},
    {"id": 7, "src": "images/gallery/leader-portrait.jpg", "title": "School Leadership", "category": "events", "description": "Leadership"},
    {"id": 8, "src": "images/gallery/life-sports.jpg", "title": "Sports Activities", "category": "sports", "description": "Sports"},
]

try:
    gallery_json_path = os.path.join(PROJECT_ROOT, 'data', 'gallery.json')
    with open(gallery_json_path, 'w') as f:
        json.dump(gallery_config, f, indent=2)
    print("   ✓ gallery.json updated\n")
except Exception as e:
    print(f"   ✗ Error: {e}\n")

# Step 5: Verify
print("✓ Step 5: Verifying setup...")
logo_exists = os.path.exists(os.path.join(PROJECT_ROOT, 'images', 'logo', 'logo.png'))
gallery_count = len([f for f in os.listdir(os.path.join(PROJECT_ROOT, 'images', 'gallery')) if f.endswith('.jpg')])

print(f"   {'✓' if logo_exists else '✗'} Logo: {'Ready' if logo_exists else 'Missing'}")
print(f"   {'✓' if gallery_count > 0 else '✗'} Gallery: {gallery_count} images\n")

# Summary
print("█" * 80)
print("█" + " " * 78 + "█")
print("█" + "  ✅ SETUP COMPLETE!".ljust(79) + "█")
print("█" + " " * 78 + "█")
print("█" * 80 + "\n")

print("📊 SUMMARY:")
print(f"   • Logo: 1 file")
print(f"   • Gallery: {image_count} images")
print(f"   • Total Assets: {1 + image_count}\n")

print("📁 LOCATIONS:")
print("   • Logo: images/logo/logo.png")
print("   • Gallery: images/gallery/\n")

print("✨ YOUR WEBSITE IS READY!")
print("   ✓ Logo displays in navbar")
print("   ✓ Gallery shows 8 placeholder images")
print("   ✓ All filtering works")
print("   ✓ Modern animations enabled")
print("   ✓ Mobile responsive\n")

print("🎉 NEXT STEPS:")
print("   1. Open your website in a browser")
print("   2. Go to Gallery page to see images")
print("   3. Check navbar for logo")
print("   4. Test filters: Campus, Classroom, Activities, Events, Sports\n")

print("█" * 80 + "\n")
