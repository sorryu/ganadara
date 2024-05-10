from readPy import code
"""
[프로그램 사용법 | 버전: Prototype]
주의) 하나의 파일에서 모듈을 불러오지 않았을 때를 기준으로 함. 즉, 하나의 코드만 확인함.

1. 파이썬 검사기를  저장함.
2. 검사하려는 코드 파일을 복사하고, 확장자를 txt로 변환하여, 저장한 파이썬 검사기가 있는 폴더에 넣음.
3. 파이썬 검사기에서, 'with open("your_code.txt","r") as f:' 구문의 'your_code.txt'에 변환한 코드 txt 파일의 이름을 넣음.
4. 실행하여 for문의 시간복잡도를 확인하고, 상황에 따른 피드백을 확인함.
"""
class Node:
    child:list|None = list()

class AST(Node):
    identifier:str #Update 예정
    power:int|None = 0 #Update 예정
    def _make_child(self, node:Node) -> None: #child list에 새로운 노드 할당
        self.child.append(node)
    def _is_child_exist(self) -> bool: #Update 예정
        return False if self.child == None else True

class Repetition(AST):
    repetition:int|None = None #Update 예정

count = 0
maxN = 0
def read_code(ast:Repetition,code:list):
    global count, maxN

    i=-1
    start = False
    start_idx = end_idx = -1
    space_idx = 0

    for lineData in enumerate(code):
        lineIndex, line = lineData[0], lineData[1]

        if not start and line.find("for") >= 0 or line.find("while") >= 0:
            space_idx = max(line.find("for"), line.find("while"))
            start_idx = lineIndex
            start = True

        elif start and -1 < line.find(line.strip()) <= space_idx or -1 < line.find(line.strip()) <= space_idx:
            end_idx = lineIndex
            start = False
            
        if lineIndex == len(code)-1:
            end_idx = lineIndex

        if start_idx >= 0 and end_idx and start_idx < end_idx:
            i+=1
            ast._make_child(Repetition())
            count += 1
            maxN = max(maxN, count)
            read_code(ast.child[i], code[start_idx+1:end_idx+1])
            count -= 1
            read_code(ast, code[end_idx:])
            return maxN

python = AST()
trial = read_code(python,code)
if trial >= 3:
    print(f"복잡도: {trial} (경고 단계)\n다중 for문이 사용되었습니다. 다음과 같은 코드 수정을 제안합니다.\n1. for문의 수를 줄이십시오.\n2. for문의 범위를 줄이거나 제한하십시오.\n*참고: 복잡도 1: 안정, 복잡도 2: 주의, 복잡도 3 이상: 경고")