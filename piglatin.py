def latin():
    print ("Pig Latin")
    input = raw_input("Please Enter a word: ")
    Pig = ("ay")
    while True:
        if input.isalpha():
            pigword= input.lower()
            firstindex= pigword[0]
            final= pigword[1:] + firstindex + Pig
            print final
            break

        if not input.isalpha():
            print ("Please Enter a Word!!!")
            return latin()
            continue

latin()
