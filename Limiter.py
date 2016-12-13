import xml.dom.minidom
import sys

def save_settings(i):
    doc = xml.dom.minidom.Document()
    settings = doc.createElement("Settings")
    settings.setAttribute("Limit_Reset",    str(i[0]))
    settings.setAttribute("Limit_Send",     str(i[1]))
    settings.setAttribute("Limit_Counter",  str(i[2]))
    settings.setAttribute("Counter_Reset",  str(i[3]))
    settings.setAttribute("Counter_Send",   str(i[4]))
    settings.setAttribute("Send_Allow",     str(i[5]))
    doc.appendChild(settings)
    doc.writexml( open('data.xml', 'w'),
                   indent="  ",
                   addindent="  ",
                   newl='\n')
    return doc

def load_settings():
    s=[0,0,0,0,0,0]
    doc = xml.dom.minidom.parse("D:\Python27\data.xml")
    name = doc.getElementsByTagName("Settings")
    s[0] = int(name[0].getAttribute("Limit_Reset"))
    s[1] = int(name[0].getAttribute("Limit_Send"))
    s[2] = int(name[0].getAttribute("Limit_Counter"))
    s[3] = int(name[0].getAttribute("Counter_Reset"))
    s[4] = int(name[0].getAttribute("Counter_Send"))
    s[5] = int(name[0].getAttribute("Send_Allow"))
    return s

def print_settings(s):
    print("Limit_Reset : "   + str(settings[0]))
    print("Limit_Send : "    + str(settings[1]))
    print("Limit_Counter : " + str(settings[2]))
    print("Counter_Reset : " + str(settings[3]))
    print("Counter_Send : "  + str(settings[4]))
    print("Send_Allow : "    + str(settings[5]))
    return

settings=[0,0,0,0,0,0]
settings=load_settings()
print_settings(settings)

Limit_Reset = settings[0]
Limit_Send = settings[1]
Limit_Counter = settings[2]
Counter_Reset = settings[3]
Counter_Send = settings[4]
Send_Allow = settings[5]


# Read 
i=0
print ("Eingabe eines neuen Wertes ")
i=int(input (">"))
print (i)
if i < Limit_Send:
    Counter_Reset=0
    Counter_Send=Counter_Send+1
    if Counter_Send > Limit_Counter:
        if Send_Allow == 1:
            print ("Send_Alarm")
            Send_Allow = 0
if i > Limit_Reset:
    Counter_Send = 0
    Counter_Reset=Counter_Reset+1
    if Counter_Reset > Limit_Counter:
        print ("Send_Okay")
        Send_Allow = 1
if i > Limit_Send:
    if i < Limit_Reset:
        Counter_Reset=0
        Counter_Send =0
        
settings[3] = Counter_Reset
settings[4] = Counter_Send
settings[5] = Send_Allow
save_settings(settings)
