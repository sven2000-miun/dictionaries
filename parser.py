remove = ["names.txt", "remove.txt", "countries.txt", "cities.txt"]

banned = set()

for each in remove:
    with open("dicts/" + each, "r") as f:
        for each in f.readlines():
            banned.add(each)

file = open("eng_dict.txt", "w")
with open("dicts/wordlist.10000", "r") as f:
    for each in f.readlines():
        if each in banned:
            continue
        file.write(each)

file.close()

file = open("known_abbr.txt", "w")
for abbr in ["abbr/it_abbr.txt", "abbr/eng_abbr.txt"]:
    with open(abbr, "r") as f:
        for each in f.readlines():
            if each in banned:
                continue
            file.write(each)

file.close()
