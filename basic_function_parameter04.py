# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average(suma):
    i=0
    s=0
    while i<len(suma):
        s+=suma[i]
        i+=1
    return s/len(suma)
print(calculate_average(suma=[2,4,6,8]))