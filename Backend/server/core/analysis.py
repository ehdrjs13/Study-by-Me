class Analyze:
    def analyze(self,text):
        import joblib
        import tensorflow as tf

        vectorizer = joblib.load('vectorizer.joblib')
        encoder = joblib.load('encoder.joblib')

        model = joblib.load('model.h5')

        new_text = vectorizer.transform(text).toarray()

        prediction = model.predict(new_text)

        predicted = encoder.inverse_transform(prediction.argmax(axis = 1))

        return predicted