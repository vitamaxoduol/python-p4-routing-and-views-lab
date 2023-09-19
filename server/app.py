#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_route(parameter):
    # To address the test_print_text_in_console test:
    print(parameter)
    return parameter

@app.route('/count/<int:range_val>')
def count(range_val):
    numbers = [str(x) for x in range(0, range_val + 1)]
    return "\n".join(numbers)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return f"<h1>Invalid operation</h1>", 400
    return str(result) 
    
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
