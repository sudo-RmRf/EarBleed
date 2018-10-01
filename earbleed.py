#!/usr/bin/python3
from Tkinter import *
import subprocess
import os
import sched, time

master = Tk(className="earbleed")
master.wm_title("EarBleed")
img = PhotoImage(file='./favicon.gif')
master.tk.call('wm', 'iconphoto', master._w, img)
master.geometry("200x75+100+50")

def set_vol(val):
    subprocess.call('pacmd list-sinks | grep "index" > ./currentSink.txt', shell=True)
    subprocess.call("sed 's/[ * index: ]//g' ./currentSink.txt > ./currentSink2.txt", shell=True)
    z=open("./currentSink2.txt", "r")
    sink = z.read()
    sink = sink.strip()
    print (sink)
    subprocess.call("pactl -- set-sink-volume "+sink+" "+val+"%", shell=True)
    subprocess.call("echo '" +val+ "' > ./eb_log.txt", shell=True)
    
w = Scale(master, length=175, from_=0, to=300, orient=HORIZONTAL, command=set_vol)
w.pack()

def last_vol():
    f=open("./eb_log.txt", "r")
    lastVol = f.read()
    w.set(lastVol)

if os.path.exists ("./eb_log.txt"):
    last_vol()
else:
    #subprocess.call("mkdir ${PWD}/eb_log.txt", shell=True)
    subprocess.call("echo '0' > ./eb_log.txt", shell=True)
    last_vol()
    
mainloop()
