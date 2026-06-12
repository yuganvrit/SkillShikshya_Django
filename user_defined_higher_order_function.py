def process_multiplication(first, second):
    def actual_multiply(first_value, second_value):
        return first_value * second_value
    

    return actual_multiply(first, second)

result = process_multiplication(2,3)
print(result)


#classwork:
#createa higher order function named as global_divider which return 
# a operation function that actually divides taking two numbers as argument.


def global_divider():
    def operation(first_value, second_value):
        if second_value == 0:
            return 'The denominator cannot be 0'
        return first_value / second_value
    

    return operation

result = global_divider()
print(result(6,0))



#create a more sophosticated higher order function as above additional there is another intermediate child function that validates if divisible is not zero

