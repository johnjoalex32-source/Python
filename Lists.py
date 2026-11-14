#Create an empty list
empty_list = []
print()

# A list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Use * operator
triples = [1, 2, 3] * 3
print(triples)

#reverse the given list
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList,"\n")



# function to check whether
# first and last character of words match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba','1221'])
print("Number of words having first and last character same:", count)



L = [4,  5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)

# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
    count += i

# divide the total elements by
# number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()

# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])
