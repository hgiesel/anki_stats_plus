from os.path import basename

from aqt.webview import AnkiWebView
from aqt.gui_hooks import webview_did_inject_style_into_page


def add_graphs_to_congrats(webview: AnkiWebView):
    page = basename(webview.page().url().path())

    if page != "congrats.html":
        return

    webview.eval("""
const graphsContainer = document.createElement("div")
graphsContainer.id = "graphsSection"
graphsContainer.style = "text-align: center;"
document.body.appendChild(graphsContainer)

const loadGraphs = () => {
    anki.graphs(graphsContainer, [
        anki.TodayStats,
    ], {
        search: `deck:current`,
        days: 0,
    })
}

const loadGraphScript = () => {
    const graphScript = document.createElement("script")
    graphScript.onload = loadGraphs
    graphScript.charset = "UTF-8"
    graphScript.src = "graphs.js"
    document.head.appendChild(graphScript)
}

const protobufScript = document.createElement("script")
protobufScript.onload = loadGraphScript
protobufScript.charset = "UTF-8"
protobufScript.src = "../js/vendor/protobuf.min.js"
document.head.appendChild(protobufScript)
""")


def init_congrats():
    webview_did_inject_style_into_page.append(add_graphs_to_congrats)
