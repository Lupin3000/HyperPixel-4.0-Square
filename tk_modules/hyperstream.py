import cv2
import tkinter as tk
from PIL import Image
from PIL import ImageTk


class HyperStream:
    """
    tkinter window to display a rtsp video stream on hyperpixel 4.0 square
    """

    _LABEL_VIDEO = None

    def __init__(self, source: str) -> None:
        """
        create tkinter window and start loop
        :param source: string of rtsp url example: rtsp://...
        """
        if source:
            print(f"[INFO]: source: {source}")
            self.cap = cv2.VideoCapture(source)

            if self.cap.isOpened():
                width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                print(f"[INFO]: video width: {width}, video height: {height}")

                self.window = tk.Tk()
                self._config_window()
                self._add_widgets()

                self.window.after(100, self.__update_image)
                self.window.mainloop()

            else:
                print(f"[ERROR]: Could not open stream {source}")
        else:
            print("[ERROR]: No source given")

    def _config_window(self) -> None:
        """
        configure tkinter window, bind events and set fullscreen mode
        :return: None
        """
        self.window.title('HyperStream')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry("720x720+0+0")
        self.window.config(bg="black")
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.window.bind('<Escape>', self._exit)

        self.window.attributes("-fullscreen", True)

    def _add_widgets(self) -> None:
        """
        add specific tkinter widgets to window
        :return: None
        """
        self._LABEL_VIDEO = tk.Label(self.window)
        self._LABEL_VIDEO.pack()

    def __update_image(self) -> None:
        """
        get frames from stream, convert and show via tkinter label
        :return: None
        """
        dim = (720, 720)

        ret, frame = self.cap.read()
        if not ret:
            self.exit()
        else:
            img_res = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
            img_rgb = cv2.cvtColor(img_res, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_fin = ImageTk.PhotoImage(img_pil)

            self._LABEL_VIDEO.configure(image=img_fin)
            self._LABEL_VIDEO.image = img_fin

        self.window.after(5, self.__update_image)

    def _on_closing(self) -> None:
        """
        catch mouse close window event
        :return: None
        """
        self._exit('close window by mouse')

    def _exit(self, event) -> None:
        """
        release stream and close window
        :return: None
        """
        print(f"[INFO]: {event}")
        self.cap.release()
        self.window.destroy()


if __name__ == '__main__':
    HyperStream(source='rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4')
