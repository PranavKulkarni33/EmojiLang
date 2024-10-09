from .lexer import Lexer
from .parser_ast import Parser
from .interpreter import Interpreter



def run():
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
