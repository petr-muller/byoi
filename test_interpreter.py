import interpreter
import pytest

class TestToken(object):
    def test_types(self):
        integer = interpreter.Token(interpreter.INTEGER, "3")
        assert integer.type == interpreter.INTEGER
        assert integer.value == "3"
        assert str(integer) == "Token(INTEGER, '3')"
        assert repr(integer) == str(integer)

        plus = interpreter.Token(interpreter.PLUS, '+')
        assert plus.type == interpreter.PLUS
        assert plus.value == "+"
        assert str(plus) == "Token(PLUS, '+')"

class TestInterpreter(object):
    def test_sanity(self):
        parser = interpreter.Interpreter("1+2")
        assert parser.text == "1+2"
        assert parser.pos == 0
        assert parser.current_token == None

    def test_error(self):
        with pytest.raises(Exception):
            interpreter.Interpreter.error()

    def test_get_next_token(self):
        parser = interpreter.Interpreter("1+")
        
        token = parser.get_next_token()
        assert token.type == interpreter.INTEGER
        assert token.value == 1
        assert parser.pos == 1

        token = parser.get_next_token()
        assert token.type == interpreter.PLUS
        assert token.value == "+"
        assert parser.pos == 2

        token = parser.get_next_token()
        assert token.type == interpreter.EOF

    def test_negative_get_next_token(self):
        parser = interpreter.Interpreter("x")
        
        with pytest.raises(Exception):
            parser.get_next_token()

    def test_eat(self):
        parser = interpreter.Interpreter("1")

        parser.current_token = interpreter.Token(interpreter.INTEGER, "1")
        parser.pos = 1
        parser.eat(interpreter.INTEGER)
        assert parser.current_token.type == interpreter.EOF

    def test_negative_eat(self):
        parser = interpreter.Interpreter("1")

        parser.current_token = interpreter.Token(interpreter.INTEGER, "1")
        with pytest.raises(Exception):
            parser.eat(interpreter.PLUS)

    def test_expr(self):
        parser = interpreter.Interpreter("2+3")
        result = parser.expr()
        assert result == 5

    def test_negative_expr(self):
        parser = interpreter.Interpreter("2 + 3")
        with pytest.raises(Exception):
            parser.expr()
