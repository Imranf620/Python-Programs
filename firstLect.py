
name="imran"
print(name)

if(5>4):
    print("true")
num = 5
num = "five"
print("typecasted", num)

typeCasted = str(5)
print(typeCasted)
print(type(typeCasted))

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

fruits = ["apple","banana", "cherry"]

fruit1, fruit2, fruit3 = fruits
print(fruit1)

res = 'awesome'
def myFunc():
    print("python is ", res)
myFunc()

newName = "imran"

def getMyName():
    global newName
    newName='imran farooq'

getMyName()
print(newName)
print("length", len(newName))

a = "Hello, World!"
print(a[1])

for x in a:
    print(x)

txt = "The best things in life are free!"
print("free" in txt)