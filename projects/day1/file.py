length = 1000001

with open("number_code.py", "w") as f:

    f.write("def number_printer():\n")

    f.write('\tnumber = int(input("Enter number: "))\n')

    f.write(f"\tif number == 0:\n")
    f.write(f"\t\tprint('number is 0')\n")

    for x in range(1, length):
        f.write(f"\telif number == {x}:\n")
        f.write(f"\t\tprint('number is {x}')\n")

    f.write(f"\telse:\n")
    f.write(f"\t\tprint('your number is not a number')\n")
    f.write("\nnumber_printer()")
