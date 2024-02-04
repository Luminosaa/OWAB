from utils.action import Action

class Effect:

    action: Action
    value: int
    n_elements: int
    
    def __init__(self, action: Action, value: int, n_elements=-1):
        self.action = action
        self.value = int(value)
        self.n_elements = int(n_elements)
        return

    def __action__(self) -> Action:
        return self.action
    
    def __value__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.action} : {self.value}" + (f" sur {self.n_elements} éléments" if self.n_elements != -1 else "" )