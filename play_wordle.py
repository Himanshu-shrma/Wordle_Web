import random
from wordle import Wordle
from colorama import Fore,init

init(convert=True)

def main():

    word_set=load_word_set("5letter_words.txt")
    print("\n\t\tWordle")
    wordle=Wordle(random.choice(list(word_set)))

    while(wordle.can_attempt):
        
        entered_word=input("\nEnter Your Guess : ").upper() 
        if len(entered_word)!=wordle.MAX_LENGTH:
            print(Fore.RED+ f"\n\t\tWord must be {wordle.MAX_LENGTH} characters long! Please Try Again"+Fore.RESET)
            continue
        if entered_word not in word_set:
            print(Fore.RED+ f"\n\t\tEntered Word doesn't Exists! Please Try Again"+Fore.RESET)
            continue
        wordle.add_word(entered_word)
        display_wordle(wordle)

    if wordle.is_solved:
        print("\n\t\tHurray!! You Guessed the Word !!")
    else:
        print(Fore.RED+"\n\t\tYou Failed to Guess the word !!\n"+ Fore.RESET)
    print("\n\t\tCorrect Word is ", Fore.GREEN+wordle.secret+Fore.RESET)

def load_word_set(path: str):
    word_set=set()
    with open(path,'r') as f:
        for word in f.readlines():
            word_set.add(word.strip().upper())
    return word_set

def display_wordle(wordle:Wordle):
    print("\nYour Wordle so far . . ")
    print(f"\n\t\tYou have {wordle.MAX_ATTEMPT-len(wordle.words)} attempts Remaining\n")
    lines=[]
    for word in wordle.words:
        word_result=wordle.check_guessed_word(word)
        colored_word_str=colored_word(word_result)
        lines.append(colored_word_str)
    for _ in range(wordle.MAX_ATTEMPT-len(wordle.words)):
        lines.append(" ".join(["_"]*wordle.MAX_LENGTH))
    drawing_box(lines,9,2)


def colored_word(array:list):
    list_colored_letter=[]
    for letter in array:
        if letter[1]=='T':
            color=Fore.GREEN
        elif letter[2]=='T':
            color=Fore.YELLOW
        else:
            color=Fore.WHITE
        colored_letter=color+letter[0]+Fore.RESET
        list_colored_letter.append(colored_letter)
    return " ".join(list_colored_letter)

def drawing_box(lines,length,padding):
    total=length+(padding*2)
    top_border="┌"+"─"*total+"┐"
    
    bottom_border="└"+"─"*total+"┘"
    print(top_border)
    for it in lines:
        print("│  "+ it + "  │")
    print(bottom_border)


if __name__=="__main__":
    main()