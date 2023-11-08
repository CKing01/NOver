import os
os.system("python3 manage.py makemigrations")
os.system("python3 manage.py migrate")
os.system("python3 manage.py collectstatic")
os.system("/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip")
os.system("pip install -U g4f")
os.system("gunicorn NOverBackend.wsgi")
