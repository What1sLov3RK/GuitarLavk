# 🎸 GuitarLavka

**GuitarLavka** is a Django-based online guitar shop where users can browse, filter, and purchase guitars, accessories, and related musical equipment.  
The project includes product pages, a cart system, and a simple checkout form.

---

## 📁 Project Structure

guitarlavochka/     
│   
├── css/ # Bootstrap and other CSS files    
│   
├── js/ # JS and Bootstrap scripts  
│   
├── GuitarLavk/ # Django project configuration (settings, urls, wsgi, etc.)     
│ ├── init.py   
│ ├── asgi.py   
│ ├── settings.py   
│ ├── urls.py   
│ └── wsgi.py   
│   
│   
├── guitarlavka/ # Main Django app (core logic)     
│ ├── migrations/   
│ ├── init.py   
│ ├── admin.py  
│ ├── app.py  
│ ├── filters.py    
│ ├── forms.py        
│ ├── models.py     
│ ├── urls.py   
│ ├── views.py  
│ ├── utils.py  
│ └── templates/    
│   
├── media/ # Uploaded product images    
│ └── product_images/   
│   
├── static/ # Static files (used in templates)  
│ ├── css/  
│ │ └── stylesheet.css  
│ ├── images/   
│ └── js/   
│   
├── templates/ # HTML templates for pages    
│ ├── authorized.html   
│ ├── base.html  
│ ├── cart.html  
│ ├── catalogue.html  
│ ├── index.html      
│ ├── login.html   
│ ├── order_success.html   
│ ├── order_view.html   
│ ├── product.html  
│ └── register.html 
│   
├── manage.py   
│   
├── db.sqlite3 # Local database     
│   
└── .env.example # Example environment file (see below) 
---

### 🐳 Docker Setup

The project includes a ready-to-use Dockerfile for easy deployment (e.g. on Railway or Render).
It installs dependencies, collects static files, and launches Gunicorn as the production WSGI server.

Dockerfile overview
```dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=GuitarLavk.settings \
    PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn GuitarLavk.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
```

## Run locally
```bash
docker build -t guitarlavka .
docker run -p 8000:8000 --env-file .env guitarlavka
```

## Then open:
```cpp
http://127.0.0.1:8000/
```

## ⚙️ Installation and Setup
### 1. Clone the repository

```bash
git clone https://github.com/yourusername/guitarlavka.git
cd guitarlavochka
```

### 2. Create a virtual environment
```bash
python -m venv env
```

```bash
source env/bin/activate  # macOS/Linux
```

```bash
env\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
```

### 5. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

## 🧱 Features

Product catalogue with filters  
Shopping cart and checkout form     
Category-based browsing
Custom design via stylesheet.css    
Fixed desktop layout 

## 🧰 Tech Stack
Backend: Django (Python 3.9+)  
Frontend: HTML, CSS, Bootstrap  
Database: SQLite (default)  
Templates: Django Templates 

## 🧑‍💻 Development Notes
All static assets are stored in /static/        
Product images are under /media/product_images/     
Universal forms styling ensures visual consistency  
Use python manage.py collectstatic before deployment if needed  