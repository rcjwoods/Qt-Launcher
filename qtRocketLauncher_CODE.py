#!/APSshare/anaconda/x86_64/bin/python2.7

#____________________________________________________________________
#  qtRocketLauncher_CODE.py
#  
#    Notes: 
#
#  Authors:	Russ Woods
#     Date:	Feb 21 2017	
#____________________________________________________________________

import sys
import os
from PyQt4 import QtCore, QtGui
from qtRocketLauncher_DESIGN import Ui_MainWindow
#from dialog import Ui_DialogUi_Dialog

print 'Huh???'

from subprocess import call

# Import xraydetector dependent info
sys.path.append('/local/config/')
import xrd_config

class MainDialog(QtGui.QMainWindow):
    '''This class modifies the GUI crrated by Qt-Designer'''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Detector List into comboBox
        self.ui.comboBox.addItems(xrd_config.DETECTOR_LIST)
			
        # Connect the 'Load' button to 'loadDetector()'
        self.ui.buttonLoad.clicked.connect(self.loadDetector)

        # Make a holder for detector window?
        self.DPWindows = dict()

    def loadDetector(self):
        # This Method launches the Detector Windows
        print 'Loading '+ self.ui.comboBox.currentText() +'...'

        if(self.ui.comboBox.currentText() == 'Vortex'):
            #import qtVortex
            import qtDetector_CODE
            try:
                self.DPWindows['vortex'] != None	
            except:
                self.DPWindows['vortex'] = qtVortex.VortexFrame(parent=self)
			
            self.DPWindows['vortex'].Center()
            self.DPWindows['vortex'].Show()
            self.DPWindows['vortex'].SetFocus()

        elif(self.ui.comboBox.currentText() == 'Ikon'):
            import qtIkon_CODE
            try:
                self.DPWindows['iKon'] != None
            except:
                self.DPWindows['iKon'] = qtIkon_CODE.MainDialog(parent=self)
			
            #self.DPWindows['iKon'].Center()
            self.DPWindows['iKon'].show()		

        else: print "Detector not supported yet..."

		

#____________________________________________________________________
# Run the GUI program 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = MainDialog()
    window.show()

    sys.exit(app.exec_())
