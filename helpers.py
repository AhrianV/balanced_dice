import random

def get_deck():
    dice_deck = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
 [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
 [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
 [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
 [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
 [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]]
    return dice_deck




def set_weights(deck, last_role):
    weights = []
    for combo in deck:
        if combo == (last_role[0] + last_role[1]):
            weights.append(0.7)
        else:
            weights.append(1)
    return weights





def role(deck, weights):
    role = random.choices(deck, weights=weights, k=1)[0]
    return role



