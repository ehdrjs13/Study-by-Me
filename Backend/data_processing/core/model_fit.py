class Model:
    SUBJECT_LABLE = ['국어','영어','수학','과탐','사탐']

    @staticmethod
    def cos_sim(x,y):
        from numpy import dot
        from numpy.linalg import norm

        return dot(x, y)/(norm(x)*norm(y))

    def __init__(self) -> None:
        import numpy as np



        pass


