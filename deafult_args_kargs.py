def sum(num1, num2):
    result=num1+num2
    return result

total = sum(99, 11)
# print('total: ', total)

# args
def all_sum(*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum
total=all_sum(34,54,65,56,45)
print('all sum:', total)

