class Node:
    child:list|None = None

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


class Quotes(Section):...
class Bracket(Section):...

class Small(Bracket):...
class Middle(Bracket):...
class Large(Bracket):...


def repeteCount(ast:Repetition) -> tuple: #tuple (int or None, 승수) #ast에 Node를 넣음.
    if ast._is_child_exist:
        for i in ast.child:
            _repetition, _power = repeteCount(i) #_power는 그 전 재귀함수 호출로 나오는 power
            if not _repetition: #None인 경우
                ast.power = max(ast.power, _power+1) #_power(= 0) + 1과 ast.power 비교 -> 차수의 최댓값을 구함.
    return ast.repetition, ast.power

"""
[repeteCount]

if) 객체의 child가 있는지 확인
    *child: Node들이 담긴 리스트

    for문에 ast의 Node들을 넣고, 각각의 반복에서 최종적으로 나올 때까지 재귀함수 생성 (for문의 반복 횟수)
    -> 나올 때: 
            None이면, ast.power와 (재귀함수의 승수 반환 값 + 1) 계산. 
                * ast.power에 대한 설명 (finally, 시간복잡도: n**ast.power)        
                ast.repetition은 n이 아님. n은 그냥 미지수이며, 최대 차항만 남길 예정. (n->∞일 때, 가장 유효한 차항)

                if) iterable Variable인 경우: repetition이 None, 미지수로 취급해 차수를 1씩 늘림. 
                    1. 1씩 늘리는 이유: 미지수적인 for문의 반복 횟수를 세기 위함.
                    2. max 값의 경우: for문이 동일한 위상을 가진 경우가 있을 수 있기 때문.

                if) 정수 값의 경우: repetition이 int, 지수에 0을 넣어 값을 1로 만듦.

더 이상 child가 없다면, 클래스 Repetition의 repetition과 AST의 power 연산을 이용해 반환한 값을 상위 재귀함수로 보냄.
"""
