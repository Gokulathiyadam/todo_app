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
            task_path = "data/"+entry_file.get()+"_task"
            save_task = open (task_path)
    except :
        tkinter.messagebox.showwarning(title="warning!",message="Select a file to load")
    listbox_tasks.delete(0,tkinter.END)
    for task in save_task:
        listbox_tasks.insert(tkinter.END,task)  
    com_path = "data/"+entry_file.get()+"_cmp_task"
    save_task_com = open (com_path)
    listbox_complete.delete(0,tkinter.END)
    for task_com in save_task_com:
        listbox_complete.insert(tkinter.END,task_com)  
#the function will save the tasks to selected path
def save_task():
    try :
        task_path = "data/"+entry_file.get()+"_task"
        os.remove(task_path)
    except :
        tkinter.messagebox.showwarning(title="warning!",message="select one file or create new")
        return
    with open (task_path,"w") as file:
        pass
    task = listbox_tasks.get(0,listbox_tasks.size())
    save_task = open (task_path,"a")
    for tasks_in_task in task:
        tasks_in_task=tasks_in_task.strip("\n")
        save_task.write(tasks_in_task)

        save_task.write("\n")

    try :
        com_path = "data/"+entry_file.get()+"_cmp_task"
        os.remove(com_path)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="select one file or create new")
        return
    with open (com_path,"w") as file:
        pass
    task_cmp = listbox_complete.get(0,listbox_complete.size())
    save_task_comp = open (com_path,"a")
    for tasks_in_task_cmp in task_cmp:
        tasks_in_task_cmp=tasks_in_task_cmp.strip("\n")
        save_task_comp.write(tasks_in_task_cmp)
        first_save = open("data/save_data")
        save_task_comp.write("\n")
        first_save = open ("data/save_data","a")

# this function will move task to completed path file

def complete_task ():

    try : 
        task_index=listbox_tasks.curselection()[0]
        cmp=listbox_tasks.get(task_index)
        listbox_tasks.delete(task_index)
        listbox_complete.insert(tkinter.END,cmp)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="Select a task")

# this function will create path file  
#initially will check for fie if its not there will create file with provided name

def create():
    file_name = entry_file.get()
    if file_name != "":

        path = "data/"+file_name+"_cmp_task"
        path_2 = "data/"+file_name+"_task"
    
    
    if file_name != "":
        listbox_complete.delete(0,END) 
        listbox_tasks.delete(0,END) 
        with open (path,"w") as file:
            pass
        with open (path_2,"w") as file:
         pass
    else:
        tkinter.messagebox.showwarning(title="warning!",message="Enter a file name")

# this function will delete data

def delete():
    listbox_complete.delete(0,END) 
    listbox_tasks.delete(0,END) 
    file_name = entry_file.get()
    entry_file.delete(0,tkinter.END)
    path = "data/"+file_name+"_cmp_task"
    path_2 = "data/"+file_name+"_task"
    if file_name != "":
        os.remove(path)
        os.remove(path_2)
    else :
        tkinter.messagebox.showwarning(title="warning!",message="Select a file")




# this section contains command for GUI 
           
frame_heading = tkinter.Frame(root,bg="yellow")
frame_heading.pack()
label_head = tkinter.Label(frame_heading,text="                        PRESENT TASKS",background="yellow",borderwidth=5)
label_head.pack(side=tkinter.LEFT)
label_head2 = tkinter.Label(frame_heading,text="                       COMPLETED TASKS",background="yellow",borderwidth=5)
label_head2.pack(side=tkinter.RIGHT)
frame_tasks = tkinter.Frame(root,bg="black")
frame_tasks.pack()
frame_button = tkinter.Frame(root)
frame_button.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10,width=30,background="light pink")
listbox_tasks.pack(side=tkinter.LEFT)
listbox_complete = tkinter.Listbox(frame_tasks, height=10,width=20,background="light green")
listbox_complete.pack(side=tkinter.RIGHT)
Scrollbar_task = tkinter.Scrollbar(frame_tasks)
Scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=Scrollbar_task.set)
Scrollbar_task.config(command=listbox_tasks.yview)
frame_entry = tkinter.Frame(root)
frame_entry.pack()
entry_task = tkinter.Entry(frame_entry,width=37,background="light blue")
entry_task.pack(side=tkinter.RIGHT)
label_entry = tkinter.Label(frame_entry,text="ENTER TASK")
label_entry.pack(side=tkinter.LEFT)
frame_button = tkinter.Frame(root)
frame_button.pack()
button_add_task = tkinter.Button(frame_button,text="Add task",width=30 ,command=add_task)
button_add_task.pack(side=tkinter.LEFT)
button_complete_task = tkinter.Button(frame_button,text="complele task",width=10 ,command=complete_task)
button_complete_task.pack(side=tkinter.RIGHT)
button_remove_task = tkinter.Button(root,text="Remove task",width=44 ,command=remove_task)
button_remove_task.pack()
button_load_task = tkinter.Button(root,text="load task",width=44 ,command=load_task)
button_load_task.pack()
button_save_task = tkinter.Button(root,text="save task",width=44 ,command=save_task)
button_save_task.pack()

#for file

frame_file = tkinter.Frame(root)
frame_file.pack()
label_file = tkinter.Label(frame_file,text="Enter task name")
label_file.pack(side=tkinter.LEFT)

entry_file = tkinter.Entry(frame_file,width=22,bg="light blue")
entry_file.pack(side=tkinter.LEFT)
button_delete_file = tkinter.Button(frame_file,text="delete",width=5 ,command=delete)
button_delete_file.pack(side=tkinter.RIGHT)
button_create_file = tkinter.Button(frame_file,text="create",width=5 ,command=create)
button_create_file.pack(side=tkinter.RIGHT)

list_files = ""
list_files=list_files+(entry_file.get())
n = StringVar()
combobox_file =ttk.Combobox(root, width = 27,textvariable=n)
combobox_file.pack()
combobox_file['values']=combobox_file['values']+list_files

combobox_file.current()
root.mainloop()







