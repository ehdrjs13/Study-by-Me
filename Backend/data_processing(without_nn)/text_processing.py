class text_processing:
  def __init__(self) -> None:
    #국어, 영어, 수학, 과학탐구, 사회탐구
    self.keyword_list = [
        [],
        [],
        ['수학','미분','적분','수열','함수'],
        ['물리','화학','생명과학','지구과학','운동량','충격량','에너지','양적','유전'],
        ['경제', '윤리','문화']]
    return

  '''tokenize sentences'''
  @staticmethod
  def tokenize(sentence:str) -> list:
    from konlpy.tag import Okt
    okt = Okt()
    morphs = okt.morphs(sentence)
    
    return morphs
  
  '''return subject index'''
  def find_sunject(self,morphs:list) -> int:
    subject_keyword = self.keyword_list

    for i in range(len(subject_keyword)):
      for j in morphs:
        if j in subject_keyword[i]:
          return i
        else:
          return 5
        
#국,영,수,과,사,OOV