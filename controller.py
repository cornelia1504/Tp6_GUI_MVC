# encoding : utf8
"""Controller: this part manages the logic of the code that makes decisions"""

from vue import Application
from model import Model

class Controller() :
    """The Controller class manages the logic of the animal management application"""
    def __init__(self):
        """Creates an instance of the Model and Application class,
         which is responsible for reading and writing data to a file
         and  displaying the user interface
        """
        self.model = Model("a.txt")
        self.model.read_file() #creation of a dictionary that contains the animals of "a.txt"
        #The self argument to establish a reference between the Controller and Application objects
        self.view = Application(self)
        self.view.view_window() #to display the user interface

    def display(self, value): #the string value as an argument represents an animal name
        """Retrieves the corresponding animal information from the Model object's dictionary
        """
        #it passes the information to the display_label method to update the interface
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """passes the dictionary ( dict_animal )to the save method of the Model object"""
        self.model.save(dict_animal)

    def delete_animal(self, del_animal):
        """ to delete a selected animal """
        self.model.delete(del_animal)

    def modify_animal(self,dict_animal):
        """This method linked to the "model" allowing to modify an animal"""
        self.model.modify(dict_animal)

    def get_model_entries(self):
        """returns a list of the attributes (keys) of the dictionaries in the file"""
        return self.model.get_attributes()

    def get_names(self):
        """Method to retrieve only the names of the animals"""
        return self.model.only_names

    def info_animal(self,name):
        """Method linked to the model to retrieve the attributes of the animals"""
        return self.model.info_animal(name)

    def quit_window(self):
        """This method prints "close app" to the console,
        calls the close method of the Model object to close the file,
        and destroys the view object (the GUI window) using the destroy method of the Tk class
        """
        print("close app")
        self.model.close() #close the file
        self.view.destroy() #destruction of the window

if __name__ == "__main__" :
    C = Controller()
    
