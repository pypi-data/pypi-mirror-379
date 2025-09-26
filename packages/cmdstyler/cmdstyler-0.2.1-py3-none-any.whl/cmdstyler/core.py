from sty import fg, bg, ef, rs
import inspect
from pyfiglet import Figlet
import os
global lines
lines = ["","","","","",""]
editedLine = 0
#arrays of doom
Space  = ["   ","   ","   ","   ","   ","   "]
A = ["    _    ","   / \\   ","  / _ \\  "," / ___ \\ ","/_/   \\_\\","         "]
B = [" ____  ","| __ ) ","|  _ \\ ","| |_) |","|____/ ","       "]
C = ["  ____ "," / ___|","| |    ","| |___ "," \\____|","       "]
D = [" ____  ","|  _ \\ ","| | | |","| |_| |","|____/ ","       "]
E = [" _____ ","| ____|","|  _|  ","| |___ ","|_____|","       "]
F = [" _____ ","|  ___|","| |_   ","|  _|  ","|_|    ","       "]
G = ["  ____ "," / ___|","| |  _ ","| |_| |"," \\____|","       "]
H = [" _   _ ","| | | |","| |_| |","|  _  |","|_| |_|","       "]
I = [" ___ ","|_ _|"," | | "," | | ","|___|","     "]
J = ["     _ ","    | |"," _  | |","| |_| |"," \\___/ ","       "]
K = [" _  __","| |/ /","| ' / ","| . \\ ","|_|\\_\\","      "]
L = [" _     ","| |    ","| |    ","| |___ ","|_____|","       "]
M = [" __  __ ","|  \\/  |","| |\\/| |","| |  | |","|_|  |_|","        "]
N = [" _   _ ","| \\ | |","|  \\| |","| |\\  |","|_| \\_|","       "]
O = ["  ___  "," / _ \\ ","| | | |","| |_| |"," \\___/ ","       "]
P = [" ____  ","|  _ \\ ","| |_) |","|  __/ ","|_|    ","       "]
Q = ["  ___  "," / _ \\ ","| | | |","| |_| |"," \\__\\_\\","       "]
R = [" ____  ","|  _ \\ ","| |_) |","|  _ < ","|_| \\_\\","       "]
S = [" ____  ","/ ___| ","\\___ \\ "," ___) |","|____/ ","       "]
T = [" _____ ","|_   _|","  | |  ","  | |  ","  |_|  ","       "]
U = [" _   _ ","| | | |","| | | |","| |_| |"," \\___/ ","       "]
V = ["__     __ ","\\ \\   / / "," \\ \\ / /  ","  \\ V /   ","   \\_/    ","          "       ]
W = ["__        __","\\ \\      / /"," \\ \\ /\\ / / ","  \\ V  V /  ","   \\_/\\_/   ","            "]
X = ["__  __","\\ \\/ /"," \\  / "," /  \\ ","/_/\\_\\","      "]
Y = ["__   __","\\ \\ / /"," \\ V / ","  | |  ","  |_|  ","       "]
Z = [" _____","|__  /","  / / "," / /_ ","/____|","      "]
a = ["       ","  __ _ "," / _` |","| (_| |"," \\__,_|","       "]
b = [" _     ","| |__  ","| '_ \\ ","| |_) |","|_.__/ ","       "]
c = ["      ","  ___ "," / __|","| (__ "," \\___|","      "]
d = ["     _ ","  __| |"," / _` |","| (_| |"," \\__,_|","       "]
e = ["      ","  ___ "," / _ \\","|  __/"," \\___|","      "]
f = ["  __ "," / _|","| |_ ","|  _|","|_|  ","     "]
g = ["       ","  __ _ "," / _` |","| (_| |"," \\__, |"," |___/ "]
h = [" _     ","| |__  ","| '_ \\ ","| | | |","|_| |_|","       "]
i = [" _ ","(_)","| |","| |","|_|","   "]
j = ["   _ ","  (_)","  | |","  | |"," _/ |","|__/ "]
k = [" _    ","| | __","| |/ /","|   < ","|_|\\_\\","      "]
l = [" _ ","| |","| |","| |","|_|","   "]
m = ["           "," _ __ ___  ","| '_ ` _ \\ ","| | | | | |","|_| |_| |_|","           "]
n = ["       "," _ __  ","| '_ \\ ","| | | |","|_| |_|","       "]
o = ["       ","  ___  "," / _ \\ ","| (_) |"," \\___/ ","       "]
p = ["       "," _ __  ","| '_ \\ ","| |_) |","| .__/ ","|_|    "]
q = ["       ","  __ _ "," / _` |","| (_| |"," \\__, |","    |_|"]
r = ["      "," _ __ ","| '__|","| |   ","|_|   ","      "]
s = ["     "," ___ ","/ __|","\\__ \\","|___/","     "]
t = [" _   ","| |_ ","| __|","| |_ "," \\__|","     "]
u = ["       "," _   _ ","| | | |","| |_| |"," \\__,_|","       "]
v = ["       ","__   __","\\ \\ / /"," \\ V / ","  \\_/  ","       "]
w = ["          ","__      __","\\ \\ /\\ / /"," \\ V  V / ","  \\_/\\_/  ","          "]
x = ["      ","__  __","\\ \\/ /"," >  < ","/_/\\_\\","      "]
y = ["       "," _   _ ","| | | |","| |_| |"," \\__, |"," |___/ "]
z = ["     "," ____","|_  /"," / / ","/___|","     "]
dot = ["   ","   ","   "," _ ","(_)","   "]
ddot = ["   "," _ ","(_)"," _ ","(_)","   "]
dash = ["       ","       "," _____ ","|_____|","       ","       "]
hashtag = ["","","","","",""]
a0 = ["  ___  "," / _ \\ ","| | | |","| |_| |"," \\___/ ","       "]
a1 = [" _ ","/ |","| |","| |","|_|","   "]
a2 = [" ____  ","|___ \\ ","  __) |"," / __/ ","|_____|","       "]
a3 = [" _____ ","|___ / ","  |_ \\ "," ___) |","|____/ ","       "]
a4 = [" _  _   ","| || |  ","| || |_ ","|__   _|","   |_|  ","        "]
a5 = [" ____  ","| ___| ","|___ \\ "," ___) |","|____/ ","       "]
a6 = ["  __   "," / /_  ","| '_ \\ ","| (_) |"," \\___/ ","       "]
a7 = [" _____ ","|___  |","   / / ","  / /  "," /_/   ","       "]
a8 = ["  ___  "," ( _ ) "," / _ \\ ","| (_) |"," \\___/ ","       "]
a9 = ["  ___  "," / _ \ ","| (_) |"," \\__, |","   /_/ ",""]
c0 = ["","","","","",""]

#main loop - optimized
letter_map = {
    " ": Space,
    "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, 
    "I": I, "J": J, "K": K, "L": L, "M": M, "N": N, "O": O, "P": P, 
    "Q": Q, "R": R, "S": S, "T": T, "U": U, "V": V, "W": W, "X": X, 
    "Y": Y, "Z": Z,
    "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h,
    "i": i, "j": j, "k": k, "l": l, "m": m, "n": n, "o": o, "p": p,
    "q": q, "r": r, "s": s, "t": t, "u": u, "v": v, "w": w, "x": x,
    "y": y, "z": z,
    ".": dot, ":": ddot, "-": dash, "#": hashtag,
    "0": a0, "1": a1, "2": a2, "3": a3, "4": a4, "5": a5, "6": a6, "7": a7, "8": a8, "9": a9
}

def center(text: str, width: int = None):
    """
    Print text centered in the terminal or within a given width.
    """
    txtlen = len(text)
    if width is None:
        ts = os.get_terminal_size()
        width = ts.columns
    pad = max((width - txtlen) // 2, 0)
    print(" " * pad + text)

def divider(char:str = "─", width: int = None):
    """
    Print a horizontal divider line across the terminal.
    """
    if width is None:
        try:
            ts = os.get_terminal_size()
            width = ts.columns
        except OSError:
            width = 80
    print(char * width)

def bold(text: str):
    """
    Print bold text.
    """
    text = ef.bold + text + rs.bold_dim
    print(text)

def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("Hex color must be in format RRGGBB")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def legacyheader(header):
    global lines
    lines = ["","","","","",""]
    for editedLine in range(6):
        for letter in header:
            if letter in letter_map:
                lines[editedLine] += letter_map[letter][editedLine]
        print(lines[editedLine])

def header(text: str, font: str = None):
    if font:
        fig = Figlet(font=font)
        print(fig.renderText(text))
    else:
        # classic array-based rendering
        lines = [""] * 6
        for i in range(6):
            for letter in text:
                if letter in letter_map:
                    lines[i] += letter_map[letter][i]
            print(lines[i])

def typefile(v):
    print(f"File valid {v}")

def textblock(value):
    print(value)
    
def empty(v):
    v = int(v)
    a = 0
    while a < v:
        print("")
        a = a + 1
    
def color(col, txt):
    v = ""
    v = fg(col) + txt + rs.fg
    print(v)

def backgroundcolor(col, txt):
    v = ""
    v = bg(col) + txt + rs.bg
    print(v)

def allcolor(fgcol, bgcol, txt):
    v = ""
    v = fg(fgcol) + bg(bgcol) + txt + rs.all
    print(v) 


def realrgbcolor(color, text: str, end: str = None):
    if isinstance(color, str):  # hex code
        rgb = hex_to_rgb(color)
        v = fg(*rgb) + text + rs.fg
    elif isinstance(color, tuple) and len(color) == 3:  # rgb tuple
        v = fg(*color) + text + rs.fg
    else:
        raise TypeError("Color must be a hex string or RGB tuple")
    if end == None:
        print(v)
    else:
        print(v, end=end)

def pdatcolor(value):
    col, txt = value.split(';', 1)
    col = col.strip()
    txt = txt.strip()

    if col.isnumeric():
        v = fg(int(col)) + txt + rs.fg
    elif col.startswith("#"):  # hex
        rgb = hex_to_rgb(col)
        v = fg(*rgb) + txt + rs.fg
    elif "," in col:  # rgb tuple as string
        rgb = tuple(map(int, col.split(',')))
        v = fg(*rgb) + txt + rs.fg
    else:
        print(fg.red + "Unsupported color format!" + rs.fg)
        return
    print(v)

function_map = {
    "typefile": typefile,
    "header": legacyheader,
    "textblock": textblock,
    "empty": empty,
    "color": pdatcolor
}

import os


def beautify(file_path):
    """
    Beautify a .pdat file.
    If file_path is relative, resolve it relative to the calling script.
    """
    global lines

    # get the path of the calling script
    caller_file = inspect.stack()[1].filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # resolve relative path from caller script's folder
    if not os.path.isabs(file_path):
        file_path = os.path.join(caller_dir, file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("{") and line.endswith("}."):
                content = line[1:-2]
                if " : " in content:
                    header_name, value = content.split(" : ", 1)
                    func = function_map.get(header_name)
                    if func:
                        lines = ["","","","","",""]
                        func(value)
                        lines = ["", "", "", "", "", ""]
                    else:
                        print(f"{header_name}: {value}")
                        lines = ["", "", "", "", "", ""]