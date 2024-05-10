code = []

with open("test.txt", "r") as f: #코드 원형으로 갖고 옴.
    code = list(map(lambda line: line.rstrip(),f.readlines()))

print(code)
