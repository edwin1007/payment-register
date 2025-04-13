#!/usr/bin/env bash
# Render build script

# Instala dependencias (opcional si usas poetry/pipenv)
pip install -r requirements.txt

# Recolecta archivos estáticos
python manage.py migrate
python manage.py collectstatic --noinput
