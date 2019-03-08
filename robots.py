from guizero import App, Text, PushButton, Box
import subprocess as sb
from subprocess import Popen, PIPE

edit = 'yourpi.local'
anotheredit = 'anotherpi.local'
## make a function to check pis online and another to return true or false
#per pi

def check():
    res = sb.run(['avahi-browse', '--browse-domains', '-p', '-t'], stdout=sb.PIPE)
    pos = res.stdout.decode('utf-8')
    print(pos)
    if edit in pos:
        #print("online")
        box.tk.configure(width="30", height="30", background="green")
    else:
        box.tk.configure(width="30", height="30", background="red")
    if anotheredit in pos:
        box2.tk.configure(width="30", height="30", background="green")
    else:
        box2.tk.configure(width="30", height="30", background="red")
        
    
    
app = App(title='Pis Status', width="300", height="300", layout="grid")
button = PushButton(app, align="right", text="yourpi", command=check, grid=[1,0]) 
box = Box(app, visible=True, layout="grid", align="left", grid=[0,0])
box.after(1000, check)

box2 = Box(app, visible=True, layout="grid", grid=[0,1])
button2 = PushButton(app, align="right", text="anotherpi", command=check, grid=[1,1])




app.display()
