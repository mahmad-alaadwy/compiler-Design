import os;
#finding the words
def loopLineContent(line):
    words=[]
    word=[]
    for i in range(len(line)-1):
        #checking if end of line 
        if(line[i]==';'):
            break

        #checking if comments 
        if(line[i]=='/'and line[i+1]=='/'):
            break
        
        #checking if whight space 
        if(line[i]==' '):
            continue

        #checking operators
        if(line[i]=='+' or line[i]=='-'or line[i]=='*'or line[i]=='/'or line[i]=='='):
            words.append(line[i])
            continue

        #checking if character follwed by operator
        if(line[i]!=' ' and (line[i+1]=='+' or line[i+1]=='-'or line[i+1]=='*'or line[i+1]=='/'or line[i+1]=='=')):
            word.append(line[i])
            realWord=''.join(word)   
            words.append(realWord)
            word=[]
            continue
        
        #checking if character and not end of word adding it to the word 
        if(line[i]!=' ' and line[i+1]!=' '):
            word.append(line[i])
            continue

        #checking if character and  end of word then adding the word to words and make word=null 
        if(line[i]!=' ' and line[i+1]==' '):
            word.append(line[i])
            realWord=''.join(word)   
            words.append(realWord)
            word=[]
            continue
    return words
            
#this function returns the file lines as lists of words for each line
def fileWords(path):
    file1 = open(path,'r')
    fileContent=file1.readlines()
    fileWords=[]
    for line in fileContent:
        lineWords=loopLineContent(line)
        fileWords.append(lineWords)
    return fileWords

TheFoundedWords=fileWords("first.txt")

def writingWordsToTextFile(TheFoundedWords):
    try:
        for LW in TheFoundedWords:
            for w in LW:
                with open('words.txt', 'a') as f:
                    f.write(w+'\n')

    except FileNotFoundError:
        print("The 'docs' directory does not exist")
        
writingWordsToTextFile(TheFoundedWords)