import os
import tkinter as tk
print("please enter to start:")
while True:
    def Todo_application(ss=""):
        if ss=="":
            myfile = open("data/initial_setup")
            for item in myfile:
                print(item, end="")
            print("\n")
            print("Select an option")
            myfile.close()
        if ss==("-l"):
            task = open("data/task")
            j=1
            for i in task:
                print(j ,"-",i, end="")
                j+=1
            print("\n")
            print("Select an option or press enter to list commands")
            task.close()
        if ss==("-a"):
            print("please enter the task :")
            new_task = str(input())
            task = open("data/task","a")
            task.write(("\n"))
            task.write((new_task))
            task.close()
            print("Select an option or press enter to list commands")
        if ss == ("-r"):
            with open("data/delete", "w") as file:
                pass
            task = open("data/task")
            j = 1
            for i in task:
                print(j, "-", i, end="")
                j += 1
            print("\n please enter the number of task to delete :")
            del_task = int(input())
            k = 1
            task = open("data/task")
            for i in task:
                task = open("data/task","a")
                dele_task = open("data/delete", "a")
                if k==del_task:
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



