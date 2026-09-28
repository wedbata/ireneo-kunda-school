#!/bin/bash
# Create placeholder images for gallery using ImageMagick

cd /c/Users/wedba/Desktop/ireneo-kunda-website/images/gallery

# Create sample images using ImageMagick (convert command)
# If ImageMagick is not available, images will need to be added manually

echo "Creating gallery placeholder images..."

# Define colors and create images
for i in 1; do
    # Campus images - Green
    convert -size 800x600 xc:'#2d8a5e' -pointsize 48 -fill white -gravity center -annotate +0+0 'School Building' campus-1.jpg
    convert -size 800x600 xc:'#2d8a5e' -pointsize 48 -fill white -gravity center -annotate +0+0 'School Library' campus-2.jpg
    convert -size 800x600 xc:'#2d8a5e' -pointsize 48 -fill white -gravity center -annotate +0+0 'Computer Lab' campus-3.jpg

    # Classroom images - Blue
    convert -size 800x600 xc:'#4f46e5' -pointsize 48 -fill white -gravity center -annotate +0+0 'Primary Classroom' classroom-1.jpg
    convert -size 800x600 xc:'#4f46e5' -pointsize 48 -fill white -gravity center -annotate +0+0 'Science Laboratory' classroom-2.jpg

    # Activities images - Orange
    convert -size 800x600 xc:'#ff8c42' -pointsize 48 -fill white -gravity center -annotate +0+0 'Art Class' activities-1.jpg
    convert -size 800x600 xc:'#ff8c42' -pointsize 48 -fill white -gravity center -annotate +0+0 'Music Class' activities-2.jpg
    convert -size 800x600 xc:'#ff8c42' -pointsize 48 -fill white -gravity center -annotate +0+0 'Drama Performance' activities-3.jpg

    # Events images - Pink
    convert -size 800x600 xc:'#ec4899' -pointsize 48 -fill white -gravity center -annotate +0+0 'Graduation Ceremony' events-1.jpg
    convert -size 800x600 xc:'#ec4899' -pointsize 48 -fill white -gravity center -annotate +0+0 'Cultural Day' events-2.jpg

    # Sports images - Amber
    convert -size 800x600 xc:'#f59e0b' -pointsize 48 -fill white -gravity center -annotate +0+0 'Football Match' sports-1.jpg
    convert -size 800x600 xc:'#f59e0b' -pointsize 48 -fill white -gravity center -annotate +0+0 'Athletics Day' sports-2.jpg
done

echo "✓ Gallery images created!"
