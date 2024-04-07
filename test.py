s = "1991-05-28"
t = ""

for i in s:
    if i == "-":
        break
    t += i
print(t)

print(s.split("-")[0])