import os
os.system("/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip")
os.system("pip install -U g4f")
import g4f
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world code in python"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')
# os.system("python manage.py makemigrations NOverBackend")
# os.system("python manage.py migrate NOverBackend")
# # os.system("python3 manage.py collectstatic")
# os.system("ls")
# os.system("gunicorn NOverBackend.wsgi")
