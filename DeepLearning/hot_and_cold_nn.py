import helpers
import numpy as np

weight = 0.5
input = 0.5
goal_prediction = 0.8
error_modifier = 0.001

def neural_network(input, weight):
    prediction = input * weight
    return prediction

for i in range(1101):
    prediction = neural_network(input, weight)
    error = (prediction - goal_prediction) ** 2

    print("Error: ", error, " Prediction: ", prediction)

    up_prediction = neural_network(input, weight + error_modifier)
    up_error = (up_prediction - goal_prediction) ** 2

    down_prediction = neural_network(input, weight - error_modifier)
    down_error = (down_prediction - goal_prediction) ** 2

    if(down_error < up_error):
        weight -= error_modifier
    
    if(up_error < down_error):
        weight += error_modifier
