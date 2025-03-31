# CONTROL FLOW

# Example for if statement
num1 = 16
if num1 > 15:
    print(num1, "is less than")
    print("I am not an if")



# EXAMPLE FOR IF STATEMENT
num2 = 20
if num2 < 15:
    print(num2, "is less than 15")
    print("I am an if block")
else:
    print(num2, "is greater than or equal to 15")
    print("I am an else block")
print("I am not an if-else block")

# Determine if a number is even or odd
num3 = 8
if num3 % 2 == 0:
    print(num3, "is even")
else:
    print(num3, "is odd")


# Nested if statements
num4 = 41
if num4 > 10:
    print("Above 10")
    if num4 > 20:
        print("and also above 20")
    else:
        print("ut less than or equal to 20")
else:
    print("less than or equal to 10")

# elif statements (more than 2 outcomes)
num5 = -9
if num5 > 0:
    print(num5, "is positive")
elif num5 == 0:
    print("Zero")
else:
    print(num5, "is negative")

# Short hand if statements



# initialize sum and counter
sum_ = 0
i = 1

while i <= n:
    sum_ = sum_ + i
    i += 1      # i = i + 1

# print the sum
print("The sum is", sum_)







# When n = 4:
# The first step of while loop: sum = 1, i = 2
# the second step of while loop: sum = 3, i = 3
# the third step of while loop: sum = 6, i = 4
# the fourth sep of while loop: sum = 10, i = 5


# for loop
print("FOR LOOP EXAMPLES:")
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum:
sum_ = 0
# iterate over the list
for val in numbers:
    sum_ = sum_ + val

print("The sum:", sum_)


# find the max in a list
# print (max(numbers))
max_ = numbers[0]
for val in numbers:
    if val > max_:
        max_ = val
print("Maximum number is:", max_)


# for loop using range()
# range(10)
# range(len(list1))
# range(start, stop, step_size)
# example:
topics = ["Blockchain", "NFTs", "ML"]
# iterate over the list using range
for i in range(len(topics)):
    print("I am interested in", topics[i])

# Question: find the index of max element in a list
# numbers = [6, 5, 3, 8, 4, 11, 2, 5, 4]
index_max = 0
for i in range(len(numbers)):
    if numbers[1] > numbers[index_min]:
        index_min = i
print("The index of the minimum element", index_min)

# FUNCTIONS
print("FUNCTIONS")

def func1(name):
    print("Welcome to our course, " + name)

# Drover Code:
func1("Jack")

def min_index(list_):
    ind_min = 0
    for j in range(len(list_))
        if list_[j] , list_[ind_min]:
            ind_min = j
    return ind_min

# Driver Code
numbers = [6, 5, 3, 8, 4, 11, 2, 5, 4]
min_index(numbers)

