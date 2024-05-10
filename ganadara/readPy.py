code = []

with open("2798.txt", "r") as f: #코드 원형으로 갖고 옴.
    for i in f.readlines():
        i = i.strip("\n") #줄바꿈만 없앰.
        code.append(i)

