import os
from sre_compile import isstring

def create_new_file(file_path,user):# Function for creating new file path
    if file_path != "data/delete" and file_path != "data/"+user+"_comp_stat":
        print("checking for "+file_path+".....")
        print("No record found Creating new files .....!")
    with open (file_path,"w") as file:
        pass 
def open_file(path):# Function for creating new file 
    var_name = open(path)
    return var_name
def start(cmp_path,task_path):# Function for starting up
    global compvar
    global comp_ref_list ,cmd_index, modi_once,listed
    modi_once = 0
    listed = 0
    comp_ref_list = []
    try: 
        compvar = open_file(cmp_path)
        for item in compvar:
            comp_ref_list.append(item)
    except :
        create_new_file(cmp_path,"")
        create_new_file(task_path,"")
        print ("You are all set please enter a command or press enter 👍🏻")

def welcome_data(user):# Function for welcome
    print("You are modifying '"+user+"' file\n")
    myfile = open("data/initial_setup")
    for data in myfile:
        print(data, end="")
    print("\n")
    print("Select an option")
def list_task(cmd_index,all,task_path):# Function for listing all task
    # try:
        if int(cmd_index) == 0 :
            task_file = open(task_path) 
            if modi_once==0:
                for data in task_file:
                    comp_ref_list.append(" ")
                    # print(len(comp_ref_list))
                if (len(comp_ref_list) == 0 ):
                        print("\nNo todos for today! 😀")
                        listed =1
                index = 0
                task_file = open(task_path)
                for data in task_file:
                    if all == "a":
                        print(index+1 ,"-","["+str(comp_ref_list[index].strip("\n"))+"]",data, end="")
                        index+=1
                    else :
                        if str(comp_ref_list[index].strip("\n")) != "X" :
                            print(index+1 ,"-","["+str(comp_ref_list[index].strip("\n"))+"]",data, end="")
                            index+=1
                        else :
                            index+=1
                print("\n")
                print("Select an option or press enter to list commands")
                task_file.close()
    # except:
    #     print (" \n' -l and -la command wont accept arguments !!!'\n")
    #     print("Select an option or press enter to list commands")
def complete_task(cmd_index,stat,task_path,cmp_path,user):#complete and undo complete function
    try :
        if len(cmd_index) !=0 :
            task_file = open(task_path)
            if modi_once == 0:
                index = 0
                for data in task_file:
                    index += 1
                    comp_ref_list.append(" ") 
            task_file = open(task_path)
            index = 1
            for data in task_file:
                for item in cmd_index:
                    if index == int(item):
                        comp_ref_list[index-1]=str(stat)
                print(index, "-", "["+comp_ref_list[index-1].strip("\n")+"]", data, end="")
                index += 1
            for item in cmd_index:
                if int(item) > index:
                    print ("Unable to complete:"+item+"index is out of bound")
            item=0
            os.remove(cmp_path)
            create_new_file(cmp_path,user)
            task_file = open(task_path)
            for ite in task_file:
                    compvar = open(cmp_path,"a")
                    compvar.write(comp_ref_list[item].strip("\n")+"\n")
                    item+=1
        
    except ValueError :
        print ("Unable to remove: index is not a number") 
        
    except :
        print("Unable to check: no index provided\n")
    print("Select an option or press enter to list commands")
def add_task(value,task_path):#add new task function
    new_task = value
    task = open(task_path,"a")
    try:
        if len(new_task) != 0:
            print("task is added\n")
            i=0
            task = open(task_path)
            for i in range (len(new_task)):
                task = open(task_path,"a")
                if new_task[i] != ",":
                    task.write(new_task[i])
                    task.write(" ")
                if new_task[i] == "," or len(new_task)==0:
                    task.write(("\n"))
            task.write(("\n"))
            
    except :
        print("Unable to add: no task provided\n")

    print("Select an option or press enter to list commands")
def remove_task(cmd_index,task_path):#remove new task function
    try : 
            if len(cmd_index) !=0 :
                    create_new_file("data/delete","")
                    
                    i = 0
                    task_file = open(task_path)
                    lis_index=1
                    task_file = open(task_path)
                    for data in task_file:
                        if lis_index ==int(cmd_index[i]):
                            print("task deleted")
                            lis_index += 1
                            for item in range (int(cmd_index[0])-1 ,len(comp_ref_list)-1):
                                comp_ref_list[int(item)]=comp_ref_list[int(item)+1]
                            if i!= (len(cmd_index)-1):
                                 i+=1
                        else :
                            dele_task = open("data/delete", "a")
                            dele_task.write(data)
                            lis_index += 1
                    for item in cmd_index:
                        if int(item) > lis_index-1:
                            print("\nindex ",int(item)," is unable to remove: index is out of bound\n")  
            for item in range (int(cmd_index[0])-1 ,len(comp_ref_list)-1):
                comp_ref_list[int(item)]=comp_ref_list[int(item)+1]
            os.remove(task_path)
            with open (task_path , "w") as file:
                pass
            dele_task = open("data/delete")
            for data in dele_task:
                task_file = open(task_path,"a")
                task_file.write(data)
    
            os.remove("data/delete")
    except ValueError:
        print("Unable to remove: index is not a number\n")
    except:
        print("Unable to remove: no index provided\n")
    
    print("Select an option or press enter to list commands") 
def Todo_application(in_val):#application structure
        cmd_index =[]
        split_val=in_val.split()
        if len(split_val)==0:
            cmd=""
        if len(split_val) ==1:
            cmd=split_val[0]
            cmd_index = 0

        if len(split_val) > 1:
            cmd = split_val[0]
            for ind in range(1,len(split_val)):
                cmd_index.append(split_val[ind])
        return cmd,cmd_index
def validate_cmd(entered_command,user):#validating commands
    cmnd_list =["-l","-c","-a","-x","-r","","-u","-la","-cu","-d"]
    valid_command=0
    for cmd in cmnd_list:
        if cmd == entered_command:
          valid_command =1
    if not valid_command:
        print("\nUnsupported argument🙁\n\n")
        welcome_data(user)
def user_selection():#user selecction function
    print("please enter user name: ")
    user = input()
    task_path = "data/"+user+"_task"
    comlt_path = "data/"+user+"_comp_stat"
    start(comlt_path,task_path)
    print("please enter to start:")
    return task_path,comlt_path,user
def user_delete():
    print("please enter user name: ")
    user = input()
    os.remove("data/"+user+"_task")
    os.remove("data/"+user+"_comp_stat")
    print(user+" deleted")

  

#main loop

task_path,comlt_path,user =user_selection()
while True:  
    entered_command,cmd_index =Todo_application(str(input()))
    validate_cmd(entered_command,user)
    if entered_command=="":
        welcome_data(user)
    if entered_command == ("-c"):
        complete_task(cmd_index,"X",task_path,comlt_path,user) 
    if entered_command == ("-u"):
        complete_task(cmd_index," ",task_path,comlt_path,user)
    if entered_command==("-l"):
        list_task(cmd_index,"",task_path)
    if entered_command==("-la"):
        list_task(cmd_index,"a",task_path)
    if entered_command==("-a"):
        add_task(cmd_index,task_path)
    if entered_command == ("-r"):
        remove_task(cmd_index,task_path)
    if entered_command == ("-cu"):
        task_path,comlt_path,user =user_selection()  
    if  entered_command == ("-d"):
        user_delete()
    if entered_command == ("-x"):
        break
    



    





