# Set - an unordered pair/collection of numbers/values that are unique.
# Jb hme bola jaaye ki list mein se duplicate numbers of remove krna hai. 

# numbers = [1,1,1,1,1,2,3,4]

# print(list(set(numbers)))

# fruits = set()

# # add() -> set mein values add krega
# fruits.add("Apple")
# fruits.add("Banana")
# fruits.add("Kiwi")

# print(fruits)

# new_fruits = {"Apple", "Orange", "Banana"}

# # union - |

# print(fruits | new_fruits)

# # intersection - &
# print(fruits & new_fruits)


# set_a.union(set_b)
# scores = {100, 200, 300}

# new_scores = {400, 500, 600, 200}

# print(scores.union(new_scores))
# print(new_scores.union(scores))

# # set_a.intersection(set_b)
# print(scores.intersection(new_scores))

# clear()
# scores.clear()
# print(scores) # set() if blank/cleared

# new_scores.clear()
# print(new_scores) 

# difference (-)
# set_a = {1,2,3,4} # 3
# set_b = {1,2,4,6}

# print(set_a - set_b)

# # set_a.difference(set_b)
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))

# # set_a.symmetric_difference(set_b)
# # It returns only the values that are not common on both the sets. Values that are unique.

# print(set_a.symmetric_difference(set_b)) 

# remove() 
# set_a.remove(3)

# print(set_a)

# pop() 
# Set ke case, pop() will remove first item from the set.
# Jbki list mein last item sbse pehle remove hota hai.
# print(set_a.pop())
# print(set_a.pop())
# print(set_a.pop())
# print(set_a.pop())
# print(set_a.pop())


# l = [1,2,3,4,5]
# index= l.index(3)
# result=l[index+1:]+l[:index+1][::-1]
# print(result)

set_a = [1,2,3,4,5]
# print(set_a.pop())
# set_a.remove(1)
# print(set_a)

# a = 10
# b = 5

# a,b = b,a 
# print(a)

# set_a[2], set_a[-1] = set_a[-1], set_a[2]

# print(set_a)