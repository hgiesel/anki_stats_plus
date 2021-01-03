from typing import List, Tuple

from aqt import QDialog

from .forms.settings_ui import Ui_Settings


class Settings(QDialog):
    def __init__(self, addons, callback):
        super().__init__(parent=addons)

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.cb = callback

    def setupUi(self, graphs_deckbrowser: List[Tuple[str, bool]], graphs_overview: List[Tuple[str, bool]]):
        self.ui.deckBrowser.setupUi(graphs_deckbrowser)
        self.ui.deckOverview.setupUi(graphs_overview)

    def accept(self):
        self.cb([], [])
        super().accept()
