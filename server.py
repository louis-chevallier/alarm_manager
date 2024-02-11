#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://usefulangle.com/post/352/javascript-capture-image-from-camera

import os, gc, sys, glob
import os, json, base64
import shutil
import re
from utillc import *
import cherrypy
import threading
import queue
import json, pickle
import time
import time as _time
from time import gmtime, strftime
from datetime import timedelta
import PIL
from PIL import Image
import os
from urllib.parse import urlparse


fileDir = os.path.dirname(os.path.abspath(__file__))
rootDir = os.path.join(fileDir, '.')
EKOX(rootDir)

port = 8083
if "PORT" in os.environ :
    port = int(os.environ["PORT"])


config = {
  '/' : {
      'tools.staticdir.on': True,
      'tools.staticdir.dir': rootDir,
#      'tools.staticdir.dir': '/mnt/hd2/users/louis/dev/git/three.js/examples/test',

    },
  'global' : {
      'server.ssl_module' : 'builtin',
      'server.socket_host' : '0.0.0.0', #192.168.1.5', #'127.0.0.1',
      'server.socket_port' : port,
      'server.thread_pool' : 2,
      'log.screen': False,
      'log.error_file': './error.log',
      'log.access_file': './access.log'
  },
}

class Task(object):
    def __init__(self, interval=1):
        self.interval = interval
        self.thread = Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
        self.buffer = []

    def run(self):
        """ Method that runs forever """
        while True:
            sleep(self.interval)
            try :
                url = "http://192.168.1.33/temperature"
                headers = {'Accept': 'application/json'}
                #r = requests.get(url, headers=headers)
                j = r.json()
                j['d'] = time.time
                #EKOX(j)
                self.buffer.append(r.json())  if len(self.buffer) > max_length :
                    self.buffer.pop(0)
            except Exception as e :
                EKOX(e)


class App:
    """
    the Webserver
    """
    def __init__(self) :
        EKOT("app init")
        self.task = Task(3)        
        
    @cherrypy.expose
    def index(self):
        """ main 
        """
        EKOT("REQ main")
        with open('./main.html', 'r') as file:
            EKOT("main")
            data = file.read()
            data = data.replace("INFO", self.info())
            return data
        
config2 = {
    "dry" : (False, " true : will not run the reconstructor"),
    "gitinfo" : "info"
}

def go() :
    app = App(gd, train_dir)
    cherrypy.log.error_log.propagate = False
    cherrypy.log.access_log.propagate = False
    EKOT("server running")
    cherrypy.quickstart(app, '/', config)
    EKOT("end server", n=LOG)

if __name__ == "__main__":
    go()
    
