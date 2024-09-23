363333
96

from tkinter import *
from tkinter import messagebox
import tempfile
import os
root=Tk()
root.title('Billing ManagementSystem')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
#root.geometry('1280x720')
bg_color='#00a3a3'



#=========================================================V==========================================================================



Bread=IntVar()
Wine=IntVar()
Rice=IntVar()
Milk=IntVar()
total=IntVar()

mpB=1.89
mpW=8.99
mpR=2.18
mpM=4.50



cb=StringVar()
cw=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()


Name=StringVar()
Mobile=IntVar()



#===========================================================F========================================================================



def Total():
   
   if Bread.get()==0 and Wine.get()==0 and Rice.get()==0 and Milk.get()==0:
      messagebox.showerror("Error","Please Select The Number of Quantity.")
   else:

      
      b=Bread.get()
      w=Wine.get()
      r=Rice.get()
      m=Milk.get()

      xx=float(b*mpB+w*mpW+r*mpR+m*mpM)
      total.set(b+w+r+m)
      total_cost.set('$'+str(round(xx,2)))

      cb.set('$'+str(round(b*mpB,2)))
      cw.set('$'+str(round(w*mpW,2)))
      cr.set('$'+str(round(r*mpR,2)))
      cm.set('$'+str(round(m*mpM,2)))



def receipt():
   if Mobile.get()==0 or Name.get()=="" or Mobile.get()>9999999999:
      if Mobile.get()==0:
         messagebox.showerror("Error","Please Enter Mobile Number.")
      if Mobile.get()>=9999999999:
         messagebox.showerror("Error","Please *Valid* Mobile Number.")
      if Name.get()=='':
         messagebox.showerror("Error","Please Enter Name.")
      
      
   else:
      textarea.delete(1.0,END)
      textarea.insert(END," ================================")
      textarea.insert(END,"\n\tBilling Management System")
      textarea.insert(END,"\n ================================")
      textarea.insert(END,f"\n  Name : \t\t{Name.get()}")
      textarea.insert(END,f"\n  phone No : \t\t{Mobile.get()}")
      textarea.insert(END,"\n ================================")
      textarea.insert(END,"\n\n  Items\tNumber of Items\t\tCost of Items")
      textarea.insert(END,f"\n\n  Bread\t\t{Bread.get()}\t  {cb.get()}")
      textarea.insert(END,f"\n\n  Wine\t\t{Wine.get()}\t  {cw.get()}")
      textarea.insert(END,f"\n\n  Rice\t\t{Rice.get()}\t  {cr.get()}")
      textarea.insert(END,f"\n\n  Milk\t\t{Milk.get()}\t  {cm.get()}")
      textarea.insert(END,"\n\n ================================")
      textarea.insert(END,f"\n Total Price\t\t{total.get()}\t  {total_cost.get()}")
      textarea.insert(END,"\n ================================")
      


   


def print():
   q=textarea.get('1.0','end-1c')
   filename=tempfile.mktemp('.txt')
   open(filename,'w').write(q)
   os.startfile(filename,'Print')



def reset():
   textarea.delete(1.0,END)
   Bread.set(0)
   Wine.set(0)
   Rice.set(0)
   Milk.set(0)
   total.set(0)
   

   cb.set('')
   cw.set('')
   cr.set('')
   cm.set('')
   total_cost.set('')


def exit():
   if messagebox.askyesno('Exit',"Do you really want to exit ?"):
      root.destroy()



#====================================================================================================================================



title=Label(root,text='Billing Management System',bg=bg_color,fg='white',font=('arial',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)



#==============================================PRODUCT DETAILS=======================================================================



F1=LabelFrame(root,text='Product Details',font=('arial',15,'bold'),fg='gold',bg=bg_color,relief=RIDGE,bd=12)
F1.place(x=5,y=80,width=590,height=460)



#==============================Heading===============================================================================================



itm=Label(F1,text="Items",font=('Helvetic',19,'bold','underline'),fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=5,pady=15)

n=Label(F1,text="No. of items",font=('Helvetic',19,'bold','underline'),fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=5,pady=15)

cost=Label(F1,text="Cost of items",font=('Helvetic',19,'bold','underline'),fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=5,pady=15)



#========================================product=====================================================================================



bread=Label(F1,text="Bread",font=('arial',15,'bold'),fg='#00FF00',bg=bg_color)
bread.grid(row=1,column=0,padx=5,pady=15)
b_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=5,pady=15)
cb_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=cb)
cb_txt.grid(row=1,column=2,padx=15,pady=15)

wine=Label(F1,text="Wine",font=('arial',15,'bold'),fg='#00FF00',bg=bg_color)
wine.grid(row=2,column=0,padx=5,pady=15)
w_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=Wine)
w_txt.grid(row=2,column=1,padx=5,pady=15)
cw_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=cw)
cw_txt.grid(row=2,column=2,padx=15,pady=15)

rice=Label(F1,text="Rice",font=('arial',15,'bold'),fg='#00FF00',bg=bg_color)
rice.grid(row=3,column=0,padx=5,pady=15)
r_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=Rice)
r_txt.grid(row=3,column=1,padx=5,pady=15)
cr_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=cr)
cr_txt.grid(row=3,column=2,padx=15,pady=15)

milk=Label(F1,text="Milk",font=('arial',15,'bold'),fg='#00FF00',bg=bg_color)
milk.grid(row=4,column=0,padx=5,pady=15)
m_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=Milk)
m_txt.grid(row=4,column=1,padx=5,pady=15)
cm_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=cm)
cm_txt.grid(row=4,column=2,padx=15,pady=15)

t=Label(F1,text="Total Price",font=('arial',15,'bold'),fg='#00FF00',bg=bg_color)
t.grid(row=5,column=0,padx=10,pady=15)
b_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=total)
b_txt.grid(row=5,column=1,padx=5,pady=15)
ct_txt=Entry(F1,font='arial 13 bold',relief=SUNKEN,bd=4,justify=CENTER,textvariable=total_cost)
ct_txt.grid(row=5,column=2,padx=15,pady=15)



#===============================================Customer Details=====================================================================



F2=LabelFrame(root,text='Customer Details',font=('arial',15,'bold'),fg='gold',bg=bg_color,relief=RIDGE,bd=12)
F2.place(x=605,y=80,width=365,height=460)



name=Label(F2,text="Name",font=('arial',15,'bold'),fg='#0000db',bg=bg_color)
name.grid(row=1,column=0,padx=10,pady=80)
name_txt=Entry(F2,font='arial 13 bold',relief=SUNKEN,bd=4,textvariable=Name)
name_txt.grid(row=1,column=1,padx=10,pady=80)


mobile=Label(F2,text="Phone No",font=('arial',15,'bold'),fg='#0000db',bg=bg_color)
mobile.grid(row=2,column=0,padx=10,pady=5)
mobile_txt=Entry(F2,font='arial 13 bold',relief=SUNKEN,bd=4,textvariable=Mobile)
mobile_txt.grid(row=2,column=1,padx=10,pady=5)



#=============================================billing================================================================================



F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=980,y=80,width=372,height=460)
bil_title=Label(F3,text="Reciept",font='arial 12 bold',bd=5,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(F3,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F3,font='arial 13 bold',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)              



#================================================Buttons=============================================================================



F4=Frame(root,relief=GROOVE,bd=10,bg=bg_color)
F4.place(x=5,y=550,width=1340,height=110)

btn1=Button(F4,text="Total",font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=16,bd=1,relief=GROOVE,command=Total)
btn1.grid(row=0,column=0,padx=24,pady=17)

btn2=Button(F4,text="Receipt",font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=16,bd=1,relief=GROOVE,command=receipt)
btn2.grid(row=0,column=1,padx=24,pady=17)

btn3=Button(F4,text="Print",font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=16,bd=1,relief=GROOVE,command=print)
btn3.grid(row=0,column=2,padx=24,pady=17)

btn4=Button(F4,text="Reset",font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=16,bd=1,relief=GROOVE,command=reset)
btn4.grid(row=0,column=3,padx=24,pady=17)

btn5=Button(F4,text="Exit",font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=16,bd=1,relief=GROOVE,command=exit)
btn5.grid(row=0,column=4,padx=24,pady=17)


root.mainloop()
