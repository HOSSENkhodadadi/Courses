# Q.03.1.3
long = input("Please enter the long sequence: ")
short = input("Please enter the short sequence: ")

flag = False
counter = 0

for i in range(len(long)-1):
    if long[i] == short[0] and long[i+1] == short[1] and long[i+2] == short[2]:
        flag = True
        counter += 1
        print(f"short sequence found at: {i}")

if flag:
    print(f"long sequence contains the short sequence and it has repeated {counter} times in it")
####################################################################################################