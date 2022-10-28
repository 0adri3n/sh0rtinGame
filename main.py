import tkinter.font as font
from threading import main_thread
import tkinter
import pyglet
from PIL import Image, ImageTk
from lib import shortFunc

#----------------------------------------------------------------------------------------

def shortCode():

    outputField.delete("1.0", "end-1c")
    code = scriptField.get("1.0", "end-1c")
    try:
        encodedCode = shortFunc.encode(code)
        shortOutput = 'exec(bytes("' + encodedCode + '","utf-16")[2:])'
        outputField.insert("end-1c", shortOutput)
    except UnicodeDecodeError:
        outputField.insert("end-1c", "Error. Please try to modify the code.")



#----------------------------------------------------------------------------------------

pyglet.font.add_file('src/font/Aucoinlight.ttf')


window = tkinter.Tk()
window.geometry("630x330")
window.title("sh0rtinGame")
window.maxsize(630, 330)
window.minsize(630, 330)
window.iconbitmap("src/img/icon.ico")
titleFont = font.Font(family='Aucoinlight', size=20)
mainFont = font.Font(family='Aucoinlight', size=13)
littleFont = font.Font(family='Aucoinlight', size=11)


titleLabel = tkinter.Label(window, text="sh0rtinGame", fg="white", bg="black")
titleLabel.place(x=38, y=8)
titleLabel['font'] = titleFont

byLabel = tkinter.Label(window, text="by akira", fg="white", bg="black")
byLabel.place(x=83, y=48)
byLabel['font'] = mainFont

logoImg = tkinter.PhotoImage(file="src/img/icon2.png")
logoImgLabel = tkinter.Label(window,image=logoImg, width=70, height=70)
logoImgLabel.place(x=90, y=77)

dsd = tkinter.Label(window, text="discord:\nakira#9322", fg="white", bg="black", justify="left")
dsd.place(x=20, y=177)
dsd['font'] = littleFont

github = tkinter.Label(window, text="github:\nakira - trinity", fg="white", bg="black", justify="left")
github.place(x=143, y=177)
github['font'] = littleFont

scriptField = tkinter.Text(window, bg="grey", fg="black", width=45, height=12)
scriptField.place(x=242, y=20)

shortButton = tkinter.Button(window, text="sh0rt it !", bg="black", fg="white", command=shortCode)
shortButton.place(x=539, y=228)
shortButton['font'] = littleFont


shortenCode = tkinter.Label(window, text="sh0rtened code:", bg="black", fg="white")
shortenCode.place(x=15, y=265)
shortenCode['font'] = littleFont

outputField = tkinter.Text(window, bg="grey", fg="black", width=75, height=1.47)
outputField.place(x=15, y=294)


window.config(background="black")
window.mainloop()
