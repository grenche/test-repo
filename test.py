print()
print('Quesiton 1')

w = -1
x = 100
y = 10
z = 55

for i in range(4):
    x = x + z
    print(x % y)

y = -50
print(y % z)
print(w)



print()
print('Quesiton 2')

for x in range(3):
    for y in range(x):
        print(x)
        
        
print()
print('Quesiton 3')
        
for i in range(20):
    if i % 4 == 1:
        print("i", i)
        print(type("i"))
        

print()
print('Quesiton 4')       
        
fave_color = 'blue'
fave_fruit = 'cherry'
age = 90
if fave_color == 'blue':
    print(age)
elif age > 50:
    print(fave_fruit)
if fave_fruit != 'apple':
    print(fave_color)
elif age < 100:
    print('definitely conflicting')

    
print()
print('Quesiton Five')  
    
a = 3
while a > 0:
    for i in range(2):
        print(a)
    a = a - 1
print(a)



print()
print('Quesiton Six')

my_range = int(input("Pick a number: "))
num_a = 0
num_b = 0
for i in range(1, my_range + 1):
    if i % 3 == 0:
        num_a = num_a + 3
    elif i % 2 == 1:
        num_b = num_b + 1
    else:
        print(i)
print(num_a, num_b)
print("Not a conflict")



print()
print('Quesiton 7')
print("Also, not a conflict")

password = ""
for ch in "Mississippi".split("i"):
    password = password + ch

print(password)



print()
print('Quesiton 8')

myString = "Northfield"
print(myString)
blah = myString.lower()
print(blah)
print(myString[:5])
print(myString[5:])
print("Yes this defintely conflicts")