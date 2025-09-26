import pyperclip
import os
try:
    if os.name == 'nt':
        import readline
    else:
        import gnureadline as readline
except ImportError:
    import readline
import re
from enum import Enum, auto
import sys
import os.path

from .lexer import Lexer
from .generator import Generator

CMD_SUBSTITUTIONS: dict[str, str] = {
    "NN": "{\\mathbb N}",
    "ZZ": "{\\mathbb Z}",
    "QQ": "{\\mathbb Q}",
    "II": "{\\mathbb I}",
    "RR": "{\\mathbb R}",
    "CC": "{\\mathbb C}",
    "balign": "\\begin{align}",
    "ealign": "\\end{align}",
    "bcases": "\\begin{cases}",
    "ecases": "\\end{cases}",
    "bmat": "\\begin{matrix}",
    "emat": "\\end{matrix}",
    "bpmat": "\\begin{pmatrix}",
    "epmat": "\\end{pmatrix}",
    "bsmat": "\\begin{bmatrix}",  # begin square-bracket matrix
    "esmat": "\\end{bmatrix}",  # end square-bracked matrix
    "bcmat": "\\begin{Bmatrix}",  # begin curly-bracket matrix
    "ecmat": "\\end{Bmatrix}",  # end curly-bracket matrix
    "bbmat": "\\begin{vmatrix}",  # begin beam matrix
    "ebmat": "\\end{vmatrix}",  # end beam matrix
    "bdmat": "\\begin{Vmatrix}",  # begin double beam matrix
    "edmat": "\\end{Vmatrix}",  # end double beam matrix
    "lp": "\\left(",  # left paren
    "rp": "\\right)",  # right paren
    "ls": "\\left[",  # left square bracket
    "rs": "\\right]",  # right square bracket
    "lc": "\\left\\{",  # left curly bracket
    "rc": "\\right\\}",  # right curly bracket
    "lb": "\\left|",  # left beam
    "rb": "\\right|",  # right beam
    "la": "\\left\\langle",  # left angle bracket
    "ra": "\\right\\rangle",  # right angle bracket
    "al": "\\alpha",
    "bt": "\\beta",
    "gm": "\\gamma",
    "dl": "\\delta",
    "DL": "\\Delta",
    "impl": "\\implies",
    "et": "&",
    "ett": "&&",
    "el": "\\\\",
    "perc": "\\%"
}


class FMTeX:

    class Mode(Enum):
        INLINE = auto()
        MULTILINE = auto()

    def __init__(self):
        self.mode = self.Mode.INLINE
        self.running = False
        self.lines: dict[int, str] = {}
        self.subs = CMD_SUBSTITUTIONS.copy()
        if sys.platform == "win32":
            self.file_location = os.path.join(os.environ["LOCALAPPDATA"], "_fmtexrc")
        else:
            self.file_location = os.path.join(os.environ["HOME"], ".fmtexrc")

    def welcome(self):
        print("Welcome to FastMathTeX!")
        print(f"Type \"'exit\" to exit the program and \"'help\" for more commands.")

    def load_init_file(self):
        try:
            with open(self.file_location, encoding="utf8") as init:
                for line in init.read().replace("\r", "").split("\n"):
                    self.exe_cmd(line)
        except FileNotFoundError:
            pass

    def input_hook(self):
        def hook():
            if self.mode == self.Mode.MULTILINE:
                readline.insert_text(f"{self.next_line_idx()}> ")
                readline.redisplay()
        return hook

    def run(self):
        self.running = True
        self.welcome()

        readline.set_pre_input_hook(self.input_hook())

        while self.running:
            line = self.get_input_line()
            if line[1].startswith("'"):
                self.exe_cmd(line[1])
                continue
            self.lines[line[0]] = line[1]
            if self.mode == self.Mode.MULTILINE and len(line[1]) != 0:
                continue
            lexer = Lexer("\n".join(ln[1] for ln in self.line_list()))
            generator = Generator(lexer.tokenize(), self.subs)
            output = generator.generate()
            print(output)
            self.copy_to_clipboard(output)
            self.lines = {}

    def next_line_idx(self):
        return (len(self.lines) + 1) * 10

    def get_input_line(self) -> tuple[int, str]:
        prompt = "> " if self.mode == self.Mode.INLINE else "| "
        line = input(prompt).replace("\r", "").removesuffix("\n")
        if self.mode == self.Mode.INLINE:
            return (self.next_line_idx(), line)

        line_match = re.match(r"^\s*(\d+)\s*>.*", line)
        if line_match is None:
            return (self.next_line_idx(), line)
        return (int(line_match.group(1)), line.split(">", 1)[1].removeprefix(" "))

    def line_list(self) -> list[tuple[int, str]]:
        return list(sorted(self.lines.items(), key=lambda x: x[0]))

    def copy_to_clipboard(self, text: str):
        if self.mode == self.Mode.INLINE:
            pyperclip.copy("$" + text + "$")
        elif self.mode == self.Mode.MULTILINE:
            pyperclip.copy("$$\\begin{align}\n " + text + " \n\\end{align}$$")

    def exe_cmd(self, cmd: str):
        try:
            cmd, *args = cmd.strip().removeprefix("'").split()
        except ValueError:
            return
        cmd = cmd.lower()
        if hasattr(self, f"cmd_{cmd}"):
            msg = getattr(self, f"cmd_{cmd}")(args)
        else:
            print(f"unknown command '{cmd}")
            msg = None

        if msg is not None:
            print(f"{cmd}: {msg}")

    def cmd_exit(self, _):
        self.running = False

    def cmd_mode(self, args: list[str]) -> str | None:
        if len(args) == 0:
            print(self.mode.name.lower())
            return None
        if len(args) > 1:
            return "invalid arguments"
        mode = args[0].lower()
        self.lines = {}
        if "inline".startswith(mode):
            self.mode = self.Mode.INLINE
        elif "multiline".startswith(mode):
            self.mode = self.Mode.MULTILINE
        else:
            return "unknown mode, valid modes are 'inline' and 'multiline'"

    def cmd_list(self, args: list[str]) -> str | None:
        if len(args) != 0:
            return "invalid arguments"

        lines = self.line_list()
        if len(lines) == 0:
            print("no lines in buffer")
        for ln in self.line_list():
            print(f"    {ln[0]}  {ln[1]}")

    def cmd_sub(self, args: list[str]) -> str | None:
        if len(args) == 0:
            subs = list(self.subs.items())
            kw_width = max(len(x[0]) for x in subs)
            for kw, sub in subs:
                print(f"    {kw:{kw_width}s} -> {sub}")
            return
        elif not args[0].isalpha():
            return f"invalid substitution name, only letters are allowed"
        elif len(args[0]) == 1:
            return f"invalid substitution name, it must be at least two letters long"

        if len(args) == 1:
            if args[0] in self.subs:
                del self.subs[args[0]]
                print(f"removed '{args[0]}'")
            else:
                print(f"substitution {args[0]} not found")
        else:
            value = " ".join(args[1:])
            self.subs[args[0]] = value
            print(f"added {args[0]} -> {value}")

    def cmd_clear(self, _):
        print("\x1b[2J\x1b[3J\x1b[H", end="")

    def cmd_help(self, _):
        print("Commands:")
        print("'help              display this message")
        print("'exit              exit the program")
        print("'mode [mode]       change the mode (inline or multiline)")
        print("                   if not specified print the current mode")
        print("'list              list the current lines or the current")
        print("'sub [name] [val]  add a substitution rule, omit val to delete")
        print("                   omit name and val to list all substitutions")
        print("'clear             clear the screen")


def main():
    prog = FMTeX()
    prog.load_init_file()
    prog.run()


if __name__ == "__main__":
    main()
