from aqt.gui_hooks import webview_will_set_content

def add_js_libraries(web_content, context):
    pass

def init_webview():
    webview_will_set_content.append(add_js_libraries)
