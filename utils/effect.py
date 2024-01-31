from enumerations.action import Action

class Effect:

    action: Action
    value: int

    def __init__(self, action: Action, value: int):
        self.action = action
        self.value = value
        return

    def __action__(self) -> Action:
        return self.action
    
    def __value__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.action} : {self.value}"