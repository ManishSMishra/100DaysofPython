with open('Day31\data.txt',encoding="utf8") as data:
    lines=data.readlines()
print(lines)

for line in lines:
    new_line=line.split()[0]
    with open('Day31\\new_data.txt',mode='a',encoding="utf8") as data:
        data.write(f"{new_line}\n")