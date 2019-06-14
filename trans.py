from tkinter import *
from googletrans import Translator


root = Tk()


f = LabelFrame(root, text='Hubery_Jun', padx=30, pady=30)
f.pack(padx=200, pady=200)

Label(f, text='谷歌翻译(v1.0.1)', font=('楷体', 14)).grid(row=0, column=1, padx=5, pady=5)

Label(f, text='源语言：').grid(row=1)
Label(f, text='目标语言：').grid(row=2)

e1 = Entry(f)
e2 = Entry(f)

e1.grid(row=1, column=1, padx=10, pady=10)
e2.grid(row=2, column=1, padx=10, pady=10)


def show():
    result = e1.get()
    # print(result)

    translator = Translator(service_urls=['translate.google.cn'])
    text = translator.translate(result, src='en', dest='zh-cn').text

    var = StringVar()
    var.set(text)
    Entry(f, textvariable=var).grid(row=2, column=1, padx=10, pady=5)

Button(f, text='翻译', width=10, command=show).grid(row=4, column=0, sticky=W, padx=10, pady=5)
Button(f, text='退出', width=10, command=root.quit).grid(row=4, column=1, sticky=E, padx=10, pady=5)

mainloop()
