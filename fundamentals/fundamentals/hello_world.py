# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello World", name)	# with a comma
print("Hello World " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", 42 )	# with a comma
print("Hello " + str(42))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

print("I love to eat %s" %fave_food1)


# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
print(drawers[1])

# Change "pens" to "useless manuals"
drawers[2] = "useless manuals"
# Change the first value to whatever is the second value
drawers[0] = drawers [1]
# What should the list look like now?
# Print the list! Does it match your prediction?
print(drawers)

nums = [1,2,3,4,5]
nums.append(99)
print(nums)


words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']



some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
print(len(some_nums))
# Use antoher python built-in function and print the result.
some_nums.append(220)
print(some_nums)
# Remove an item from the list. Remember to verify that it was removed.
some_nums.pop()
print(some_nums)
# Utilize a method from the documentation and print the result.
print(some_nums.count(2))

x = [5,34,10,1,6]
x += 2

print(x)