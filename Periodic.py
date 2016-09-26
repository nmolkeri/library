from Media import Media

class Periodic(Media):
    
    def __init__(self,callNumber, title, subjects, notes, author, description, publisher, publishingHistory, series, relatedTitles, otherFormsOfTitle, govDocNum):
        Media.__init__(self,callNumber, title, subjects, notes)
        self.author = author
        self.description = description
        self.publisher = publisher
        self.publishingHistory = publishingHistory
        self.series = series
        self.relatedTitles = relatedTitles
        self.otherFormsOfTitle = otherFormsOfTitle
        self.govDocNum = govDocNum
    
    def display(self):
        print ("Call Number: %s " % self.callNumber)
        print ("Title : %s " % self.title)
        print ("Subjects : %s " % self.subjects)
        print ("Notes : %s " % self.notes)
        print ("Author : %s" % self.author)
        print ("Description : %s " % self.description)
        print ("Publisher : %s " % self.publisher)
        print ("Publishing history : %s " % self.publishingHistory)
        print ("Series : %s " % self.series)
        print ("Related titles : %s " % self.relatedTitles)
        print ("Other forms of Title : %s " % self.otherFormsOfTitle)
        print ("Governement Doc Number : %s " % self.govDocNum)


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
        if word in self.author:
            x += 1
        if word in self.description:
            x += 1
        if word in self.publisher:
            x += 1
        if word in self.publishingHistory:
            x += 1
        if word in self.series:
            x += 1
        if word in self.notes:
            x += 1
        if word in self.relatedTitles:
            x += 1
        if word in self.otherFormsOfTitle:
            x += 1
        if word in self.govDocNum:
            x+=1
        if x > 0:
            return True




