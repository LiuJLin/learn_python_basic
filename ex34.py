#Accessing Elements of Lists
#How to access the elements of a list.
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print("Please input a number (0~5).")
num_cardinal = int(input())
print("The animal at %d:"% num_cardinal)
while(not(num_cardinal >= 0 and num_cardinal <= 5)):
    print("OUT OF SCALES! Please input a number from 0 on, but not larger than 5.")
    num_ordinal = int(input())
    print("The animal at %d\n>>"% num_cardinal)
print(animals[num_cardinal])

print("Please input a number (1~6).")
num_ordinal = int(input())
print("The No.%d animal:"% num_ordinal)
while(not(num_cardinal >= 1 and num_cardinal <= 6)):
    print("OUT OF SCALES! Please input a number from 1 on, but not larger than 6.")
    num_ordinal = int(input())
    print("The No.%d animal"% num_ordinal)
print(animals[num_ordinal - 1])
