# tcp server darkhole open source made by @weasleyRonald
# import required modules
import sys
import socket
import webbrowser
import tkinter as tk
from tkinter import *

# tkinter configs
conf = tk.Tk()
title = 'DarkHole'
conf.title(title)
conf.geometry('430x225')
title = lambda tl: conf.title(tl)
conf.configure(background='black')

# client binds, socket shits
bind_port = 12
bind_ip = '1.1.1.1'
website = 'https://mywebsite.com'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# functions for the buttons
def connect():
	client.connect((bind_ip, bind_port))
	client.send(b'Received a connection!')
	response = client.recv(4096)
	print (response)

def close():
	print('Closed the session!')	
	client.close()


def unlock():
    print('Get the full version now!')	
    webbrowser.open(website)

def quit():
	print('Thank you for connecting!')
	sys.exit(1)

# display the GUI
tk.Button(text='Connect!', command = connect, width = 30, height= 2, bg="black", fg="white", font = ('arial black', 15, 'bold')).pack()
tk.Button(text='Close the session', command = close, width = 30, height= 1, bg="black", fg="white", font = ('arial black', 15, 'bold')).pack()
tk.Button(text='Unlock Full Version', command = unlock, width = 30,bg="black", fg="white", font = ('arial black', 15, 'bold')).pack()
tk.Button(text='Quit', command = quit, width = 30, height= 1, bg="black", fg="white", font = ('arial black', 15, 'bold')).pack()
conf.mainloop()