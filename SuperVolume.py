#!/usr/bin/python
from Tkinter import *
import subprocess
import os

master = Tk()
master.title("Super Volume")
master.geometry("200x75+100+50")

subprocess.call('pacmd list-sinks | grep "index" > /home/tyler/SuperVolume/currentSink.txt', shell=True)
subprocess.call("sed 's/[ * index: ]//g' /home/tyler/SuperVolume/currentSink2.txt", shell=True)
z=open("/home/tyler/SuperVolume/currentSink2.txt", "r")
sink = z.read()

def set_vol(val):
    #subprocess.call("pactl -- set-sink-volume "+sink+" "+value, shell=True)
    value = val+"%"
    command = "pactl -- set-sink-volume "+sink+" "+value
    subprocess.call(command)
    subprocess.call("echo '" +val+ "' > /home/tyler/SuperVolume/SVlog.txt", shell=True)

w = Scale(master, length=175, from_=0, to=300, orient=HORIZONTAL, command=set_vol)
w.pack()

def last_vol():
    f=open("/home/tyler/SuperVolume/SVlog.txt", "r")
    lastVol = f.read()
    w.set(lastVol)

if os.path.exists ('/home/tyler/SuperVolume'):
    subprocess.call("sed 's/[ % ]//g' /home/tyler/SuperVolume/SVlog.txt", shell=True)
    last_vol()
else:
    subprocess.call("mkdir /home/tyler/SuperVolume", shell=True)
    subprocess.call("echo '0' > /home/tyler/SuperVolume/SVlog.txt", shell=True)
    subprocess.call("sed 's/[ % ]//g' /home/tyler/SuperVolume/SVlog.txt", shell=True)
    last_vol()
    
mainloop()
