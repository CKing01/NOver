import os
os.system("/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip")
os.system("pip install -U g4f")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
# os.system("python3 manage.py collectstatic")
os.system("ls")
os.system("gunicorn NOverBackend.wsgi")
