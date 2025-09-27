from sty import fg, bg, ef, rs

def bold(text: str):
    """
    Print bold text.
    """
    text = ef.bold + text + rs.bold_dim
    print(text)

def italic(text: str):
    """
    Print italic text.
    """
    text = ef.italic + text + rs.italic
    print(text)

def underline(text: str):
    """
    Print text with an underline.
    """
    text = ef.underl + text + rs.underl
    print(text)

def blink(text: str):
    """
    Print blinking text.
    """
    text = ef.blink + text + rs.blink
    print(text)