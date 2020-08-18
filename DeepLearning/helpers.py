###########################################
# Helper Functions

# Multiplies the elements of two equal vectors together
# into a third vector 
def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    vec_mult = []

    for i in range(len(vec_a)):
        vec_mult.append(vec_a[i] * vec_b[i])
    
    return vec_mult

# Sums the elements of two equal vectors together
# into a third vector
def elementwise_addition(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    vec_sum = []

    for i in range(len(vec_a)):
        vec_sum.append(vec_a[i] + vec_b[i])
    
    return sum

# Finds the sum of the numbers in a vector
def vector_sum(vec):
    sum = 0

    for i in range(len(vec)):
        sum += vec[i]
    
    return sum

# Finds the average of the numbers in a vector
def vector_average(vec):
    assert(len(vec) > 0)
    sum = 0

    for i in range(len(vec)):
        sum += vec[i]
    
    return (sum / len(vec))