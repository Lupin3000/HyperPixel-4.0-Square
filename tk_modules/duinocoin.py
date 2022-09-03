import tkinter as tk
import tkinter.font as tkf
import requests


class HyperDuinoCoin:
    """
    tkinter window class to display duino coins status for specific user on hyperpixel 4.0 square
    """

    _LABEL_USER = None
    _LABEL_BALANCE = None
    _LABEl_MINERS = None

    def __init__(self, user: str = 'revox', fullscreen: bool = False) -> None:
        """
        create tkinter window and start loop
        :param user: duino username as string
        :param fullscreen: set window fullscreen mode as bool
        """
        print(f"[INFO]: username: {user}, fullscreen: {fullscreen}")
        self.user = str(user)
        self.fullscreen = bool(fullscreen)

        self.window = tk.Tk()
        self._config_window()
        self._add_widgets()

        self.window.after(100, self.__set_values)
        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window, bind events and set fullscreen mode
        :return: None
        """
        self.window.title(f"HyperCoin: {self.user}")
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")

        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.attributes("-fullscreen", True)

    def _add_widgets(self) -> None:
        """
        add specific tkinter widgets to window
        :return: None
        """
        big_font = tkf.Font(family="Arial", size=90, weight='normal')
        small_font = tkf.Font(family="Arial", size=20, weight='normal')

        self._LABEL_USER = tk.Label(self.window, text=self.user, font=big_font, bg="black", fg="#39ff14")
        self._LABEL_BALANCE = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self._LABEl_MINERS = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")

        self._LABEL_USER.place(anchor=tk.CENTER, relx=.5, rely=.4)
        self._LABEL_BALANCE.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self._LABEl_MINERS.place(anchor=tk.CENTER, relx=.5, rely=.55)

    def __set_values(self) -> None:
        """
        call rest api and update tkinter labels
        :return: None
        """
        response = requests.get('https://server.duinocoin.com/users/' + self.user)

        if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type'):

            json_response = response.json()

            try:
                balance = f"{json_response['result']['balance']['balance']} DUCO\'s"
                miners = f"Active miners: {len(json_response['result']['miners'])}"

                self._LABEL_BALANCE.configure(text=balance)
                self._LABEl_MINERS.configure(text=miners)
            except KeyError as e:
                print(f"[ERROR]: {e}")

        self.window.after(1000, self.__set_values)

    def _exit(self, event) -> None:
        """
        exit and close tkinter window
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.destroy()


if __name__ == '__main__':
    HyperDuinoCoin()
