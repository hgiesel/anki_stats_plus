from aqt import QWidget

from .forms.graph_list_ui import Ui_GraphList


class GraphList(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.ui = Ui_GraphList()
        self.ui.setupUi(self)

    def setupUi(self):
        pass
