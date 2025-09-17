from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq

def insert():
    ps= passw.get()
    nm = name.get()
    cur.execute("INSERT INTO info VALUES(?,?)",(nm,ps))
    con.commit()
    messagebox.showinfo(title="Выполнено",message = "Пароль успешно добавлен")

def find():
    nam = pnam.get()
    cur.execute("SELECT (password) FROM info WHERE name = ?",(nam,))
    mes = cur.fetchone()
    messagebox.showinfo(title="Пароль",message=f"Пароль от {nam}: {mes[0]}")

def delete():
    nme = pan.get()
    cur.execute("DELETE FROM info WHERE name = ?",(nme,))
    try:
        con.commit()
        messagebox.showinfo(title = "Удаление",message = "Пароль успешно удалён")
    except:
        messagebox.showerror("Ошибка","Возможно, пароль, который вы хотите удалить не присутствует в базе данных," \
        "проверьте правильность написание названия")

with sq.connect("Pass.db",check_same_thread=False) as con: #Insert the name of your db instead "Pass.db"
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS info(
                name TEXT,
                password TEXT)""")

root = Tk()
root.title("Pass Inserter")
icon = PhotoImage(file = "icon2.png")
root.geometry("500x300")
root.iconphoto(False,icon)
root.resizable(False,False)

notebook = ttk.Notebook(root)
notebook.pack(expand=True,fill=BOTH)


frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)


name_1 = ttk.Label(frame1,text = "Название пароля")
name_1.pack()

name = ttk.Entry(frame1)
name.pack()

name_12 = ttk.Label(frame1,text = "Пароль")
name_12.pack()

passw = ttk.Entry(frame1)
passw.pack()

info = ttk.Label(frame1)
info.pack()

btn1=ttk.Button(frame1,text = "Ввести данные в базу",command=insert)
btn1.pack()


title_2 = ttk.Label(frame2,text="Введите название пароля")
title_2.pack()

pnam = ttk.Entry(frame2)
pnam.pack()

findbtn=ttk.Button(frame2,text = "Найти",command=find)
findbtn.pack() 


title_3 = ttk.Label(frame3,text = "Введите название пароля который вы хотите удалить")
title_3.pack()

pan = ttk.Entry(frame3)
pan.pack()

delbutton = ttk.Button(frame3,text = "Удалить пароль",command = delete)
delbutton.pack()


frame1.pack(fill=BOTH,expand=True)
frame2.pack(fill=BOTH,expand=True)
frame3.pack(fill=BOTH,expand=True)

notebook.add(frame1,text="Ввести пароль")
notebook.add(frame2,text="Получить пароль")
notebook.add(frame3,text="Удалить пароль")

root.mainloop()

