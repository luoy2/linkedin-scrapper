'''
this file is a Qt5 render engine basically copied from a stack over flow answer @Veehmot:
https://stackoverflow.com/questions/37754138/how-to-render-html-with-pyqt5s-qwebengineview

I find out the Qt5 is really neat to wrap up since it does not appear any real window. 
Another way to render a full web page is using module selenium. However, you need to download a chromedriver.exe for that.
'''


import bs4 as bs
url = 'https://www.fxstreet.com/economic-calendar'
def render(source_html):
    """Fully render HTML, JavaScript and all."""

    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, html):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            self.app.exec_()

        def _loadFinished(self, result):
            # This is an async call, you need to wait for this
            # to be called before closing the app
            self.page().toHtml(self.callable)

        def callable(self, data):
            self.html = data
            # Data has been stored, it's safe to quit the app
            self.app.quit()

    return Render(source_html).html
  
if __name__ == "__main__":
  import requests
  sample_html = requests.get(url).text
  print(render(sample_html))
  
