import random
import sys
from tkinter import *
import tkinter.messagebox as box

# GUI
window = Tk()

window.title("Game Time")

label = Label(window, text="Make a Choice ")
label.pack(padx=10, pady=50)

frame = Frame(window)
frame.pack(padx=100, pady=50)

listbox = Listbox(frame)

listbox.insert(1, 'Rock')
listbox.insert(2, 'Paper')
listbox.insert(3, 'Scissors')

win = 0
lose = 0





def print1():

    b3.configure(state=DISABLED)
    b1.configure(state=NORMAL)
    box.showinfo("GAME", "Lets Start")
    file = open("result.txt", "w")
    file.write("");
    file.close()

def game():
    b2.configure(state=NORMAL)
    box.showinfo("GAME", "Your Choice" + " " + listbox.get(listbox.curselection()))
    global p_choice


    p_choice = listbox.get(listbox.curselection())










def result():
    cpu_random = ['Rock', 'Paper', 'Scissors']
    secure_random = random.SystemRandom()
    global c_choice
    c_choice = secure_random.choice(cpu_random)
    b2.configure(state=NORMAL)

def compare():

    result()

    global win
    global lose


    file = open("result.txt", "a+")
    #Tie   outcome
    print(p_choice,c_choice)
    if p_choice == c_choice:
        box.showinfo("Result","TIE  .. Computer Chose "+c_choice)
        file.write( "\n" +p_choice +" "+ c_choice +"\n TIE" )
        print("Tie!")


    # Rock outcome

    elif p_choice == "Rock" and c_choice == "Paper":
        box.showinfo("Result", "You Lose! ..   Computer Chose "+c_choice)
        print("You Lose!")
        lose +=1
        file.write("\n" + p_choice + " " + c_choice + "\n You Lose!")

    elif p_choice == "Rock" and c_choice == "Scissors":
        box.showinfo("Result", "You Win!  ..  Computer Chose "+c_choice)
        print("You Win!")
        win += 1
        file.write("\n" + p_choice + " " + c_choice + "\n You Win!")

    # Paper outcome

    elif p_choice == "Paper" and c_choice == "Scissors":
        box.showinfo("Result", "You Lose!  .. Computer chose "+c_choice)
        print("You Lose!")
        lose += 1
        file.write("\n" + p_choice + " " + c_choice + "\n You Lose!")

    elif p_choice == "Paper" and c_choice == "Rock":
        box.showinfo("Result", "You Win!  .. Computer Chose "+c_choice )
        print("You Win!")
        win += 1
        file.write("\n" + p_choice + " " + c_choice + "\n You Win!")


    # Scissors outcome

    elif p_choice == "Scissors" and c_choice == "Rock":
        box.showinfo("Result", "You Lose! .. Computer Chose "+c_choice)
        print("You Lose!")
        lose += 1
        file.write("\n" + p_choice + " " + c_choice + "\n You Lose!")

    elif p_choice == "Scissors" and c_choice == "Paper":
        box.showinfo("Result", "You Win! .. Computer Chose "+c_choice)
        print("You Win!")
        win += 1
        file.write("\n" + p_choice + " " + c_choice + "\n You Win!")



    file.close()
    b2.configure(state=DISABLED)
    print(win)
    print(lose)
    label12['text'] = win
    label13['text'] = lose


listbox.pack()
b3 = Button(text="Start Game",fg='green' ,command=print1)
b3.pack(padx=10,pady=10, side=LEFT)

b1 = Button(text="Confirm" ,state=DISABLED,fg='red', command=game)
b1.pack(padx=30, pady=10, side=LEFT)

b2 = Button(text="Result",state= DISABLED,fg='blue' ,command=compare)
b2.pack(padx=10, pady=10, side=LEFT)



label1 = Label(frame,text="You :")
label1.pack(padx=10,pady=10,side=LEFT)
label12 =Label(frame,text="0")
label12.pack(padx=10,pady=10,side=LEFT)

label4 = Label(frame,text="Com   : ")
label4.pack(padx=10,pady=10,side=LEFT)

label13 =Label(frame,text="0")
label13.pack(padx=10,pady=10,side=LEFT)


window.mainloop()

