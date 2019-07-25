#!/bin/bash

rm -rf qtGSD_DESIGN.py
rm -rf dialog.py

/APSshare/anaconda/x86_64/bin/pyuic4 qtGSD_DESIGN.ui > qtGSD_DESIGN.py
/APSshare/anaconda/x86_64/bin/pyuic4 dialog.ui > dialog.py
