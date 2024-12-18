from rps_login_ui import *

if __name__.__eq__("__main__"):
    application = QApplication([])
    window = RPSLoginUI()
    window.child = RPSGameUI(window)
    window.show()
    application.exec()