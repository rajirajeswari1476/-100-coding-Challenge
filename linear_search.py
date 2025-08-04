list=[10,20,30,40]
element=30
position=1
for i in range(len(list)):
    if element==list[i]:
        position=i
        break
if position==1:
    print(f"{element} not found")
else:
    print(f"{element} found at the {position}")
