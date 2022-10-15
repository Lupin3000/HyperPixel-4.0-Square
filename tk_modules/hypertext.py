import threading
import tkinter as tk
import tkinter.font as tkf

import pyttsx3
import speech_recognition as sr


class HyperText:

    __MAX_SPEACH_TIME = 3

    def __init__(self, fullscreen: bool = False):
        """
        create tkinter window and start loop
        :param fullscreen: true or false
        """
        self.fullscreen = bool(fullscreen)

        self.frames = {}
        self.label_first_frame = None
        self.label_second_frame = None
        self.txt_t2s = None
        self.txt_s2t = None
        self.btn_first_frame = None
        self.btn_second_frame = None
        self.btn_record = None
        self.btn_speach = None

        self.record = sr.Recognizer()

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 0.9)
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[3].id)

        self.window = tk.Tk()
        self._config_window()

        self._create_frames()
        self._add_widgets()
        self._switch_frames(0)

        self.window.mainloop()

    def _config_window(self) -> None:
        """
        configure tkinter window behavior
        :return: None
        """
        self.window.title('HyperShow')
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
        create all frames
        :return: None
        """
        self.frames[0] = tk.Frame(self.window, bg='black')
        self.frames[1] = tk.Frame(self.window, bg='black')

        for frame in (self.frames[0], self.frames[1]):
            frame.grid(row=0, column=0, sticky='news')

    def _add_widgets(self) -> None:
        """
        add all widgets to frames
        :return: None
        """
        lbl_font = tkf.Font(family="Technology", size=50, weight='normal')
        txt_font = tkf.Font(family='Arial', size=20, weight='normal')
        btn_font = tkf.Font(family='Arial', size=25, weight='normal')

        bgc = 'black'
        fgc = 'white'

        self.label_first_frame = tk.Label(self.frames[0], font=lbl_font, text='Speach to text', bg=bgc, fg=fgc)
        self.label_second_frame = tk.Label(self.frames[1], font=lbl_font, text='Text to Speach', bg=bgc, fg=fgc)

        self.label_first_frame.place(anchor=tk.CENTER, relx=.5, rely=.2)
        self.label_second_frame.place(anchor=tk.CENTER, relx=.5, rely=.2)

        self.txt_s2t = tk.Text(self.frames[0], font=txt_font, bg=bgc, fg=fgc, height=10, width=45)
        self.txt_s2t.insert(1.0, f"Press record button and speak (for max {self.__MAX_SPEACH_TIME} seconds)")
        self.txt_t2s = tk.Text(self.frames[1], font=txt_font, bg=bgc, fg=fgc, height=10, width=45)
        self.txt_t2s.insert(1.0, "Hi all, I'm a simple example text. You could also type your own.")

        self.txt_s2t.place(anchor=tk.CENTER, relx=.5, rely=.5)
        self.txt_t2s.place(anchor=tk.CENTER, relx=.5, rely=.5)

        self.btn_first_frame = tk.Button(self.frames[0], font=btn_font, text='Text2Speach', padx=5, pady=5,
                                         command=lambda: self._switch_frames(1))
        self.btn_second_frame = tk.Button(self.frames[1], font=btn_font, text='Speach2Text', padx=5, pady=5,
                                          command=lambda: self._switch_frames(0))

        self.btn_first_frame.place(anchor=tk.CENTER, relx=.65, rely=.8)
        self.btn_second_frame.place(anchor=tk.CENTER, relx=.65, rely=.8)

        self.btn_record = tk.Button(self.frames[0], font=btn_font, text='Record', padx=5, pady=5,
                                    command=self.__speach_to_text)
        self.btn_speach = tk.Button(self.frames[1], font=btn_font, text='Speach', padx=5, pady=5,
                                    command=lambda: threading.Thread(target=self.__text_to_speach, daemon=True).start())

        self.btn_record.place(anchor=tk.CENTER, relx=.35, rely=.8)
        self.btn_speach.place(anchor=tk.CENTER, relx=.35, rely=.8)

    def _switch_frames(self, frame_number: int) -> None:
        """
        switch tkinter frames
        :param frame_number: integer of frame to switch
        :return: None
        """
        frame = self.frames[frame_number]
        frame.tkraise()

    def __switch_bt_state(self, state: str) -> None:
        """
        set state for button
        :param state: set state on or off
        :return: None
        """
        if state == 'on':
            self.btn_record.config(state=tk.NORMAL)
            self.btn_speach.config(state=tk.NORMAL)
        else:
            self.btn_record.config(state=tk.DISABLED)
            self.btn_speach.config(state=tk.DISABLED)

    def __speach_to_text(self) -> None:
        """
        record speach, try to identify and display
        :return: None
        """
        text = None

        self.__switch_bt_state('off')

        with sr.Microphone(device_index=1) as source:
            print(f"[Info] start record for {self.__MAX_SPEACH_TIME} seconds")
            audio = self.record.listen(source, phrase_time_limit=self.__MAX_SPEACH_TIME)
        try:
            text = self.record.recognize_google(audio, language='en-US')
            # text = self.record.recognize_sphinx(audio, language='en-US')
        except sr.UnknownValueError:
            print("[Error] could not understand audio")
        except sr.RequestError as err:
            print(f"[Error] {err}")

        if isinstance(text, str):
            print(f"[Info] following text was identified: {text}")
        else:
            text = 'Sorry I could not understand you!'

        self.txt_s2t.delete(1.0, "end")
        self.txt_s2t.insert(1.0, text)

        self.__switch_bt_state('on')

    def __text_to_speach(self) -> None:
        """
        convert text to speach
        :return: None
        """
        self.__switch_bt_state('off')

        text = self.txt_t2s.get(1.0, "end-1c")

        self.engine.say(text)
        self.engine.runAndWait()

        self.__switch_bt_state('on')

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
    HyperText()
