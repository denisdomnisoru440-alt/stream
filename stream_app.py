import sys, os, webview

def resource_path(p):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, p)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), p)

html_path = resource_path('stream.html')
url = 'file:///' + html_path.replace('\\', '/')

window = webview.create_window(
    'StreamLang',
    url,
    width=1280,
    height=800,
    min_size=(800, 500),
    text_select=True
)
webview.start(debug=('--debug' in sys.argv))
