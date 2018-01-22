#EtnaZeneli
#Reading Files

def main():
    countF=0

    inputF= input ("Enter a name of a txt file:")
    f= open(inputF)
    for rresht in f:

        print (countF, rresht)
        countF= countF+1
main()

        

    
