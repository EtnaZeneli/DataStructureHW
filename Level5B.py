def search(datain):

    d= open ("wordlist.txt", "r")
    words= d.readline().split(",")

    index=0

    for word in words:
        
        print(word)
        if datain==(word.strip().strip()):
            return index
        else:
            index+=1
def main():

    user= input("Type a word from the word list: ")
    print(search(user))

main()


    
