
# сложный пример
# num = 452022
# count = 0
# while True:
#     sqrtI = round(num ** 0.5)
#     for j in range(2, sqrtI + 1):
#         if num % j == 0:
#             if (j + num // j) % 7 == 3:
#                 count += 1
#                 # print(num, ' ', j + num // j);
#                 break
#             else:
#                 break
#     if count == 5:
#         break
#     num += 1


# w = round(1200 ** 0.5)
# print(w)

# здесь неправильно числа в ответе повторяются 2 раза
for i in range(174457,174505+1):
    for q in range(2, i+1):
        if i % q == 0:
            print(q , i//q)



# здесь правильно , но посмотри примеры ещё
for i in range(174457,174505+1):
    for q in range(2, (i // 2) +1):
        if i % q == 0:
            print(q , i//q)
# print(174505//2)