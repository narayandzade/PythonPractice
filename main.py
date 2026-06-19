mylist = [1,2,3,4,5]


squers = list(map(lambda x: x*x, mylist))
print(squers)



evens = list(filter(lambda x: x%2==0, mylist))

print(evens)

from functools import reduce



factor = reduce(lambda x,y: x*y, mylist)
print(factor)