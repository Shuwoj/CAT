# finding GCD

def gcd_recursive(a, b):
    if b == 0:    # Base case: if b becomes 0, return a (which is the GCD)

        return a
   
    else:   # Recursive case: calculate the remainder and call the function with updated values
        return gcd_recursive(b, a % b)


num1 = 14  #  taking both num as intput
num2 = 16
result = gcd_recursive(num1, num2)
print("The GCD of {} and {} is: {}".format(num1, num2, result)) # printing the result

