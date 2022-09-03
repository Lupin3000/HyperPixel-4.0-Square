import os

os.environ['KIVY_VIDEO'] = 'ffpyplayer'

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.core.window import Window
from kivy.config import Config


class VideoCarousel(App):

    def build(self):
        carousel = Carousel(direction='right', loop=True)

        for i in range(0, 3):
            src = f"videos/demo_{i}.mp4"
            video = Video(source=src, play=True, options={'eos': 'loop'})
            carousel.add_widget(video)
            Clock.schedule_interval(carousel.load_next, 4)

        return carousel


if __name__ == '__main__':
    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '720')
    Window.maximize()

    VideoCarousel().run()
