import cv2
import tkinter as tk
from PIL import Image
from PIL import ImageTk


class HyperStream:
    """
    simple rtsp client for hyperpixel 4.0 square
    """
    def __init__(self, source):

        if source:
            self.cap = cv2.VideoCapture(source)
        else:
            print("No source given")

        if self.cap.isOpened():
            width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            print(f"video source width: {width} x height: {height}")

            self.window = tk.Tk()
            self.window.title('HyperStream')
            self.window.resizable(width=tk.FALSE, height=tk.FALSE)
            self.window.geometry("720x720+0+0")
            self.window.config(bg="black")
            self.window.bind('<Escape>', exit)
            self.window.attributes("-fullscreen", True)

            self.label = tk.Label(self.window)
            self.label.pack()

            self.window.after(100, self.update_image)
            self.window.mainloop()

        else:
            print(f"Could not open stream {source}")

    def update_image(self):
        """
        get frames from stream, convert and show into label
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

            self.label.configure(image=img_fin)
            self.label.image = img_fin

        self.window.after(5, self.update_image)

    def exit(self):
        self.cap.release()
        self.window.quit()


if __name__ == '__main__':
    RUN = HyperStream("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")
