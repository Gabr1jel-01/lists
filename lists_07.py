#numbers = []

#for i in range(100):
   # numbers.append(i)

numbers = list(range(100))

first_element = numbers[0]
last_element = numbers[-1]

print()
print(numbers)
print()
print(first_element)
print(last_element)
print()

new_list = []
for i in range(10, 21): # -> 10,11,12,...,19,20
    new_list.append(numbers[i])
    
print()
print(new_list)
print()


new_list = numbers[10 : 21]
print()
print(new_list)
print()