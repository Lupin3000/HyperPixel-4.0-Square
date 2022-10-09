import tkinter as tk
import tkinter.font as tkf
import time


class HyperClock:
    """
    tkinter window class to display a digital clock on hyperpixel 4.0 square
    """

    _LABEL_TIME = None
    _LABEL_DATE = None

    def __init__(self, fullscreen: bool = False) -> None:
        """
        create tkinter window and start loop
        :param fullscreen: set window fullscreen mode as bool
        """
        print(f"[INFO]: fullscreen: {fullscreen}")
        self.fullscreen = bool(fullscreen)

        self.window = tk.Tk()
        self._config_window()
        self._add_widgets()

        self.window.after(1000, self.__set_current_time)
        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window, bind events and set fullscreen mode
        :return: None
        """
        self.window.title('HyperClock')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.config(cursor='none')
            self.window.attributes("-fullscreen", True)

    def _add_widgets(self) -> None:
        """
        add specific tkinter widgets to window
        :return: None
        """
        big_font = tkf.Font(family="Open 24 Display St", size=90, weight="normal")
        small_font = tkf.Font(family="Open 24 Display St", size=20, weight="normal")

        self._LABEL_TIME = tk.Label(self.window, text='', font=big_font, bg="black", fg="#39ff14")
        self._LABEL_DATE = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")

        self._LABEL_TIME.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self._LABEL_DATE.place(anchor=tk.CENTER, relx=.5, rely=.65)

    def __set_current_time(self) -> None:
        """
        get time/date values and update tkinter labels
        :return: None
        """
        current_time = f"{time.strftime('%H')}:{time.strftime('%M')}:{time.strftime('%S')}"
        current_date = f"{time.strftime('%B')} {time.strftime('%d')} {time.strftime('%Y')} {time.strftime('%A')}"

        self._LABEL_TIME.configure(text=current_time)
        self._LABEL_DATE.configure(text=current_date)

        self.window.after(1000, self.__set_current_time)

    def _on_closing(self) -> None:
        """
        catch mouse close window event
        :return: None
        """
        self._exit('close window by mouse')

    def _exit(self, event) -> None:
        """
        exit and close tkinter window
        :param event:
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.destroy()


if __name__ == '__main__':
    HyperClock()
