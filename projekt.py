from tkinter import *
root=Tk()
root.geometry("500x300")

def getvals():
    print("Accepteret")


# Titel

Label(root, text="Registrerings Panel", font="ar 15 bold").grid(row=0, column=3)

# Navnefelter

navn = Label(root, text="Navn")
tlf = Label(root, text="Tlf Nr")
køn = Label(root, text="Køn")
land = Label(root, text="Land")
by = Label(root, text="By")

#Pakkede felter

navn.grid(row=1, column=2)
tlf.grid(row=2, column=2)
køn.grid(row=3, column=2)
land.grid(row=4, column=2)
by.grid(row=5, column=2)

#Variabler for opbevaring af data

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
countryvalue = StringVar
cityvalue = StringVar
checkvalue = IntVar

#Entry Felt

nameentry =Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
countryentry = Entry(root, textvariable =countryvalue)
cityentry = Entry(root, textvariable =cityvalue)

#Pakkede entry felter

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
countryentry.grid(row=4, column=3)
cityentry.grid(row=5, column=3)

#Checkbox (Husk mig knap)

checkbtn = Checkbutton(text="Husk mig?", variable = checkvalue)
checkbtn.grid(row=6, column= 3)


#Indsend knap
Button(text="Indsend", command=getvals).grid(row=7, column=3)


root.mainloop()