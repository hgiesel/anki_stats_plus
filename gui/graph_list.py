from typing import List, Tuple

from aqt import Qt, QWidget, QListWidget, QListWidgetItem

from .forms.graph_list_ui import Ui_GraphList


class GraphListItem(QListWidgetItem):
    def __init__(self, parent: QListWidget, name: str, enabled: bool):
        super().__init__(parent)

        self.setText(name)
        self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemNeverHasChildren)
        self.setCheckState(Qt.Checked if enabled else Qt.Unchecked)


class GraphList(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.ui = Ui_GraphList()
        self.ui.setupUi(self)

        self.ui.list.clear()

    def setupUi(self, items: List[Tuple[str, bool]]):
        for name, enabled in items:
            self.ui.list.addItem(GraphListItem(self.ui.list, name, enabled))
