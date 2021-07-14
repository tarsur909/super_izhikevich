# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:46:32 2021

@author: tarsur
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    def _init_(self, stimVal):
        super().__init__(stimVal)
        self.celltype = 'Chattering'
        self.C = 50
        self.k=1.5
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25

def createCell():
    myCell = cCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=='__main__':
    createCell()