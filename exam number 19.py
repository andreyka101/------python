# n = 7 
# if n > 5:
#     print("n > 5")
# elif n == 7:
#     print ("n == 7")
# else:
#     if n == 7:
#         print ("n == 7")



# def f(x, h):
#     if h == 3 and x >= 65:
#         return 1
#     elif h == 3 and x < 65:
#         return 0
    
#     # это нужно ,если программа не сработала , не нужно
#     # elif x >= 65 and h < 3:
#     #     return 0

#     else:
#         return f(x + 1, h + 1) or f(x * 2, h + 1)
 
# for x in range(1, 65):
#     if f(x, 1) == 1:
#         print(x)
#         break






# def f(x, h):
#     if h == 4 and x >= 65:
#         return 1
#     elif h == 4 and x < 65:
#         return 0
#     elif x >= 65 and h < 4:
#         return 0
#     else:
#         if h % 2 != 0:
#             return f(x + 1, h + 1) or f(x * 2, h + 1)   # стратегия победителя
#         else:
#             return f(x + 1, h + 1) and f(x * 2, h + 1)  # стратегия проигравшего
 
# for x in range(1, 65):
#     if f(x, 1) == 1:
#         print(x)