# cmdstyler

Easily style your CMD/terminal output with headers, colors, and more.  
Supports `.pdat` files for larger projects to keep your code clean.

## ✨ Features
- ASCII art headers
- 8-bit text coloring
- Empty line spacing
- `.pdat` file support (optional)

Planned:
- Background colors
- Easier custom header fonts
- 24-bit (truecolor) support
- Progress bars
- Centered text

## 📦 Installation

```bash
pip install cmdstyler
```

## Usage
How to use cmdstyler:
```python
import cmdstyler as cs

# Print a header
cs.header("Hello World")

# Add empty lines
cs.empty(2)

# Print colored text (8-bit)
cs.color("34;This is blue text")

# Load from a .pdat file
cs.beautify("example.pdat")
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
