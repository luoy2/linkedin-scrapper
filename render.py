'''
this file is a Qt5 render engine basically copied from a stack over flow answer @Veehmot:
https://stackoverflow.com/questions/37754138/how-to-render-html-with-pyqt5s-qwebengineview

I find out the Qt5 is really neat to wrap up since it does not appear any real window. 
Another way to render a full web page is using module selenium. However, you need to download a chromedriver.exe for that.
'''


def qt_render(source_html):
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
  

    
'''
for windows 10, download chromedriver from this webpage:
https://sites.google.com/a/chromium.org/chromedriver/downloads
and put it under C:/Windows/
'''
def selenium_render(source_html):
    from selenium import webdriver
    import time

    driver = webdriver.Chrome('C:/Windows/chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get(source_html);
    time.sleep(10) # Let the user actually see something!
    htmlSource = driver.page_source
    driver.quit()
    return htmlSource
    

    
if __name__ == "__main__":
  import requests
  url = 'http://msfe.illinois.edu/current-students/index.aspx'
  sample_html = requests.get(url).text
  print(render(sample_html))
  
