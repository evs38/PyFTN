#!/bin/env python3

from ftnconfig import *
import ftnimport
import os

db=connectdb()

SENDERNAME=SYSOP
REPLY = None
FLAGS = [] # ['AuditRequest']

#DESTDOM, DESTTXT, DESTNAME = "node", "2:5020/1042", "Michael Dukelsky"
DESTDOM,DESTTXT, DESTNAME = "echo", "RU.PYTHON", "All"
SUBJ = "test"
BODY = "а кто-нибудь конструкции for..else или while..else использует?"


with ftnimport.session(db) as sess:
    sess.send_message(SENDERNAME, (DESTDOM, DESTTXT), 
                DESTNAME, REPLY, SUBJ, 
"""Hello %s,

%s

"""%(DESTNAME.split(" ")[0], BODY), FLAGS)
