# encoding : utf8
"""View: this part focuses on the display."""
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Listbox
from tkinter import Tk
from tkinter import END

from tkinter import messagebox

class Application(Tk):
    """Class of the interface"""
    def __init__(self, controller):
        """The Application class has a constructor "init" which takes a
        "controller" object as an argument"""
        Tk.__init__(self)
        self.controller = controller
        #gets the model entries from the controller object using the method
        self.attributes = self.controller.get_model_entries()
        self.names = self.controller.get_names() #recovers only the names of the animals
        self.creer_widgets()

    def creer_widgets(self):
        """Creates the widgets for the GUI interface.
        It creates several labels, buttons, and entries using
        the tkinter widgets Label, Button, and Entry.
        The method also creates a dictionary of entries with the keys taken from the attributes.
        """
        self.label = Label(self, text="Animal list manipulation!", font='Arial 20 bold')
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Research")
        #all buttons
        self.bouton_display = Button(self, text="Display", command=self.display_something)
        self.bouton = Button(self, text="Quit", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add/Save modification",
                                        command=self.add_modif_animal)
        self.button_del = Button(self, text="Delete", command=self.delete_animal)
        self.button_modify = Button(self, text="Modify", command=self.info_animal)
        #creates a dictionary of entries with the keys taken from the attributes
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        #create entries corresponding of number and name of attributes
        for att in self.attributes:
            #Loop displaying a label and an entry for each attribute
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        #create listbox
        self.listebox = Listbox(self)
        counter = 0
        for names in self.names: # for each animal we take the name
            counter += 1
            self.listebox.insert(counter, names) # add the name at the new position

        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        self.listebox.pack()
        self.button_del.pack()
        self.button_modify.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.bouton.pack()

    def quit_window(self):
        """Method to exit the window via the Controler script.
        It is linked to the "quitter" button."""
        self.controller.quit_window()

    def display_something(self):
        """The method is called when the user clicks the Quit button"""
        self.controller.display(self.search.get())

    def display_label(self, value):
        """Function to display the animal and its attributes that the user has searched for."""
        self.label1['text'] = value

    def add_modif_animal(self):
        """Method to add or modify an animal."""
        dict_animal = {} #dictionary containing the animals with their attributes
        for key in self.entries:
            dict_animal[key] = self.entries[key].get() #saves the elements entered in dict_animal
        if dict_animal["name"] in self.names:
            #if the name of the animal is already present, it adds that the modifications
            self.controller.modify_animal(dict_animal)
            messagebox.showinfo(title="Modified", message="The animal has been modified")
        if dict_animal["name"] not in self.names:
            #if the name of the animal is not present, it adds the new animal and its attributes
            self.controller.add_animal(dict_animal)
            self.listebox.insert(END, dict_animal["name"])
            messagebox.showinfo(title ="Added", message ="The animal has been added")
        for key in self.entries: #empty the fields
            self.entries[key].delete(0, END)

    def delete_animal(self):
        """Method to delete an animal."""
        deletion = self.listebox.get(self.listebox.curselection())#retrieves the animal selected
        self.controller.delete_animal(deletion)#removes the animal
        for i in range(self.listebox.size()):
            #allows you to remove the animal from the listbox
            if self.listebox.get(i) == deletion :
                self.listebox.delete(i)
        messagebox.showinfo(title = "Deleted", message ="The animal has been deleted")

    def info_animal(self):
        """Method to have the attributes of the animals in order to display
        them on the input fields when the user wants to modify them"""
        for key in self.entries:
            self.entries[key].delete(0, END) #empty the fields
        modification = self.listebox.get(self.listebox.curselection())
        info = self.controller.info_animal(modification)
        nb_entries = len(self.attributes)
        for i in range(0,nb_entries):
            #inserts the attributes of the animal on the corresponding input fields
            self.entries[self.attributes[i]].insert(0,info[i])
        messagebox.showinfo(title = "Modification",
                            message ="modify the characteristics of the animal then press the Add/Save modification button")

    def view_window(self):
        """The "view_window" method sets the title of the GUI window and
        starts the main loop of the Tk object using "mainloop()" to display the window"""
        self.title("My first App :-)")
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.view_window()
