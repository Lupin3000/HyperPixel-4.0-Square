from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config


class HyperCarousel(App):

    def build(self):
        carousel = Carousel(direction='right', loop=True)

        for i in range(4):
            src = f"pictures/demo_{i}.png"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
            Clock.schedule_interval(carousel.load_next, 5)

        return carousel


if __name__ == '__main__':
    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '720')
    Window.fullscreen = True
    # Config.set('graphics', 'fullscreen', 'auto')

    HyperCarousel().run()
