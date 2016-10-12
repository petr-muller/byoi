#!/usr/bin/env python3

"""A base of a toy Pascal-like language interpreter

Credits: Ruslan Spivak (https://ruslanspivak.com/lsbasi-part1/)
"""

INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"

class Token(object):
    """Represents a language token"""

    # pylint: disable=too-few-public-methods

    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return "Token({token_type}, {value})".format(token_type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    """Base interpreter class"""

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    @staticmethod
    def error():
        """Raises a general exception"""
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Obtains a next token from the input (lexer stub)"""

        text = self.text
        if self.pos >= len(text):
            return Token(EOF, None)

        current_char = text[self.pos]
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        Interpreter.error()

    def eat(self, token_type):
        """Checks whether current token matches the expected token (parser stub)"""

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            Interpreter.error()

    def expr(self):
        """Parses a simple X+Y expression (parser stub)"""
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result

def main():
    """Main program loop"""
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()
