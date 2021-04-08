# day26NestedLogic.py
# author: william pulkownik
# simple logic / arithmetic program to calculate late fee

# collect space separated single line inputs representing the return date and due date
rDay, rMonth, rYear = [int(x) for x in input().split()]
dDay, dMonth, dYear = [int(x) for x in input().split()]
# calculate the differences between dates
#dayDiff, monDiff, yrDiff = rDay-dDay, rMonth-dMonth, rYear-dYear

if (rYear, rMonth, rDay) <= (dYear, dMonth, dDay):
    print('0')
elif (rYear, rMonth) == (dYear, dMonth):
    print(f'{15 * (rDay-dDay)}')
elif rYear == dYear:
    print(f'{500* (rMonth-dMonth)}')
else:
    print('10000')
