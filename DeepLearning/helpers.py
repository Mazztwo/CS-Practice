# Helper functions

def elementwise_multiplication(vec_a,vec_b):
    assert(len(vec_a) == len(vec_b))
    product = []

    for i in range(len(vec_a)):
        product.append(vec_a[i] * vec_b[i])

    return product
    
def elementwise_addition(vec_a,vec_b):
    assert(len(vec_a) == len(vec_b))
    sum = []

    for i in range(len(vec_a)):
        sum.append(vec_a[i] + vec_b[i])
    
    return sum

def vector_sum(vec_a):
    sum = 0

    for n in vec_a:
        sum += n

    return sum

def vector_average(vec_a):
    average = vector_sum(vec_a) / len(vec_a)

    return average

def weighted_sum(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))

    prod = elementwise_multiplication(vec_a, vec_b)
    wsum = vector_sum(prod)
    
    return wsum
