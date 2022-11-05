x = input()
b = ""
for i in x:
    if i == " ":
        continue
    else:
        b += i
c = 0
for i in range(len(b)//2):
    if b[i] == b[-(i+1)]:
        c = 1
        continue
    else:
        print("false")
        break
if c == 1:
    print("true")