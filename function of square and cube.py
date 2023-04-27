def myfunc(n):
  return lambda a : a * n

square = myfunc(2)
cube = myfunc(3)

print(square(2))
print(cube(2))
