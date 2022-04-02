from asyncio import tasks
from asyncore import read, write
from cProfile import label
from ctypes.wintypes import SIZE

import os
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.messagebox
from turtle import bgcolor
file_list=["x"]
root = Tk()
root.title("TODO app")
# this function will data task to path file
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message="You must enter a task")

# this function will remove task to path file
def remove_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except :
        tkinter.messagebox.showwarning(title="warning!",message="You must select a task")

# this function will load task from path file
def load_task():
    try : 
            task_path = "data/task"
            save_task = open (task_path)
    except :
        with open (task_path) as file:
            pass
    listbox_tasks.delete(0,tkinter.END)
    for task in save_task:
        listbox_tasks.insert(tkinter.END,task)  
   
    try :
        com_path = "data/cmp_task"
        save_task_com = open (com_path)
    except:
        with open (com_path) as file:
            pass
    listbox_complete.delete(0,tkinter.END)
    for task_com in save_task_com:
        listbox_complete.insert(tkinter.END,task_com)  
#the function will save the tasks to selected path
def save_task():
    try :
        task_path = "data/task"
        os.remove(task_path)
    except :
        with open (task_path,"w") as file:
            pass
    
    task = listbox_tasks.get(0,listbox_tasks.size())
    save_task = open (task_path,"a")
    for tasks_in_task in task:
        tasks_in_task=tasks_in_task.strip("\n")
        save_task.write(tasks_in_task)

        save_task.write("\n")

    try :
        com_path = "data/cmp_task"
        os.remove(com_path)
    except:
        with open (com_path,"w") as file:
            pass
    
    task_cmp = listbox_complete.get(0,listbox_complete.size())
    save_task_comp = open (com_path,"a")
    for tasks_in_task_cmp in task_cmp:
        tasks_in_task_cmp=tasks_in_task_cmp.strip("\n")
        save_task_comp.write(tasks_in_task_cmp)

        save_task_comp.write("\n")
       

# this function will move task to completed path file

def complete_task ():

    try : 
        task_index=listbox_tasks.curselection()[0]
        cmp=listbox_tasks.get(task_index)
        listbox_tasks.delete(task_index)
        listbox_complete.insert(tkinter.END,cmp)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="Select a task")



# this section contains command for GUI 
def frams(fram_name,color):
    fram_name = tkinter.Frame(root,bg=color)
    fram_name.pack()
    return fram_name
def listbox_tasks_fun(btn_name,bg_clr,wid):
    btn_name = tkinter.Listbox(frame_tasks, height=10,width=wid,background=bg_clr)
    btn_name.pack(side=tkinter.LEFT)   
    Scrollbar_task = tkinter.Scrollbar(frame_tasks)
    Scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)  
    btn_name.config(yscrollcommand=Scrollbar_task.set)
    Scrollbar_task.config(command=btn_name.yview)
    return btn_name
def make_btn(btn_frm,but_name,btn_text,wid,cmd,position):
    but_name = tkinter.Button(btn_frm,text=btn_text,width=wid ,command=cmd)
    but_name.pack(side = position)
    return but_name

def label_head(lbl_name,lbl_frm,lbl_text,clor,wid):
    lbl_name = tkinter.Label(lbl_frm,text=lbl_text,background=clor,borderwidth=wid)
    lbl_name.pack(side=LEFT)
    return lbl_name

frame_heading = frams("frame_heading","yellow")
label_head1 = label_head("label_head",frame_heading,"                       PRESENT TASKS","yellow",10)
label_head2 = label_head("label_head2",frame_heading,"                    COMPLETED TASKS","yellow",10)
frame_tasks = frams("frame_tasks","black")
frame_button = frams("frame_button","")
listbox_tasks = listbox_tasks_fun("listbox_tasks","light pink",30)
listbox_complete  = listbox_tasks_fun("listbox_complete","light green",20)
frame_entry = tkinter.Frame(root)
frame_entry.pack()
label_entry = label_head("label_entry",frame_entry,"ENTER TASK","white",5)
entry_task = tkinter.Entry(frame_entry,width=37,background="light blue")
entry_task.pack(side=tkinter.RIGHT)
button_add_task = make_btn(frame_button,"button_add_task","Add task",30,add_task,tkinter.LEFT)
button_complete_task = make_btn(frame_button,"button_complete_task","complele task",10,complete_task,tkinter.RIGHT)
button_remove_task = make_btn(root,"button_remove_task","Remove task",44,remove_task,tkinter.BOTTOM)
button_load_task = make_btn(root,"button_load_task","load task",44,load_task,tkinter.BOTTOM)
button_save_task = make_btn(root,"button_save_task","save task",44,save_task,tkinter.BOTTOM)




#for file


root.mainloop()







