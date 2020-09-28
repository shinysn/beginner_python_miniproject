#simple GUI format
from tkinter import *

root=Tk()
root.title("Tik-tac-toe")

player = 1
flag=0
p1_name=""
p2_name=""

def start():
	global p1_name,p2_name
	info["text"] = ""
	p1_name=str(p1.get())
	p2_name=str(p2.get())
	start_btn.configure(state='disabled')
	p1.configure(state='disabled')
	p2.configure(state='disabled')
	b1.configure(state="normal")
	b2.configure(state="normal")
	b3.configure(state="normal")
	b4.configure(state="normal")
	b5.configure(state="normal")
	b6.configure(state="normal")
	b7.configure(state="normal")
	b8.configure(state="normal")
	b9.configure(state="normal")

def btndisable():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)

def click(bt_num):
	global flag
	global player
	if bt_num["text"]==" " and player==1:
		bt_num["text"]="X"
		info["text"] = ""
		check(player)
		player=2
		flag+=1


	elif bt_num["text"]==" " and player==2:
		bt_num["text"]="O"
		info["text"] = ""
		check(player)
		player=1
		flag+=1

	elif flag==9:
		info["text"] = "Match is tie:)"
		btndisable()

	else:
		info["text"] = "This box is already filled"

def check(n):
	global p1_name,p2_name
    #check rows
	if (b1["text"]==b2["text"]==b3["text"]=="X" or 
	b4["text"]==b5["text"]==b6["text"]=="X" or 
	b7["text"]==b8["text"]==b9["text"]=="X" or 
	b1["text"]==b2["text"]==b3["text"]=="O" or 
	b4["text"]==b5["text"]==b6["text"]=="O" or 
	b7["text"]==b8["text"]==b9["text"]=="O"):
		btndisable()
		if n==1:
			info["text"] = (p1_name,"Won the match")
		else:
			info["text"] = (p2_name,"Won the match")			
    
    #check columns
	elif (b1["text"]==b4["text"]==b7["text"]=="X" or 
	b2["text"]==b5["text"]==b8["text"]=="X" or 
	b3["text"]==b6["text"]==b9["text"]=="X" or
	b1["text"]==b4["text"]==b7["text"]=="O" or 
	b2["text"]==b5["text"]==b8["text"]=="O" or 
	b3["text"]==b6["text"]==b9["text"]=="O"):
		btndisable()
		if n==1:
			info["text"] = (p1_name,"Won the match")
		else:
			info["text"] = (p2_name,"Won the match")

    #check diagonals
	elif (b1["text"]==b5["text"]==b9["text"]=="X" or 
	b3["text"]==b5["text"]==b7["text"]=="X" or 
	b1["text"]==b5["text"]==b9["text"]=="O" or 
	b3["text"]==b5["text"]==b7["text"]=="O"):
		btndisable()
		if n==1:
			info["text"] = (p1_name,"Won the match")
		else:
			info["text"] = (p2_name,"Won the match")


player1=Text(root,width=8,height=1)
player1.insert('end', 'Player1: ')
player1.configure(state='disabled')

player2=Text(root,width=8,height=1)
player2.insert('end', 'Player2: ')
player2.configure(state='disabled')

p1=Entry(root,width=8)
p2=Entry(root,width=8)

start_btn=Button(root,text="Go",command=start)

info=Label(root,text="Welcome, Enter players name...",height=1)
	
b1=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b1),state='disabled')
b2=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b2),state='disabled')
b3=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b3),state='disabled')
b4=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b4),state='disabled')
b5=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b5),state='disabled')
b6=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b6),state='disabled')
b7=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b7),state='disabled')
b8=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b8),state='disabled')
b9=Button(root,text=" ",padx=40,pady=20,command=lambda:click(b9),state='disabled')

player1.grid(row=1,column=1)
player2.grid(row=2,column=1)
p1.grid(row=1,column=2)
p2.grid(row=2,column=2)
start_btn.grid(row=1,rowspan=2,column=3,columnspan=4)

b1.grid(row=5,column=1)
b2.grid(row=5,column=2)
b3.grid(row=5,column=3)

b4.grid(row=6,column=1)
b5.grid(row=6,column=2)
b6.grid(row=6,column=3)

b7.grid(row=7,column=1)
b8.grid(row=7,column=2)
b9.grid(row=7,column=3)

info.grid(row=4,column=1,columnspan=3)

root.mainloop()
