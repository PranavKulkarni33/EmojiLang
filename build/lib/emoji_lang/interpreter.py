import operator
from .lexer import Lexer
from .parser_ast import Parser, BinOp, Num


class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.operations = {
            '➕': operator.add,  # Emoji for addition
            '➖': operator.sub,  # Emoji for subtraction
            '✖️': operator.mul,  # Emoji for multiplication
            '➗': operator.truediv  # Emoji for division
        }

    def visit(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, BinOp):
            left_val = self.visit(node.left)
            right_val = self.visit(node.right)
            operation = self.operations.get(node.op.value)
            if operation:
                return operation(left_val, right_val)
            else:
                raise Exception(f"Unknown operation: {node.op.value}")

    def interpret(self):
        tree = self.parser.expr()
        return self.visit(tree)

# Main program loop
if __name__ == "__main__":
    while True:
        try:
            text = input("Enter your expression: ")
            if text.lower() == 'exit':
                break
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
