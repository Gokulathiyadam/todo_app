from asyncio import tasks
from asyncore import read, write
from cProfile import label
from ctypes.wintypes import SIZE
import os
import sys
import tkinter
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("TODO app")
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message="You must enter a task")
def remove_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except :
        tkinter.messagebox.showwarning(title="warning!",message="You must select a task")
def load_task():
    save_task = open ("data/task")
    listbox_tasks.delete(0,tkinter.END)
    for task in save_task:
        listbox_tasks.insert(tkinter.END,task)    
def save_task():
    
    os.remove("data/task")
    with open ("data/task","w") as file:
        pass
    task = listbox_tasks.get(0,listbox_tasks.size())
    save_task = open ("data/task","a")
    for tasks_in_task in task:
        tasks_in_task=tasks_in_task.strip("\n")
        save_task.write(tasks_in_task)
        first_save = open("data/save_data")
        save_task.write("\n")
        first_save = open ("data/save_data","a")

    os.remove("data/cmp_task")
    with open ("data/cmp_task","w") as file:
        pass
    task_cmp = listbox_complete.get(0,listbox_complete.size())
    save_task_comp = open ("data/cmp_task","a")
    for tasks_in_task_cmp in task_cmp:
        tasks_in_task_cmp=tasks_in_task_cmp.strip("\n")
        save_task_comp.write(tasks_in_task_cmp)
        first_save = open("data/save_data")
        save_task_comp.write("\n")
        first_save = open ("data/save_data","a")
def complete_task ():

    task_index=listbox_tasks.curselection()[0]
    cmp=listbox_tasks.get(task_index)
    listbox_tasks.delete(task_index)
    listbox_complete.insert(tkinter.END,cmp)

        
   
            

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
frame_button = tkinter.Frame(root)
frame_button.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10,width=40)
listbox_tasks.pack(side=tkinter.LEFT)
listbox_complete = tkinter.Listbox(frame_tasks, height=10,width=10)
listbox_complete.pack(side=tkinter.RIGHT)
Scrollbar_task = tkinter.Scrollbar(frame_tasks)
Scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=Scrollbar_task.set)
Scrollbar_task.config(command=listbox_tasks.yview)
frame_entry = tkinter.Frame(root)
frame_entry.pack()
entry_task = tkinter.Entry(frame_entry,width=37)
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
root.mainloop()








# print("please enter to start:")

# global compvar

# global comp_ref_list ,row, modi_once
# modi_once = 0

# comp_ref_list = []
# compvar=open("data/comp_stat")
# for item in compvar:
#     comp_ref_list.append(item)
# print(comp_ref_list)
# while True:
#     def Todo_application(in_val):

#         row =1
#         d=in_val.split()
#         if len(d)==0:
#             ss=""
#         if len(d) ==1:
#             ss=d[0]

#         if len(d) > 1:
#             ss = d[0]
#             row = d[1]

#         if ss=="":
#             myfile = open("data/initial_setup")
#             for item in myfile:
#                 print(item, end="")
#             print("\n")
#             print("Select an option")

#             myfile.close()
#         if ss == ("-c"):
#             task = open("data/task")
#             if modi_once == 0:
#                 j = 0
#                 for i in task:
#                     j += 1
#                     comp_ref_list.append("")

#             task = open("data/task")
#             j = 1
#             for i in task:
#                 if j == int(row):
#                     comp_ref_list[j-1]=str("X")

#                 print(j, "-", "["+comp_ref_list[j-1].strip("\n")+"]", i, end="")
#                 j += 1
#             print(comp_ref_list)
#             item=0
#             os.remove("data/comp_stat")
#             task = open("data/task")
#             for ite in task:
#                     compvar = open("data/comp_stat","a")
#                     compvar.write(comp_ref_list[item]+"\n")
#                     item+=1
#         if ss == ("-u"):
#             comp_ref_list[int(int(row)-1)]=""
#             item = 0
#             os.remove("data/comp_stat")
#             task = open("data/task")
#             for ite in task:
#                 compvar = open("data/comp_stat", "a")
#                 compvar.write(comp_ref_list[item] + "\n")
#                 item += 1
#         if ss==("-l"):
#             task = open("data/task")
#             if modi_once==0:
#                 j = 0
#                 for i in task:
#                     j += 1
#                     comp_ref_list.append("")

#             j = 0
#             task = open("data/task")
#             for i in task:
#                 print(j+1 ,"-","["+str(comp_ref_list[j].strip("\n"))+"]",i, end="")
#                 j+=1
#             print("\n")
#             print("Select an option or press enter to list commands")
#             task.close()
#         if ss==("-a"):
#             # print("please enter the task :")
#             new_task = row
#             print(new_task)
#             task = open("data/task","a")
#             task.write((str(new_task)))
#             task.write(("\n"))
#             task.close()
#             print("Select an option or press enter to list commands")
#         if ss == ("-r"):
#             with open("data/delete", "w") as file:
#                 pass
#             k=1
#             task = open("data/task")

#             for i in task:
#                 task = open("data/task","a")
#                 dele_task = open("data/delete", "a")
#                 if k==int(row):
#                     print("deleted")
#                     k += 1
#                 else :
#                     dele_task.write(i)
#                     k += 1
#                 task.close()
#             for item in range (int(row)-1 ,len(comp_ref_list)-1):

#                 comp_ref_list[int(item)]=comp_ref_list[int(item)+1]

#             print(comp_ref_list)

#             dele_task = open("data/delete")
#             task = open("data/task", "a")
#             os.remove("data/task")
#             with open("data/task", "w") as file:
#                 pass
#             for val in dele_task:
#                 task = open("data/task","a")
#                 task.write(str(val))

#             task.close()
#             os.remove("data/delete")
#             print("Select an option or press enter to list commands")


#     Todo_application(str(input()))





