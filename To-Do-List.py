

import shelve
list_task=shelve.open("to-do.dat")

list_task['tasks']=[]
a=list_task['tasks']
r='\0'
p=""


user_name=input('Hello,what is your name?: ')
print("Hello "+user_name+"! and welcome to the To-Do List application!")
print("What would you like to do today "+user_name+"?")

while r.lower() != 'q'.lower():
  r=input("[Q]uit/[A]dd/[R]emove/[S]how/[C]lear ")
  if r.lower()=='s'.lower():
     if len(a)==0:
       print ("There are no task on your to-do list.")
       continue 
     else:
       for i in range(len(a)):
         print (str(i+1)+"."+a[i])
  
  if r.lower()=='c'.lower():
    total_delete=input("Are you sure you want to clear your to-do list? [Y] or [N]?")
    if total_delete.lower()=='Y'.lower():
      a.clear()
      print ("List is deleted!")
    else:
      print("To-Do List will not be deleted")
  
  if r.lower()=='r'.lower():
    print("Here is your list")
    for i in range(len(a)):
      print (str(i+1)+"."+a[i])
    remove=int(input("What do you want to remove from your list,Please choose the task number: "))
    remove-=1
    a.pop(remove)
   



  

  elif r.lower()=='a'.lower():
    p=input("Type what you want to put on your To-Do List: ") 
    a.append(p)
  
  elif r.lower()=='q'.lower():
    print("Thanks for using the To-Do list application!")