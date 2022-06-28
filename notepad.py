from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    general_status['text'] = 'Create a New file'


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    general_status['text'] = 'Opening a File'

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    general_status['text'] = 'Saving the File'

def quitApp():
    root.destroy()
    general_status['text'] = 'Exit'
def cut():
    TextArea.event_generate(("<<Cut>>"))
    general_status['text'] = 'Cut'

def copy():
    TextArea.event_generate(("<<Copy>>"))
    general_status['text'] = 'Copy'

def paste():
    TextArea.event_generate(("<<Paste>>"))
    general_status['text'] = 'Paste'

def about():
    showinfo("Notepad", "Notepad by Mugdha")
    general_status['text'] = 'About - Notepad By Mugdha'


if __name__ == '__main__':
    #Basic Tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("icon.ico")
    root.geometry("644x708")

    #Add text area
    font1 = ["lucida", 13, 'normal']
    TextArea = Text(root, font=font1)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    def zoom(str1):
        if str1 == 'ZoomIn':
            font1[1] = font1[1] + 2
            general_status['text'] = 'ZoomIn'
        else:
            font1[1] = font1[1] - 2
            general_status['text'] = 'ZoomOut'
        TextArea.config(font=font1)
    
    #MenuBar creation
    MenuBar = Menu(root)

    #File menu creation
    FileMenu = Menu(MenuBar, tearoff=0)

    #To create new file
    FileMenu.add_command(label="New", command=newFile)
    #To open file
    FileMenu.add_command(label="Open", command=openFile)

    # To save new file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    #File Menu ends

    # Edit menu creation
    EditMenu = Menu(MenuBar, tearoff=0)

    #TO cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu )
    # Edit Menu Ends

    #View menu creation

    ViewMenu = Menu(MenuBar, tearoff=0)

    # To add zoom in and zoom out
    ViewMenu.add_command(label="ZoomIn", command=lambda:zoom('ZoomIn'))
    ViewMenu.add_command(label="ZoomOut", command=lambda:zoom('ZoomOut'))
    MenuBar.add_cascade(label="View", menu=ViewMenu)
    root.config(menu=MenuBar)
    #view menu ends


    # Help menu creation 
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    #help menu ends

    #Adding Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    #Adding Statusbar
    statusbar_frame = Frame(root, bg="white", borderwidth=1, relief=SUNKEN)
    statusbar_frame.pack(side=BOTTOM, fill="x")
     
    #general information on status bar and it gets updated when we click on various menu options
    general_status = Button(statusbar_frame, text="Welcome to Notepad", bg="white", borderwidth=0, anchor='sw')
    general_status.pack(side=LEFT)

    # Setting the line column number and updating it with the hover of mouse

    line_col_var = StringVar()
    line_col_status = Button(statusbar_frame, textvariable=line_col_var, bg="white", borderwidth=0, anchor='se')
    line_col_status.pack(side=RIGHT)

    # function to update the line and column number with the cursor
    def update_label():
        row, col = TextArea.index('insert').split('.')
        line_col_var.set(f'Ln:{row}, Col:{col}')
        root.after(100, update_label)

    update_label()

    # encoding type on statusbar
    encoding_type = Button(statusbar_frame, text="UTF-8", bg="white", borderwidth=0, anchor='se', padx=12)
    encoding_type.pack(side=RIGHT)
    
    
    root.mainloop()