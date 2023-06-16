# for a in range(1000):
#     t = 0
#     for x in range(1000):
#         if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
#             t+=1
#     if (t == 1000):
#         print(a)
#         break


p=range(4, 16)
q=range(12,20)
for A in range(100):
  print(type(A))
  for x in range(100):
    if (((x in p) and ((x in q))) <= (x in int(A))):
      A=A[1:]
    else:
      print(len(A))


# print ("5" in "5")