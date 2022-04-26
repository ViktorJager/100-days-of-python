''' 
# open uses read mode="r" by default
with open("C:/Users/jagervik/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)
 '''

with open("../../../../../Users/jagervik/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)


''' 
with open("new_file.txt", mode="a") as file:
    file.write("New file.")

 '''


# Alternative to open files:
''' 
file = open("my_file.txt")
content = file.read()
print(content)

# Close file after opening, free up resources.
file.close() 
'''