import pyfiglet
name=input("Enter your name:")
print("=====================")

print("banner3-D")
print("block")
print("Doom")
print("Digital")
print("Diamond")
print("epic")


font_style=input("choice the font style from Above:")
font=pyfiglet.figlet_format(f"{name}",f"{font_style}")
print(font)
