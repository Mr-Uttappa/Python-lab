# if, elif, else, condintion explaining 

 # example number 1


light = "Blue"


if (light == "Red"):
    print("Stop")
elif( light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Ready for Go")
else:
    print("light is Broken")



# example number 1


# Traffic light example with if, elif, else

if → first condition
elif → next possible condition
else → fallback if none match


# Code 

traffic_light = input("Enter the traffic light color (red, yellow, green): ").lower()

if traffic_light == "red":
    print("Stop! 🚦")
elif traffic_light == "yellow":
    print("Slow down and prepare to stop. ⚠️")
elif traffic_light == "green":
    print("Go! ✅")
else:
    print("Invalid color entered. Please choose red, yellow, or green.")





for i in range(1, 7):
  
    for j in range(6 - i):
        print(" ", end="")

    for k in range(i):
        print("*", end=" ")
  
    print()








# a = 6   # number of rows

# for i in range(a, 0, -1):   # start from 6 down to 1
#     # print spaces
#     for j in range(a - i):
#         print(" ", end="")

#     # print stars
#     for k in range(i):
#         print("*", end=" ")

#     # move to next line
#     print()


















File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file: