#!/APSshare/anaconda/x86_64/bin/python2.7

#____________________________________________________________________
#  qtDetector_CODE.py
#  
#  This is a conversion of the DP Launcher from WX to Qt4
#
#  Authors:	Russ Woods
#     Date:	Feb 22 2017	
#____________________________________________________________________

import sys
import os
from PyQt4 import QtCore, QtGui
from qtDetector_DESIGN import Ui_MainWindow
from dialog import Ui_Dialog
from subprocess import call

# Import xraydetector dependent info
sys.path.append('/local/config/')
import DPOStools
import xrd_config

# Detector Constants
DETECTOR = 'Ikon'
pv_Prefix = xrd_config.DP_PV_SECTOR + 'ikon'+ xrd_config.DP_PV_SUFFIX


class MainDialog(QtGui.QMainWindow):
    '''This class modifies the GUI crrated by Qt-Designer'''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.processes = {	
            'IOC':{
            'pid': -999,
            'running': False,
            'search': 'st.cmd_ikon',
            'file': ['/local/DPbin/Scripts/start_ioc', 'ikon'],
            },
            'MEDM':{
            'pid': -999,
            'running': False,
            'search': 'Andor.adl',
            'file': '/local/DPbin/Scripts/start_medm_ikon',
            },
            'IMAGEJ':{
            'pid': -999,
            'running': False,
            'search': './jre/bin/java -Xmx1024m -jar ij.jar -run EPICS AD Viewer',
            'file': '/local/DPbin/Scripts/start_imageJ',
            },
            'SAVE-RESTORE MENU':{
            'pid': -999,
            'running': False,
            'search': 'medm -x -macro P='+ pv_Prefix +':,CONFIG=setup, configMenu_small.adl',
            'file': ['/local/DPbin/Scripts/start_medm_configMenu',pv_Prefix,]
            },
            'caQtDM':{
            'pid': -999,
            'running': False,
            'search': 'caQtDM -macro P='+ pv_Prefix + ':, R=cam1: Andor.ui',
            'file': ['/local/DPbin/Scripts/start_caQtDM_ikon',pv_Prefix,]
            },
        }

        # Connect the 'EPICS' buttons to methods()
        self.ui.buttonIOCstart.clicked.connect(self.iocStart)
        self.ui.buttonIOCstop.clicked.connect(self.iocStop)

        # Connect the 'MEDM' buttons to methods()
        self.ui.buttonMEDMstart.clicked.connect(self.medmStart)
        self.ui.buttonMEDMstop.clicked.connect(self.medmStop)

        # Connect the 'ImageJ' buttons to methods()
        self.ui.buttonIMAGEJstart.clicked.connect(lambda event: self.start_Event(event, 'IMAGEJ'))
        self.ui.buttonIMAGEJstop.clicked.connect(lambda event: self.stop_Event(event, 'IMAGEJ'))

        # Connect the 'Autosave' buttons to methods()
        self.ui.buttonSAVEstart.clicked.connect(self.saveStart)
        self.ui.buttonSAVEstop.clicked.connect(self.saveStop)

    def start_Event(self, event, app):
        '''Start an App'''
        if not(self.processes[app]['running']):
            print 'Starting ' + str(app) + '...'
            # Start the subprocess
            tempCommand = self.processes[app]['file']
			
            if app=='MEDM' or app=='IMAGEJ':
                print 'starting ImageJ...'
                subprocess.Popen([tempCommand, pv_Prefix], preexec_fn=os.setsid)
            else:
                subprocess.Popen(tempCommand, preexec_fn=os.setsid)

            # Grab the subprocess I.D.
            self.processes[app]['pid'] = DPOStools.waitforprocess(self.processes[app]['search'])
            self.processes[app]['running']=True
			
            # Set the button state
            self.button_status(app, 'on')
            print 'process id ' + str(app) + ' = ' + str(self.processes[app]['pid'])
			
        else:
            print str(app)+' already running!'


    def iocStart(self):
        # This Method starts the ioc
        print 'starting ioc...'

    def iocStop(self):
        # This Method stop the ioc
        print 'stopping ioc...'
		
    def medmStart(self):
        # This Method starts the MEDM
        print 'starting MEDM...'

    def medmStop(self):
        # This Method stop the MEDM
        print 'stopping MEDM...'

    def imagejStart(self):
        # This Method starts imageJ
        print 'starting imageJ...'

    def imagejStop(self):
        # This Method stops imageJ
        print 'stopping imageJ...'

    def saveStart(self):
        # This Method starts Autosave
        print 'starting autosave...'

    def saveStop(self):
        # This Method stops Autosave
        print 'stopping autosave...'

#____________________________________________________________________
# Run the GUI program 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = MainDialog()
    window.show()

    sys.exit(app.exec_())
