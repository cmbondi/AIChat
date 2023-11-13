from flask import Flask, render_template, request
from functions import get_response

app = Flask(__name__)

# Main Page route to deliver index page and handle form request to API call
@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == "POST":
        role = request.form["role"]
        question = request.form["question"]
        response = get_response(role, question)
        return render_template('index.html',
                               role=role,
                               question=question,
                               response=response
                               )
    return render_template('index.html')
