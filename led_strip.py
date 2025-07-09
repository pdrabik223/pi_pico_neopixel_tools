try:
    from pi_pico_neopixel_tools.neopixel import Neopixel
    from pi_pico_neopixel_tools.color import Color
    
except ImportError:
    from neopixel import Neopixel
    from color import Color

class LedStrip:
    
    def __init__(self, no_leds:int, pin:int) -> None:
        self._led_strip = Neopixel(no_leds, 0, pin, "GRB")
        self._led_strip.brightness(100)
        self._led_strip.fill(Color.red().to_tuple())
        self._led_strip.show()

    def fill(self, color: Color, show: bool = True):
        self._led_strip.fill(color.to_tuple())
        if show:
            self._led_strip.show()

    def set_pixels(
        self, indexes, color: Color, brightness: int = 100, show: bool = True
    ):
        for index in indexes:
            self._led_strip.set_pixel(index, color.to_tuple(), how_bright=brightness)
        if show:
            self._led_strip.show()

    def set_pixel(
        self, index: int, color: Color, brightness: int = 100, show: bool = True
    ):
        self._led_strip.set_pixel(index, color.to_tuple(), how_bright=brightness)
        if show:
            self._led_strip.show()

    def show(self):
        self._led_strip.show()

    def brightness(self, brightness: int, show: bool = True):
        self._led_strip.brightness(brightness)
        if show:
            self._led_strip.show()

    def size(self):
        return self._led_strip.num_leds