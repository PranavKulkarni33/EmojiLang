class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Invalid syntax. Expected {token_type}.")

    def factor(self):
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return Num(token.value)
        raise Exception("Syntax error: Expected a number.")

    def expr(self):
        """Parse an expression with two numbers and an emoji operator."""
        # Parse the operator (emoji like ➕, ➖, etc.)
        op = self.current_token
        self.eat('OP')
        # Parse left-hand side
        left = self.factor()
        # Parse right-hand side
        right = self.factor()
        return BinOp(left, op, right)
