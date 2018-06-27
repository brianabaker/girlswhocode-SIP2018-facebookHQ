'''
1. Variables: Print out variable values.
2. Variables: Check that the variable exists.
3. Variables: Check variable data type.
4. Variables: Check variable operations.
5. Conditionals: Add prints inside conditional.
6. Conditionals: Check condition.
7. Conditionals: Check if variable created in a conditional doesn’t exist.
8. While Loops: Check if conditional is incorrect.
9. For Loops: Check if range is incorrect. '''

##Variables - print out the variable value

addition = 5 + 7
print(5+7)
## want to make sure variable addition is set to 12

##Variables: Check that the variable exists.
bananas = "yummy"
(apple)
## what do we expect to happen

## Variables: Check variable data type.
numberOne = "one"
numberOne += 1
print(numberOne)
##What error do we expect?

##Variables: Check variable operations.
num1 = 4
num2 = 9
print(num1+num2)

moreNum = 8
anotherNum = 4
print(moreNum//anotherNum)
print(moreNum%anotherNum)
print(anotherNum%moreNum)
##Whats the difference between them?

##Conditionals: Add prints inside conditional/Check condition.
print("Enter a number 1-10!")
x = int(input())

if x%2 == 0:
    print("x is even!")
    print(x)
else:
    print ("x is odd")
##Why is printing the value of x important in the conditional?

##While loops: check if conditional is not incorrect
    ##We want only 6 cats, what's wrong with this program?
numCats = 2

while (numCats <= 6):
    numCats += 1
    print("I love cats, I need more")

print("Sad... no more cats for me")
print(numCats)

##For Loops: Check if range is incorrect

colors = ['blue','red','green']
for i in range(len(colors)):
    print(i)
