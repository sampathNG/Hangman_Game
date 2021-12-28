import random
f=open("words.txt","rt")
wordsList=list(map(str,f.read().strip().split()))

def Words(level):
    while 1:
            
        if level=='Easy':
            word= random.choice(wordsList)
            if len(word)<6:
                return word 
        elif level=='Midium':
            word= random.choice(wordsList)
            if len(word)<10:
                return word 
        elif level=='Hard' :
            word= random.choice(wordsList)
            if len(word)>=10:
                return word 