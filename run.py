import os
# os.system("python3 manage.py makemigrations")
# os.system("python3 manage.py migrate")
os.system("gunicorn NOverBackend.wsgi")
