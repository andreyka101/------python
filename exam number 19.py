# n = 7 
# if n > 5:
#     print("n > 5")
# if n == 7:
#     print ("n == 7")
# else:
#     print ("else")



def f(x, h):
    print(x, h)
    if h == 3 and x >= 65:
        return 1
    elif h == 3 and x < 65:
        return 0
    # это нужно ,если программа не сработала , не нужно
    # elif x >= 65 and h < 3:
    #     return 0
    else:
        return f(x + 1, h + 1) or f(x * 2, h + 1)
 
for x in range(1, 65):
    if f(x, 1) == 1:
        print(x)
        break