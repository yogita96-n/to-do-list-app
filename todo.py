import tkinter
import tkinter.messagebox
import pickle
root = tkinter.Tk()
root.title("To-Do app by @yogita")

def add_task():
    task =entry_task.get()
    if task !="":
     listbox_task.insert(tkinter.END,task)
     entry_task.delete(0 , tkinter.END)
    else:
     tkinter.messagebox.showwarning(title="warning!!!!", message="You must enter a task") 

def markcompleted_task():
      marked=listbox_task.curselection()
      temp=marked[0]
      temp_marked=listbox_task.get(marked)
      temp_marked=temp_marked+" ✔️ "
      listbox_task.delete(temp)
      listbox_task.insert(temp,temp_marked)

def delete_task():
    try:
     task_index=listbox_task.curselection()[0]
     listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!!", message="You must select a task")

def save_task():
    task=listbox_task.get(0, listbox_task.size())
    pickle.dump(task,open("tasks.dat","wb"))

#create GUI
frame_task=tkinter.Frame(root)
frame_task.pack()

listbox_task= tkinter.Listbox(frame_task, height=10,width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_task=tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task= tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_markcompleted_task= tkinter.Button(root, text="Markcompleted task", width=48, command=markcompleted_task)
button_markcompleted_task.pack()

button_delete_task= tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_save_task= tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()


root.mainloop()
