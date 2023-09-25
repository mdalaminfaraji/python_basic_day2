def full_name(firs, last):
    name=f'full Name is: {firs} {last}'
    return name
# take parameters in order(serial wise)
# name=full_name('Alu', 'kodu')
name=full_name(last='alue', firs="345")
print(name)

def my_car(name, weight, *model, **others):
    full_name=f'{name} weight is: {weight}'
    print(full_name)
    print(model)
    for val in model:
        print (val)
    print(others)
    for key , val in others.items():
        print(key, val)


my_car('vlv', 456, 'bangla', 'vai', caka=456, window=455)

# returns multiple things from an array
def a_lot (num1, num2):
    sum=num1+num2
    mul=num2*num1
    # return[sum, mul]
    return sum, mul
val=a_lot(34, 234)
print(val)

    