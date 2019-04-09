#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 09, 2019 03:23:59 PM

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import tkFileDialog
import FinalInterfacce_support
import main
import sys

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    FinalInterfacce_support.set_Tk_var()
    top = Emotion_Detection (root)
    FinalInterfacce_support.init(root, top)
    root.mainloop()

w = None
def create_Emotion_Detection(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    FinalInterfacce_support.set_Tk_var()
    top = Emotion_Detection (w)
    FinalInterfacce_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Emotion_Detection():
    global w
    w.destroy()
    w = None


class Emotion_Detection:

    def get_file_1(self):
        self.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.trainingtextbox.delete(1.0, 'end')
        self.trainingtextbox.insert('end', self.filename)

    def get_file_2(self):
        self.filename2 = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.trainingvaluesbox.delete(1.0, 'end')
        self.trainingvaluesbox.insert('end', self.filename2)

    def start_training(self):
        rs = self.resetYN.get()
        tweettextfile = self.trainingtextbox.get(1.0, 'end')
        tweetvaluefile = self.trainingvaluesbox.get(1.0, 'end')
        main.do_train(tweettextfile.strip(), tweetvaluefile.strip(), rs)

    def get_file_3(self):
        self.filename3 = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.testingtextbox.delete(1.0, 'end')
        self.testingtextbox.insert('end', self.filename3)

    def get_file_4(self):
        self.filename4 = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.testingvaluesbox.delete(1.0, 'end')
        self.testingvaluesbox.insert('end', self.filename4)

    def start_testing(self):
        tweettextfile = self.testingtextbox.get(1.0, 'end')
        tweetvaluefile = self.testingvaluesbox.get(1.0, 'end')
        main.do_test(tweettextfile.strip(), tweetvaluefile.strip())

    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Levenim MT} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Levenim MT} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Levenim MT} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("745x578+242+64")
        top.title("Emotion Detection")
        top.configure(background="#d9d9d9")

        self.resetYN = tk.BooleanVar()

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.02, relheight=0.29, relwidth=0.96)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=715)

        self.traintextbutton = tk.Button(self.Frame1)
        self.traintextbutton.place(relx=0.14, rely=0.3, height=26, width=93)
        self.traintextbutton.configure(activebackground="#d9d9d9")
        self.traintextbutton.configure(activeforeground="#000000")
        self.traintextbutton.configure(background="#d9d9d9")
        self.traintextbutton.configure(disabledforeground="#a3a3a3")
        self.traintextbutton.configure(font=font9)
        self.traintextbutton.configure(foreground="#000000")
        self.traintextbutton.configure(highlightbackground="#d9d9d9")
        self.traintextbutton.configure(highlightcolor="black")
        self.traintextbutton.configure(pady="0")
        self.traintextbutton.configure(text='''Tweet Text''')
        self.traintextbutton.configure(width=93)
        self.traintextbutton.configure(command=self.get_file_1)

        self.trainvaluesbutton = tk.Button(self.Frame1)
        self.trainvaluesbutton.place(relx=0.15, rely=0.55, height=26, width=88)
        self.trainvaluesbutton.configure(activebackground="#d9d9d9")
        self.trainvaluesbutton.configure(activeforeground="#000000")
        self.trainvaluesbutton.configure(background="#d9d9d9")
        self.trainvaluesbutton.configure(disabledforeground="#a3a3a3")
        self.trainvaluesbutton.configure(font=font9)
        self.trainvaluesbutton.configure(foreground="#000000")
        self.trainvaluesbutton.configure(highlightbackground="#d9d9d9")
        self.trainvaluesbutton.configure(highlightcolor="black")
        self.trainvaluesbutton.configure(pady="0")
        self.trainvaluesbutton.configure(text='''Tweet Values''')
        self.trainvaluesbutton.configure(command=self.get_file_2)

        self.trainingtextbox = tk.Text(self.Frame1)
        self.trainingtextbox.place(relx=0.32, rely=0.3, relheight=0.15
                , relwidth=0.5)
        self.trainingtextbox.configure(background="white")
        self.trainingtextbox.configure(font="TkTextFont")
        self.trainingtextbox.configure(foreground="black")
        self.trainingtextbox.configure(highlightbackground="#d9d9d9")
        self.trainingtextbox.configure(highlightcolor="black")
        self.trainingtextbox.configure(insertbackground="black")
        self.trainingtextbox.configure(selectbackground="#c4c4c4")
        self.trainingtextbox.configure(selectforeground="black")
        self.trainingtextbox.configure(width=354)
        self.trainingtextbox.configure(wrap='word')
        

        self.trainingvaluesbox = tk.Text(self.Frame1)
        self.trainingvaluesbox.place(relx=0.32, rely=0.55, relheight=0.15
                , relwidth=0.5)
        self.trainingvaluesbox.configure(background="white")
        self.trainingvaluesbox.configure(font="TkTextFont")
        self.trainingvaluesbox.configure(foreground="black")
        self.trainingvaluesbox.configure(highlightbackground="#d9d9d9")
        self.trainingvaluesbox.configure(highlightcolor="black")
        self.trainingvaluesbox.configure(insertbackground="black")
        self.trainingvaluesbox.configure(selectbackground="#c4c4c4")
        self.trainingvaluesbox.configure(selectforeground="black")
        self.trainingvaluesbox.configure(width=354)
        self.trainingvaluesbox.configure(wrap='word')

        self.starttrainingbutton = tk.Button(self.Frame1)
        self.starttrainingbutton.place(relx=0.77, rely=0.79, height=26, width=67)

        self.starttrainingbutton.configure(activebackground="#d9d9d9")
        self.starttrainingbutton.configure(activeforeground="#000000")
        self.starttrainingbutton.configure(background="#d9d9d9")
        self.starttrainingbutton.configure(disabledforeground="#a3a3a3")
        self.starttrainingbutton.configure(font=font9)
        self.starttrainingbutton.configure(foreground="#000000")
        self.starttrainingbutton.configure(highlightbackground="#d9d9d9")
        self.starttrainingbutton.configure(highlightcolor="black")
        self.starttrainingbutton.configure(pady="0")
        self.starttrainingbutton.configure(text='''Train''')
        self.starttrainingbutton.configure(width=67)
        self.starttrainingbutton.configure(command=self.start_training)

        self.resettraincheckbox = tk.Checkbutton(self.Frame1)
        self.resettraincheckbox.place(relx=0.66, rely=0.79, relheight=0.16
                , relwidth=0.08)
        self.resettraincheckbox.configure(activebackground="#d9d9d9")
        self.resettraincheckbox.configure(activeforeground="#000000")
        self.resettraincheckbox.configure(background="#d9d9d9")
        self.resettraincheckbox.configure(disabledforeground="#a3a3a3")
        self.resettraincheckbox.configure(font=font9)
        self.resettraincheckbox.configure(foreground="#000000")
        self.resettraincheckbox.configure(highlightbackground="#d9d9d9")
        self.resettraincheckbox.configure(highlightcolor="black")
        self.resettraincheckbox.configure(justify='left')
        self.resettraincheckbox.configure(text='''Reset''')
        self.resettraincheckbox.configure(variable=self.resetYN)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.03, rely=0.12, height=28, width=67)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Training''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.03, rely=0.35, relheight=0.3, relwidth=0.96)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=715)

        self.testtextbutton = tk.Button(self.Frame2)
        self.testtextbutton.place(relx=0.15, rely=0.34, height=26, width=77)
        self.testtextbutton.configure(activebackground="#d9d9d9")
        self.testtextbutton.configure(activeforeground="#000000")
        self.testtextbutton.configure(background="#d9d9d9")
        self.testtextbutton.configure(disabledforeground="#a3a3a3")
        self.testtextbutton.configure(font=font9)
        self.testtextbutton.configure(foreground="#000000")
        self.testtextbutton.configure(highlightbackground="#d9d9d9")
        self.testtextbutton.configure(highlightcolor="black")
        self.testtextbutton.configure(pady="0")
        self.testtextbutton.configure(text='''Tweet  Text''')
        self.testtextbutton.configure(command=self.get_file_3)

        self.testvaluesbutton = tk.Button(self.Frame2)
        self.testvaluesbutton.place(relx=0.15, rely=0.57, height=26, width=88)
        self.testvaluesbutton.configure(activebackground="#d9d9d9")
        self.testvaluesbutton.configure(activeforeground="#000000")
        self.testvaluesbutton.configure(background="#d9d9d9")
        self.testvaluesbutton.configure(disabledforeground="#a3a3a3")
        self.testvaluesbutton.configure(font=font9)
        self.testvaluesbutton.configure(foreground="#000000")
        self.testvaluesbutton.configure(highlightbackground="#d9d9d9")
        self.testvaluesbutton.configure(highlightcolor="black")
        self.testvaluesbutton.configure(pady="0")
        self.testvaluesbutton.configure(text='''Tweet Values''')
        self.testvaluesbutton.configure(command=self.get_file_4)

        self.testingtextbox = tk.Text(self.Frame2)
        self.testingtextbox.place(relx=0.34, rely=0.34, relheight=0.14
                , relwidth=0.48)
        self.testingtextbox.configure(background="white")
        self.testingtextbox.configure(font="TkTextFont")
        self.testingtextbox.configure(foreground="black")
        self.testingtextbox.configure(highlightbackground="#d9d9d9")
        self.testingtextbox.configure(highlightcolor="black")
        self.testingtextbox.configure(insertbackground="black")
        self.testingtextbox.configure(selectbackground="#c4c4c4")
        self.testingtextbox.configure(selectforeground="black")
        self.testingtextbox.configure(width=344)
        self.testingtextbox.configure(wrap='word')

        self.testingvaluesbox = tk.Text(self.Frame2)
        self.testingvaluesbox.place(relx=0.34, rely=0.57, relheight=0.14
                , relwidth=0.48)
        self.testingvaluesbox.configure(background="white")
        self.testingvaluesbox.configure(font="TkTextFont")
        self.testingvaluesbox.configure(foreground="black")
        self.testingvaluesbox.configure(highlightbackground="#d9d9d9")
        self.testingvaluesbox.configure(highlightcolor="black")
        self.testingvaluesbox.configure(insertbackground="black")
        self.testingvaluesbox.configure(selectbackground="#c4c4c4")
        self.testingvaluesbox.configure(selectforeground="black")
        self.testingvaluesbox.configure(width=344)
        self.testingvaluesbox.configure(wrap='word')

        self.starttestingbutton = tk.Button(self.Frame2)
        self.starttestingbutton.place(relx=0.81, rely=0.8, height=26, width=73)
        self.starttestingbutton.configure(activebackground="#d9d9d9")
        self.starttestingbutton.configure(activeforeground="#000000")
        self.starttestingbutton.configure(background="#d9d9d9")
        self.starttestingbutton.configure(disabledforeground="#a3a3a3")
        self.starttestingbutton.configure(font=font9)
        self.starttestingbutton.configure(foreground="#000000")
        self.starttestingbutton.configure(highlightbackground="#d9d9d9")
        self.starttestingbutton.configure(highlightcolor="black")
        self.starttestingbutton.configure(pady="0")
        self.starttestingbutton.configure(text='''Test''')
        self.starttestingbutton.configure(width=73)
        self.starttestingbutton.configure(command=self.start_testing)

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.03, rely=0.06, height=28, width=61)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Testing''')

        self.evaluatetextbutton = tk.Button(top)
        self.evaluatetextbutton.place(relx=0.04, rely=0.69, height=35, width=118)

        self.evaluatetextbutton.configure(activebackground="#d9d9d9")
        self.evaluatetextbutton.configure(activeforeground="#000000")
        self.evaluatetextbutton.configure(background="#d9d9d9")
        self.evaluatetextbutton.configure(disabledforeground="#a3a3a3")
        self.evaluatetextbutton.configure(font=font11)
        self.evaluatetextbutton.configure(foreground="#000000")
        self.evaluatetextbutton.configure(highlightbackground="#d9d9d9")
        self.evaluatetextbutton.configure(highlightcolor="black")
        self.evaluatetextbutton.configure(pady="0")
        self.evaluatetextbutton.configure(text='''Evaluate Text''')
        self.evaluatetextbutton.configure(command=main.evaluate)

        self.guievaluationbutton = tk.Button(top)
        self.guievaluationbutton.place(relx=0.43, rely=0.69, height=35
                , width=129)
        self.guievaluationbutton.configure(activebackground="#d9d9d9")
        self.guievaluationbutton.configure(activeforeground="#000000")
        self.guievaluationbutton.configure(background="#d9d9d9")
        self.guievaluationbutton.configure(disabledforeground="#a3a3a3")
        self.guievaluationbutton.configure(font=font11)
        self.guievaluationbutton.configure(foreground="#000000")
        self.guievaluationbutton.configure(highlightbackground="#d9d9d9")
        self.guievaluationbutton.configure(highlightcolor="black")
        self.guievaluationbutton.configure(pady="0")
        self.guievaluationbutton.configure(text='''GUI Evaluation''')
        self.guievaluationbutton.configure(command=main.gui)

        self.informationbutton = tk.Button(top)
        self.informationbutton.place(relx=0.82, rely=0.69, height=35, width=103)
        self.informationbutton.configure(activebackground="#d9d9d9")
        self.informationbutton.configure(activeforeground="#000000")
        self.informationbutton.configure(background="#d9d9d9")
        self.informationbutton.configure(disabledforeground="#a3a3a3")
        self.informationbutton.configure(font=font11)
        self.informationbutton.configure(foreground="#000000")
        self.informationbutton.configure(highlightbackground="#d9d9d9")
        self.informationbutton.configure(highlightcolor="black")
        self.informationbutton.configure(pady="0")
        self.informationbutton.configure(text='''Information''')
        self.informationbutton.configure(command=main.printInfo)

        self.exitbutton = tk.Button(top)
        self.exitbutton.place(relx=0.43, rely=0.87, height=35, width=130)
        self.exitbutton.configure(activebackground="#d9d9d9")
        self.exitbutton.configure(activeforeground="#000000")
        self.exitbutton.configure(background="#d9d9d9")
        self.exitbutton.configure(disabledforeground="#a3a3a3")
        self.exitbutton.configure(font=font11)
        self.exitbutton.configure(foreground="#000000")
        self.exitbutton.configure(highlightbackground="#d9d9d9")
        self.exitbutton.configure(highlightcolor="black")
        self.exitbutton.configure(pady="0")
        self.exitbutton.configure(text='''Exit''')
        self.exitbutton.configure(width=130)
        self.exitbutton.configure(command=sys.exit)






if __name__ == '__main__':
    vp_start_gui()



