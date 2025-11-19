print("A" + "B" * 3 + "C" * 0 + "D")  
a = "Hello"
b = "World"
c = 5
print(a+" "+b)

age = 36
#This will produce an error:
txt = f"My name is John, I am { age}"
print(txt)
txt = "We are the so-called."
print(txt.capitalize())
print(txt.casefold())

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 5
x += 3
print(x)