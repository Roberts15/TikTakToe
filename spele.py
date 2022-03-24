from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi​
#from termcolor import colored
speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus​
count=0 #aizpildīto rūtiņu skaits
winner=False
#print=(colored("This is red"), "red")
def btnClick(button): #padod pogu​
    global speletajsX,count #kādi mainīgie tiks izmantoti​
    if button["text"]==" "and speletajsX==True:#spēlē X spēlētājs​
        button["text"]="x" #maina uz X​
        button["fg"]="red"      
        speletajsX=False
        count+=1 # palielina rūtiņu skaitu​
        checkWinner()
    elif button["text"]==" " and speletajsX==False: # mainās spēlētāji​
        button["text"]="o"
        button["fg"]="green"        
        #button.config(state=DISABLED)
        speletajsX=True
        count+=1
        checkWinner()
    else:       
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")
    return 0
#def checkWinner():
    global winner 
    if (btn1["text"]=="x"and btn4["text"]=="x" and btn7["text"]=="x" or
     btn2["text"]=="x"and btn5["text"]=="x" and btn8["text"]=="x" or 
     btn3["text"]=="x"and btn6["text"]=="x" and btn9["text"]=="x"or

     btn1["text"]=="x"and btn2["text"]=="x" and btn3["text"]=="x"or
     btn4["text"]=="x"and btn5["text"]=="x" and btn6["text"]=="x"or
     btn7["text"]=="x"and btn8["text"]=="x" and btn9["text"]=="x"or
    
     btn1["text"]=="x"and btn5["text"]=="x" and btn9["text"]=="x"or
     btn3["text"]=="x"and btn5["text"]=="x" and btn7["text"]=="x"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs X ir uzvarētājs")
        disableButtons()
    elif (btn1["text"]=="o"and btn4["text"]=="o" and btn7["text"]=="o" or
     btn2["text"]=="o"and btn5["text"]=="o" and btn8["text"]=="o" or 
     btn3["text"]=="o"and btn6["text"]=="o" and btn9["text"]=="o"or
     btn1["text"]=="o"and btn2["text"]=="o" and btn3["text"]=="o"or
     btn4["text"]=="o"and btn5["text"]=="o" and btn6["text"]=="o"or
     btn7["text"]=="o"and btn8["text"]=="o" and btn9["text"]=="o"or    
     btn1["text"]=="o"and btn5["text"]=="o" and btn9["text"]=="o"or
     btn3["text"]=="o"and btn5["text"]=="o" and btn7["text"]=="o"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs o ir uzvarētājs")
        disableButtons()
    elif count==9 and winner==False:        
        messagebox.showinfo("TicTacToe", "Neizšķirts")
        disableButtons()
    return 0 
def checkWinner():
    global winner 
    if (btn1["text"]=="x"and btn4["text"]=="x" and btn7["text"]=="x" ):
        winner=True
        x=True
        btn1["bg"]="white"
        btn4["bg"]="white"
        btn7["bg"]="white"
    if (btn2["text"]=="x"and btn5["text"]=="x" and btn8["text"]=="x" ):
        winner=True
        x=True
        btn2["bg"]="white"
        btn5["bg"]="white"
        btn8["bg"]="white"
    if (btn3["text"]=="x"and btn6["text"]=="x" and btn9["text"]=="x"):
        winner=True
        x=True
        btn3["bg"]="white"
        btn6["bg"]="white"
        btn9["bg"]="white"

    if (btn1["text"]=="x"and btn2["text"]=="x" and btn3["text"]=="x"):
        winner=True
        x=True
        btn1["bg"]="white"
        btn2["bg"]="white"
        btn3["bg"]="white"
    if (btn4["text"]=="x"and btn5["text"]=="x" and btn6["text"]=="x"):
        winner=True
        x=True
        btn4["bg"]="white"
        btn5["bg"]="white"
        btn6["bg"]="white"
    if (btn7["text"]=="x"and btn8["text"]=="x" and btn9["text"]=="x"):
        winner=True
        x=True
        btn7["bg"]="white"
        btn8["bg"]="white"
        btn9["bg"]="white"
    
    if (btn1["text"]=="x"and btn5["text"]=="x" and btn9["text"]=="x"):
        winner=True
        x=True
        btn1["bg"]="white"
        btn5["bg"]="white"
        btn9["bg"]="white"
    if (btn3["text"]=="x"and btn5["text"]=="x" and btn7["text"]=="x"):
        winner=True
        x=True
        btn3["bg"]="white"
        btn5["bg"]="white"
        btn7["bg"]="white"
    if winner==True and x==True:
        messagebox.showinfo("TicTacToe","Speletajs X ir uzvarētājs")
        disableButtons()
    if (btn1["text"]=="o"and btn4["text"]=="o" and btn7["text"]=="o" ):
        winner=True
        o=True
        btn1["bg"]="white"
        btn4["bg"]="white"
        btn7["bg"]="white"
    if (btn2["text"]=="o"and btn5["text"]=="o" and btn8["text"]=="o" ):
        winner=True
        o=True
        btn2["bg"]="white"
        btn5["bg"]="white"
        btn8["bg"]="white"
    if (btn3["text"]=="o"and btn6["text"]=="o" and btn9["text"]=="o"):
        winner=True
        o=True
        btn3["bg"]="white"
        btn6["bg"]="white"
        btn9["bg"]="white"
    if (btn1["text"]=="o"and btn2["text"]=="o" and btn3["text"]=="o"):
        winner=True
        o=True
        btn1["bg"]="white"
        btn2["bg"]="white"
        btn3["bg"]="white"
    if (btn4["text"]=="o"and btn5["text"]=="o" and btn6["text"]=="o"):
        winner=True
        o=True
        btn4["bg"]="white"
        btn5["bg"]="white"
        btn6["bg"]="white"
    if (btn7["text"]=="o"and btn8["text"]=="o" and btn9["text"]=="o"):
        winner=True
        o=True
        btn7["bg"]="white"
        btn8["bg"]="white"
        btn9["bg"]="white"  
    if (btn1["text"]=="o"and btn5["text"]=="o" and btn9["text"]=="o"):
        winner=True
        o=True
        btn1["bg"]="white"
        btn5["bg"]="white"
        btn9["bg"]="white"
    if (btn3["text"]=="o"and btn5["text"]=="o" and btn7["text"]=="o"):
        winner=True
        o=True
        btn3["bg"]="white"
        btn5["bg"]="white"
        btn7["bg"]="white"
    if winner==True and o==True:
        messagebox.showinfo("TicTacToe","Speletajs O ir uzvarētājs")
        disableButtons()
    elif count==9 and winner==False:        
        messagebox.showinfo("TicTacToe", "Neizšķirts")
        disableButtons()
    return 0 

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0
def reset():

    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

    global winner, count, speletajsX
    winner=False
    count=0
    speletajsX=True
    
    return 0

def infoLogs():
        jaunsLogs=Toplevel()
        jaunsLogs.title('Info par programmu')
        jaunsLogs.geometry("300x300")
        apraksts=Label(jaunsLogs,text='Spēles noteikumi')
        apraksts2=Label(jaunsLogs,text='Uzvar, ja trīs vienādi simboli taisnā rindā. ')
        apraksts3=Label(jaunsLogs,text='Spēli var sākt no jauna pie opcijām "Jauns"')
        apraksts4=Label(jaunsLogs,text='Spēli var beigt pie opcijām "Iziet"')
        apraksts5=Label(jaunsLogs,text='Pirmais sāk spēlētājs X')
        apraksts.grid(row=0,column=0)
        apraksts2.grid(row=4,column=0)
        apraksts3.grid(row=2,column=0)
        apraksts4.grid(row=3,column=0)
        apraksts5.grid(row=1,column=0)
        return 0

mansLogs=Tk()
mansLogs.title("TicTacToe")
btn1=Button(mansLogs,bg="black" ,fg="white", bd=10 , text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn1))
btn2=Button(mansLogs,bg="grey", fg="white", bd=10 , text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn2))
btn3=Button(mansLogs,bg="black", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn3))
btn4=Button(mansLogs,bg="grey", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn4))
btn5=Button(mansLogs,bg="black", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn5))
btn6=Button(mansLogs,bg="grey", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn6))
btn7=Button(mansLogs,bg="black", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn7))
btn8=Button(mansLogs,bg="grey", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn8))
btn9=Button(mansLogs,bg="black", fg="white", bd=10 ,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn9))

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)

galvenaIzvelne=Menu(mansLogs)#izveido galveno izvēlni​
mansLogs.config(menu=galvenaIzvelne)#pievieno galvenajam logam​

opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvēlne​
galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)#lejupkrītošais saraksts​

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

galvenaIzvelne.add_command(label="Par programmu",command=infoLogs) # pievieno mazajai izvēlnei

mansLogs.mainloop()





