# 🎨 E-Commerce Website Customization Guide

## How to Customize Your E-Commerce Website

This guide explains how to modify the website to suit your needs: change colors, branding, products, and more.

---

## 1. 📦 Add or Edit Products

### Via Django Admin (Easiest)
1. Go to **http://127.0.0.1:8000/admin/**
2. Login with: `admin` / `admin123`
3. Click **"Products"** → **"Add Product"**
4. Fill in:
   - **Name:** Product title
   - **Price:** Product price (e.g., 99.99)
   - **Description:** Product details
   - **Stock:** Number available
   - **Image URL:** Paste URL from Google Images, Unsplash, or any CDN
5. Click **"Save"**

### Via Script (Bulk Upload)
Edit `reload_products.py` to add/modify products:
```python
{
    "name": "Your Product Name",
    "price": Decimal("99.99"),
    "description": "Product description here",
    "stock": 50,
    "image_url": "https://images.unsplash.com/photo-XXXXX?w=500&q=80"
}
```
Then run: `python reload_products.py`

### Find Product Images
- **Unsplash:** https://unsplash.com (free, high-quality)
- **Pexels:** https://pexels.com (free)
- **Pixabay:** https://pixabay.com (free)
- **Google Images:** Right-click → "Open image in new tab" → copy URL

---

## 2. 🎨 Change Website Colors & Styling

Edit `static/css/style.css` to customize:

### Change Primary Color (Blue)
Find and replace `#007bff` with your color code:
```css
.btn-primary { background-color: #YOUR_COLOR; }
.navbar { background-color: #YOUR_COLOR; }
```

### Change Product Card Gradient
Edit the purple-pink gradient in `templates/store/home.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
Use a color picker to generate gradients: https://cssgradient.io/

### Change Accent Colors
- Success (Green): `#28a745`
- Danger (Red): `#dc3545`
- Warning (Orange): `#ffc107`
- Info (Blue): `#17a2b8`

---

## 3. 📝 Update Website Text

### Homepage Title
Edit `templates/store/home.html`:
```html
<h2 class="mb-4">Featured Products</h2>
<!-- Change to: -->
<h2 class="mb-4">Our Best Sellers</h2>
```

### Navbar Brand Name
Edit `templates/base.html`:
```html
<a class="navbar-brand" href="/">ShopDemo</a>
<!-- Change to: -->
<a class="navbar-brand" href="/">Your Shop Name</a>
```

### Footer Text
Edit `templates/base.html`:
```html
<div class="container text-center">© Demo Shop - Built with Django</div>
<!-- Change to: -->
<div class="container text-center">© Your Company - All rights reserved</div>
```

---

## 4. 💰 Update Pricing & Stock

### Quick Update via Admin
1. Go to admin → Products
2. Click product name to edit
3. Change **Price** or **Stock**
4. Click **"Save"**

---

## 5. 🖼️ Add Custom Logo/Images

### Add Website Logo
1. Place logo image in `static/img/logo.png`
2. Edit `templates/base.html`:
```html
<a class="navbar-brand" href="/">
    <img src="/static/img/logo.png" height="40" alt="Logo"> ShopDemo
</a>
```

---

## 6. 🔐 Change Admin Credentials

### Create New Admin User
```bash
. .\.venv\Scripts\Activate.ps1
python manage.py createsuperuser
```

### Delete Old Admin User (via admin panel)
1. Go to http://127.0.0.1:8000/admin/
2. Click "Users" → select user → "Delete"

---

## 7. 📧 Customize Email Messages

Edit `store/views.py` to change success/error messages:
```python
messages.success(request, 'Added to cart!')  # Change this text
messages.error(request, 'Login required')    # Change this text
```

---

## 8. 🌍 Change Website Layout

### Modify Product Grid (Products Per Row)
Edit `templates/store/home.html`:
```html
<!-- Currently 3 columns on desktop: -->
<div class="row row-cols-1 row-cols-md-3 g-4">

<!-- Change to 4 columns: -->
<div class="row row-cols-1 row-cols-md-4 g-4">

<!-- Or 2 columns: -->
<div class="row row-cols-1 row-cols-md-2 g-4">
```

### Adjust Product Image Height
Edit `templates/store/home.html`:
```html
<img ... style="height: 220px; object-fit: cover;">
<!-- Change 220px to desired height, e.g., 300px -->
```

---

## 9. 🛒 Customize Cart & Checkout

### Add Order Notes
Edit `templates/store/checkout.html` to add textarea:
```html
<div class="mb-3">
    <label class="form-label">Order Notes</label>
    <textarea class="form-control" name="notes" placeholder="Special requests..."></textarea>
</div>
```

### Change Checkout Button Text
Edit `templates/store/checkout.html`:
```html
<button type="submit" class="btn btn-success btn-lg">Complete Purchase</button>
<!-- Change to: -->
<button type="submit" class="btn btn-success btn-lg">Confirm & Pay</button>
```

---

## 10. 📱 Responsive Design Tweaks

### Mobile Button Sizes
Edit `static/css/style.css`:
```css
@media (max-width: 576px) {
  .btn { padding: 0.5rem 1rem; font-size: 0.95rem; }
}
```

### Adjust Spacing
```css
.container { padding: 20px; }  /* Adjust container padding */
.card { margin-bottom: 20px; }  /* Space between cards */
```

---

## 11. 🔍 SEO & Metadata

Edit `templates/base.html` to update page title:
```html
<title>Ecommerce Demo</title>
<!-- Change to: -->
<title>Your Store Name - Shop Online</title>
```

---

## 12. 💾 Backup Your Changes

### Create Database Backup
```bash
# Copy the database file
copy db.sqlite3 db.sqlite3.backup
```

### Save Custom Code
Keep a backup of modified files:
- `static/css/style.css`
- `templates/base.html`
- Any other custom files

---

## 🎯 Popular Customization Examples

### Example 1: Change Brand Colors to Blue & Gold
```css
--primary: #003d82;  /* Dark Blue */
--accent: #ffd700;   /* Gold */
```

### Example 2: Add More Product Categories
Modify `store/models.py`:
```python
class Product(models.Model):
    category = models.CharField(max_length=50)  # Add this field
```

### Example 3: Add Product Reviews
Create new model:
```python
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(1, 5)
    comment = models.TextField()
```

---

## 🚀 Deploy Custom Website

### Before Deployment
1. Update `ecommerce/settings.py`:
   - Set `DEBUG = False`
   - Update `SECRET_KEY`
   - Set `ALLOWED_HOSTS = ['yourdomain.com']`

2. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

3. Use production server (Gunicorn, uWSGI)

### Hosting Options
- **Heroku:** Free tier available
- **AWS:** Elastic Beanstalk
- **DigitalOcean:** VPS starting $5/month
- **PythonAnywhere:** Django-specific hosting
- **Render:** Easy Django deployment

---

## 📚 Resources

- **Django Docs:** https://docs.djangoproject.com/
- **Bootstrap Docs:** https://getbootstrap.com/docs/
- **Color Picker:** https://colorpicker.com/
- **Gradient Generator:** https://cssgradient.io/
- **Font Awesome Icons:** https://fontawesome.com/

---

## ❓ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Images not loading | Check image URL is accessible; test in browser |
| Colors not changing | Clear browser cache (Ctrl+Shift+Delete) |
| Styles not applied | Run `python manage.py collectstatic` |
| Admin not accessible | Check if superuser exists |
| Products disappear | Check database backup |

---

## 💡 Tips

1. **Always backup before major changes**
2. **Test changes on local server first**
3. **Use browser DevTools (F12) to inspect/debug CSS**
4. **Keep a list of customizations for future updates**
5. **Use version control (Git) to track changes**

---

Enjoy customizing your e-commerce website! 🎉
