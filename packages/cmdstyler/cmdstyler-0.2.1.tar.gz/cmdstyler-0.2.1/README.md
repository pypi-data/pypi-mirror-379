# cmdstyler

Easily style your CMD/terminal output with headers, colors, and more.  
Supports `.pdat` files for larger projects to keep your code clean.

## ✨ Features

- ASCII art headers (based on figlet)
- 8-bit text coloring
- Empty line spacing
- `.pdat` file support (optional)
- Background colors
- 24-bit (truecolor) support
- cursor control
- Centered text

Planned:

- Progress bars
- layout control

## 📦 Installation

```bash
pip install cmdstyler
```

## Usage

How to use cmdstyler:

```python
import cmdstyler as cs

# Print a header, you can specify any figlet font
cs.header("Hello World", "slant")

# Print a centered text
cs.center("I am centered!")

# Add empty lines
cs.empty(2)

# Print colored text (8-bit)
cs.color("34;This is blue text")

#Print colored text (24-bit or Hex)
cs.rgbcolor("#FFD700", "I am an yellow text!")
cs.rgbcolor((255, 215, 0), "I am an yellow text too!")

#print text with colored background(8-bit)
cs.background(161, "I have a red background!")

#print colored text with colored background(8-bit, first fg, the bg)
cs.bothcolors(161, 19, "I am a red text on a blue background!")

# Load from a .pdat file
cs.beautify("example.pdat")

#cs.cursor
#Cursor functions

# Clears this line
cs.cursor.clear_line()      

# Clears the screen
cs.cursor.clear()

# Hides/shows the cursor
cs.cursor.hide()
cs.cursor.show()

# Saves loads cursor position
cs.cursor.save()
cs.cursor.restore()

# Moves the cursor
# Relative movement
cs.cursor.moveby(x, y) #moves the cursor in the x or y direction
cs.cursor.up(y)
cs.cursor.down(y)
cs.cursor.forward(x)
cs.cursor.back(x)

#movement from (0, 0)
cs.cursor.move(x, y)
```

### PDAT file syntax

```bash
{header : Hello Guys!}.
# The first word is the function name
# The : separates the function from its argument
# Everything after that is the output

{empty : 2}.
# Creates 2 empty lines

{color : 161 ; This text is red}.
# Prints a colored line with the specified 8-bit color

{textblock : Hallo Welt}.
# Prints a simple line of text
```
