# Q.03.1.2 Identikit of the string
def String(s):
  for chr in s:
    if chr.isdigit():
      print("The string contains numbers")
      break

  if (s.isupper()):
    print("all letters are capital")

  if (s.islower()):
    print("All letters are lower")

  if (s.isdigit()):
    print("All chars are digits")

  if (s.isalnum()):
    print("String contains letters and numbers not symbols")

  if(s[0].islower()):
    print("The string starts with lowercase letter")

  if (s.endswith(".")):
    print("String ends with point")
      
s = input("Please Enter the String: ")
String(s)
####################################################################################################
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
