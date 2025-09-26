from enum import Enum, auto
from typing import Callable


class TokenKind(Enum):
    TEXT = auto()
    RAW = auto()
    ALPHA = auto()
    NUM = auto()
    SPACE = auto()
    LINE = auto()


class Token:
    def __init__(self, kind: TokenKind, val: str):
        self.kind = kind
        self.val = val

    def __repr__(self):
        return f"{self.__class__.__name__}({self.kind.name}, {self.val!r})"


class Lexer:
    def __init__(self, text: str):
        self.text: str = text
        self.idx = -1

    def next(self) -> str:
        self.idx += 1
        if self.idx < len(self.text):
            ch = self.text[self.idx]
        else:
            ch = ""
        return ch

    def prev(self) -> None:
        if self.idx > 0:
            self.idx -= 1

    @property
    def ch(self) -> str:
        if self.idx < len(self.text):
            return self.text[self.idx]
        else:
            return ""

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = []

        while ch := self.next():
            if ch == '\n':
                tokens.append(Token(TokenKind.LINE, ch))
            elif ch.isspace():
                tokens.append(self.aggregate(TokenKind.SPACE, str.isspace))
            elif ch.isalpha():
                tokens.append(self.aggregate(TokenKind.ALPHA, str.isalpha))
            elif ch.isdigit():
                tokens.append(self.aggregate(TokenKind.NUM, str.isdigit))
            elif ch == '"':
                tokens.append(self.enclosed_string(TokenKind.TEXT, True))
            elif ch == "%":
                tokens.append(self.enclosed_string(TokenKind.RAW, False))
            else:
                tokens.append(Token(TokenKind.RAW, ch))

        return tokens

    def aggregate(self, kind: TokenKind, cond: Callable) -> Token:
        val = self.ch
        while (ch := self.next()) and cond(ch):
            val += ch
        self.prev()

        return Token(kind, val)

    def enclosed_string(self, kind: TokenKind, allow_escape: bool) -> Token:
        val = ""
        terminator = self.ch
        escape = False
        while ch := self.next():
            if ch == '\\' and allow_escape:
                escape = True
                continue
            if escape or ch != terminator:
                val += ch
                escape = False
            else:
                break
        return Token(kind, val)
