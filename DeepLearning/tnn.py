import helpers
import numpy as np

###########################################
# NN, 1 input, 1 output
input_data = [8.5, 9.5, 10, 9]
weight = 0.1

def t_neural_network(input, weight):
    pred = input * weight
    return pred

network_input = input_data[0]
prediction = t_neural_network(network_input, weight)

# print ("Win prediction: ", prediction)

###########################################
# NN, 3 inputs, 1 output
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

#print("Win prediction: ", prediction)

###########################################
# NN, 3 inputs, 1 output, with numpy
weights2 = np.array([0.1, 0.2, 0])

def t_neural_network_three(input, weights):
    pred = input.dot(weights)
    return pred

toes2 = np.array([8.5, 9.5, 9.9, 9.0])
win_loss_record2 = np.array([0.65, 0.8, 0.8, 0.9])
num_fans2 = np.array([1.2, 1.3, 0.5, 1.0])

network_input2 = np.array([toes2[0], win_loss_record2[0], num_fans2[0]])
prediction2 = t_neural_network_three(network_input2, weights2)

#print("Win prediction: ", prediction2)

###########################################
# NN, 1 input, 3 outputs
weights3 = [0.3, 0.2, 0.9]
win_loss_record3 = [0.65, 0.8, 0.8, 0.9]
network_input3 = win_loss_record3[0]

def ele_mul(number, vector):
    output = []

    for i in range(len(vector)):
        output.append(number * vector[i])
    
    return output

def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred

prediction3 = neural_network(network_input3, weights3)

#print("Percent of team hurt: ", prediction3[0])
#print("Win prediction: ", prediction3[1])
#print("Percent of players sad: ", prediction3[2])

###########################################
# NN, 3 inputs, 3 outputs
weights4 = [
    [0.1, 0.1, -0.3], # hurt?
    [0.1, 0.2, 0.0],  # win?
    [0.0, 1.3, 0.1]   # sad?
]

def vec_mat_mul(vector, matrix):
    assert(len(vector) == len(matrix))
    output = []

    for i in range(len(vector)):
       output.append(
           helpers.vector_sum(helpers.elementwise_multiplication(vector, matrix[i]))
       ) 

    return output

def neural_network2(input, weights):
    pred = vec_mat_mul(input, weights)
    return pred

toes3 = [8.5, 9.5, 9.9, 9.0]
win_loss_record4 = [0.65, 0.8, 0.8, 0.9]
num_fans3 = [1.2, 1.3, 0.5, 1.0]

neural_network_input = [toes3[0], win_loss_record4[0], num_fans3[0]]
prediction4 = neural_network2(neural_network_input, weights4)

#print("Percent of team hurt: ", prediction4[0])
#print("Win prediction: ", prediction4[1])
#print("Percent of players sad: ", prediction4[2])

###########################################
# NN, 3 inputs, 3 outputs, 1 hidden layer, with numpy
ih_wgt = np.array([
    [0.1, 0.2, -0.1],
    [-0.1, 0.1, 0.9],
    [0.1, 0.4, 0.1]
])

hp_wgt = np.array([
    [0.3, 1.1, -0.3],
    [0.1, 0.2, 0.0],
    [0.0, 1.3, 0.1]
])

input_weights = [ih_wgt, hp_wgt]

def hidden_neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes4 = np.array([8.5, 9.5, 9.9, 9.0])
win_loss_record5 = np.array([0.65, 0.8, 0.8, 0.9])
num_fans4 = np.array([1.2, 1.3, 0.5, 1.0])

network_input4 = np.array([toes4[0], win_loss_record5[0], num_fans4[0]])

prediction5 = hidden_neural_network(network_input4, input_weights)

print("Percent of team hurt: ", prediction5[0])
print("Win prediction: ", prediction5[1])
print("Percent of players sad: ", prediction5[2])
