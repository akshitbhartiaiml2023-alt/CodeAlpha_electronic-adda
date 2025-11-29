# Ecommerce Demo (Django)

This is a minimal e-commerce demo built with Django, providing:
- Product listing and detail pages
- Session-based shopping cart
- User registration, login, logout
- Checkout and order creation

Requirements
```
Python 3.10+
pip install -r requirements.txt
```

Setup (Windows PowerShell)
```powershell
cd "c:\Users\vaibh\OneDrive\E commerces\ecommerce"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Notes
- This is a development demo. Replace `SECRET_KEY` in `ecommerce/settings.py` and set `DEBUG=False` for production.
- Add product images in `media/products/` or via Django admin.
