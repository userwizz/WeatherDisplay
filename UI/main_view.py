#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, BOTH, W, N, E, S, Label, Frame, PhotoImage, LEFT
import time
from UI.weather_data import WeatherData
from UI.icon_helper import IconHelper



class WeatherUI(Frame):
    def __init__(self):
        super().__init__()
        self.secs_since_last_update = 11
        self.icon_helper = IconHelper()
        self.initUI()

    def initUI(self):

        self.deg_sign = chr(176)

        # main view
        self.master.title('Windows')
        self.pack(fill=BOTH, expand=True)
        self.configure(background='black')

        # args
        self.text_style_args = dict(fg='white', bg='black', font='14')
        self.text_padding_args = dict(pady=5, padx=5)
        self.photo_style_args = dict(borderwidth=0, highlightthickness=0)

        # columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # view frames
        self._add_time_and_date_frame()
        self._add_current_weather_frame()
        self._add_forecast_today_frame()
        self._add_inside_status_frame()
        self._add_forecast_for_coming_days_frame()

        self.updateView()

    def _add_time_and_date_frame(self):

        frame_date_time = Frame(self, highlightcolor="grey", highlightthickness=1, background='black')
        frame_date_time.columnconfigure(0, weight=1)
        self.txt_label_time = Label(frame_date_time, text='', **self.text_style_args)
        self.txt_label_time.grid(row=0, column=0, **self.text_padding_args)
        self.txt_label_date = Label(frame_date_time, text='14..2017', **self.text_style_args)
        self.txt_label_date.grid(row=0, column=1, sticky=E, **self.text_padding_args)
        frame_date_time.grid(row=0, column=0, columnspan=4, sticky=W + E + N + S)

    def _add_current_weather_frame(self):

        frame_current_weather = Frame(self, highlightcolor="grey", highlightthickness=1, background='black')
        img = PhotoImage(file='../resource/92.png')
        self.img_label_current = Label(frame_current_weather, image=img, **self.photo_style_args)
        self.img_label_current.image = img
        self.img_label_current.grid(row=0, column=0, sticky=W + N)

        self.txt_label_current = Label(frame_current_weather, text='',justify=LEFT, **self.text_style_args)
        self.txt_label_current.grid(row=0, column=1, sticky=W + N, **self.text_padding_args)
        frame_current_weather.grid(row=1, column=0, sticky=W + E + N + S)

    def _add_forecast_today_frame(self):

        # forecast today, +3h +6 +9h
        frame_forecast_today = Frame(self, highlightcolor="grey", highlightthickness=1, background='black')
        frame_forecast_today.rowconfigure(0, weight=1)
        self.txt_label_forecast_today = Label(frame_forecast_today, text='', justify=LEFT, **self.text_style_args)
        self.txt_label_forecast_today.grid(row=0, column=0, **self.text_padding_args)
        frame_forecast_today.grid(row=1, column=1, sticky=W + E + N + S)

    def _add_inside_status_frame(self):

        frame_inside = Frame(self, highlightcolor="grey", highlightthickness=1, background='black')
        frame_inside.rowconfigure(0, weight=1)
        self.txt_label_inside = Label(frame_inside, justify=LEFT, text='22' + ' ' + self.deg_sign + 'C\n' +
                                                                       'humidity: 70%\n',
                                      **self.text_style_args)
        self.txt_label_inside.grid(row=0, column=0, **self.text_padding_args)
        frame_inside.grid(row=1, column=2, sticky=W + E + N + S)

    def _add_forecast_for_coming_days_frame(self):

        frame_forecast = Frame(self, highlightcolor="grey", highlightthickness=1, background='black')

        # forecast + 1 day
        img = PhotoImage(file='../resource/92.png')
        self.img_label_plus_1d = Label(frame_forecast, image=img, **self.photo_style_args)
        self.img_label_plus_1d.image = img
        self.img_label_plus_1d.grid(row=0, column=0, sticky=W + N)

        self.txt_label_plus_1d = Label(frame_forecast, text='', justify=LEFT, **self.text_style_args)
        self.txt_label_plus_1d.grid(row=0, column=1, sticky=W + N, **self.text_padding_args)

        # forecast + 2 days
        img = PhotoImage(file='../resource/92.png')
        self.img_label_plus_2d = Label(frame_forecast, image=img, **self.photo_style_args)
        self.img_label_plus_2d.image = img
        self.img_label_plus_2d.grid(row=0, column=2, sticky=W + N)

        self.txt_label_plus_2d = Label(frame_forecast,text='', justify=LEFT, **self.text_style_args)
        self.txt_label_plus_2d.grid(row=0, column=3, sticky=W + N, **self.text_padding_args)

        # forecast + 3 days
        img = PhotoImage(file='../resource/92.png')
        self.img_label_plus_3d = Label(frame_forecast, image=img, **self.photo_style_args)
        self.img_label_plus_3d.image = img
        self.img_label_plus_3d.grid(row=0, column=4, sticky=W + N)

        self.txt_label_plus_3d = Label(frame_forecast, text='', justify=LEFT, **self.text_style_args)
        self.txt_label_plus_3d.grid(row=0, column=5, sticky=W + N, **self.text_padding_args)

        # forecast + 4 days
        img = PhotoImage(file='../resource/92.png')
        self.img_label_plus_4d = Label(frame_forecast, image=img, **self.photo_style_args)
        self.img_label_plus_4d.image = img
        self.img_label_plus_4d.grid(row=0, column=6, sticky=W + N)

        self.txt_label_plus_4d = Label(frame_forecast, text='', justify=LEFT, **self.text_style_args)
        self.txt_label_plus_4d.grid(row=0, column=7, sticky=W + N, **self.text_padding_args)

        frame_forecast.grid(row=2, column=0, columnspan=4, sticky=W + E + N + S)

    def updateView(self):
        self.secs_since_last_update += 1

        time_now = time.strftime("%H:%M:%S")
        date_now = time.strftime("%d.%m.%Y")

        if self.secs_since_last_update > 10:
            self.secs_since_last_update = 0
            self._my_data = WeatherData(time_now)
            self._my_data.start()

        if not self._my_data.is_alive():
            self.txt_label_current.configure(text=self._get_current_weather_text())
            self.txt_label_forecast_today.configure(text=self._get_next_hours_text())
            self.txt_label_plus_1d.configure(text=self._get_next_days_text(self._my_data.get_forecast_plus_1d()))
            self.txt_label_plus_2d.configure(text=self._get_next_days_text(self._my_data.get_forecast_plus_2d()))
            self.txt_label_plus_3d.configure(text=self._get_next_days_text(self._my_data.get_forecast_plus_3d()))
            self.txt_label_plus_4d.configure(text=self._get_next_days_text(self._my_data.get_forecast_plus_4d()))

            img = PhotoImage(file=self.icon_helper.get_icon_path(self._my_data.get_current_weather().weather_id))
            self.img_label_current.configure(image=img)
            self.img_label_current.image = img

            img = PhotoImage(file=self.icon_helper.get_icon_path(self._my_data.get_forecast_plus_1d().weather_id))
            self.img_label_plus_1d.configure(image=img)
            self.img_label_plus_1d.image = img

            img = PhotoImage(file=self.icon_helper.get_icon_path(self._my_data.get_forecast_plus_2d().weather_id))
            self.img_label_plus_2d.configure(image=img)
            self.img_label_plus_2d.image = img

            img = PhotoImage(file=self.icon_helper.get_icon_path(self._my_data.get_forecast_plus_3d().weather_id))
            self.img_label_plus_3d.configure(image=img)
            self.img_label_plus_3d.image = img

            img = PhotoImage(file=self.icon_helper.get_icon_path(self._my_data.get_forecast_plus_4d().weather_id))
            self.img_label_plus_4d.configure(image=img)
            self.img_label_plus_4d.image = img

        self.txt_label_time.configure(text=time_now)
        self.txt_label_date.configure(text=date_now)

        self.after(1000, self.updateView)

    def _get_current_weather_text(self):
        text = str(self._my_data.get_current_weather().temp) + ' ' + self.deg_sign + 'C\n' + \
               str(self._my_data.get_current_weather().wind) + ' m/s\n' + \
               str(self._my_data.get_current_weather().deg) + ' ' + self.deg_sign
        return text

    def _get_next_hours_text(self):
        data = [self._my_data.get_forecast_next_3_hours(),
                self._my_data.get_forecast_next_6_hours(),
                self._my_data.get_forecast_next_9_hours(),
                self._my_data.get_forecast_next_12_hours()]
        ret_val = ""

        for i in range(len(data)):
            text = \
                '@' + str(data[i].time) + ': ' + \
                str(data[i].temp) + ' ' + self.deg_sign + 'C, ' + \
                str(data[i].wind) + ' m/s, ' + \
                str(data[i].description)
            ret_val += text + '\n'
            print(str(i) + ' ' + ret_val)

        return ret_val

    def _get_next_days_text(self, data):
        text = 'Day: ' + str(data.temp_day) + ' ' + self.deg_sign + 'C\n' + \
               'Night: ' + str(data.temp_night) + ' ' + self.deg_sign + 'C\n' + \
               str(data.wind) + ' m/s\n' + \
               str(data.deg) + ' ' + self.deg_sign
        return text


def main():
    root = Tk()
    # root.attributes('-fullscreen', True)
    app = WeatherUI()
    root.minsize(width=800, height=480)
    root.maxsize(width=800, height=480)

    root.mainloop()


if __name__ == '__main__':
    main()
