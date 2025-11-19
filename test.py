print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = "Hello, World!"
print(len(a))

for x in "banana":
  print(x)

txt1 = "The best things in life are free!"
print("free" in txt1)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt3 = "The best things in life are free!"
print("expensive" not in txt3)

# Slicing Strings

b = "Hello, World!"
print(b[5:])

b = "Hello, World!"
print(b[-5:-2])

a = " Hello, World! "
print(a.strip())

a = "HeHlo, Horld!"
print(a.replace("H", "J"))

a = "Hello! World! rohiy"
print(a.split("!")) 

