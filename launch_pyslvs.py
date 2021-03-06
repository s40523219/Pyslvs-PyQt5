# -*- coding: utf-8 -*-

"""Launch script of Pyslvs."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from sys import exit
from core import (
    QApplication,
    MainWindow,
    ARGUMENTS,
    INFO,
    PyslvsSplash,
)


if __name__ == '__main__':
    for info in INFO:
        print(info)
    print('-' * 7)
    QApp = QApplication([])
    if ARGUMENTS.fusion:
        QApp.setStyle('fusion')
    splash = PyslvsSplash()
    splash.show()
    run = MainWindow(ARGUMENTS)
    run.show()
    splash.finish(run)
    exit(QApp.exec())
