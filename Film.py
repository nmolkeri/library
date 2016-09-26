from Media import Media

class Film(Media):
    
    def __init__(self,callNumber, title, subjects, notes, director , year):
        Media.__init__(self,callNumber, title, subjects, notes)
        self.director = director
        self.year = year
    
    def display(self):
        print ("Call Number: %s " % self.callNumber)
        print ("Title : %s " % self.title)
        print ("Subjects : %s " % self.subjects)
        print ("Year : %s " % self.year)
        print ("Director : %s " % self.director)
        print ("Notes : %s " % self.notes)
    
    def searchByCallNumber(self, word):
        if word in self.callNumber:
            return True


    def searchByTitle(self, word):
        if word in self.title:
            return True

    def searchBySubjects(self, word):
        if word in self.subjects:
            return True


    def searchByOthers(self, word):
        x = 0
        if word in self.year:
            x += 1
        if word in self.director:
            x += 1
        if word in self.notes:
            x += 1
        if x > 0:
            return True
