import tkinter as tk
import tkinter.font as tkf
from datetime import date

import holidays


class HyperHoliday:
    """
    tkinter window class to display next holiday on hyperpixel 4.0 square
    """

    _LABEL_NUM = None
    _LABEL_TXT = None

    def __init__(self,
                 country: str = 'CH',
                 region: str = None,
                 vacation: dict = None,
                 fullscreen: bool = False) -> None:
        """
        create tkinter window and start loop
        :param country: 2-letter country code (ISO3166) as string eq. CH, US or etc.
        :param region: optional subdivisions as string eq. AG, AR, AI, BL, BS and etc.
        :param vacation: dictionary of dates and description
        :param fullscreen: set window fullscreen mode as bool
        """
        if vacation is None:
            vacation = {}
        self.country = str(country)
        self.region = str(region.strip())
        self.vacation = dict(vacation)
        self.fullscreen = bool(fullscreen)

        self.today = date.today()
        self.holidays = None

        self.window = tk.Tk()
        self._config_window()
        self._add_widgets()

        self.window.after(10, self._show_result)
        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window behavior
        :return: None
        """
        self.window.title(f'HyperHoliday')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry('720x720+0+0')
        self.window.config(bg='black')
        self.window.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.config(cursor='none')
            self.window.attributes("-fullscreen", True)

    def _add_widgets(self) -> None:
        """
        add specific tkinter widgets to window
        :return: None
        """
        font_num = tkf.Font(family='LED Display7', size=100, weight='normal')
        font_txt = tkf.Font(family='LED Display7', size=25, weight='normal')

        self._LABEL_NUM = tk.Label(self.window, font=font_num, bg='black', fg='#8ED1FC')
        self._LABEL_TXT = tk.Label(self.window, font=font_txt, bg='black', fg='#EEEEEE')

        self._LABEL_NUM.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self._LABEL_TXT.place(anchor=tk.CENTER, relx=.5, rely=.6)

    def __get_holidays(self) -> None:
        """
        get specific holidays for country on actual year
        :return: None
        """
        if not self.region:
            self.holidays = holidays.country_holidays(country=self.country, years=self.today.year)
        else:
            self.holidays = holidays.country_holidays(country=self.country, subdiv=self.region, years=self.today.year)

    def __add_holidays(self) -> None:
        """
        add own holidays to dictionary
        :return: None
        """
        self.holidays.append(self.vacation)

    def _show_result(self):
        """
        update all tkinter labels
        :return: None
        """
        self.__get_holidays()
        self.__add_holidays()

        my_list = []

        for item in self.holidays:
            diff = (item - self.today).days
            if diff >= 0:
                my_list.append(diff)

        count = min(my_list)

        if count > 10:
            txt_info = 'That takes a while'
        elif count > 0 < 10:
            txt_info = 'It is almost time'
        else:
            txt_info = 'Finally vacation'
            count = 'YES'

        self._LABEL_NUM.config(text=count)
        self._LABEL_TXT.config(text=txt_info)

        self.window.after(30000, self._show_result)

    def _on_closing(self) -> None:
        """
        catch mouse close window event
        :return: None
        """
        self._exit('close window by mouse')

    def _exit(self, event) -> None:
        """
        exit and close tkinter window
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.destroy()


if __name__ == '__main__':
    HyperHoliday(region='ZH', vacation={'2022-10-08': 'private'})
