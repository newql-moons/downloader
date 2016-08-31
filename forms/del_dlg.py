from PyQt5.QtWidgets import QDialog
from ui import ui_del_dlg


class DelDlg(QDialog):
    def __init__(self, label_1, label_2, parent=None):
        super().__init__(parent)
        self.ui = ui_del_dlg.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('提示')

        self.ui.label.setText('<h3>%s<h3/>' % label_1)
        self.ui.checkBox.setText(label_2)

    def is_checked(self):
        return self.ui.checkBox.isChecked()
