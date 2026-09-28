# Ireneo Kunda Complex School Website

A complete, modern school website for Ireneo Kunda Complex in Wau, South Sudan. This website features a clean, responsive design optimized for low-bandwidth environments and includes a simple JSON-based content management system.

## 🌟 Features

- **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- **Low Bandwidth Optimized** - Lightweight design suitable for South Sudan's connectivity
- **Easy Content Management** - Update announcements and gallery via simple JSON files
- **Complete Pages**:
  - Home - Hero section with quick info cards
  - About - Mission, vision, values, and facilities
  - Programs - Detailed information about Nursery, Primary, and Secondary programs
  - Admissions - Requirements, fee structure, and online application form
  - Gallery - Filterable photo gallery with lightbox view
  - Announcements - Latest school news and updates
  - Contact - Contact form and school information

## 📁 File Structure

```
ireneo-kunda-website/
├── index.html              # Homepage
├── about.html              # About the school
├── programs.html           # Educational programs
├── admissions.html         # Admissions information
├── gallery.html            # Photo gallery
├── announcements.html      # School announcements
├── contact.html            # Contact page
├── css/
│   └── style.css          # Main stylesheet
├── js/
│   ├── main.js            # Core JavaScript
│   ├── announcements.js   # Announcements functionality
│   ├── admissions.js      # Admissions form handling
│   ├── contact.js         # Contact form handling
│   └── gallery.js         # Gallery functionality
├── data/
│   ├── announcements.json # Announcements data (CMS)
│   └── gallery.json       # Gallery data (CMS)
├── images/
│   └── gallery/           # Gallery images folder
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Setup

Simply open `index.html` in a web browser. No server required for basic functionality.

For full functionality (forms, JSON loading), use a local web server:

**Option A: Python**
```bash
cd ireneo-kunda-website
python -m http.server 8000
```
Then visit: http://localhost:8000

**Option B: PHP**
```bash
cd ireneo-kunda-website
php -S localhost:8000
```
Then visit: http://localhost:8000

**Option C: Node.js (http-server)**
```bash
npm install -g http-server
cd ireneo-kunda-website
http-server -p 8000
```
Then visit: http://localhost:8000

### 2. Customize Content

#### Update School Information

Edit the HTML files directly to update:
- School name and contact details (in navigation and footer)
- Phone numbers and email addresses
- Physical address
- Social media links

#### Manage Announcements

Edit `data/announcements.json`:

```json
[
    {
        "id": 1,
        "title": "Your Announcement Title",
        "date": "2026-09-27",
        "content": "Your announcement content here...",
        "category": "events"
    }
]
```

Categories: `admissions`, `schedule`, `events`, `academic`

#### Manage Gallery

1. Add images to `images/gallery/` folder
2. Edit `data/gallery.json`:

```json
[
    {
        "id": 1,
        "src": "images/gallery/your-image.jpg",
        "title": "Image Title",
        "category": "campus",
        "description": "Image description"
    }
]
```

Categories: `campus`, `classroom`, `activities`, `events`, `sports`

## 📝 Content Management

### Adding Announcements

1. Open `data/announcements.json`
2. Add new announcement object:
```json
{
    "id": 6,
    "title": "New Announcement",
    "date": "2026-09-27",
    "content": "Announcement text...",
    "category": "events"
}
```
3. Save the file
4. Refresh the website

### Adding Gallery Photos

1. Save your photos to `images/gallery/` (use descriptive names like `classroom-science-lab.jpg`)
2. Open `data/gallery.json`
3. Add entry:
```json
{
    "id": 13,
    "src": "images/gallery/your-photo.jpg",
    "title": "Photo Title",
    "category": "classroom",
    "description": "Photo description"
}
```
4. Save and refresh

## 🎨 Customization

### Colors

Edit `css/style.css` to change the color scheme. Look for the `:root` section at the top:

```css
:root {
    --primary-color: #2c5f2d;      /* Main green color */
    --primary-dark: #1e4620;       /* Darker green */
    --secondary-color: #f39c12;    /* Orange accent */
    /* ... more colors ... */
}
```

### Logo

To add a school logo:
1. Save logo image to `images/logo.png`
2. Edit the `.logo` section in each HTML file's navigation
3. Replace text with: `<img src="images/logo.png" alt="Ireneo Kunda Complex" style="height: 50px;">`

## 📱 Mobile Optimization

The website is fully responsive and works on all screen sizes. The mobile menu automatically activates on screens smaller than 768px.

## 🌐 Browser Support

Works on all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera
- Mobile browsers

## 📧 Form Handling

The contact and application forms currently display success messages without sending data. To enable actual form submission:

### Option 1: Use a Form Service (Easiest)

Use services like:
- **Formspree** (https://formspree.io) - Free tier available
- **Netlify Forms** (if hosting on Netlify)
- **Google Forms** - Embed Google Form

### Option 2: Backend Integration

Connect to a backend server:
1. Create a server endpoint (PHP, Node.js, Python, etc.)
2. Update form submission in `js/contact.js` and `js/admissions.js`
3. Replace `console.log()` with actual fetch/AJAX call

Example:
```javascript
fetch('/api/contact', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
})
```

## 🚀 Deployment

### Option 1: Static Hosting (Recommended)

Upload to any of these free services:
- **Netlify** (https://netlify.com) - Drag & drop, free SSL
- **Vercel** (https://vercel.com) - Free hosting
- **GitHub Pages** - Free with GitHub account
- **Firebase Hosting** - Google's free tier

### Option 2: Shared Hosting

Upload all files via FTP to your web hosting provider.

### Option 3: VPS/Dedicated Server

1. Install web server (Apache/Nginx)
2. Upload files to web root
3. Configure domain

## 🔧 Maintenance

### Regular Updates

1. **Announcements**: Update weekly or as needed
2. **Gallery**: Add photos after events
3. **Contact Info**: Keep phone/email current
4. **Programs**: Update at start of each academic year

### Backup

Regularly backup:
- `data/` folder (your content)
- `images/` folder (your photos)
- Any customized HTML files

## 📊 Adding Features

### Google Analytics

Add before closing `</head>` tag in each HTML file:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Facebook Pixel

Add tracking code before closing `</head>` tag.

## 🆘 Troubleshooting

**Forms not working?**
- Use a local web server (not just opening HTML files)
- Check browser console for errors (F12)

**Announcements not loading?**
- Verify `data/announcements.json` has valid JSON
- Use JSONLint.com to validate JSON syntax

**Images not showing?**
- Check file paths in `data/gallery.json`
- Ensure images exist in `images/gallery/` folder
- Verify image file names match exactly (case-sensitive on Linux)

**Mobile menu not working?**
- Clear browser cache
- Check that `js/main.js` is loading

## 📞 Support

For technical support or customization help, contact your web developer or:
- Web development community forums
- Stack Overflow
- Local IT support in Wau

## 📄 License

This website template is provided for use by Ireneo Kunda Complex. Feel free to modify and customize as needed.

## ✅ Checklist Before Launch

- [ ] Update all contact information (phone, email, address)
- [ ] Add school logo
- [ ] Customize colors to match school branding
- [ ] Add real announcements
- [ ] Upload school photos to gallery
- [ ] Test all forms
- [ ] Test on mobile devices
- [ ] Set up form submission backend or service
- [ ] Configure domain name
- [ ] Add Google Analytics (optional)
- [ ] Test all links
- [ ] Backup all files

---

**Built for Ireneo Kunda Complex, Wau, South Sudan**  
*Excellence in Education*
