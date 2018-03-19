input("Insert a string longer than 1");

a=input();
if len(a)<2:
    print("String is shorter than two")
    exit(1)

print(a[0])
print(a[1])
print(a[len(a)-2])
print(a[len(a)-1])