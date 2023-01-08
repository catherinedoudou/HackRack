# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
#phone = ["sam 99912", "tom 8627", "des 8968724"]
n = 3
phonenumber = tuple(input().split() for i in range(n))
phonebook = {key: value for key, value in phonenumber}
while True:
    try:
        name=input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not Found")
    except:
        break
