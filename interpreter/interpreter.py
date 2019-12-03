import abc

class IOperand(metaclass = abc.ABCMeta):
    def get_operand_string(self):
        pass

class IOperator(metaclass = abc.ABCMeta):
    def excecute(self):
        pass

class Ingredient(IOperand):
    def __init__(self, operand_str):
        self.operand = operand_str

    def get_operand_string(self):
        return self.operand

class Expression(IOperand):
    def __init__(self, operator):
        self.operator = operator

    def get_operand_string(self):
        return self.operator.execute.get_operand_string()

class AddOperator(IOperator):
    def __init__(operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute():
        operand_str = operand1.get_operand_string() + "+" + operand2.get_operand_string()
        new_operand = Ingradient(operand_str)

        return new_operand

class WaitOperator(IOperator):
    def __init__(operand):
        self.operand = operand

    def execute():
        operand_str = operand.get_operand_string() + 'の後3分待機'
        new_operand = Ingradient(operand_str)
        return new_operand



