message = "wiqceeo1"
# mes = "abc"
key = "key"
 

# for i in range(len(message)):   
#     print(chr(ord(message[i]) ^ ord(mes[i])))


mes = [ord('d')^10, ord('e')^2, ord('f')^10]



def enc(k, m): 
    for i in range(len(k)):
        ki= ord(k[i])
        # mi=ord(m[i])
        print((ki ^ m[i])&10, end = " ")


enc(key,mes)


# f(m1) = 10 2 10 
# f(10 2 10 + m2) = 0 2 0 
# 



# m1m2m3
# f(m1) = c1 -> 6
# f(c1 + m2) = c2 -> 777
# f(c2 + m3) = c3

# m1m4m5
# f(m1) = c1 -> 6
# f(c1 + m4) = c2' -> 666
# f(c2' + m3') = c3

# c3 = 290