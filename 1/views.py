from flask import url_for, request


def hello_world():
    return "Hello World From Maktab 78 (Akbar)"


def power(x, y):
    return f"{x} ** {y} = {x ** y}" if x or y else "Enter x and y value!"


def test():
    return request.method


def info(endpoint: str) -> str:
    return f" info : {url_for(endpoint)} <br> {url_for('power', x=3, y=5)}"


def not_found(e):
    return "Not found error | Maktab 78", 404
