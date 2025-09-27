# cmdstyler/cursor/__init__.py
"""
Cursor control helpers.

- move(x, y): absolute (1-indexed) position -> same behaviour as before.
- move_by(dx=0, dy=0): relative movement (dx right, dy down).
- up/down/forward/back: convenience wrappers.
- save/restore: save and restore cursor position.
- clear_line / clear_screen: erasing helpers.
- hide/show: cursor visibility.
"""

def move(x: int, y: int):
    """Move cursor to absolute column x, row y (1-indexed).
    Example: move(10, 3) -> column 10, row 3."""
    # ANSI expects positive 1-indexed coords; if user passed 0, clamp to 1
    x = max(1, int(x))
    y = max(1, int(y))
    print(f"\033[{y};{x}H", end="")

def move_by(dx: int = 0, dy: int = 0):
    """Move cursor relative to current position.
    Positive dx -> right, negative dx -> left.
    Positive dy -> down, negative dy -> up.
    Example: move_by(5, 0) -> move right 5 columns
             move_by(0, 5) -> move down 5 lines"""
    dx = int(dx)
    dy = int(dy)
    if dy > 0:
        print(f"\033[{dy}B", end="")   # down
    elif dy < 0:
        print(f"\033[{abs(dy)}A", end="")  # up

    if dx > 0:
        print(f"\033[{dx}C", end="")   # forward/right
    elif dx < 0:
        print(f"\033[{abs(dx)}D", end="")  # back/left

def up(n: int = 1):
    print(f"\033[{int(n)}A", end="")

def down(n: int = 1):
    print(f"\033[{int(n)}B", end="")

def forward(n: int = 1):
    print(f"\033[{int(n)}C", end="")

def back(n: int = 1):
    print(f"\033[{int(n)}D", end="")

def clear_line():
    """Clear the entire current line (leave cursor in same column)."""
    print("\033[2K", end="")

def clear(mode="ansi"):
    """
    Clear the terminal screen.

    mode = "ansi" (default) -> fast, works on modern terminals
    mode = "system"         -> uses cls/clear for legacy support
    """
    if mode == "ansi":
        print("\033[2J\033[H", end="")
    else:
        import os, platform
        os.system("cls" if platform.system() == "Windows" else "clear")

def save():
    """Save current cursor position."""
    print("\033[s", end="")

def restore():
    """Restore cursor to last saved position."""
    print("\033[u", end="")

def hide():
    """Hide the cursor."""
    print("\033[?25l", end="")

def show():
    """Show the cursor."""
    print("\033[?25h", end="")
