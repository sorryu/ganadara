import typing

class Node:
    child:typing.List[int]

class AST(Node):
    identifier:type
    Power:int|None = 0
    def _make_child(self, node:Node):
        self.child.append(node)

class DefFunc(AST):
    Power:int|None = 0

class Repetition(AST):
    repetition:int|None = None

class For(Repetition):...
class While(Repetition):...
class In(Repetition):...