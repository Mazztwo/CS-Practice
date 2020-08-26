# Gradient Descent Neural Network

weight = 0.5
true_prediction = 0.8
input = 0.5

def neural_network(input, weight):
    prediction = input * weight
    return prediction

def gradient_descent_learner(input, weight, true_prediction):
    for i in range(100):
        prediction = neural_network(input, weight)
        error = (prediction - true_prediction) ** 2 # Mean Squared Error
        gradient_descent_modifier = (prediction - true_prediction) * input
        weight -= gradient_descent_modifier
        print("Iteration: ", i, " Prediction: ", prediction, " Error: ", error)

gradient_descent_learner(input, weight, true_prediction)