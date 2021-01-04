from typing import List, Tuple

from aqt import Qt, QWidget, QListWidget, QListWidgetItem

from .forms.graph_list_ui import Ui_GraphList
from ..src.graphs import get_display_name


list_item_flags = (
    Qt.ItemIsEnabled
    | Qt.ItemIsSelectable
    | Qt.ItemIsDragEnabled
    | Qt.ItemIsDropEnabled
    | Qt.ItemIsUserCheckable
    | Qt.ItemNeverHasChildren
)


class GraphListItem(QListWidgetItem):
    def __init__(self, parent: QListWidget, name: str, enabled: bool):
        super().__init__(parent)

        self._name = name
        self.setText(get_display_name(name))

        self.setFlags(self.flags() & list_item_flags)
        self.setCheckState(Qt.Checked if enabled else Qt.Unchecked)

    def name(self) -> str:
        return self._name


class GraphList(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.ui = Ui_GraphList()
        self.ui.setupUi(self)

        self.ui.list.clear()

    def setupUi(self, items: List[Tuple[str, bool]]):
        for name, enabled in items:
            self.ui.list.addItem(GraphListItem(self.ui.list, name, enabled))

    def exportData(self) -> List[Tuple[str, bool]]:
        data = []

        count = self.ui.list.count()
        index = 0

        while index < count:
            item = self.ui.list.item(index)
            data.append(
                [
                    item.name(),
                    item.checkState() == Qt.Checked,
                ]
            )

            index += 1

        return data
