import os
global compvar
global comp_ref_list ,row, modi_once
modi_once = 0
comp_ref_list = [] 
def create_new_file(file_path):
    with open (file_path,"w") as file:
        pass

def open_file(path):
    var_name = open(path)
    return var_name

create_new_file("data/comp_stat")
compvar = open_file("data/comp_stat")
for item in compvar:
    comp_ref_list.append(item)
print(comp_ref_list)

def welcome_data():
    try:
         myfile = open("data/initial_setup")
    except:
        create_new_file("data/initial_setup")
    for item in myfile:
        print(item, end="")
    print("\n")
    print("Select an option")

def list_task():
    try:
        task = open("data/task") 
        if modi_once==0:
            for i in task:
                comp_ref_list.append("")
            j = 0
            print(comp_ref_list)
            task = open("data/task")
            for i in task:
                print(j+1 ,"-","["+str(comp_ref_list[j].strip("\n"))+"]",i, end="")
                j+=1
            print("\n")
            print("Select an option or press enter to list commands")
            task.close()
    except:
        create_new_file("data/task")

def complete_task():
    try : 
        task = open("data/task")
        if modi_once == 0:
            print("cccc")
            j = 0
            for i in task:
                j += 1
                comp_ref_list.append("")

        task = open("data/task")
        j = 1
        for i in task:
            if j == int(row):
                comp_ref_list[j-1]=str("X")

            print(j, "-", "["+comp_ref_list[j-1].strip("\n")+"]", i, end="")
            j += 1
        print(comp_ref_list)
        item=0
        os.remove("data/comp_stat")
        task = open("data/task")
        for ite in task:
                compvar = open("data/comp_stat","a")
                compvar.write(comp_ref_list[item]+"\n")
                item+=1
    except:
        open_file("data/task")

def add_task(row):

    new_task = row
    print(new_task)
    task = open("data/task","a")
    task.write((str(new_task)))
    task.write(("\n"))
    task.close()
    print("Select an option or press enter to list commands")

def remove_task(row):
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
            for item in range (int(row)-1 ,len(comp_ref_list)-1):

                comp_ref_list[int(item)]=comp_ref_list[int(item)+1]

            print(comp_ref_list)

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
        return ss,row

def undo(row):
            comp_ref_list[int(int(row)-1)]=""
            item = 0
            os.remove("data/comp_stat")
            task = open("data/task")
            for ite in task:
                compvar = open("data/comp_stat", "a")
                compvar.write(comp_ref_list[item] + "\n")
                item += 1

print("please enter to start:")
while True:
        ss,row =Todo_application(str(input()))
        if ss=="":
            welcome_data()
        if ss == ("-c"):
            complete_task() 
        if ss == ("-u"):
            undo(row)
        if ss==("-l"):
            list_task()
        if ss==("-a"):
            add_task(row)
        if ss == ("-r"):
            remove_task(row)


    





