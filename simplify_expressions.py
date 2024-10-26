# Problem 1: Simplify the following expression
a = True
b = False
c = True
result1 = a and (b or c)
answer1 = (a and b) or (b and c)
# Problem 2: Simplify the following expression
x = True
y = False
result2 = x or (x and y)
answer2 = x
# Problem 3: Simplify the following expression
p = False
q = True
result3 = not (p or q)
answer3 = not p and not q
# Problem 4: Simplify the following expression
m = True
n = False
result4 = m and not m
answer4 = False
# Problem 5: Simplify the following expression
d = True
e = False
result5 = d or not d
answer5 = True

print(result1)
print(answer1)
print(result2)
print(answer2)
print(result3)
print(answer3)
print(result4)
print(answer4)
print(result5)
print(answer5)
