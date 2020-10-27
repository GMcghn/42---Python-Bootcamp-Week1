# Forbidden functions : while
# Remarks : use zip & enumerate

class Evaluator:
    

    def __init__(self, coefs, words):
        self.coefs = coefs
        self.words = words
    
    def zip_evaluate(self):
        import sys
        if len(self.words) != len(self.coefs):
            print(-1)
            sys.exit(1)

        list_len_words = [len(word) for word in self.words]
        new_list = [x*y for x, y in zip(list_len_words, self.coefs)]
        
        aggreg = 0
        for x in new_list:
            aggreg += x
        
        return(aggreg)

    def enumerate_evaluate(self):
        import sys
        if len(self.words) != len(self.coefs):
            print(-1)
            sys.exit(1)
        
        list_len_words = [len(word) for word in self.words]
        x = list(enumerate(list_len_words))
        y = list(enumerate(self.coefs))

        aggreg = 0
        for i in range(len(x)):
            aggreg += (x[i][1]*y[i][1])
        
        return(aggreg)


    # def zip_evaluate(self, coefs, words):
    #     import sys
    #     if len(words) != len(coefs):
    #         print(-1)
    #         sys.exit(1)

    #     list_len_words = [len(word) for word in words]
    #     new_list = [x*y for x, y in zip(list_len_words, coefs)]
    #     aggreg = 0
    #     for x in new_list:
    #         aggreg += x
        
    #     print(aggreg)
    

        


    