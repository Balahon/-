x = input()
if  x.count("[") == x.count("]") and x.count("{") == x.count("}") and x.count("(") == x.count(")"):
    print("True")
else:
    print("False")