def test_function(x):
    a=x**2
    def inner_function(x):
        a = x*10
        if a < 0:
            print("Ошибка")
        else:
            print ("Я в области видимости функции test_function")
    inner_function(x)
    return a

d=test_function(7)
print(d)
#a = inner_function(4) - ошибка
#print(a)