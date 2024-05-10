from readPy import code

class Node:
    child:list|None = list()

class AST(Node):
    identifier:str # 코드의 종류
    power:int|None = 0 # 반복 승수, 자식의 repetition이 None인 경우에만 +1
    def _make_child(self, node:Node) -> None: # child list에 새로운 노드 할당
        self.child.append(node)
    def _is_child_exist(self) -> bool: #child가 존재하는지 확인
        return False if self.child == None else True

class DefFunc(AST):...

class Repetition(AST):
    repetition:int|None = None # 반복 횟수, None이면 n번 반복, range() 안에 숫자가 있는 경우 그 숫자로 할당
    
class For(Repetition):...
class While(Repetition):...
class In(Repetition):...

class Section(AST):
    isOpen:bool|None = True #Section의 열림 여부

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
print(read_code(python,code))