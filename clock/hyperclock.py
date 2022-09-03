import tkinter as tk
import tkinter.font as tkf
import time


class HyperClock:
    """
    simple digital clock for hyperpixel 4.0 square
    """

    _LABEL_TIME = None
    _LABEL_DAY = None
    _LABEL_DATE = None

    def __init__(self, user: str = 'john', fullscreen: bool = False) -> None:
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

            self.window.after(1000, self.__set_current_time)
            self.window.mainloop()
        else:
            exit('Please provide a user name')

    def _config_window(self) -> None:
        """
        configure window
        :return: None
        """
        self.window.title(f"HyperClock: {self.user}")
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
        big_font = tkf.Font(family="Open 24 Display St", size=90, weight="normal")
        small_font = tkf.Font(family="Open 24 Display St", size=20, weight="normal")

        self._LABEL_TIME = tk.Label(self.window, text='', font=big_font, bg="black", fg="#39ff14")
        self._LABEL_DAY = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self._LABEL_DATE = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")

        self._LABEL_TIME.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self._LABEL_DAY.place(anchor=tk.CENTER, relx=.65, rely=.6)
        self._LABEL_DATE.place(anchor=tk.CENTER, relx=.4, rely=.6)

    def __set_current_time(self) -> None:
        """
        get values and set into labels
        :return: None
        """
        current_time = f"{time.strftime('%H')}:{time.strftime('%M')}:{time.strftime('%S')}"
        current_day = f"{time.strftime('%A')}"
        current_date = f"{time.strftime('%B')} {time.strftime('%d')} {time.strftime('%Y')}"

        self._LABEL_TIME.configure(text=current_time)
        self._LABEL_DAY.configure(text=current_day)
        self._LABEL_DATE.configure(text=current_date)

        self.window.after(1000, self.__set_current_time)

    def _exit(self, event) -> None:
        """
        exit and close window
        :param event:
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.quit()


if __name__ == '__main__':
    HyperClock()
