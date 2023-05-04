from flask import jsonify
from app import app

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route('/')
def index():
    return jsonify(incomes)
