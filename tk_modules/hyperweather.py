import tkinter as tk
import tkinter.font as tkf
import requests


class HyperWeather:
    """
    tkinter window class to display weather for specific location on hyperpixel 4.0 square
    """

    _LABEL_CITY = None
    _LABEL_TEMPERATURE = None
    _LABEL_DESCRIPTION = None

    def __init__(self, apikey: str,
                 zipcode: int = 8405,
                 countrycode: str = 'CH',
                 measurement: str = 'standard',
                 fullscreen: bool = False) -> None:
        """
        create tkinter window and start loop
        :param apikey: set OpenWeather API key as string
        :param zipcode: zipcode as int
        :param countrycode: 2-letter country code (ISO3166) as string eq. CH, US or etc.
        :param measurement: measurement as 'standard', 'metric' or 'imperial'
        :param fullscreen: set window fullscreen mode as bool
        """
        print(f"[INFO]: zip: {zipcode}, country: {countrycode}, measurement: {measurement}, fullscreen: {fullscreen}")
        self.fullscreen = bool(fullscreen)
        self.apikey = str(apikey)
        self.countrycode = str(countrycode)
        self.measurement = str(measurement)
        self.zipcode = int(zipcode)
        self.count = 1

        self.window = tk.Tk()
        self._config_window()
        self._add_widgets()

        self.window.after(10, self.__set_values)
        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window behavior
        :return: None
        """
        self.window.title(f"HyperWeather")
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.attributes("-fullscreen", True)

    def _add_widgets(self) -> None:
        """
        add specific tkinter widgets to window
        :return: None
        """
        temp_font = tkf.Font(family='Arial', size=20, weight='normal')
        city_font = tkf.Font(family='Arial', size=20, weight='normal')
        desc_font = tkf.Font(family='Arial', size=10, weight='normal')

        self._LABEL_CITY = tk.Label(self.window, text='unknown', font=city_font, bg="black", fg='#39ff14')
        self._LABEL_TEMPERATURE = tk.Label(self.window, text='unknown', font=temp_font, bg="black", fg='#39ff14')
        self._LABEL_DESCRIPTION = tk.Label(self.window, text='unknown', font=desc_font, bg="black", fg='#39ff14')

        self._LABEL_CITY.place(anchor=tk.CENTER, relx=.5, rely=.4)
        self._LABEL_TEMPERATURE.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self._LABEL_DESCRIPTION.place(anchor=tk.CENTER, relx=.5, rely=.6)

    @staticmethod
    def get_measurement_units(measurement: str) -> str:
        """
        convert measurement into units
        :param measurement: measurement standard, metric or imperial
        :return: string of units
        """
        if measurement == 'imperial':
            unit = u"\N{DEGREE SIGN}" + 'F'
        elif measurement == 'metric':
            unit = u"\N{DEGREE SIGN}" + 'C'
        else:
            unit = 'K'

        return str(unit)

    def __set_values(self) -> None:
        """
        call rest api and update tkinter labels
        :return: None
        """
        city = ''
        temp = ''
        desc = ''

        zip_code = f"{self.zipcode},{self.countrycode}"
        api_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = dict(zip=zip_code, units=self.measurement, appid=self.apikey)

        response = requests.get(api_url, params)
        print(f'[INFO]: send {self.count} request to {api_url}')

        if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type'):
            json_response = response.json()
            city = f"{json_response['name']}"
            temp = f"{json_response['main']['temp']} {HyperWeather.get_measurement_units(self.measurement)}"
            desc = f"{json_response['weather'][0]['description']}"
        try:
            self.count += 1
            self._LABEL_CITY.configure(text=city)
            self._LABEL_TEMPERATURE.configure(text=temp)
            self._LABEL_DESCRIPTION.configure(text=desc)
        except KeyError as err:
            print(f"[ERROR]: {err}")

        self.window.after(30000, self.__set_values)

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
    HyperWeather(apikey='', measurement='metric')
