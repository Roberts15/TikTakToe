from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi​

speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus​
count=0 #aizpildīto rūtiņu skaits
winner=False

def btnClick(button): #padod pogu​
    global speletajsX,count #kādi mainīgie tiks izmantoti​
    if button["text"]==" "and speletajsX==True:#spēlē X spēlētājs​
        button["text"]="X"#maina uz X​
        speletajsX=False
        count+=1 # palielina rūtiņu skaitu​
    elif button["text"]==" " and speletajsX==False: # mainās spēlētāji​
        button["text"]="0"
        speletajsX=True
        count+=1
    else:       
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")
    return 0
def checkWinner():
    global winner 
    if (btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or
     btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or 
     btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X"or

     btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X"or
     btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X"or
     btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X"or
     
     btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X"or
     btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs X ir uzvarētājs")
    elif (btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O" or
     btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O" or 
     btn3["text"]=="O"and btn6["text"]=="O" and btn9["text"]=="O"or
     btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O"or
     btn4["text"]=="O"and btn5["text"]=="O" and btn6["text"]=="O"or
     btn7["text"]=="O"and btn8["text"]=="O" and btn9["text"]=="O"or    
     btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O"or
     btn3["text"]=="O"and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs O ir uzvarētājs")
    elif count==9 and winner==False:        
        messagebox.showinfo("TicTacToe", "Neizšķirts")
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

mansLogs=Tk()
mansLogs.title("TicTacToe")
btn1=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick())
btn2=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(2))
btn3=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(3))
btn4=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(4))
btn5=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(5))
btn6=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(6))
btn7=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(7))
btn8=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(8))
btn9=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=btnClick(9))

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)
mansLogs.mainloop()

speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus​
count=0 #aizpildīto rūtiņu skaits
