import os
# os.system("python3 manage.py makemigrations")
# os.system("python3 manage.py migrate")
os.system("pip3 install -U g4f")
os.system("gunicorn NOverBackend.wsgi")
