from tkinter import *

# Create the main window
window = Tk()
window.title("Grade Calculator")
window.geometry("500x400")

# Function to perform grade calculation
def Calculation():
    # Get input values from entry widgets
    analyse = int(analyseentry.get())
    algebre = int(algebreentry.get())
    statique = int(statiqueentry.get())

    # Calculate total and display it
    total = (analyse + algebre + statique)
    Label(text=total, font="arial 15 bold").place(x=250, y=170)

    # Calculate average and display it
    avr = float(total / 3)
    Label(text=avr, font="arial 15 bold").place(x=250, y=220)

    # Determine grade based on average and display it in blue color
    if avr >= 16:
        grade = "Excellent"
    elif 14 <= avr < 16:
        grade = "Good"
    elif 12 <= avr < 14:
        grade = "Satisfactory"
    elif 10 <= avr < 12:
        grade = "Passable"
    else:
        grade = "Insufficient"

    Label(text=grade, font="arial 15 bold", fg="blue").place(x=250, y=270)

# Labels for subject names and grade details
analyse = Label(window, text="Analysis:", font="arial 10")
algebre = Label(window, text="Algebra:", font="arial 10")
statique = Label(window, text="Statics:", font="arial 10")
total = Label(window, text="Total:", font="arial 10")
avr = Label(window, text="Average:", font="arial 10")
grade = Label(window, text="Grade:", font="arial 10")

# Place labels in window
analyse.place(x=50, y=20)
algebre.place(x=50, y=70)
statique.place(x=50, y=120)
total.place(x=50, y=170)
avr.place(x=50, y=220)
grade.place(x=50, y=270)

# StringVars to store entry values
analysevalue = StringVar()
algebrevalue = StringVar()
statiquevalue = StringVar()

# Entry widgets for input
analyseentry = Entry(window, textvariable=analysevalue, font="arial 10", width=15)
algebreentry = Entry(window, textvariable=algebrevalue, font="arial 10", width=15)
statiqueentry = Entry(window, textvariable=statiquevalue, font="arial 10", width=15)

# Place entry widgets in window
analyseentry.place(x=250, y=20)
algebreentry.place(x=250, y=70)
statiqueentry.place(x=250, y=120)

# Buttons for calculation and exit
Button(text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=320)
Button(text="Exit", font="arial 15", bg="white", bd=10, width=8, command=lambda: exit()).place(x=350, y=320)

# Start the Tkinter event loop
window.mainloop()
