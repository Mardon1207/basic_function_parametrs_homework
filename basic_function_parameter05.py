# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(matn):
    s=0
    i=0
    while i<len(matn):
        if matn[i] in ('a','e','i','o','u','A','E','I','O','U'):
            s+=1
        i+=1
    return s
print(count_vowels(matn="Hello World!"))
    
