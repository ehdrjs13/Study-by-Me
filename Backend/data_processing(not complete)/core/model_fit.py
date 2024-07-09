import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from numpy import dot
from numpy.linalg import norm
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class Model:
    SUBJECT_LABLE = ['국어','영어','수학','과탐','사탐']
    #imbed sample sentenced about subjects. 
    SUBJECT_DATASET = []

    @staticmethod
    def cos_sim(x,y) -> float:

        return dot(x, y)/(norm(x)*norm(y))

    def __init__(self) -> None:
        
        pass

    def get_data(self) -> None:
        
        texts = Model.SUBJECT_DATASET
        labels = Model.SUBJECT_LABLE

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts).toarray()


        encoder = LabelEncoder()
        y = encoder.fit_transform(labels)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        joblib.dump(vectorizer, 'vectorizer.joblib')
        joblib.dump(encoder, 'encoder.joblib')

        return
    
    def train_model(self) -> None:

        model = Sequential()

        model.add(Dense(128, input_shape=(self.X_train.shape[1],), activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(5, activation='softmax') )

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(self.X_train, self.y_train, epochs=200, validation_data=(self.X_test, self.y_test))
        model.save('model.h5')

        return


