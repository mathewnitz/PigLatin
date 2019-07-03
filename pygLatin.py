def main():
    type = str(input("Is input English or Pig Latin?: "))
    if type.lower() == "english":
        sentence = str(input("English: ")).split()
        for i in sentence:
            print(i[1:] + i[0] + "ay", end = ' ')
    elif type.lower() == "pig latin":
        sentence = str(input("Pig Latin: ")).split()
        for i in sentence:
            print(i[len(i) - 3] + i[0:len(i) - 3], end = ' ')
    else:
        print("Error, the input you typed does not match english or pig latin")
        main()

main()
