import tkinter as tk
import tkinter.font as tkf
import time
import requests


class HyperTimeWeather:

    def __init__(self,
                 apikey: str = None,
                 zipcode: int = None,
                 countrycode: str = None,
                 measurement: str = 'standard',
                 fullscreen: bool = False):
        """
        create tkinter application and loop
        :param apikey: OpenWeather API key
        :param zipcode: zipcode as int
        :param countrycode: 2-letter country code (ISO3166)
        :param measurement: 'standard', 'metric' or 'imperial'
        :param fullscreen: show window as fullscreen
        """
        self.apikey = str(apikey)
        self.zipcode = int(zipcode)
        self.countrycode = str(countrycode)
        self.measurement = str(measurement)
        self.fullscreen = bool(fullscreen)

        self.top_frame = None
        self.bottom_frame = None
        self.label_time = None
        self.label_date = None
        self.label_temperature = None
        self.label_information = None

        self.window = tk.Tk()
        self._config_window()
        self._create_frames()
        self._add_widget()

        self.window.after(1, self.__start_frame_updates)
        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window behavior
        :return: None
        """
        self.window.title('HyperTime')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.geometry('720x720+0+0')
        self.window.config(bg='black')
        self.window.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.config(cursor='none')
            self.window.attributes("-fullscreen", True)

    def _create_frames(self) -> None:
        """
        create tkinter frames
        :return: None
        """
        background = 'black'

        self.top_frame = tk.Frame(self.window, bg=background, height=360, width=100)
        self.bottom_frame = tk.Frame(self.window, bg=background, height=360)

        self.top_frame.grid(column=0, row=0, sticky=tk.E+tk.W)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.bottom_frame.grid(column=0, row=1, sticky=tk.E+tk.W)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)

    def _add_widget(self) -> None:
        """
        add specific tkinter widgets to frames
        :return: None
        """
        font_time = tkf.Font(family="LED Display7", size=80, weight='normal')
        font_date = tkf.Font(family="LED Display7", size=25, weight='normal')
        font_temp = tkf.Font(family="LED Display7", size=80, weight='normal')
        font_info = tkf.Font(family="LED Display7", size=25, weight='normal')

        self.label_time = tk.Label(self.top_frame, font=font_time, bg='black', fg='#8ED1FC')
        self.label_time.place(anchor=tk.CENTER, relx=.5, rely=.5)

        self.label_date = tk.Label(self.top_frame, font=font_date, bg='black', fg='#33FFFD')
        self.label_date.place(anchor=tk.CENTER, relx=.5, rely=.7)

        self.label_temperature = tk.Label(self.bottom_frame, font=font_temp, bg='black', fg='#8ED1FC')
        self.label_temperature.place(anchor=tk.CENTER, relx=.5, rely=.25)

        self.label_information = tk.Label(self.bottom_frame, font=font_info, bg='black', fg='#33FFFD')
        self.label_information.place(anchor=tk.CENTER, relx=.5, rely=.55)

    def __start_frame_updates(self) -> None:
        """
        call initial methods to update values
        :return: None
        """
        self.__set_time_values()
        self.__set_weather_values()

    def __set_time_values(self) -> None:
        """
        update values for clock and call itself
        :return: None
        """
        current_time = f"{time.strftime('%H')}:{time.strftime('%M')}:{time.strftime('%S')}"
        current_date = f"{time.strftime('%B')} {time.strftime('%d')} {time.strftime('%Y')} - {time.strftime('%A')}"

        self.label_time.config(text=current_time)
        self.label_date.config(text=current_date)

        self.top_frame.after(1000, self.__set_time_values)

    @staticmethod
    def get_measurement_units(measurement: str) -> tuple:
        """
        convert measurement into units
        :param measurement: measurement standard, metric or imperial
        :return: tuple of units and speed
        """
        if measurement == 'imperial':
            unit = u"\N{DEGREE SIGN}" + 'F'
            speed = 'm/h'
        elif measurement == 'metric':
            unit = u"\N{DEGREE SIGN}" + 'C'
            speed = 'm/s'
        else:
            unit = 'K'
            speed = 'm/s'

        return str(unit), str(speed)

    def __set_weather_values(self) -> None:
        """
        update values for weather and call itself
        :return: None
        """
        zip_code = f'{self.zipcode},{self.countrycode}'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = dict(zip=zip_code, units=self.measurement, appid=self.apikey)
        response = requests.get(url, params)

        temperature = ''
        pressure = ''
        humidity = ''
        wind = ''

        if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type'):
            json_response = response.json()
            units = HyperTimeWeather.get_measurement_units(self.measurement)
            temperature = f"{json_response['main']['temp']}{units[0]}"
            pressure = f"{json_response['main']['pressure']} hPa"
            humidity = f"{json_response['main']['humidity']} %"
            wind = f"{json_response['wind']['speed']} {units[1]}"

        self.label_temperature.config(text=temperature)
        self.label_information.config(text=f"Pressure: {pressure}\nHumidity: {humidity}\nWind Speed:{wind}")

        self.bottom_frame.after(30000, self.__set_weather_values)

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
    HyperTimeWeather(apikey='',
                     zipcode=8405,
                     countrycode='CH',
                     measurement='metric',
                     fullscreen=True)
