import random
from image import Show_Image
from words_hangman import Words
           

def hint(hin,characters):
    if hin>0:
        print('\n\nyour hint is to enter ',end='')
        print(random.choice(characters),' as input for choice\n')
    else:
        print('\nyou do not have any hint\n')        
    

if __name__=="__main__":
    
    print('\t\t ______WELCOME TO THE HANGMAN GAME_______ ')
    while 1:
        while 1:
            print('\n\nChoose your level-\n1)Easy \n2)Midium \n3)Hard')
            choice=int(input())
            if choice==1:
                word=list(Words('Easy'))
                break
            elif choice==2:
                word=list(Words('Midium'))
                break
            elif choice==3:
                word=list(Words('Hard'))
                break
            else:
                print('\tInvalid choice\nChoose again')
        
        c=[]
        characters=list(dict.fromkeys(word))
        print(characters)
        for i in range(len(word)):
            c.append('_')

        s='abcdefghijklmnopqrstuvwxyz'
        chance=0
        hin=2
            

        while word!=c:
            while 1:   
                print('you have to guss a word which is of',len(word),'letters and you have', (6-chance),'chances\nyou can also enter 0 for hint\n')
                print('WORD IS :',end='')
                
                for x in c:
                    print(x,end=' ')

                
                print('\nAVAILABLE LETTERS-',s)
                ch=input('\nEnter your letter\t')

                if ch=='0':
                    hint(hin,characters)
                    hin-=1
                elif ch in s:
                    break
                else:
                    chance+=1
                    print('wrong input\n',Show_Image(chance),'\n\nEnter again\n')
                    if chance==6:
                        break
            if chance==6:
                break        
                    
      

            if ch in word:
                a=0
                for i in word:
                    if ch==i:
                        c[a]=ch
                    a+=1    
                print('Good guess\n',Show_Image(chance-1))
                characters.remove(ch) 
            else:
                if chance<6:
                    print('wrong guss\n',Show_Image(chance))
                    chance+=1
                else:
                    break
            s=s[:(s.index(ch))]+s[(s.index(ch)+1):]        

        if chance==6:
            print('you lost, the word is',word,'and got hanged\n',Show_Image(-2))
        else:
            print("********congrates you won********\n")
        num=int(input('\t\t\tIf you want to try again press 9\n'))
        if num!=9:
            print('THANKYOU!!! FOR PLAYING')
            break        
