#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, BOTH, W, N, E, S, Label, Frame, Button, PhotoImage, LEFT, CENTER
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

        deg_sign = chr(176)

        self.master.title('Windows')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        #self.columnconfigure(3, pad=7)
        #self.rowconfigure(1, weight=1)
        #self.rowconfigure(5, pad=7)

        # time and date
        frame_date_time = Frame(self, highlightcolor="grey", highlightthickness=1,background='black')
        frame_date_time.columnconfigure(1, weight=1)
        txt_label_time = Label(frame_date_time, text='13:22:34', **self.text_style_args)
        txt_label_time.grid(row=0, column=1, **self.text_padding_args)
        txt_label_date = Label(frame_date_time, text='14.11.2017', **self.text_style_args)
        txt_label_date.grid(row=0, column=3, sticky=E, **self.text_padding_args)
        frame_date_time.grid(row=0,column=0, columnspan=3, sticky = W+E+N+S)

        # current weather
        frame_current_weather = Frame(self, highlightcolor="grey", highlightthickness=1,background='black')
        #frame_date_time.columnconfigure(2, weight=1)
        img = PhotoImage(file='../resource/2.ppm')
        img_label_current = Label(frame_current_weather, image=img, **self.photo_style_args)
        img_label_current.image = img
        img_label_current.grid(row=1, column=0, sticky=W+N)

        text_current = Label(frame_current_weather, text='-13' + ' ' + deg_sign + 'C\n3 m/s\n88' +
                                        deg_sign, justify=LEFT, **self.text_style_args)
        text_current.grid(row=1, column=1, sticky=W+N, **self.text_padding_args)
        frame_current_weather.grid(row=1, column=0, sticky=W+E+N+S)


        # forecast today, +3h +6 +9h
        frame_forecast_today = Frame(self, highlightcolor="grey", highlightthickness=1,background='black')
        frame_forecast_today.rowconfigure(0, weight=1)
        text_forecast_today = Label(frame_forecast_today, text='-10' + ' ' + deg_sign + 'C, 3 m/s, clear sky\n' +
                                                               '-8' + ' ' + deg_sign + 'C, 3 m/s, light snow\n' +
                                                               '-5' + ' ' + deg_sign + 'C, 1 m/s, light snow\n',
                                                                **self.text_style_args)
        text_forecast_today.grid(row=0, column=0, **self.text_padding_args)
        frame_forecast_today.grid(row=1, column=1, sticky=W+E+N+S)


        # inside
        frame_inside = Frame(self, highlightcolor="grey", highlightthickness=1,background='black')
        frame_inside.rowconfigure(0, weight=1)
        text_inside = Label(frame_inside, justify=LEFT, text='22' + ' ' + deg_sign + 'C\n' +
                                                               'humidity: 70%\n',
                                                                **self.text_style_args)
        text_inside.grid(row=0, column=0, **self.text_padding_args)
        frame_inside.grid(row=1, column=2, sticky=W+E+N+S)


def main():
    root = Tk()
    #root.attributes('-fullscreen', True)
    app = WeatherUI()
    root.minsize(width=800, height=480)
    root.maxsize(width=800, height=480)



    root.mainloop()


if __name__ == '__main__':
    main()

