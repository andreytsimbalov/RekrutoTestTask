from flask import request
from app import app


@app.route('/')
def welcome_page():
    name = request.args.get('name')
    message = request.args.get('message')

    if name:
        name = f"Hello {name}!"
    else:
        name = "Rekruto!"

    if message is None:
        message = "Давай дружить!"
    else:   
        message = f"{message}!"
    return f"{name} {message}"
