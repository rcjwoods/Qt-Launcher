#!/APSshare/anaconda/x86_64/bin/python2.7

#____________________________________________________________________
#  qtDetector_CODE.py
#  
#  This is a conversion of the DP Launcher from WX to Qt4
#
#  Authors:	Russ Woods, Matt Moore
#     Date:	Feb 22 2017	
#____________________________________________________________________

import sys
import os
from PyQt4 import QtCore, QtGui
from qtDetector_DESIGN import Ui_MainWindow
#from dialog import Ui_Dialog
import subprocess
import signal
import threading

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

        # Dictionary for software information and status
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
            'SAVE':{
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

        # Connect the 'IOC' buttons to methods
        self.ui.buttonIOCstart.clicked.connect(lambda event: self.start_Event(event, 'IOC'))
        self.ui.buttonIOCstop.clicked.connect(lambda event: self.stop_Event(event, 'IOC'))

        # Connect the 'MEDM' buttons to methods
        self.ui.buttonMEDMstart.clicked.connect(lambda event: self.start_Event(event, 'MEDM'))
        self.ui.buttonMEDMstop.clicked.connect(lambda event: self.stop_Event(event, 'MEDM'))

        # Connect the 'ImageJ' buttons to methods
        self.ui.buttonIMAGEJstart.clicked.connect(lambda event: self.start_Event(event, 'IMAGEJ'))
        self.ui.buttonIMAGEJstop.clicked.connect(lambda event: self.stop_Event(event, 'IMAGEJ'))

        # Connect the 'Autosave' buttons to methods
        self.ui.buttonSAVEstart.clicked.connect(lambda event: self.start_Event(event, 'SAVE'))
        self.ui.buttonSAVEstop.clicked.connect(lambda event: self.stop_Event(event, 'SAVE'))

    def start_Event(self, event, app):
        '''Start an App'''
        if not(self.processes[app]['running']):
            print 'Starting ' + str(app) + '...'

            # Start the subprocess
            tempCommand = self.processes[app]['file']			
            if app=='MEDM' or app=='IMAGEJ':
                subprocess.Popen([tempCommand, pv_Prefix], preexec_fn=os.setsid)
            else:
                subprocess.Popen(tempCommand, preexec_fn=os.setsid)

            # Get the subprocess ID
            self.processes[app]['pid'] = DPOStools.waitforprocess(self.processes[app]['search'])
            self.processes[app]['running']=True
 
            # Set the button state
            self.button_status(app, 'on')
            print 'process id ' + str(app) + ' = ' + str(self.processes[app]['pid'])
			
        else:
            print str(app)+' already running!'


    def stop_Event(self, event, app):
        '''Stop an App'''
        if(self.processes[app]['running']):
            print 'Stopping '+str(app)+'...'
            os.kill(self.processes[app]['pid'], signal.SIGKILL)
            self.button_status(app, 'off')
        else:
            print "No process to stop."


    def button_status(self, app, switch):
        '''Change a button status'''
        if switch == 'on':
            if app == 'IOC':
                self.ui.buttonIOCstart.setStyleSheet('background-color: green')
                self.ui.buttonIOCstart.setText('Running...')
            elif app == 'MEDM':
                self.ui.buttonMEDMstart.setStyleSheet('background-color: green')
                self.ui.buttonMEDMstart.setText('Running...')
            elif app == 'IMAGEJ':
                self.ui.buttonIMAGEJstart.setStyleSheet('background-color: green')
                self.ui.buttonIMAGEJstart.setText('Running...')
            elif app == 'SAVE':
                self.ui.buttonSAVEstart.setStyleSheet('background-color: green')
                self.ui.buttonSAVEstart.setText('Running...')

        elif switch == 'off':
            if app in self.processes:
                print 'switching the button OFF...'
                self.processes[app]['pid'] = -999
                self.processes[app]['running'] = False
            if app == 'IOC':
                self.ui.buttonIOCstart.setStyleSheet('background-color: white')
                self.ui.buttonIOCstart.setText('Start')
            elif app == 'MEDM':
                self.ui.buttonMEDMstart.setStyleSheet('background-color: white')
                self.ui.buttonMEDMstart.setText('Start')
            elif app == 'IMAGEJ':
                self.ui.buttonIMAGEJstart.setStyleSheet('background-color: white')
                self.ui.buttonIMAGEJstart.setText('Start')
            elif app == 'SAVE':
                self.ui.buttonSAVEstart.setStyleSheet('background-color: white')
                self.ui.buttonSAVEstart.setText('Start')


		


#____________________________________________________________________
# Run the GUI program 
#if __name__ == '__main__':
#    app = QtGui.QApplication(sys.argv)

#    window = MainDialog()
#    window.show()

#    sys.exit(app.exec_())
