def main():
    input_file_path="all_words.txt"
    output_file_path="5letter_words.txt"
    five_letter_word=[]
    with open(input_file_path,'r') as f:
        for line in f.readlines():
            word=line.strip()
            if len(word)==5:
                five_letter_word.append(word)
    
    with open(output_file_path,'w') as f:
        for word in five_letter_word:
            f.write(word+'\n')
    
    print(f"i found {len(five_letter_word)} words \n")

if __name__=='__main__':
    main()