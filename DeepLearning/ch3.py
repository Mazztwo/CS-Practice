import helpers

#3.24 Simplest neural network
weight = 0.1

def prediction(input, weight):
    pred = input * weight
    return pred

num_toes = [8.5, 9.5, 10, 9]
input = num_toes[0]

pred = prediction(input, weight)
#print(pred)


#3.28 NN w/ multiple inputs
weights = [0.1, 0.2, 0]

def neural_network(input, weights):
    pred = helpers.weighted_sum(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
win_loss_record = [0.65, 0.8, 0.8, 0.9]
num_fans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], win_loss_record[0], num_fans[0]]

pred = neural_network(input, weights)
print(pred)



