#!/usr/bin/python3
from Tkinter import *
import subprocess
import os
import sched, time


master = Tk(className="earbleed")
master.wm_title("EarBleed")
master.geometry("200x75+100+50")

def set_vol(val):
    subprocess.call('pacmd list-sinks | grep "index" > /home/thollar/earbleed/currentSink.txt', shell=True)
    subprocess.call("sed 's/[ * index: ]//g' /home/thollar/earbleed/currentSink.txt > /home/thollar/earbleed/currentSink2.txt", shell=True)
    z=open("/home/thollar/earbleed/currentSink2.txt", "r")
    sink = z.read()
    sink = sink.strip()
    print (sink)
    subprocess.call("pactl -- set-sink-volume "+sink+" "+val+"%", shell=True)
    subprocess.call("echo '" +val+ "' > /home/thollar/earbleed/eb_log.txt", shell=True)
    
w = Scale(master, length=175, from_=0, to=300, orient=HORIZONTAL, command=set_vol)
w.pack()

def last_vol():
    f=open("/home/thollar/earbleed/eb_log.txt", "r")
    lastVol = f.read()
    w.set(lastVol)

if os.path.exists ('/home/thollar/earbleed'):
    last_vol()
else:
    subprocess.call("mkdir /home/thollar/earbleed", shell=True)
    subprocess.call("echo '0' > /home/tholar/earbleed/eb_log.txt", shell=True)
    last_vol()
    
mainloop()
