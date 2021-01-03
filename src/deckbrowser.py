
from aqt.gui_hooks import deck_browser_will_render_content

def add_graphs_to_deckbrowser(self, content):
    pass

def init_deckbrowser():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)
