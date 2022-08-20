import tkinter as tk
import tkinter.font as tkf
import requests


class HyperDuinoCoin:
    """
    simple app to display duino coins
    """

    LABEL_USER = None
    LABEL_BALANCE = None
    LABEl_MINERS = None

    def __init__(self, user):
        """
        create window and start loop
        """
        if user:
            self.user = str(user)
            self.txt_stake_amount = None

            self.window = tk.Tk()
            self._config_window()
            self._add_widgets()

            self.window.after(100, self.__set_values)
            self.window.mainloop()
        else:
            exit('Please provide a user name')

    def _config_window(self):
        """
        configure window
        :return: None
        """
        self.window.title('HyperCoin')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")
        self.window.bind('<Escape>', exit)
        self.window.attributes("-fullscreen", True)

    def _add_widgets(self):
        """
        add widgets to window
        :return: None
        """
        big_font = tkf.Font(family="Arial", size=90, weight='normal')
        small_font = tkf.Font(family="Arial", size=20, weight='normal')

        self.LABEL_USER = tk.Label(self.window, text=self.user, font=big_font, bg="black", fg="#39ff14")
        self.LABEL_USER.place(anchor=tk.CENTER, relx=.5, rely=.4)

        self.LABEL_BALANCE = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self.LABEL_BALANCE.place(anchor=tk.CENTER, relx=.5, rely=.5)

        self.LABEl_MINERS = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self.LABEl_MINERS.place(anchor=tk.CENTER, relx=.5, rely=.55)

    def __set_values(self):
        """
        call rest api and update labels
        :return: None
        """
        response = requests.get('https://server.duinocoin.com/users/' + self.user)

        if response.status_code == 200:
            json_response = response.json()
            txt_balance = f"{json_response['result']['balance']['balance']} DUCO\'s"
            txt_miners = f"Active miners: {len(json_response['result']['miners'])}"

            self.LABEL_BALANCE.configure(text=txt_balance)
            self.LABEl_MINERS.configure(text=txt_miners)

        self.window.after(1000, self.__set_values)

    def _exit(self, event):
        """
        exit and close window
        :param event:
        :return: None
        """
        self.window.quit()


if __name__ == '__main__':
    RUN = HyperDuinoCoin(user='revox')
