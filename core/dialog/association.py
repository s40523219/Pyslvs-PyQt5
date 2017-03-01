# -*- coding: utf-8 -*-
from ..QtModules import *
from .Ui_association import Ui_Dialog as association_Form

class Association_show(QDialog, association_Form):
    def __init__(self, PointList, LineList, ChainList, ShaftList, SliderList, RodList, parent=None):
        super(Association_show, self).__init__(parent)
        self.setupUi(self)
        self.PointList = PointList
        self.LineList = LineList
        self.ChainList = ChainList
        self.ShaftList = ShaftList
        self.SliderList = SliderList
        self.RodList = RodList
        for i in range(1, len(PointList)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Point'+str(i)))
    
    @pyqtSlot(int, int, int, int)
    def on_tableWidget_currentCellChanged(self, pos, _cc, _pr, _pc):
        net = list()
        for i in range(len(self.LineList)):
            check = [self.LineList[i]['start'], self.LineList[i]['end']]
            if pos in check: net.append('Line{}: '.format(i)+', '.join(['Point{}'.format(k) for k in check if k!=pos]))
        self.lineLable.setText('\n'.join(net) if net!=[] else 'None')
        net.clear()
        for i in range(len(self.ChainList)):
            check = [self.ChainList[i]['p1'], self.ChainList[i]['p2'], self.ChainList[i]['p3']]
            if pos in check: net.append('Chain{}: '.format(i)+', '.join(['Point{}'.format(k) for k in check if k!=pos]))
        self.chainLable.setText('\n'.join(net) if net!=[] else 'None')
        net.clear()
        for i in range(len(self.ShaftList)):
            check = [self.ShaftList[i]['cen'], self.ShaftList[i]['ref']]
            if pos in check: net.append('Shaft{}: '.format(i)+', '.join(['Point{}'.format(k) for k in check if k!=pos]))
        self.shaftLable.setText('\n'.join(net) if net!=[] else 'None')
        net.clear()
        for i in range(len(self.SliderList)):
            check = [self.SliderList[i]['cen'], self.SliderList[i]['start'], self.SliderList[i]['end']]
            if pos in check: net.append('Slider{}: '.format(i)+', '.join(['Point{}'.format(k) for k in check if k!=pos]))
        self.sliderLable.setText('\n'.join(net) if net!=[] else 'None')
        net.clear()
        for i in range(len(self.RodList)):
            check = [self.RodList[i]['cen'], self.RodList[i]['start'], self.RodList[i]['end']]
            if pos in check: net.append('Rod{}: '.format(i)+', '.join(['Point{}'.format(k) for k in check]))
        self.rodLable.setText('\n'.join(net) if net!=[] else 'None')