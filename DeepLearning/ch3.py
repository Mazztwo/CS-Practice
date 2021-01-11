#3.24 Simplest neural network
weight = 0.1

def prediction(input, weight):
    pred = input * weight
    return pred

num_toes = [8.5, 9.5, 10, 9]
input = num_toes[0]

pred = prediction(input, weight)
print(pred)

