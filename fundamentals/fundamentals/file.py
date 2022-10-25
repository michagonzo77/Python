num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration - initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration - initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration - initialize tuple
print(type(fruit)) # type check - tuple
print(pizza_toppings[1]) # log statement - access value in list
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # access value in dictionary and log
person['name'] = 'George' #  variable change value - dictionary
person['eye_color'] = 'blue' #  variable add value - dictionary
print(fruit[2]) # access tuple - print banana

if num1 > 45: # conditional if statement
    print("It's greater") #log statement
else: # conditional else statemnet
    print("It's lower") #log statement

if len(string) < 5: # conditional if statement -- length check
    print("It's a short word!") #log statement
elif len(string) > 15: # conditional elif statement -- length check
    print("It's a long word!") #log statement
else: # conditional else statemnet
    print("Just right!") #log statement

for x in range(5):
    print(x) #log statement
for x in range(2,5): #for loop
    print(x) #log statement
for x in range(2,10,3): #for loop increment by 3 starting at 2
    print(x) #log statement
x = 0 # variable declaration
while(x < 5): #while start
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() # list - remove last value
pizza_toppings.pop(1) #list remove value at index of 1

print(person) # print dictionary
person.pop('eye_color') # delete value from dictionary
print(person) # print dictionary

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if statement
        continue #continue (skip if pepperoni)
    print('After 1st if statement')
    if topping == 'Olives': # conditional if statement
        break # break (stop for loop if true)

def print_hello_ten_times(): # function initialize
    for num in range(10): # for loop
        print('Hello') #log statement

print_hello_ten_times() #run function

def print_hello_x_times(x): # function initialize
    for num in range(x): #for loop 
        print('Hello') #log statement

print_hello_x_times(4) #run function with parameter 4

def print_hello_x_or_ten_times(x = 10): # function initialize
    for num in range(x): #for loop 
        print('Hello') #log statement

print_hello_x_or_ten_times() #print 10 times
print_hello_x_or_ten_times(4) #print 4 times


"""
Bonus section
"""

# print(num3) NameError: name <variable name> is not defined
# num3 = 72 variable declaration
# fruit[0] = 'cranberry' TypeError: 'tuple' object does not support item assignment 
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  AttributeError: 'tuple' object has no attribute 'pop'
