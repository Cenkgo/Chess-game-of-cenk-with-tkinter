from tkinter import *
import tkinter.filedialog
pen=Tk()

fr=Frame(pen)
tt=[]
scl=False
x,y=0,0
x1,y1=0,0
def fnk(a,b):
	def dnd():
		global tt,scl,x,y,x1,y1
		if not scl:
			bt=False
			if tt[b][a]["text"]=="♟" and tt[b][a]["fg"]=="white":
				if b==6:
					if tt[b-1][a]["text"]=="":
						tt[b-1][a].config(bg="red")
						bt=True
						if tt[b-2][a]["text"]=="":
							tt[b-2][a].config(bg="red")
							bt=True
				else:
					if tt[b-1][a]["text"]=="":
						tt[b-1][a].config(bg="red")
						bt=True
				if b-1>=0 and a+1<=7:
					if tt[b-1][a+1]["fg"]=="black" and tt[b-1][a+1]["text"]!="":
						tt[b-1][a+1].config(bg="red")
						bt=True
				if b-1>=0 and a-1>=0 and tt[b-1][a-1]["text"]!="":
					if tt[b-1][a-1]["fg"]=="black":
						tt[b-1][a-1].config(bg="red")
						bt=True
				scl=bt
			if tt[b][a]["text"]=="♟" and tt[b][a]["fg"]=="black":
				if b==1:
					if tt[b+1][a]["text"]=="":
						tt[b+1][a].config(bg="red")
						bt=True
						if tt[b+2][a]["text"]=="":
							tt[b+2][a].config(bg="red")
							bt=True
				else:
					if tt[b+1][a]["text"]=="":
						tt[b+1][a].config(bg="red")
						bt=True
				if b+1<=7 and a+1<=7:
					if tt[b+1][a+1]["fg"]=="white" and tt[b+1][a+1]["text"]!="":
						tt[b+1][a+1].config(bg="red")
						bt=True
				if b+1<=7 and a-1>=0 and tt[b+1][a-1]["text"]!="":
					if tt[b+1][a-1]["fg"]=="white":
						tt[b+1][a-1].config(bg="red")
						bt=True
			if tt[b][a]["text"]=="♞":
				if a+1<=7 and b+2<=7:
					if tt[b+2][a+1]["fg"]!=tt[b][a]["fg"] or tt[b+2][a+1]["text"]=="":
						tt[b+2][a+1].config(bg="red")
						bt=True
				if a+2<=7 and b+1<=7:
					if tt[b+1][a+2]["fg"]!=tt[b][a]["fg"] or tt[b+1][a+2]["text"]=="":
						tt[b+1][a+2].config(bg="red")
						bt=True
				if a-1>=0 and b+2<=7 :
					if tt[b+2][a-1]["fg"]!=tt[b][a]["fg"] or tt[b+2][a-1]["text"]=="":
						tt[b+2][a-1].config(bg="red")
						bt=True
				if a-2>=0 and b+1<=7:
					if tt[b+1][a-2]["fg"]!=tt[b][a]["fg"] or tt[b+1][a-2]["text"]=="":
						tt[b+1][a-2].config(bg="red")
						bt=True
				if a-1>=0 and b-2>=0:
					if tt[b-2][a-1]["fg"]!=tt[b][a]["fg"] or tt[b-2][a-1]["text"]=="":
						tt[b-2][a-1].config(bg="red")
						bt=True
				if a-2>=0 and b-1>=0:
					if tt[b-1][a-2]["fg"]!=tt[b][a]["fg"] or tt[b-1][a-2]["text"]=="":
						tt[b-1][a-2].config(bg="red")
						bt=True
				if a+1<=7 and b-2>=0:
					if tt[b-2][a+1]["fg"]!=tt[b][a]["fg"] or tt[b-2][a+1]["text"]=="":
						tt[b-2][a+1].config(bg="red")
						bt=True
				if a+2<=7 and b-1>=0:
					if tt[b-1][a+2]["fg"]!=tt[b][a]["fg"] or tt[b-1][a+2]["text"]=="":
						tt[b-1][a+2].config(bg="red")
						bt=True
			if tt[b][a]["text"]=="♝":
				d=1
				while b+d<=7 and a+d<=7:
					if tt[b+d][a+d]["text"]=="":
						tt[b+d][a+d].config(bg="red")
						bt=True
					elif tt[b+d][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a+d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b+d<=7 and a-d>=0:
					if tt[b+d][a-d]["text"]=="":
						tt[b+d][a-d].config(bg="red")
						bt=True
					elif tt[b+d][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a-d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b-d>=0 and a-d>=0:
					if tt[b-d][a-d]["text"]=="":
						tt[b-d][a-d].config(bg="red")
						bt=True
					elif tt[b-d][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a-d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b-d>=0 and a+d<=7:
					if tt[b-d][a+d]["text"]=="":
						tt[b-d][a+d].config(bg="red")
						bt=True
					elif tt[b-d][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a+d].config(bg="red")
						bt=True
						break
					d+=1
			if tt[b][a]["text"]=="♜":
				d=1
				while b-d>=0:
					if tt[b-d][a]["text"]=="":
						tt[b-d][a].config(bg="red")
						bt=True
					elif tt[b-d][a]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b+d<=7:
					if tt[b+d][a]["text"]=="":
						tt[b+d][a].config(bg="red")
						bt=True
					elif tt[b+d][a]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while a+d<=7:
					if tt[b][a+d]["text"]=="":
						tt[b][a+d].config(bg="red")
						bt=True
					elif tt[b][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b][a+d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while a-d>=0:
					if tt[b][a-d]["text"]=="":
						tt[b][a-d].config(bg="red")
						bt=True
					elif tt[b][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b][a-d].config(bg="red")
						bt=True
						break
					d+=1
			if tt[b][a]["text"]=="♛":
				d=1
				while b-d>=0:
					if tt[b-d][a]["text"]=="":
						tt[b-d][a].config(bg="red")
						bt=True
					elif tt[b-d][a]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b+d<=7:
					if tt[b+d][a]["text"]=="":
						tt[b+d][a].config(bg="red")
						bt=True
					elif tt[b+d][a]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while a+d<=7:
					if tt[b][a+d]["text"]=="":
						tt[b][a+d].config(bg="red")
						bt=True
					elif tt[b][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b][a+d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while a-d>=0:
					if tt[b][a-d]["text"]=="":
						tt[b][a-d].config(bg="red")
						bt=True
					elif tt[b][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b][a-d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b+d<=7 and a+d<=7:
					if tt[b+d][a+d]["text"]=="":
						tt[b+d][a+d].config(bg="red")
						bt=True
					elif tt[b+d][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a+d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b+d<=7 and a-d>=0:
					if tt[b+d][a-d]["text"]=="":
						tt[b+d][a-d].config(bg="red")
						bt=True
					elif tt[b+d][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b+d][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b+d][a-d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b-d>=0 and a-d>=0:
					if tt[b-d][a-d]["text"]=="":
						tt[b-d][a-d].config(bg="red")
						bt=True
					elif tt[b-d][a-d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a-d]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a-d].config(bg="red")
						bt=True
						break
					d+=1
				d=1
				while b-d>=0 and a+d<=7:
					if tt[b-d][a+d]["text"]=="":
						tt[b-d][a+d].config(bg="red")
						bt=True
					elif tt[b-d][a+d]["fg"]==tt[b][a]["fg"]:
						if d>1:
							bt=True
						break
					elif tt[b-d][a+d]["fg"]!=tt[b][a]["fg"]:
						tt[b-d][a+d].config(bg="red")
						bt=True
						break
					d+=1
			if tt[b][a]["text"]=="♚":
				if a+1<=7 and b+1<=7:
					if tt[b+1][a+1]["fg"]!=tt[b][a]["fg"] or tt[b+1][a+1]["text"]=="":
						tt[b+1][a+1].config(bg="red")
						bt=True
				if a-1>=0 and b+1<=7:
					if tt[b+1][a-1]["fg"]!=tt[b][a]["fg"] or tt[b+1][a-1]["text"]=="":
						tt[b+1][a-1].config(bg="red")
						bt=True
				if a+1<=7 and b-1>=0:
					if tt[b-1][a+1]["fg"]!=tt[b][a]["fg"] or tt[b-1][a+1]["text"]=="":
						tt[b-1][a+1].config(bg="red")
						bt=True
				if a-1>=0 and b-1>=0:
					if tt[b-1][a-1]["fg"]!=tt[b][a]["fg"] or tt[b-1][a-1]["text"]=="":
						tt[b-1][a-1].config(bg="red")
						bt=True
				if a-1>=0:
					if tt[b][a-1]["fg"]!=tt[b][a]["fg"] or tt[b][a-1]["text"]=="":
						tt[b][a-1].config(bg="red")
						bt=True
				if a+1<=7:
					if tt[b][a+1]["fg"]!=tt[b][a]["fg"] or tt[b][a+1]["text"]=="":
						tt[b][a+1].config(bg="red")
						bt=True
				if b-1>=0:
					if tt[b-1][a]["fg"]!=tt[b][a]["fg"] or tt[b-1][a]["text"]=="":
						tt[b-1][a].config(bg="red")
						bt=True
				if b+1<=7:
					if tt[b+1][a]["fg"]!=tt[b][a]["fg"] or tt[b+1][a]["text"]=="":
						tt[b+1][a].config(bg="red")
						bt=True
			scl=bt
			if bt:
				x=a
				y=b
		if scl:
			if tt[b][a]["text"]=="" and tt[b][a]["bg"]!="red":
				for i in range(8):
					for e in range(8):
						rnk1=""
						if i%2==0:
							if e%2==0:
								rnk="salmon4"
							else:
								rnk="tan2"
						else:
							if e%2==1:
								rnk="salmon4"
							else:
								rnk="tan2"
						tt[i][e].config(bg=rnk)
				scl=False
			if tt[b][a]["bg"]=="red":
				tt[b][a].config(text=tt[y][x]["text"])
				tt[b][a].config(fg=tt[y][x]["fg"])
				tt[y][x]["text"]=""
				for i in range(8):
					for e in range(8):
						rnk1=""
						if i%2==0:
							if e%2==0:
								rnk="salmon4"
							else:
								rnk="tan2"
						else:
							if e%2==1:
								rnk="salmon4"
							else:
								rnk="tan2"
						tt[i][e].config(bg=rnk)
					scl=False
					if tt[b][a]["text"]=="♟" and tt[b][a]["fg"]=="white" and b==0:
						fr2.pack()
						x1,y1=a,b
					if tt[b][a]["text"]=="♟" and tt[b][a]["fg"]=="black" and b==7:
						fr2.pack()
						x1,y1=a,b
	btt=[]
	for e in range(8):
		rnk=""
		rnk1=""
		if i%2==0:
			if e%2==0:
				rnk="salmon4"
				rnk1="tan2"
			else:
				rnk="tan2"
				rnk1="salmon4"
		else:
			if e%2==1:
				rnk="salmon4"
				rnk1="tan2"
			else:
				rnk="tan2"
				rnk1="salmon4"
	return dnd
for i in range(8):
	btt=[]
	for e in range(8):
		rnk=""
		rnk1=""
		if i%2==0:
			if e%2==0:
				rnk="salmon4"
				rnk1="tan2"
			else:
				rnk="tan2"
				rnk1="salmon4"
		else:
			if e%2==1:
				rnk="salmon4"
				rnk1="tan2"
			else:
				rnk="tan2"
				rnk1="salmon4"
		btt.append(Button(fr,width=1,padx=20,bg=rnk,fg=rnk1,command=fnk(e,i)))
	tt.append(btt)
def fnk2():
	if dg.get()=="at":
		tt[y1][x1].config(text="♞")
	if dg.get()=="vezir":
		tt[y1][x1].config(text="♛")
	if dg.get()=="kale":
		tt[y1][x1].config(text="♜")
	if dg.get()=="fil":
		tt[y1][x1].config(text="♝")
	fr2.pack_forget()
fr.pack(pady=(50,0))
for i in range(8):
	for e in range(8):
		tt[i][e].grid(row=i+1,column=e+1)
for i in range(ord("A"),ord("A")+8):
	Label(fr,text=chr(i)).grid(column=i-ord("A")+1,row=0)
for i in range(1,9):
	Label(fr,text=i).grid(row=i,column=0)
art=0
for i in "♜♞♝♛♚♝♞♜":
	tt[0][art].config(text=i,fg="black")
	tt[7][art].config(text=i,fg="white")
	art+=1
art=0
for i in range(8):
	tt[1][art].config(text="♟",fg="black")
	tt[6][art].config(text="♟",fg="white")
	art+=1
	
fr2=Frame(pen)
dg=StringVar()
dg.set("vezir")
fl=OptionMenu(fr2,dg,"vezir","kale","fil","at")
tm=Button(fr2,text="Tamam",command=fnk2)
fl.pack()
tm.pack()
pen.mainloop()