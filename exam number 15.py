# for a in range(1000):
#     t = 0
#     for x in range(1000):
#         if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
#             t+=1
#     if (t == 1000):
#         print(a)
#         break



# p=range(4, 16)
# q=range(12,20)
# A=[int(i) for i in range(1,16)]
# for x in range(100):
#     if (((x in p) and ((x in q))) <= (x in A)):
#         A=A[1:]
#     else:
#         print(len(A))


# print ("5" in "5")



# for a in range(1000):
#     t = 0
#     for x in range(1000):
#         if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
#             t+=1
#     if (t == 1000):
#         print(a)
#         break



# for a in range():
#     k = 0
#     for x in range(1, 1000):
#         if (x%a!=0)<=((x%6==0)<=(x%4!=0)):
#             k += 1
#     if k == 999:
#         print(a)
#         break




for a in range(300, 0, -1): 
    k = 0
    for x in range(100):
        for y in range(100):
            if (2*x + 3*y < 30) or (x + y >= a):
                k += 1
    if k == 100*100:
        print(a)
        break