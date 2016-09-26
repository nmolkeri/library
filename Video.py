from Media import Media

class Video(Media):
    
    def __init__(self,callNumber, title, subjects, notes, description, distributor, series, label):
        Media.__init__(self,callNumber, title, subjects, notes)
        self.description = description
        self.distributor = distributor
        self.series = series
        self.label = label
    
    def display(self):
        print ("Call Number: %s " % self.callNumber)
        print ("Title : %s " % self.title)
        print ("Subjects : %s " % self.subjects)
        print ("Distributor : %s" % self.distributor)
        print ("Description : %s " % self.description)
        print ("Series : %s " % self.series)
        print ("Notes : %s " % self.notes)
        print ("Label: %s " % self.label)
    
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
        if word in self.description:
            x += 1
        if word in self.distributor:
            x += 1
        if word in self.series:
            x += 1
        if word in self.notes:
            x += 1
        if word in self.label:
            x += 1
        if x > 0:
            return True




