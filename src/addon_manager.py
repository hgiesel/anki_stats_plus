from typing import Optional, List, Tuple

from aqt import mw, dialogs
from aqt.addons import AddonsDialog
from aqt.gui_hooks import profile_did_open

from ..gui.settings import Settings

from .utils import graphs_deckbrowser, graphs_overview, graphs_congrats
from .graphs import update_graphs


def update_graphs_data():
    graphs_deckbrowser.value = update_graphs(graphs_deckbrowser.value)
    graphs_overview.value = update_graphs(graphs_overview.value)
    graphs_congrats.value = update_graphs(graphs_congrats.value)


def set_settings(
    new_graphs_deckbrowser: List[Tuple[str, bool]],
    new_graphs_overview: List[Tuple[str, bool]],
    new_graphs_congrats: List[Tuple[str, bool]],
):
    graphs_deckbrowser.value = new_graphs_deckbrowser
    graphs_overview.value = new_graphs_overview
    graphs_congrats.value = new_graphs_congrats


def show_settings():
    addons = dialogs._dialogs["AddonsDialog"][1]
    dialog = Settings(addons, set_settings)

    dialog.setupUi(
        graphs_deckbrowser.value,
        graphs_overview.value,
        graphs_congrats.value,
    )
    return dialog.open()


def init_addon_manager():
    profile_did_open.append(update_graphs_data)
    mw.addonManager.setConfigAction(__name__, show_settings)
