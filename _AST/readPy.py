code = []

with open("test.txt", "r") as f: #코드 원형으로 갖고 옴.
    code = list(map(lambda line: line.rstrip(),f.readlines())) #줄바꿈 없애기 (By using Lambda)

print(code)




"""
[This Code's Ver 1.0]
code = []

with open("test.txt", "r") as f: #코드 원형으로 갖고 옴.
    for i in f.readlines():
        i = i.strip("\n") #줄바꿈만 없앰.
        code.append(i)
"""
