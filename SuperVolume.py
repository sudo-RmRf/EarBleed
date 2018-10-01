#!/usr/bin/python3
from Tkinter import *
import subprocess
import os
import sched, time


master = Tk(className="supervolume")
master.wm_title("Super Volume")
master.geometry("200x75+100+50")

def set_vol(val):
    subprocess.call('pacmd list-sinks | grep "index" > /home/thollar/SuperVolume/currentSink.txt', shell=True)
    subprocess.call("sed 's/[ * index: ]//g' /home/thollar/SuperVolume/currentSink.txt > /home/thollar/SuperVolume/currentSink2.txt", shell=True)
    z=open("/home/thollar/SuperVolume/currentSink2.txt", "r")
    sink = z.read()
    sink = sink.strip()
    print (sink)
    subprocess.call("pactl -- set-sink-volume "+sink+" "+val+"%", shell=True)
    subprocess.call("echo '" +val+ "' > /home/thollar/SuperVolume/SVlog.txt", shell=True)
    #com = sink+" "+value
    #command = "pactl -- set-sink-volume "+value+sink+""
    #print com
    
w = Scale(master, length=175, from_=0, to=300, orient=HORIZONTAL, command=set_vol)
w.pack()

def last_vol():
    f=open("/home/thollar/SuperVolume/SVlog.txt", "r")
    lastVol = f.read()
    w.set(lastVol)

if os.path.exists ('/home/thollar/SuperVolume'):
    #subprocess.call("sed 's/[ % ]//g' /home/tyler/SuperVolume/SVlog.txt", shell=True)
    last_vol()
else:
    subprocess.call("mkdir /home/thollar/SuperVolume", shell=True)
    subprocess.call("echo '0' > /home/tholar/SuperVolume/SVlog.txt", shell=True)
    #subprocess.call("sed 's/[ % ]//g' /home/tyler/SuperVolume/SVlog.txt", shell=True)
    last_vol()
    
mainloop()
