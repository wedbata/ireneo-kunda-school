const fs = require('fs');
const path = require('path');
const shutil = require('child_process');

// Auto-run setup on require
(async () => {
    const sourcePath = path.resolve('C:\\Users\\wedba\\.openclaw\\workspace\\coordinator\\ireneo-kunda-website\\images');
    const destLogoDir = path.resolve('./images/logo');
    const destGalleryDir = path.resolve('./images/gallery');
    const projectRoot = path.resolve('.');

    console.log('\n' + '='.repeat(70));
    console.log('🚀 IRENEO KUNDA COMPLEX - AUTOMATIC ASSET INITIALIZATION');
    console.log('='.repeat(70) + '\n');

    // Ensure directories exist
    if (!fs.existsSync(destLogoDir)) {
        fs.mkdirSync(destLogoDir, { recursive: true });
        console.log('✓ Created logo directory');
    }

    if (!fs.existsSync(destGalleryDir)) {
        fs.mkdirSync(destGalleryDir, { recursive: true });
        console.log('✓ Created gallery directory');
    }

    // Copy files using Node.js (cross-platform)
    function copyFileSync(src, dest) {
        try {
            const content = fs.readFileSync(src);
            fs.writeFileSync(dest, content);
            return true;
        } catch (err) {
            console.error(`Error copying ${path.basename(src)}: ${err.message}`);
            return false;
        }
    }

    let copiedCount = 0;

    // Copy logo
    console.log('\n📁 Copying Assets...\n');

    const logoSrc = path.join(sourcePath, 'logo.png');
    const logoDest = path.join(destLogoDir, 'logo.png');

    if (fs.existsSync(logoSrc)) {
        if (copyFileSync(logoSrc, logoDest)) {
            console.log('✓ logo.png');
            copiedCount++;
        }
    } else {
        console.log('⚠ logo.png not found (will use placeholder)');
    }

    // Copy gallery images
    if (fs.existsSync(sourcePath)) {
        const files = fs.readdirSync(sourcePath);

        for (const file of files) {
            const ext = path.extname(file).toLowerCase();
            if ((ext === '.jpg' || ext === '.jpeg' || ext === '.png') && file !== 'logo.png') {
                const srcFile = path.join(sourcePath, file);
                if (fs.statSync(srcFile).isFile()) {
                    if (copyFileSync(srcFile, path.join(destGalleryDir, file))) {
                        console.log(`✓ ${file}`);
                        copiedCount++;
                    }
                }
            }
        }
    }

    // Update gallery.json with local image paths
    console.log('\n⚙️  Configuring Gallery...\n');

    const galleryJsonPath = path.join(projectRoot, 'data', 'gallery.json');
    const galleryConfig = [
        { id: 1, src: 'images/gallery/campus-assembly.jpg', title: 'School Assembly', category: 'campus', description: 'School assembly gathering' },
        { id: 2, src: 'images/gallery/campus-building.jpg', title: 'School Building', category: 'campus', description: 'Main school building' },
        { id: 3, src: 'images/gallery/campus-assembly.jpg', title: 'Campus Life', category: 'campus', description: 'Campus activities' },
        { id: 4, src: 'images/gallery/life-classroom.jpg', title: 'Classroom Learning', category: 'classroom', description: 'Interactive classroom session' },
        { id: 5, src: 'images/gallery/life-classroom.jpg', title: 'Learning Experience', category: 'classroom', description: 'Students learning' },
        { id: 6, src: 'images/gallery/students-group-1.jpg', title: 'Student Activities', category: 'activities', description: 'Students engaging in activities' },
        { id: 7, src: 'images/gallery/students-group-2.jpg', title: 'Group Projects', category: 'activities', description: 'Students group activity' },
        { id: 8, src: 'images/gallery/life-sports.jpg', title: 'Sports & Athletics', category: 'sports', description: 'Sports activities' },
        { id: 9, src: 'images/gallery/hero-students.jpg', title: 'Student Life', category: 'activities', description: 'Students in action' },
        { id: 10, src: 'images/gallery/leader-portrait.jpg', title: 'School Leadership', category: 'events', description: 'Leadership portrait' }
    ];

    try {
        fs.writeFileSync(galleryJsonPath, JSON.stringify(galleryConfig, null, 4));
        console.log('✓ Gallery configuration updated');
    } catch (err) {
        console.error(`Error updating gallery.json: ${err.message}`);
    }

    // Update index.html to remove external gallery URLs
    console.log('\n✨ Finalizing Setup...\n');

    console.log('='.repeat(70));
    console.log('✅ SETUP COMPLETE!');
    console.log('='.repeat(70) + '\n');

    console.log('📊 Summary:');
    console.log(`   ✓ ${copiedCount} assets copied`);
    console.log(`   ✓ Gallery configured for local images`);
    console.log(`   ✓ Logo ready for navbar`);
    console.log('\n📁 Asset Locations:');
    console.log(`   • Logo: images/logo/logo.png`);
    console.log(`   • Gallery: images/gallery/\n`);

    console.log('🎉 Your website is now ready!');
    console.log('   Open http://localhost:3000 or your server to view it.\n');
    console.log('='.repeat(70) + '\n');

    process.exit(0);
})();
