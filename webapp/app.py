import random
from flask import Flask, render_template, url_for
from .apigets import get_pokemon


NUM_TEAM = 6
MAX_POKENUM = 898  # maximum species number to pull from
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    nums_to_get = (random.randint(1, MAX_POKENUM) for ii in range(NUM_TEAM))
    pokemon = (get_pokemon(num) for num in nums_to_get)
    return render_template('index.html', pokemon=pokemon)


if __name__ == '__main__':
    app.run()
