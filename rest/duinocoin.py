import tkinter as tk
import tkinter.font as tkf
import requests


class HyperDuinoCoin:
    """
    simple app to display duino coins
    """

    _LABEL_USER = None
    _LABEL_BALANCE = None
    _LABEl_MINERS = None

    def __init__(self, user: str = 'revox', fullscreen: bool = False) -> None:
        """
        create window and start loop
        :param user: duino username
        :param fullscreen: set window fullscreen mode
        """
        if user:
            print(f"[INFO]: username: {user}, fullscreen: {fullscreen}")
            self.user = str(user)
            self.fullscreen = bool(fullscreen)

            self.window = tk.Tk()
            self._config_window()
            self._add_widgets()

            self.window.after(100, self.__set_values)
            self.window.mainloop()
        else:
            exit('Please provide a user name')

    def _config_window(self) -> None:
        """
        configure window
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
        add widgets to window
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
        call rest api and update labels
        :return: None
        """
        response = requests.get('https://server.duinocoin.com/users/' + self.user)

        if response.status_code == 200:
            json_response = response.json()
            txt_balance = f"{json_response['result']['balance']['balance']} DUCO\'s"
            txt_miners = f"Active miners: {len(json_response['result']['miners'])}"

            self._LABEL_BALANCE.configure(text=txt_balance)
            self._LABEl_MINERS.configure(text=txt_miners)

        self.window.after(1000, self.__set_values)

    def _exit(self, event) -> None:
        """
        exit and close window
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.destroy()


if __name__ == '__main__':
    HyperDuinoCoin()
