#!/usr/bin/env python
"""Populate initial products into the database with real images from Unsplash."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product
from decimal import Decimal

# Create sample products with real images from Unsplash
products = [
    {
        "name": "Premium Laptop Pro",
        "price": Decimal("1299.99"),
        "description": "High-performance laptop with latest specs. Intel i7, 16GB RAM, 512GB SSD. Perfect for professionals and developers.",
        "stock": 15,
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&q=80"
    },
    {
        "name": "Wireless Headphones",
        "price": Decimal("199.99"),
        "description": "Premium noise-cancelling headphones with 30-hour battery life. Crystal clear sound and comfortable design.",
        "stock": 30,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80"
    },
    {
        "name": "Smart Watch Pro",
        "price": Decimal("299.99"),
        "description": "Feature-rich smartwatch with heart rate monitoring, GPS, water resistance. 14-day battery life.",
        "stock": 20,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80"
    },
    {
        "name": "Fast USB-C Cable",
        "price": Decimal("29.99"),
        "description": "High-speed USB-C charging cable (2m). Supports fast charging and data transfer. Durable design.",
        "stock": 100,
        "image_url": "https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500&q=80"
    },
    {
        "name": "RGB Mechanical Keyboard",
        "price": Decimal("149.99"),
        "description": "RGB mechanical gaming keyboard. Programmable keys, mechanical switches, ergonomic design.",
        "stock": 25,
        "image_url": "https://images.unsplash.com/photo-1587829191301-3f23e9ca19cb?w=500&q=80"
    },
    {
        "name": "4K IPS Monitor",
        "price": Decimal("499.99"),
        "description": "27-inch 4K IPS display with HDR support. 144Hz refresh rate. Perfect for gaming and video editing.",
        "stock": 10,
        "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&q=80"
    },
    {
        "name": "Portable SSD 1TB",
        "price": Decimal("99.99"),
        "description": "Super fast portable SSD with 1TB storage. Up to 550MB/s read speed. Compact and durable.",
        "stock": 40,
        "image_url": "https://images.unsplash.com/photo-1629429813432-2121ee9b6382?w=500&q=80"
    },
    {
        "name": "Webcam 4K",
        "price": Decimal("79.99"),
        "description": "Professional 4K webcam with auto-focus. Perfect for streaming, video calls, and content creation.",
        "stock": 35,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&q=80"
    },
]

for prod in products:
    obj, created = Product.objects.get_or_create(
        name=prod["name"],
        defaults={
            "price": prod["price"],
            "description": prod["description"],
            "stock": prod["stock"],
            "image_url": prod["image_url"],
        }
    )
    if created:
        print(f"✓ Created: {prod['name']}")
    else:
        print(f"~ Already exists: {prod['name']}")

print(f"\nDone! Total products: {Product.objects.count()}")

