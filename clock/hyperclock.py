import tkinter as tk
import tkinter.font as tkf
import time


class HyperClock:
    """
    simple digital clock for hyperpixel 4.0 square
    """
    def __init__(self):
        """
        create window with settings and start loop
        """
        self.window = tk.Tk()
        self.window.title('HyperClock')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")
        self.window.bind('<Escape>', exit)
        self.window.attributes("-fullscreen", True)

        big_font = tkf.Font(family="Open 24 Display St", size=90, weight="normal")
        small_font = tkf.Font(family="Open 24 Display St", size=20, weight="normal")

        self.txt_time = tk.Label(self.window, text='', font=big_font, bg="black", fg="#39ff14")
        self.txt_time.place(anchor=tk.CENTER, relx=.5, rely=.5)

        self.txt_day = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self.txt_day.place(anchor=tk.CENTER, relx=.65, rely=.6)

        self.txt_date = tk.Label(self.window, text='', font=small_font, bg="black", fg="#39ff14")
        self.txt_date.place(anchor=tk.CENTER, relx=.4, rely=.6)

        self.window.after(1000, self.set_current_time)
        self.window.mainloop()

    def set_current_time(self):
        """
        get values and set into labels
        :return: None
        """
        current_time = f"{time.strftime('%H')}:{time.strftime('%M')}:{time.strftime('%S')}"
        current_day = f"{time.strftime('%A')}"
        current_date = f"{time.strftime('%B')} {time.strftime('%d')} {time.strftime('%Y')}"

        self.txt_time.configure(text=current_time)
        self.txt_day.configure(text=current_day)
        self.txt_date.configure(text=current_date)

        self.window.after(1000, self.set_current_time)

    def exit(self, event):
        """
        exit and close window
        :param event:
        :return: None
        """
        self.window.quit()


if __name__ == '__main__':
    RUN = HyperClock()
