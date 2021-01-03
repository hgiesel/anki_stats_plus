from typing import Optional

from aqt import mw, dialogs
from aqt.addons import AddonsDialog

from ..gui.settings import Settings

from .utils import graphs_deckbrowser, graphs_overview
from .graphs import update_graphs


def set_settings(
    new_graphs_deckbrowser,
    new_graphs_overview,
):
    graphs_deckbrowser.value = new_graphs_deckbrowser
    graphs_overview.value = new_graphs_overview


def show_settings():
    addons = dialogs._dialogs['AddonsDialog'][1]
    dialog = Settings(addons, set_settings)

    graphs_deckbrowser.remove()
    graphs_overview.remove()

    dialog.setupUi(
        update_graphs(graphs_deckbrowser.value),
        update_graphs(graphs_overview.value),
    )
    return dialog.open()


def init_addon_manager():
    mw.addonManager.setConfigAction(__name__, show_settings)
