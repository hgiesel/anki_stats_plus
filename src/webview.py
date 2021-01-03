from aqt.gui_hooks import webview_will_set_content
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from aqt.utils import showText


def add_js_libraries(web_content, context):
    if isinstance(context, (DeckBrowser, Overview)):
        web_content.js.extend(
            [
                "js/vendor/protobuf.min.js",
                "pages/graphs.js",
            ]
        )

        web_content.css.append(
            "pages/graphs.css",
        )


def init_webview():
    webview_will_set_content.append(add_js_libraries)
