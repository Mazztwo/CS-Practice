# GCD of two ints


def recurseGCD(divisor, num1, num2):

    smaller = min(num1, num2)

    if(divisor <= smaller):
        gcd = max(divisor, recurseGCD(divisor+1, num1, num2))

        if(num1 % gcd == 0 and num2 % gcd == 0):
            return gcd
        
        return gcd - 1
        
    else:
        if(num1 % divisor == 0 and num2 % divisor == 0):
            return divisor
        
        return divisor - 1

    return gcd


print(recurseGCD(1, 110, 100))




