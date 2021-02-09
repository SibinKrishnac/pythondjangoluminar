#accepts only number values
from functools import reduce #this is to be done
# lst=[10,11,12,13,14,15]
# sum=reduce(lambda no1,no2:no1+no2,lst)
# print(sum)

lst=[10,11,12,13,14,15]
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)

# low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
# print(low)


