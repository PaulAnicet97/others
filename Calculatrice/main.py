from tkinter import *
from tkinter import ttk

color1 = "#1e1f1e" #black
color2 = "#feffff" #white
color3 = "#229ac9" #blue
color4 = "#ECEFF1" #gray
color5 = "#FFAB40" #Orange


window = Tk()
window.title("Calculator")

window.geometry("235x310") # config main window
window.config(bg=color1)
#frames
frame_screen = Frame(window, width = 235 , height=50, bg = color3) # create the display
frame_screen.grid(row=0, column= 0)

frame_command = Frame(window, width = 235 , height = 268) # create the command 
frame_command.grid(row=1, column= 0)

#logic
all_value = ''
def enter_value(event):
    global all_value
    all_value = all_value + str(event)

    text_valor.set(all_value)

text_valor = StringVar()

def calculate():
    global all_value
    result = eval(all_value)
    text_valor.set(str(result))
    all_value = str(result)
    

def delete_display():
    global all_value
    all_value = ""
    text_valor.set("")
    






#Label
app_label = Label(frame_screen, textvariable = text_valor, width= 16 , height= 2, padx=7, relief= FLAT, anchor="e", justify= RIGHT, font=('Ivy 18'), bg = color3, fg = color2 )
app_label.place(x=0, y = 0)





#buttom
b_1 = Button(frame_command, command= delete_display, text = "C", width= 11, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_1.place(x=0, y=0)
b_2 = Button(frame_command, command= lambda: enter_value("%"),  text = "%", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_2.place(x=118, y=0)
b_3 = Button(frame_command, command= lambda: enter_value("/"),text = "/", width= 5, height= 2, bg = color5, fg = color2, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_3.place(x=177, y=0)

b_4 = Button(frame_command, command= lambda: enter_value("7"),text = "7", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_4.place(x=0, y=52)
b_5 = Button(frame_command,command= lambda: enter_value("8"), text = "8", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_5.place(x=59, y=52)
b_6 = Button(frame_command, command= lambda: enter_value("9"),text = "9", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_6.place(x=118, y=52)
b_7 = Button(frame_command, command= lambda: enter_value("*"),text = "*", width= 5, height= 2, bg = color5, fg = color2, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_7.place(x=177, y=52)

b_8 = Button(frame_command, command= lambda: enter_value("4"),text = "4", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_8.place(x=0, y=104)
b_9 = Button(frame_command,command= lambda: enter_value("5"),text = "5", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_9.place(x=59, y=104)
b_10 = Button(frame_command,command= lambda: enter_value("6"), text = "6", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_10.place(x=118, y=104)
b_11 = Button(frame_command, command= lambda: enter_value("-"),text = "-", width= 5, height= 2, bg = color5, fg = color2, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_11.place(x=177, y=104)

b_12 = Button(frame_command,command= lambda: enter_value("1"), text = "1", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_12.place(x=0, y=156)
b_13 = Button(frame_command, command= lambda: enter_value("2"),text = "2", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_13.place(x=59, y=156)
b_14 = Button(frame_command, command= lambda: enter_value("3"),text = "3", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_14.place(x=118, y=156)
b_15 = Button(frame_command, command= lambda: enter_value("+"),text = "+", width= 5, height= 2, bg = color5, fg = color2, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_15.place(x=177, y=156)

b_16 = Button(frame_command, command= lambda: enter_value("0"),text = "0", width= 11, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_16.place(x=0, y=208)
b_17 = Button(frame_command,command= lambda: enter_value("."), text = ".", width= 5, height= 2, bg = color4, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_17.place(x=118, y=208)
b_18 = Button(frame_command,command= calculate , text = "=", width= 5, height= 2, bg = color5, fg = color2, font = ("Ivy 13 bold"), relief = RAISED, overrelief= RIDGE )
b_18.place(x=177, y=208)





window.mainloop()

