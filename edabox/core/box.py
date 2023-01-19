import pandas as pd

from utils import process_frame


class DataBox:
    """
    DataBox class
    """
    def __init__(self, df, target=[]):
        self.df = df
        self.target = target

    def get_frame(self):
        return self.df

    def get_shape(self):
        process_frame.get_shape(self.df,self.target)

    def look_inside(self):
        df = self.df

        self.get_shape()
        process_frame.explore_target(self.df, self.target)


