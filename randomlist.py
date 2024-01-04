import os
import json
from random import choice

#clear screen
def screenClear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

#display
def display(data):
    text=''
    for datum in data:
            if datum!=data[-1]:
                text+=f'({data.index(datum)+1}) {datum}.\n'
            else:
                text+=f'({data.index(datum)+1}) {datum}.'
    return text

#showing lists
def ordering(show=True):
    screenClear()
    jsonFiles=[file for file in os.listdir(os.path.join(os.getcwd(),"data")) if ".json" in file]
    if jsonFiles:
        text=display(jsonFiles)
        file=input(f'file choices :\n{text}\nchoice: ')
        screenClear()
        while True:
            if file in [str(i) for i in range(1,len(jsonFiles)+1)]:
                return jsonFiles[int(file)-1]
            else:
                print("invalid input!")
                file=input(f'file choices :\n{text}\nchoice: ')
                screenClear() 
    else:
        if show:
            input("No files to display")
        return 0
    

def commonLand():#block that i may use later.
    screenClear()
    while True:
        ans=input("Do you want to edit existed file? (y/n)\n response: ")
        screenClear()
        if ans=='y':
            FileName=ordering()
            if not FileName:
                return (0,0)
            break
        elif ans=='n':
            FileName=f"{input("please, enter the file name: ")}.json"
            screenClear()
            break
        else:
            print("invalid input!")
    jsonFiles=[file for file in os.listdir(os.path.join(os.getcwd(),"data")) if ".json" in file]
    path=os.path.join(os.getcwd(),"data",FileName)
    #if json file existed
    if  FileName in jsonFiles:
        #take it
        with open(path,'r') as file:
            dic=json.load(file)
        return (dic,path)
    #no
    else:
        return (0,path)

#saving to json
def adding():
    (dic,path)=commonLand()
    if dic:
        pass
    elif not path:
        screenClear()
        return 0
    else:
        dic=[]
    #resulted list 
    value=input(f"please,enter a value: ")
    screenClear()
    dic.append(value)
    #loop to enter more
    while True:
        more=input("do yo want to add more? (y/n)\nrespond: ")
        screenClear()
        if more=='y':
            value=input(f"please,enter a value: ")
            screenClear()
            dic.append(value)
        elif more=="n":
            break
        else:
            print("invalid input!")
    with open(path,'w') as file:
        json.dump(dic,file,indent=4)

#showing json
def show():
        value=ordering()
        if value:
            with open(os.path.join(os.getcwd(),"data",value)) as file:
                input(display(json.load(file)))
        screenClear()

#deleting
def delete():
    value=ordering()
    if value:
        path=os.path.join(os.getcwd(),"data",value)
        with open(path) as file:
                data=json.load(file)
        item=input(f"Delete choice:\n{display(data)}\nchoice: ")
        while item not in [str(i) for i in range(1,len(data)+1)]:
            screenClear()
            print("inavlid input!")
            item=input(f"Delete choice:\n{display(data)}\nchoice: ")
        data.remove(data[int(item)-1])
        screenClear()
        while True:
            more=input("do yo want to delete more? (y/n)\nrespond: ")
            screenClear()
            if more=='y':
                item=input(f"Delete choice:\n{display(data)}\nchoice: ")
                while item not in [str(i) for i in range(1,len(data)+1)]:
                    screenClear()
                    print("inavlid input!")
                    item=input(f"Delete choice:\n{display(data)}\nchoice: ")
                    data.remove(data[int(item)-1])
                    screenClear()
            elif more=="n":
                break
            else:
                print("invalid input!")
        with open(path,'w') as file:
            json.dump(data,file,indent=4)

def deleteList():
    value=ordering()
    if value:
        if os.name=="nt":
            os.system(f'del "{os.path.join(os.getcwd(),"data",value)}"')
        else:
            os.system(f'rm "{os.path.join(os.getcwd(),"data",value)}"')

def rand():
    value=ordering()
    if value:
        with open(os.path.join(os.getcwd(),"data",value)) as file:
            data=json.load(file)
        target=choice(data)
        try:
            os.system(f'echo "{target}"|clip')
        except:
            pass
        input(f"your random value is : {target}")
        screenClear()

def app():
    screenClear()
    while True:
        choices=["Add","Show","Delete","Random","Delete List","Exit"]
        txt=display(choices)
        ans=input(f"Choices:\n{txt}\nresponse: ")
        if ans in [str(i) for i in range(1,len(choices)+1)]:
            if ans =="1":
                adding()
            elif ans =="2":
                show()
            elif ans=="3":
                delete()
            elif ans=="5":
                deleteList()
            elif ans=="4":
                rand()
            else:
                screenClear()
                break
        else:
            screenClear()
            print("invalid input!")

if __name__=="__main__":
    app()