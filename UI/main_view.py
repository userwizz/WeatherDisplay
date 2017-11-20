#!/user/bin/env python
# -*- coding: utf-8 -*-
from tkinter import * #Tk, Text, BOTH, W, N, E, S, Label, Frame, Button
#from tkinter.ttk import Frame, Button, Style


class WeatherUI (Frame):


    def __init__(self):
        super().__init__()

        self.configure(background='black')

        self.text_style_args = dict(fg='white', bg='black', font = '14')
        self.text_padding_args = dict(pady = 4, padx = 5)

        self.photo_style_args = dict(borderwidth=0, highlightthickness=0)

        self.initUI()

    def initUI(self):
        self.master.title('Windows')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        # time and date
        time = Label(self, text='13:22:34', **self.text_style_args)
        time.grid(row=0, column=1, **self.text_padding_args)
        date = Label(self, text='14.11.2017', **self.text_style_args)
        date.grid(row=0, column=3, sticky=E, **self.text_padding_args)

        # current weather
        img = PhotoImage(file='../resource/2.ppm')
        icon_current = Label(self, image=img, **self.photo_style_args)
        icon_current.image = img
        icon_current.grid(row=1, column=0, padx=5, sticky=W+N)

        deg_sign = chr(176)
        text_current = Label(self, text='-13' + deg_sign + ' C\n3 m/s\n88' +
                                        deg_sign, justify=LEFT, **self.text_style_args)
        text_current.grid(row=1, column=1, sticky=W+N, **self.text_padding_args)


        abtn = Button(self, text='Activate')
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text='Close')
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text='Help')
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text='OK')
        obtn.grid(row=5, column=3)


def main():
    root = Tk()
    #root.geometry('350x300+300+300')
    root.attributes('-fullscreen', True)
    app = WeatherUI()
    #root.configure(background='black')
    #root.minsize(width=800, height=480)
    #root.maxsize(width=800, height=480)
    root.mainloop()


if __name__ == '__main__':
    main()

'''
root = tk.Tk()
#root.attributes('-fullscreen', True)
root.configure(background='black')
root.minsize(width=800, height=480)
root.maxsize(width=800, height=480)



explanation='Hello Tkinter!'
logo = tk.PhotoImage(file='../resource/2.ppm')

w1 = tk.Label(root,
              image=logo,
              borderwidth=0,
              highlightthickness=0,).pack(side='right')

w2 = tk.Label(root,
              justify = tk.LEFT,
              fg = 'white',
              bg = 'black',
              font = '12',
              text=explanation).pack(side='left')


root.mainloop()
'''