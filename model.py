# encoding : utf8
"""Model: this part manages the data of the application."""

from Animal import Animal

class Model():
    """class of the model"""
    def __init__(self, filename):
        """initializes a file object in read and write mode using the given filename.
        It also initializes an empty dictionary dico_animaux."""
        self.filename = filename
        self.file=open(self.filename, "r+", encoding="utf8") #open the file in read+write
        self.dico_animaux = {}
        self.only_names = []

    def read_file(self):
        """Reads the file line by line and creates an Animal object for each line.
        It then adds the object to the dictionary dico_animaux with the animal name as key."""
        for line in self.file:
            line = line.strip() #remove line breaks
            tab = line.split(",") #separate line from ","
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a #key = animal's name, value = all the attributs
            self.only_names.append(a.name) #list containing only the names of the animals
            self.only_names.sort()

    def save(self, dict_animal):
        """writes a new line to the file using the values in the dictionary"""
        self.file.write("\n"+dict_animal["species"]+","+
        dict_animal["age"]+","+dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"])

    def delete(self, del_animal):
        """Methode to delete a selected animal, both in the "dico_animaux" dictionary
        and in the file. it takes as input the name of the animal to delete."""
        del self.dico_animaux[del_animal] #delete from the dico
        #delete from the file
        self.file.seek(0) #position the cursor on the beginning of the file
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate() #clear the file of it's content
        for line in lines:
            line_split=line.strip("\n").split(",") #recovery of the animal's name
            if line_split[-1] != del_animal:
                #write the name of the animal if it is different from del_animal
                self.file.write(line)

    def modify(self, dict_animal):
        """Modify an animal.
        It uses the "delete" function, in order to delete the name
        and the attributes of the animal to be modified,
        and the "save" functon, in order to save the modifications on the file."""
        self.delete(dict_animal["name"])
        self.save(dict_animal)

    def close(self):
        """closes the file object"""
        self.file.close()

    def get_attributes(self):
        """Retrieve the attributes of an animal"""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def info_animal(self,name):
        """This method retrieve the attributes of the animals.
        it will be used in case the user wants to modify an animal.
        It allows to display in the input fields the information about the selected animal."""
        self.file.seek(0)
        for line in self.file:
            if name in line:
                line = line.strip("\n").split(",")
                return line

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
