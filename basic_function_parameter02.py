# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(suma):
    i=0
    s=0
    while i<len(suma):
        s+=suma[i]
        i+=1
    return s
print(calculate_sum(suma=[2,4,6,8]))