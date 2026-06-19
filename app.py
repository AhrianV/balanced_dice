from flask import Flask, render_template, redirect, url_for

import random

from helpers import get_deck, set_weights, role


app = Flask(__name__)


#func defs and setup

last_role = [0, 0]
rolled = [6,6]

# deffinitons of functions

def restart():
    dice_deck = get_deck()
    global last_role 
    last_role = [0, 0]
    random.shuffle(dice_deck)
    return dice_deck

def reset_deck():
    global dice_deck
    dice_deck = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
 [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
 [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
 [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
 [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
 [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]]
    

def check_shuffle(deck):
    global dice_deck
    if len(deck) <= 12:
        print("shuffle start")
        reset_deck()
        random.shuffle(dice_deck)
        print("shuffle end")

#start code
dice_deck = restart()
print('starting code + setup ran')

# home
@app.route("/")
def home():
    global rolled
    return render_template("index.html", d1="_" + str(rolled[0]), d2="_" + str(rolled[1]))



#execution of weighted dice
@app.route("/turn")
def turn():
    global last_role
    global rolled

    print(f"""
        turn route running (starting). Starting Info: 
        last_role(list) - {last_role}
        current dice_deck(2d list) - {dice_deck}
        """)
    
    weights = set_weights(dice_deck, last_role)
    rolled = role(dice_deck, weights)
    last_role = rolled
    dice_deck.remove(rolled)
    check_shuffle(dice_deck)

    print(f"""
        turn route running (ending). Ending Info: 
        rolled(list) - {rolled}
        current dice_deck(2d list) - {dice_deck}
        last_role(list) - {last_role}
        """)

    return redirect(url_for("home"))

 
# code to make app.py run
if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)





