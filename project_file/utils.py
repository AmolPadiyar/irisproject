import pickle
import numpy as np
import pandas as pd
import config


class IrisClass():
    def __init__(self,SepalLength,SepalWidth,PetalLength,PetalWidth):
        self.SepalLength = SepalLength
        self.SepalWidth = SepalWidth
        self.PetalLength = PetalLength
        self.PetalWidth = PetalWidth

    def load_model(self):
        with open(config.model_path,"rb") as m:
            self.logistic_model=pickle.load(m)

    def get_prediction(self):
        self.load_model()

        test_array = np.array([[self.SepalLength,self.SepalWidth,self.PetalLength,self.PetalWidth]])

        return self.logistic_model.predict(test_array)[0]