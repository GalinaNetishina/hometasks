class Stack:
    '''
    методы:
    is_empty — проверка стека на пустоту, возвращает True или False;
    push — добавляет новый элемент на вершину, ничего не возвращает;
    pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    size — возвращает количество элементов в стеке.
    '''
    def __init__(self):
        self.len = 0
        self.elements = []

    def is_empty(self) -> bool:
        return not bool(self.len)

    def push(self, element) -> None:
        self.elements.append(element)
        self.len += 1

    def pop(self):
        self.len -= 1
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def size(self) -> int:
        return self.len
