# try
# except
# else
# finally

""" 
try:
    file = open("a_randomfile.txt")
    a_dict = {"key": "val"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_randomfile.txt", "w")
    file.write("Hello Error!")
except KeyError as err:
    print(f"The key {err} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise TypeError("I just made this error error")
 """

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human is smool.")


bmi = weight / height**2
print(bmi)
