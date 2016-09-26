from Media import Media
from Book import Book
from Film import Film
from Video import Video
from Periodic import Periodic

class Search:
    def __init__(self):
        self.read()


    def read(self):
        self.readBook()
        self.readFilm()
        self.readVideo()
        self.readPeriodic()

    def readBook(self):
        f = open('data/book.txt')
        line = f.readline()
        self.stack = []
        while line:
            x = line.split('|')
            callNumber = x[0]
            title = x[1]
            subjects = x[2]
            author = x[3]
            description = x[4]
            publisher = x[5]
            city = x[6]
            year = x[7]
            series = x[8]
            notes = x[9]
            
            b = Book(callNumber, title, subjects, notes, author, description, publisher, city, year, series)
            self.stack.append(b)
            line = f.readline()


    def readFilm(self):
        f = open('data/film.txt')
        line = f.readline()
        while line:
            #print line
            x = line.split('|')
            callNumber = x[0]
            title = x[1]
            subjects = x[2]
            director = x[3]
            notes = x[4]
            year = x[5]
            
            fi = Film(callNumber, title, subjects, notes, director , year)
            self.stack.append(fi)
            line = f.readline()

    def readVideo(self):
        f = open('data/video.txt')
        line = f.readline()
        while line:
            #print line
            x = line.split('|')
            callNumber = x[0]
            title = x[1]
            subjects = x[2]
            description = x[3]
            distributor = x[4]
            notes = x[5]
            series = x[6]
            label = x[7]

            v = Video(callNumber, title, subjects, notes, description, distributor, series, label)
            self.stack.append(v)
            line = f.readline()

    def readPeriodic(self):
        f = open('data/periodic.txt')
        line = f.readline()
        while line:
            #print line
            x = line.split('|')
            callNumber = x[0]
            title = x[1]
            subjects = x[2]
            author = x[3]
            description = x[4]
            publisher = x[5]
            publishingHistory = x[6]
            series = x[7]
            notes = x[8]
            relatedTitles = x[9]
            otherFormsOfTitle = x[10]
            govDocNum = x[11]
            
            p = Periodic(callNumber, title, subjects, notes, author, description, publisher, publishingHistory, series, relatedTitles, otherFormsOfTitle, govDocNum)
            self.stack.append(p)
            line = f.readline()

    def searchCallNumber(self, word):
        results = []
        for i in range(0,len(self.stack)):
            x = self.stack[i]
            xx = x.searchByCallNumber(word)
            if xx == True:
                #print "True"
                results.append(self.stack[i])
        return results

    def searchTitle(self, word):
        results = []
        for i in range(0,len(self.stack)):
            x = self.stack[i]
            xx = x.searchByTitle(word)
            if xx == True:
                #print "True"
                results.append(self.stack[i])
        return results

    def searchSubjects(self, word):
        results = []
        for i in range(0,len(self.stack)):
            x = self.stack[i]
            xx = x.searchBySubjects(word)
            if xx == True:
                #print "True"
                results.append(self.stack[i])
        return results


    def searchOthers(self, word):
        results = []
        for i in range(0,len(self.stack)):
            x = self.stack[i]
            xx = x.searchByOthers(word)
            if xx == True:
                #print "True"
                results.append(self.stack[i])
        return results

