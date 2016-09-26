from Media import Media

class Book(Media):

    def __init__(self,callNumber, title, subjects, notes, author, description, publisher, city, year, series):
        Media.__init__(self,callNumber, title, subjects, notes)
        self.author = author
        self.description = description
        self.publisher = publisher
        self.city = city
        self.year = year
        self.series = series

    def display(self):
        print ("Call Number: %s " % self.callNumber)
        print ("Title : %s " % self.title)
        print ("Subjects : %s " % self.subjects)
        print ("Author : %s" % self.author)
        print ("Description : %s " % self.description)
        print ("Publisher : %s " % self.publisher)
        print ("City : %s" % self.city)
        print ("Year : %s " % self.year)
        print ("Series : %s " % self.series)
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
        if word in self.author:
            x += 1
        if word in self.description:
            x += 1
        if word in self.publisher:
            x += 1
        if word in self.city:
            x += 1
        if word in self.year:
            x += 1
        if word in self.series:
            x += 1
        if word in self.notes:
            x += 1
        if x > 0:
            return True




