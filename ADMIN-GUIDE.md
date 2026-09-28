# Content Management Guide

## For School Administrators

This guide explains how to update the website content yourself without technical knowledge.

---

## 📢 Managing Announcements

### To Add a New Announcement:

1. **Open the file:** `data/announcements.json` (use Notepad, TextEdit, or any text editor)

2. **Add your announcement** at the top of the list:

```json
{
    "id": 6,
    "title": "Your Announcement Title Here",
    "date": "2026-09-27",
    "content": "Write the full announcement text here. Include all important details that parents and students need to know.",
    "category": "events"
}
```

3. **Add a comma** after the closing `}` if there are more announcements below

4. **Save the file**

5. **Refresh the website** - your announcement will appear automatically!

### Announcement Categories:

- `admissions` - For enrollment and registration news
- `schedule` - For term dates, holidays, exam schedules
- `events` - For school events, meetings, celebrations
- `academic` - For academic achievements, curriculum updates

### Tips:
- Always use the format: "YYYY-MM-DD" for dates (e.g., 2026-09-27)
- Increase the `id` number for each new announcement
- Most recent date appears first
- Keep announcements clear and concise

---

## 📸 Managing the Photo Gallery

### To Add Photos:

1. **Prepare your photos:**
   - Use JPG or PNG format
   - Keep file size under 1MB for faster loading
   - Use descriptive names (e.g., `sports-day-2026.jpg`)

2. **Copy photos to:** `images/gallery/` folder

3. **Update gallery.json:**

Open `data/gallery.json` and add:

```json
{
    "id": 13,
    "src": "images/gallery/your-photo-name.jpg",
    "title": "Photo Title - What students see",
    "category": "campus",
    "description": "Brief description of the photo"
}
```

4. **Save and refresh!**

### Photo Categories:

- `campus` - School buildings, facilities, grounds
- `classroom` - Teaching and learning activities
- `activities` - Art, music, clubs, special activities
- `events` - Graduations, ceremonies, celebrations
- `sports` - Sports day, games, physical education

### Photo Tips:
- Get permission before posting student photos
- Choose clear, well-lit photos
- Show the best of your school
- Update regularly (monthly recommended)

---

## 📝 Updating Text Content

### Homepage Hero Section

**File:** `index.html`

**Find this section** (around line 45):

```html
<h1 class="hero-title">Welcome to Ireneo Kunda Complex</h1>
<p class="hero-subtitle">Nurturing Young Minds in Wau, South Sudan</p>
<p class="hero-description">Quality education from Nursery through Secondary School</p>
```

**Change the text** between the tags to update your homepage message.

### About Page

**File:** `about.html`

Update the mission, vision, and "Our Story" sections with your school's information.

### Programs Page

**File:** `programs.html`

Update subject lists, program descriptions, and activity details as your curriculum changes.

---

## 📞 Updating Contact Information

### To Change Phone Number, Email, or Address:

1. **Open each HTML file** (all 7 pages)
2. **Find the footer section** (at the bottom)
3. **Look for:**

```html
<li><i class="fas fa-phone"></i> +211 XXX XXX XXX</li>
<li><i class="fas fa-envelope"></i> info@ireneokunda.edu.ss</li>
```

4. **Replace** with your actual contact details
5. **Save all files**

### To Update Social Media Links:

Find this in the footer:

```html
<a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
```

Replace the `#` with your Facebook page URL (e.g., `https://facebook.com/yourschool`)

---

## 🎨 Changing Colors

### To Match Your School Colors:

1. **Open:** `css/style.css`
2. **Find the `:root` section** at the top (first 30 lines)
3. **Change these values:**

```css
--primary-color: #2c5f2d;      /* Main school color */
--secondary-color: #f39c12;    /* Accent color */
```

**Color Codes:**
- Green: `#2c5f2d`
- Blue: `#3498db`
- Red: `#e74c3c`
- Orange: `#f39c12`
- Purple: `#9b59b6`

Use a color picker tool online to get codes for your school colors.

---

## 💼 Managing Forms

### Viewing Form Submissions:

**Currently:** Forms show success messages but don't send emails.

**To Receive Submissions:**

Use **Formspree** (free and easy):

1. Go to https://formspree.io
2. Sign up with school email
3. Create a form
4. Copy the form endpoint URL
5. Send to your web developer to integrate

**Alternative:** Set up email forwarding through your web host.

---

## ⚠️ Important Rules

### DO:
✅ Backup files before editing
✅ Test changes on a copy first
✅ Keep announcements current (update weekly)
✅ Use clear, error-free language
✅ Compress photos before uploading
✅ Keep student privacy in mind

### DON'T:
❌ Delete files you don't understand
❌ Change file names (breaks links)
❌ Post student full names without permission
❌ Use very large image files (slow loading)
❌ Forget to save after editing
❌ Edit multiple files without backing up

---

## 🔄 Regular Maintenance Schedule

### Weekly:
- [ ] Check and update announcements
- [ ] Review contact form submissions (if active)
- [ ] Post new photos from school events

### Monthly:
- [ ] Update gallery with event photos
- [ ] Review all page content for accuracy
- [ ] Check all links work

### Quarterly:
- [ ] Update program information if changed
- [ ] Refresh homepage content
- [ ] Add new achievements to About page

### Yearly:
- [ ] Update academic year information
- [ ] Refresh all program descriptions
- [ ] Update staff information (if added)
- [ ] Archive old announcements

---

## 🆘 Common Issues & Solutions

### "My changes don't appear!"
**Solution:** 
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Make sure you saved the file
- Check you edited the right file

### "I broke something!"
**Solution:**
- Restore from your backup copy
- Undo recent changes (Ctrl+Z in text editor)
- Ask your web developer for help

### "Photos are too slow to load"
**Solution:**
- Compress images using TinyPNG.com or similar
- Keep images under 500KB each
- Resize large photos before uploading

### "JSON file won't save"
**Solution:**
- Check all brackets `{ }` and `[ ]` match
- Check all commas are in the right place
- Validate JSON at JSONLint.com

---

## 📋 Content Checklist

Before publishing any changes:

- [ ] Spelling and grammar checked
- [ ] Phone numbers and emails correct
- [ ] Dates in correct format (YYYY-MM-DD)
- [ ] Photos have descriptive titles
- [ ] All links work
- [ ] Tested on phone and computer
- [ ] Backup created
- [ ] Changes look good

---

## 👥 Who Can Help

**For content questions:**
- School administrators
- Department heads

**For technical issues:**
- Local IT support in Wau
- Web development community online
- Your web hosting support

**For design changes:**
- Hire a web developer
- Check online tutorials
- Ask in web development forums

---

## 📞 Emergency Contacts

Keep these handy:

- **Web hosting support:** [Your hosting provider contact]
- **Domain registrar:** [Your domain provider]
- **Backup location:** [Where your backups are stored]
- **Web developer:** [If you have one]

---

Remember: **When in doubt, make a backup first!**

This website is yours to manage. Take it slow, test changes, and you'll become comfortable updating it quickly.

Good luck! 🎓
