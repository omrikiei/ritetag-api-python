from .enums import *


class ImageBuilder:

    def __init__(self, quote, author=''):
        # type: (str, str) -> ImageBuilder
        # default values
        self.__data = {
            'fontSize': 60,
            'quoteFont': FontList.Lora,
            'quoteColor': '#4f4f4f',
            'authorFont': FontList.Lato_Black,
            'authorFontColor': '#e5e5e5',
            'enableHighlight': int(True),
            'highlightColor': '#f0ea66',
            'bgType': BackgroundType.gradient,
            'backgroundColor': '#000000',
            'gradientType': GradientType.linear,
            'gradientColor1': '#1ee691',
            'gradientColor2': '#1ddad6',
            'brandLogo': 'https://cdn.ritekit.com/assets/img/common/made-with-ritekit-white.png',
            'animation': AnimationType.glint,
            'showQuoteMark': int(True)
        }
        self.quote(quote).author(author)

    def quote(self, text):
        # type: (str) -> ImageBuilder
        self.__data['quote'] = text
        return self

    def author(self, text):
        # type: (str) -> ImageBuilder
        self.__data['author'] = text
        return self

    def font_size(self, number):
        # type: (int) -> ImageBuilder
        self.__data['fontSize'] = number
        return self

    def quote_font(self, font):
        # type: (FontList) -> ImageBuilder
        self.__data['quoteFont'] = font
        return self

    def quote_font_color(self, color):
        # type: (str) -> ImageBuilder
        self.__data['quoteFontColor'] = color
        return self

    def author_font(self, font):
        # type: (FontList) -> ImageBuilder
        self.__data['authorFont'] = font
        return self

    def enable_highlight(self, on):
        # type: (bool) -> ImageBuilder
        self.__data['enableHighlight'] = int(on)
        return self

    def highlight_color(self, color):
        # type: (str) -> ImageBuilder
        self.__data['highlightColor'] = color
        return self

    def background_type(self, background_type):
        # type: (BackgroundType) -> ImageBuilder
        self.__data['bgType'] = str(background_type)
        return self

    def background_color(self, color):
        # type: (str) -> ImageBuilder
        self.__data['backgroudColor'] = color
        return self

    def gradient_type(self, gradient_type):
        # type: (GradientType) -> ImageBuilder
        self.__data['gradientType'] = gradient_type
        return self

    def gradient_color_1(self, color):
        # type: (str) -> ImageBuilder
        self.__data['gradientColor1'] = color
        return self

    def gradient_color_2(self, color):
        # type: (str) -> ImageBuilder
        self.__data['gradientColor2'] = color
        return self

    def brand_logo(self, url):
        # type: (str) -> ImageBuilder
        self.__data['brandLogo'] = url
        return self

    def animation(self, animation_type):
        # type: (AnimationType) -> ImageBuilder
        self.__data['animation'] = animation_type
        return self

    def show_quote_mark(self, on):
        # type: (bool) -> ImageBuilder
        self.__data['showQuoteMark'] = int(on)
        return self

    def build(self):
        return self.__data
