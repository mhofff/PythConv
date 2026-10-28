#converter png to jpeg
from tkinter import *
from tkinter.filedialog import *
from os import *
from PIL import Image

#root = Tk()

file = askopenfilename()

img = Image.open(file)
rgb_file = img.convert("RGB")

new_file_path = (path.splitext(file)[0] + ".jpg")

rgb_file.save(new_file_path)
#new_file_path.show()
rgb_file.show()
#img.load()
#img.show()

#print(img)

#root.mainloop()
