def myfunc():
    for num in range(10):
        yield num ** num

total = range(0,10)
print(tuple(total))