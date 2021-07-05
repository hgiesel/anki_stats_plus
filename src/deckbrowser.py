from typing import Any

from anki.hooks import wrap

from aqt.gui_hooks import deck_browser_will_render_content, profile_will_close, main_window_did_init, deck_browser_did_render
from aqt.deckbrowser import DeckBrowser

from .utils import make_graph_js, get_active_deckbrowser_graphs, add_browser_search_link


def add_graphs_to_deckbrowser(self, content):
    graph_js = make_graph_js(get_active_deckbrowser_graphs())

    content.stats += f"""
<div id="graphsSection"></div>
<script>{graph_js}</script>
"""


def add_deckbrowser_hook():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)


def remove_deckbrowser_hook():
    deck_browser_will_render_content.remove(add_graphs_to_deckbrowser)

def handle_initial_render(self):
    add_deckbrowser_hook()
    deck_browser_did_render.remove(handle_initial_render)
    self.refresh()

def init_deckbrowser():
    deck_browser_did_render.append(handle_initial_render)
    profile_will_close.append(remove_deckbrowser_hook)
    DeckBrowser._linkHandler = wrap(DeckBrowser._linkHandler, add_browser_search_link, "before")
