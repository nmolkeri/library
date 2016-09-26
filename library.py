from Search import Search

print ("1) Call Number")
print ("2) Title")
print ("3) Subjects")
print ("4) Other")
print ("5) Exit")


inp = input()
print (inp)
while(inp != '5'):
    if(inp == '1'):
        print ("Search by Call number")
        keyWord = input( 'Enter the keyword to be searched: ')
        x = Search()
        returnWords = x.searchCallNumber(keyWord)
        
        for i in range(0, len(returnWords)):
            returnWords[i].display()


    if(inp == '2'):
        print ("Search by Title")
        keyWord = input( 'Enter the keyword to be searched: ')
        x = Search()
        returnWords = x.searchTitle(keyWord)
        
        for i in range(0, len(returnWords)):
            returnWords[i].display()


    if(inp == '3'):
        print ("Search by Subjects")
        keyWord = input( 'Enter the keyword to be searched: ')
        x = Search()
        returnWords = x.searchSubjects(keyWord)
        
        for i in range(0, len(returnWords)):
            returnWords[i].display()


    if(inp == '4'):
        print ("Search by others")
        keyWord = input( 'Enter the keyword to be searched: ')
        x = Search()
        returnWords = x.searchOthers(keyWord)
        
        for i in range(0, len(returnWords)):
            returnWords[i].display()
    print ("1) Call Number")
    print ("2) Title")
    print ("3) Subjects")
    print ("4) Other")
    print ("5) Exit")
    inp = input()

