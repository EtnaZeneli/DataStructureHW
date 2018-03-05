def binarysearch(datain):

    d= open ("wordlist.txt", "r")
    words= d.readline().split(",")
    print(len(words))
    def recursion(first, last):

        middlenum= (first+last)//2
        middleword= (words[middlenum]).lower().strip()
        #print(middleword+ " "+ str(first)+ " "+ str(last)+" "+str(datain > middleword)+" "+str(datain < middleword))
        if first>last:
            return None
        elif datain > middleword:
            return recursion (middlenum + 1, last)
        elif datain < middleword:
            return recursion (first, middlenum -1)
        else:
            return middlenum
    return recursion(0, len(words)-1)
        
def main():

    user= input("Type a word from the word list: ").strip().lower()
    print(binarysearch(user))
main()

