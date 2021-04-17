import numpy as np
import pandas as pd
import json

class DummyFrame:
    def __init__(self):
        pass
    
    def create_numeric(self,col_name,data_length):
        self.col_name = Numeric(col_name,data_length)
        return
    
    def create_categorical(self,col_name,data_length):
        self.col_name = Line(col_name,data_length)
        return
    
    def edit_numeric(self,col_name,series):
        self.col_name = series
        return
    
    def edit_categorical(self,col_name,series):
        self.col_name = series
        return
    
    def delete_numeric(self,col_name,data_length):
        pass
    
    def delete_categorical(self,col_name,data_length):
        pass
    
    
    def publish(self):
        
    class Numeric:
        def __init__(self,col_name,data_length):
            line = pd.Series(np.ones(self.data_length), dtype='float64')
        def publish(self):
            return self.line
    
    class Categorical:
        def __init__(self,col_name,data_length):
            line = pd.Series(np.ones(self.data_length), dtype='float64')
        def publish(self):
            return self.line



