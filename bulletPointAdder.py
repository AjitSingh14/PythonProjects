#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip

text = pyperclip.paste()

lines= text.split('\n')

for i in range(len(lines)):
    if len(lines[i].strip())>1:
        lines[i] = "*" + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

txt = "E:\\aa\\bb"

x = txt.rsplit("\\",1)[1]

print(x)

print(round(23.22))
