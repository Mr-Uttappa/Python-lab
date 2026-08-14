# import datetime

# x = datetime.datetime(2018, 1, 30)

# print(x.strftime("%A a"))



f = open("demofile.txt")


import os

if os.path.exists("demofile.txt"):
    print("demofile.txt allready exists")

else:
    f = open("demofile.txt","x")

# # print(f.read())
# print(f.readline())
# print(f.readlines())


# with open("demofile.txt", "w") as file:
#     # print(file.readlines())
#     f.write("\nNow the file has more content!")