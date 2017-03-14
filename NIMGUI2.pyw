import tkinter
from random import randint
from tkinter import *
a,b,c,x,y=randint(0,63),randint(0,63),randint(0,63),"",5
def d(x ,y):
    global a,b,c,xww,xxw,xxx
    if (not(x=="a"  or x=="A" or x=="C" or x=="B" or x=="b" or x=="c")):
        return    
    if((x=="a"or x=="A") and y<=a and y>0):
        a=a-y
    elif((x=="b"or x=="B") and y<=b and y>0):
        b=b-y
    elif((x=="c"or x=="C") and y<=c and y>0):
        c=c-y
    else:
        return
    if(a==0 and b==0 and c==0):
        xxxy = Label(t, text="---  YOU WON!!   ---")
        xxxy.config(fg="black",bg="white",font = "Verdana 10 bold italic")
        xxxy.pack()
        input()
        exit
    u,v,w="{0:b}".format(int(a)),"{0:b}".format(int(b)),"{0:b}".format(int(c)) 
    v,u,w=v.zfill(6),u.zfill(6),w.zfill(6)
    u,v,w=list(u),list(v),list(w)
    j,l,lo,m,n,i,y=0,0,0,0,1,0,['a','a','a','a','a','a']
    while(i<6):
        y[i]=int(u[i])+int(v[i])+int(w[i])
        i+=1
    while(j<6):
        if(y[j]==3 or y[j]==1 ):
           if(u[j]=="1" and (m==0 or m==1)):
                u[j],m,l,j,lo="0",1,1,j+1,1
                continue
           if(u[j]=="0" and l==1 and m==1):
                u[j],n="1",n+1
                if(n<5):
                    j=j+1;
                    continue    
           if(v[j]=="1" and(m==0 or m==2)):
                 v[j],l,m,j,lo="0",2,2,j+1,1
                 continue
           if(v[j]=="0"and l==2 and m==2):
               v[j],n="1",n+1
               if(n<5):
                    j=j+1;
                    continue    
           if(w[j]=="1"and(m==0 or m==3)):
                w[j],m,l,j,lo="0",3,3,j+1,1
                continue
           if(w[j]=="0" and l==3 and m==3):
                w[j],n="1",n+1
                if(n<5):
                    j=j+1;
                    continue  
        j=j+1;
    if(lo==0):
        j=0
        while(j<6):
           if(u[j]=="1"):
                u[j],j="0",7
           elif(v[j]=="1"):
                 v[j],j="0",7
           elif(w[j]=="1"):
               w[j],j="0",7
           j=j+1
    k,i,y=0,0,['a','a','a','a','a','a']
    while(i<6):
        y[i]=int(u[i])+int(v[i])+int(w[i])
        i+=1
    e=f=g=""
    while(k<6):
        e,f,g,k=e+u[k],f+v[k],g+w[k],k+1
    a,b,c=int(e,2),int(f,2),int(g,2)
    xww.pack_forget()
    xxw.pack_forget()
    xxx.pack_forget()
    xww = Label(t, text="---->>SET a = "+str(a)+"<<----")
    xxw = Label(t, text="---->>SET b = "+str(b)+"<<----")
    xxx = Label(t, text="---->>SET c = "+str(c)+"<<----")
    xxx.config(fg="red",bg="black",font = "Verdana 10 bold italic")
    xww.config(fg="green",bg="black",font = "Verdana 10 bold italic")
    xxw.config(fg="blue",bg="black",font = "Verdana 10 bold italic")
    xww.pack()
    xxw.pack()
    xxx.pack()
    if(a==0 and b==0 and c==0):
        xxxx = Label(t, text="---  YOU LOST NICE TRY   ---")
        xxxx.config(fg="black",bg="white",font = "Verdana 10 bold italic")
        xxxx.pack()
t = tkinter.Tk()
def foo():
        global nt,ent
        oo,ii=""+ent.get(),int(nt.get())
        ent.delete(0, tkinter.END)
        nt.delete(0, tkinter.END)
        d(oo,ii)
w = Label(t, text="WELCOME TO NIM")
w.pack()
ww = Label(t, text="Enter the set you want to select ")
ww.pack()
ent = tkinter.Entry(t)
ent.pack()
www = Label(t, text="How many element u want to delete?")
www.pack()
nt = tkinter.Entry(t)
nt.pack()
wwww = Label(t, text="")
wwww.pack()
bb = tkinter.Button(t, text="MAKE YOUR MOVE", command=foo)
bb.pack()
xww = Label(t, text="---->>SET a = "+str(a)+"<<----")
xww.pack()
xxw = Label(t, text="---->>SET b = "+str(b)+"<<----")
xxw.pack()
xxx = Label(t, text="---->>SET c = "+str(c)+"<<----")
xxx.pack()
wwww.config(fg="black",bg="black",font = "Verdana 10 bold italic")
ent.config(fg="black",bg="white",font = "Verdana 10 bold italic")
nt.config(fg="black",bg="white",font = "Verdana 10 bold italic")
bb.config(fg="black",bg="white",pady="5",font = "Verdana 10 bold italic")
w.config(fg="white",bg="black",font = "Verdana 10 bold italic")
ww.config(fg="white",bg="black",font = "Verdana 10 bold italic")
www.config(fg="white",bg="black",font = "Verdana 10 bold italic")
xxx.config(fg="red",bg="black",font = "Verdana 10 bold italic")
xww.config(fg="green",bg="black",font = "Verdana 10 bold italic")
xxw.config(fg="blue",bg="black",font = "Verdana 10 bold italic")
t.config(bg="black")
tkinter.mainloop()


