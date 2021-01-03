from .webview import init_webview
from .deckbrowser import init_deckbrowser
from .overview import init_overview


def init():
    init_webview()
    init_deckbrowser()
    init_overview()
