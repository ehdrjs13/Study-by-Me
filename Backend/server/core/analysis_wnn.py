class Analysis:
    def __init__(self) -> None:
        from core.text_processing import Text_processing

        self.processing = Text_processing()

        self.ans = {0:'국어',
                    1:'영어',
                    2:'수학',
                    3:'사회탐구',
                    4:'과학탐구',
                    5:'기타'}
        pass

    def classify(self,sentence):
        morph = self.processing.tokenize(sentence)
        res = self.processing.find_sunject(morph)

        return self.ans[res]
    



        

        
        