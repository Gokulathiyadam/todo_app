import os
import sys
import tkinter as tk
print("please enter to start:")
global comp_ref_list ,row, modi_once
comp_ref_list = []
global modi_once
modi_once = 0
while True:
    def Todo_application(in_val):

        row =1
        d=in_val.split()
        if len(d)==0:
            ss=""
        if len(d) ==1:
            ss=d[0]

        if len(d) > 1:
            ss = d[0]
            row = d[1]

        if ss=="":
            myfile = open("data/initial_setup")
            for item in myfile:
                print(item, end="")
            print("\n")
            print("Select an option")

            myfile.close()
        if ss == ("-c"):
            task = open("data/task")
            if modi_once == 0:
                j = 0
                for i in task:
                    j += 1
                    comp_ref_list.append("")

            task = open("data/task")
            j = 1
            for i in task:
                if j == int(row):
                    comp_ref_list[j-1]=str("X")
                else :
                    pass
                print(j, "-", "["+str(comp_ref_list[j-1])+"]", i, end="")
                j += 1
        if ss==("-l"):
            task = open("data/task")
            if modi_once==0:
                j = 0
                for i in task:
                    j += 1
                    comp_ref_list.append("")

            j = 0
            task = open("data/task")
            for i in task:
                print(j+1 ,"-","["+str(comp_ref_list[j])+"]",i, end="")
                j+=1
            print("\n")
            print("Select an option or press enter to list commands")
            task.close()
        if ss==("-a"):
            print("please enter the task :")
            new_task = str(input())
            task = open("data/task","a")
            task.write((new_task))
            task.write(("\n"))
            task.close()
            print("Select an option or press enter to list commands")
        if ss == ("-r"):
            with open("data/delete", "w") as file:
                pass
            k=1
            task = open("data/task")

            for i in task:
                task = open("data/task","a")
                dele_task = open("data/delete", "a")
                if k==int(row):
                    print("deleted")
                    k += 1
                else :
                    dele_task.write(i)
                    k += 1

                task.close()
            dele_task = open("data/delete")
            task = open("data/task", "a")
            os.remove("data/task")
            with open("data/task", "w") as file:
                pass
            for val in dele_task:
                task = open("data/task","a")
                task.write(str(val))

            task.close()
            os.remove("data/delete")
            print("Select an option or press enter to list commands")




    Todo_application(str(input()))



