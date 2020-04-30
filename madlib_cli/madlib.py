from textwrap import dedent

#features

Welcome = """
**********************************************************
**   Welcome to the Mid Lib Game!                       **
**   Please see game template below                     **
**   you need to proivde the word for hint given in {}  **
**   When prompted for "Do you want to play again"      **
**   Type  'Y' to continue, 'N' to quit                 **
**********************************************************
"""

def Midlib_parse_fn():
    print (Welcome)
    print ("Here is the Game :")
    #read teamplate file - i have three templates, can run game with any!!

    #template1 : {exclamation} he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife.
    #Sample Answer : Ouch! he said stupidly as he jumped into his convertible car and drove off with his brave wife.

    #template1 : A {adjective} and {adjective} {Noun}. 
    #Sample Answer : A dark and stromy night.

    #assumption the hintword would be one word with in {}

    with open('files/template1.txt') as file:
        tmp_str = file.read()
        print(tmp_str)

    print ("\n")

    inp_txt =''
    out_txt =''

    #present choices to user
    #get input from user
    #inject user input into template

    for word in tmp_str.split():
        if word.find("{") == 0:
            inp_txt  = input(f"Please input {word} :") 
            out_txt = out_txt +' ' + inp_txt
        else:    
            out_txt =out_txt + ' ' + word
    
    out_txt =(dedent(out_txt)) + '\n'   
    print ("\n Here is your answer:")

    #display to to use
    print (out_txt)    
    #return out_txt    

    #wirte completed mad lib into a file -Append-adds at last on the existing answers
    Ans = open("files/Madlib_Answers.txt","a")#append mode 
    Ans.write(out_txt) 
    Ans.close()     

if __name__ == '__main__':
    
    cont = 'Y' 
    while cont != 'N':
        Midlib_parse_fn()
        cont = input("Do you want to play again Y/N :" )
