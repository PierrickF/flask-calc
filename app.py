from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("app.html")

@app.route("/calculate", methods=['POST'])

def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
        return render_template('app.html', result=result)

    elif operation == 'subtract':
        result = subtract(num1, num2)
        return render_template('app.html', result=result)

    elif operation == 'multiply':
        result = multiply(num1, num2)
        return render_template('app.html', result=result)

    elif operation == 'divide':
        result = divide(num1, num2)
        return render_template('app.html', result=result)
    else:
        return render_template('app.html')

def add(num1, num2):
    return float(num1) + float(num2)

def subtract(num1, num2):
    return float(num1) - float(num2)

def multiply(num1, num2):
    return float(num1) * float(num2)

def divide(num1, num2):
    return float(num1) / float(num2)
