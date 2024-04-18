from tkinter import *


root = Tk()
root.title("CV Generator")


# Name
label_name = Label(root, text="Name")
label_name.pack()
entry_name = Entry(root)
entry_name.pack()


# Email
label_email = Label(root, text="Name")
label_email.pack()
entry_email = Entry(root)
entry_email.pack()


# Phone Number
label_phone = Label(root, text="Name")
label_phone.pack()
entry_phone = Entry(root)
entry_phone.pack()


# Address
label_address = Label(root, text="Name")
label_address.pack()
entry_address = Entry(root)
entry_address.pack()


# Website
label_website = Label(root, text="Name")
label_website.pack()
entry_website = Entry(root)
entry_website.pack()


# Skills
label_skills = Label(root, text="Skills (Enter one skill per line)")
label_skills.pack()
entry_skills = Text(root, height=5)
entry_skills.pack()


# Education
label_education = Label(root, text="Education (Enter one per line in format 'Degree, School, Year')")
label_education.pack()
entry_education = Text(root, height=5)
entry_education.pack()


# Work Experience
label_experience = Label(root, text="Experience (Enter one per line in format 'Job Title, Company, Year')")
label_experience.pack()
entry_experience = Text(root, height=5)
entry_experience.pack()


# About Me
label_about_me = Label(root, text="About Me")
label_about_me.pack()
entry_about_me = Text(root, height=5)
entry_about_me.pack()


# Button to generate CV
button_generate = Button(root, text="Generate CV")
button_generate.pack()


root.mainloop()