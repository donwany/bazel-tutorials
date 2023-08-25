from calculator.calc import Calculator
from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def randomNumberCalculator():
    randomInt1 = randint(0, 250)
    randomInt2 = randint(0, 250)
    results = Calculator.add(randomInt1, randomInt2)
    return f"{randomInt1} + {randomInt2} = {results}?"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1957, debug=True)
