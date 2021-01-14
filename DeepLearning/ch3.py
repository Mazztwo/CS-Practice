import helpers
import numpy as np

#######################################
#3.24 Simplest neural network, one input and one output
weight = 0.1

def prediction(input, weight):
    pred = input * weight
    return pred

num_toes = [8.5, 9.5, 10, 9]
input = num_toes[0]

pred = prediction(input, weight)
#print(pred)

#######################################
#3.28 nn w/ multiple inputs and one 
weights = [0.1, 0.2, 0]

def neural_network_mult_input(input, weights):
    pred = helpers.weighted_sum(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
win_loss_record = [0.65, 0.8, 0.8, 0.9]
num_fans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], win_loss_record[0], num_fans[0]]

pred = neural_network_mult_input(input, weights)
#print(pred)

#######################################
#3.37 nn w/ one input and multiple outputs
weights = np.array([0.3, 0.2, 0.9])

def neural_network_mult_output(input, weights):
    input_vec = [input] * len(weights)
    pred = helpers.elementwise_multiplication(input_vec, weights)
    return pred

input = win_loss_record[0]
pred = neural_network_mult_output(input, weights)
#print(pred)

#######################################
# 3.38 nn w/ multiple inputs and multiple outputs
weights = [[0.1, 0.1, -0.3],
           [0.1, 0.2, 0.0],
           [0.0, 1.3, 0.1]]

def neural_network_mult_input_mult_out(input, weights):
    pred = vec_mat_mult(input, weights)
    return pred

def vec_mat_mult(vec, mat):
    assert(len(vec) == len(mat))
    result = []

    for i in range(len(vec)):
        result.append(helpers.weighted_sum(vec, weights[i]))

    return result

input = [toes[0], win_loss_record[0], num_fans[0]]
pred = neural_network_mult_input_mult_out(input, weights)

print(pred)