
names = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split (",")
        name = {"name": name, "house": house }
        names.append(name)



def get_name(names):
    return name["name"]



for name in sorted(name, key=get_name):
    print(f"{name['name']} is in {name['house']}")