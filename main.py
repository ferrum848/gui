
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import messagebox as mb


def openfile():
    def change(event):
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        canvas.create_oval(x, y, x, y, width = 3, outline = 'red')


    file_name = fd.askopenfilename()
    if len(file_name) == 0:
        return True
    if file_name.split('.')[1] not in  ['png', 'jpg', 'jpeg']:
        mb.showinfo('Info', 'Choise image!!!')
        return True
    image = Image.open(file_name)
    photo = ImageTk.PhotoImage(image)
    canvas = Canvas(bg='white')
    sby = Scrollbar()
    sbx = Scrollbar()
    canvas.config(scrollregion = (0, 0, image.size[0] + 10, image.size[1] + 10), highlightthickness=0, yscrollcommand=sby.set, xscrollcommand=sbx.set)
    sby.config(command=canvas.yview)
    sbx.config(orient=HORIZONTAL, command=canvas.xview)
    sby.pack(side=RIGHT, fill=Y)
    sbx.pack(side=BOTTOM, fill=X, anchor=W)
    canvas.create_image(10, 10, anchor = NW ,image=photo)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.bind('<Button1-Motion>', change)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry('400x200+100+50')
    root.title("Window title")
    b = Button(text="Choise image")
    b.config(command=openfile)
    b.pack()
    root.mainloop()

