from .webview import init_webview
from .deckbrowser import init_deckbrowser


def init():
    init_webview()
    init_deckbrowser()
