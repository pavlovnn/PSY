# Graphics for PSY
# 9 March 2017

Version = "V6"
Title = "  Telepathy test software " + " " + Version

TABOUT='''
                       The software for mind reading experiments  \n\n
                                 Ndevices Ltd.  Cork,Ireland,2017  \n\n
                                   http:\\\www.ndevices.ie                  '''


# CONSTANTS:

import Tkinter as tk
from PIL import ImageTk
from datetime import datetime
import  time 
import tkFileDialog
import ast
import tkMessageBox
import sys
from random import randrange
import yaml
import io
from dateutil import parser

#global
gl_pic_number_choosen =-1



"""

import yaml
import io

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
with open("data.yaml", 'r') as stream:
    data_loaded = yaml.load(stream)

print(data == data_loaded)
    
"""
def timestpu(): # Time stamp over the web
        try:
            import ntplib
            x = ntplib.NTPClient()
            dtz = str (datetime.utcfromtimestamp(x.request('europe.pool.ntp.org').tx_time))
        except:
            dtz = " No Internet connection to Universal Time Service "
        print dtz
        return dtz

class psyr(): # Record of either transmtted or received session
        
         # Session object
        utime = timestpu()
        time = str(datetime.now())
        columns =3
        rows =3
        pic_number_choosen = []
        wait_sec = 3
        tr ="" # Transmit-receive switch
                
        def writef(self):# Save READING to file
                print("\n save results to file")
                file_path_string = tkFileDialog.asksaveasfilename()#pic_number_choosen
                mfile =open(file_path_string,"w+")
                print >> mfile, self.tr + " record", "\n Local time = "+ self.time + "\n Internet time = "+ self.utime, \
                        "\n columns to choose = %d " % self.columns,"\n rows = %d " % self.rows, "\n wait_sec = %d " % self.wait_sec,\
                        "\n Choises: \n", self.pic_number_choosen, "\n End"
                print " ..Saving finished "
                mfile.close()
                
        def sp(self,sp): # insert and read sp
                self.pic_number_choosen.append(sp)

'''                
        def readf (self): # Read from file -only for analysis later 
                print("\n read file") 
                file_path_string = tkFileDialog.askopenfilename(parent=tw)
                mfile =open(file_path_string,"r+")
                v = mfile.read()
                self = ast.literal_eval(v)
                print "v, self= ",v, self      
                mfile.close()
                return self
'''

class ses_as():

        utime = timestpu()
        time = str(datetime.now())
        columns =5
        rows =3
        wait_sec = 3
        pic_number_choosen = -1

        def writef(self,form):
                print("\n creating file")
                file_path_string = tkFileDialog.asksaveasfilename()
                mfile =open(file_path_string,"w+")
                yaml.dump(self, mfile,default_flow_style=False)
                print  " Session shedule ", "\n Local time = "+ str(self.time) + "\n Internet time = "+ str(self.utime), \
                        "\n columns to choose = %d " % self.columns,"\n rows = %d " % self.rows, "\n wait_sec = %d " % self.wait_sec,\
                        "\n Choises to be randomly genertaed and post-recorded at the transmission side: \n End"
                print " ..Saving finished "
                mfile.close()
                form.destroy()
        def readf(self):
                print("\n reading file")
                file_path_string = tkFileDialog.askopenfilename()
                mfile =open(file_path_string,"r+")
                v = mfile.read()
                v = yaml.load(v)
                print str(v)
                self=v
                mfile.close()
                return v

def exit_p(xk): # Exit to OS
        xk.destroy()
        sys.exit()
      
def about_menu():# About software
        tkMessageBox.showinfo(title = "About",message = TABOUT)


# Countdown timer
def countdown(tw,count,wait_sec,rows,current_row,):
    tt =  " Seconds left = %d" % count + " of %d" % wait_sec +"     Row = %d" % current_row + " of %d" % rows
    clabel = tk.Label(tw, text = tt , font = ('Helvetica', 12))
    clabel.place(x=1,y=1)
    print tt
    if count > 0:
        # call countdown again after 1000ms (1s)
        tw.after(1000, countdown, tw,count-1, wait_sec,rows,current_row)
    else:
        tw.destroy()
   

# Transmit-receiver ----------------------------------------------------

def pic_choice(psrecord,current_row,sp):
        
        trd = psrecord.tr
        columns = psrecord.columns
        wait_sec = psrecord.wait_sec
        
        def click(u):
                global gl_pic_number_choosen
                print "u",u
                gl_pic_number_choosen = u
                
        # Open tw  = actual test window
        tw = tk.Tk()

        
        # Label it
        if  trd == "Transmit":
                ta = "TRANSMIT!"
        else:
                ta = "Receiving"
                trd = "r" # Force receiving 
        tw.wm_title("PSY test in progress.. " + ta)

        p1 = tk.Label(tw, text ="")
        p2 = tk.Label(tw, text ="")
        p1.grid(row=0,column=columns) # blamk row
        p2.grid(row=1,column=columns) # blamk row

        # Choice picture buttons
        bb =[]

        for i in xrange(0,columns):
            bb.append(tk.Button(tw))
            print bb 
            k = i + 1 # Offset 1 for natural number
            pfile = "%02d.png" % k
            pk = "%d" % k
            image = ImageTk.PhotoImage(file=pfile)
            bb[i].config(image=image)
            bb[i].image = image
            bb[i].pack()
            bb[i].grid(row=3, column=i)

            nlabel = tk.Label(tw, text = pk, font = ("Purisa", 18)) 
            nlabel.grid(row=2, column=i)

            if trd == "Transmit": # Grey out for transmit
                    if k == sp :
                        bb[i].config(borderwidth=10)
                        bb[i].config(state="normal")
                        nlabel.config(font=("Purisa", 22))
                        
                    else:
                        bb[i].config(borderwidth=0)
                        bb[i].config(state="disabled")
                        nlabel.config(font=("Purisa", 10))
                        nlabel.config(state="disabled")
                        
            else: # Draw for receiving - all enabled 
                    bb[i].config(borderwidth=2)
                    bb[i].config(state="normal")
                    bb[i].config(command = lambda k=k: click(k))
                    nlabel.config(font=("Purisa", 22))
        # call countdown first time
        c = wait_sec
        countdown(tw,c,wait_sec,psrecord.rows,current_row)
        tw.mainloop()
# End of tr-re


# ---------------
def trans(): #Transmit
        global stw 
        stw.destroy()
        psrecord = psyr()

        sesi = ses_as()
        psrecord.rows = sesi.rows
        psrecord.columns = sesi.columns
        psrecord.wiat_sec = sesi.wait_sec

        psrecord.time = sesi.time
        psrecord.utime = sesi.utime

        psrecord.tr = "Transmit"

        print str(psrecord)

        for j in xrange(0,psrecord.rows):
                #Assign random number
                rn = randrange(1, psrecord.columns)
                pic_choice(psrecord,j+1,rn) 
                print "rn = %d" % rn
                psrecord.sp(rn)
        psrecord.writef()
        exit_p()
        
#---------
def resv(): #Receive
        global gl_pic_number_choosen
        global stw
        stw.destroy()
        psrecord = psyr()

        sesi = ses_as()
        sesi = sesi.readf()
        psrecord.rows = sesi.rows
        psrecord.columns = sesi.columns
        psrecord.wiat_sec = sesi.wait_sec

        psrecord.time = sesi.time
        psrecord.utime = sesi.utime

        psrecord.tr = "Receiving"

        print str(psrecord)

        for j in xrange(0,psrecord.rows):
                
                pic_choice(psrecord,j+1,0) 
                rn = gl_pic_number_choosen
                print "rn = %d" % rn
                psrecord.sp(rn)
        psrecord.writef()


def new_as():
        rsesi = ses_as()# New session created (real values)
        sesi = ses_as()# control boxes
        se = tk.Tk()# Session assigment window
        se.wm_title("Assign PSY ession parameters and time")

        # sesi.time ONLY Utime!
        
        # sesi.utime
        tk.Label(se, text="UTC Start time ").grid(column=0,row=0)
        sesi.utime = tk.Entry(se, width=17)
        sesi.utime.grid(column=1,row=0)
        sesi.utime.insert(tk.END, str(rsesi.utime))
        rsesi.utime = parser.parse(sesi.utime.get())
        
        
        #sesi.rows
        tk.Label(se, text="Trials(rows)  ").grid(column=0,row=1)
        sesi.rows = tk.Entry(se, width=17)
        sesi.rows.grid(column=1,row=1)
        sesi.rows.insert(tk.END,str(rsesi.rows))
        rsesi.rows = int(sesi.rows.get())

        #sesi.columns
        tk.Label(se, text="Choose from (columns) ").grid(column=0,row=3)
        sesi.columns = tk.Entry(se, width=17)
        sesi.columns.grid(column=1,row=3)
        sesi.columns.insert(tk.END,str(rsesi.columns))
        rsesi.columns = int(sesi.columns.get())
        
        #sesi.wait_sec        
        tk.Label(se, text="Wait per trial (sec) ").grid(column=0,row=4)
        sesi.wait_sec = tk.Entry(se, width=17)
        sesi.wait_sec.grid(column=1,row=4)
        sesi.wait_sec.insert(tk.END,str(rsesi.wait_sec))
        rsesi.wait_sec = int(sesi.wait_sec.get())

        #sesi.writef()
        tk.Button(se, text='Save new session file', width=17, command=lambda :  rsesi.writef(se) ).grid(column=2,row=5)
        #exit dialogue
        tk.Button(se, text='Close dialogue', width=17, command=lambda :  se.destroy() ).grid(column=0,row=5)
        
def waitw():
        ww = tk.Tk()
        ww.wm_title("Awaiting PSY session...")
        tk.Button(ww,text= 'Force session now!',width=17).grid(column=1,row=3)
        tk.Label(ww,text= 'Session time ',width=17).grid(column=0,row=1)        
        tk.Label(ww,text= 'Time to session ',width=17).grid(column=0,row=2)
        


# MAIN ==============================================================================================================

# Open settings  window
stw = tk.Tk()
# Label it
stw.wm_title(Title)


tk.Button(stw, text='Create new session file', width=25, command=lambda :  new_as() ).grid(column=1,row=0)
tk.Button(stw, text='Receiving session', width=25, command=lambda : resv()).grid(column=0,row=1)
tk.Button(stw, text='Transmitting session', bg= "orange",width=25, command=lambda : trans()).grid(column=0,row=2)
tk.Button(stw, text='EXIT', fg= "blue",width=25, command=lambda: exit_p(stw) ).grid(column=1,row=4)
tk.Button(stw, text='ABOUT', fg= "brown",width=25,command=lambda: about_menu()).grid(column=1,row=3)


stw.mainloop()



    

