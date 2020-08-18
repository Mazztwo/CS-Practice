import helpers

###########################################
# NN, 1 input
input_data = [8.5, 9.5, 10, 9]
weight = 0.1

def t_neural_network(input, weight):
    pred = input * weight
    return pred

network_input = input_data[0]
prediction = t_neural_network(network_input, weight)
# print ("Win prediction: ", prediction)

###########################################
# NN, 3 inputs
weights = [0.1, 0.2, 0.0]
toes  = [8.5, 9.5, 9.9, 9.0]
win_loss_rec = [0.65, 0.8, 0.8, 0.9]
num_fans = [1.2, 1.3, 0.5, 1.0]

def t_neural_network_two(input, weights):
    mult = helpers.elementwise_multiplication(input, weights)
    pred = helpers.vector_sum(mult)
    return pred
network_input = [toes[0], win_loss_rec[0], num_fans[0]]
prediction = t_neural_network_two(network_input, weights)

print("Win prediction: ", prediction)
