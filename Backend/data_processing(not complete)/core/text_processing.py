class Text_processing:
    def __init__(self) -> None:
        from konlpy.tag import Okt
        self.okt = Okt()

        pass

    '''Split a sentence into morphs, deleting stopwords. '''
    def split(self,text: str) -> list:
        morphs = self.okt.morphs(text)

        #Bring Stopwords from external source
        stopwords = []

        text_lists = [word for word in morphs if not word in stopwords]

        return text_lists
    
    



