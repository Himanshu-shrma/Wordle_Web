class Wordle:
    
    MAX_LENGTH=5
    MAX_ATTEMPT=6

    def __init__(self,secret:str):
        self.secret:str=secret
        self.words=[]
        pass

    def add_word(self,word:str):
        word=word.upper()
        self.words.append(word)

    def check_guessed_word(self,word:str):
        
        result=[]
        for i in range(self.MAX_LENGTH):
            temp=word[i]
            if word[i]==self.secret[i]:
                temp+='T'
            else:
                temp+='F'
            
            if word[i] in self.secret:
                temp+='T '
            else:
                temp+='F'

            result.append(temp)
            
        return result

    @property
    def is_solved(self):
        return len(self.words) and  self.words[-1]==self.secret

    @property
    def can_attempt(self):
        return len(self.words) < self.MAX_ATTEMPT and not self.is_solved

    