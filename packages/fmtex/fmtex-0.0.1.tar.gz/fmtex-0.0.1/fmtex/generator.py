from .lexer import Token, TokenKind


class Generator:
    def __init__(self, tokens: list[Token], substitutions: dict[str, str]):
        self.tokens = tokens
        self.idx = 0
        self.substitutions = substitutions

    def next(self) -> None:
        self.idx += 1

    def prev(self) -> None:
        self.idx -= 1

    @property
    def tok(self) -> Token | None:
        if self.idx < len(self.tokens):
            return self.tokens[self.idx]
        else:
            return None

    def generate(self) -> str:
        s = ""

        while self.tok is not None:
            if self.tok.kind == TokenKind.SPACE:
                s += " "
            elif self.tok.kind == TokenKind.TEXT:
                s += self.generate_text()
            elif self.tok.kind == TokenKind.RAW:
                s += self.tok.val
            elif self.tok.kind == TokenKind.ALPHA:
                s += self.generate_alpha()
            elif self.tok.kind == TokenKind.LINE:
                s += "\n"
            elif self.tok.kind == TokenKind.NUM:
                if len(self.tok.val) == 1:
                    s += self.tok.val
                else:
                    s += "{" + self.tok.val + "}"
            else:
                raise RuntimeError(f"unhandled token kind {self.tok.kind.name}")
            self.next()

        return s.strip()

    def generate_text(self) -> str:
        assert(self.tok is not None and self.tok.kind == TokenKind.TEXT)

        val = (
            self.tok.val
                .replace("\\", "\\\\")
                .replace("{", "\\{")
                .replace("}", "\\}")
        )
        return f"\\text{{{val}}}"

    def generate_alpha(self) -> str:
        assert(self.tok is not None and self.tok.kind == TokenKind.ALPHA)
        assert(len(self.tok.val) > 0)

        if len(self.tok.val) > 1:
            return self.substitutions.get(self.tok.val, "\\" + self.tok.val)

        s = self.tok.val
        self.next()
        if self.tok is not None and self.tok.kind == TokenKind.NUM:
            s = s + "_" + self.tok.val
        else:
            self.prev()

        return s
