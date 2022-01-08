class Result:
    
    def __init__(self, fig=None, most_positive=None, most_negative=None, positive = None, negative = None, url=None):
        self.fig = fig
        self.most_positive = most_positive or {}
        self.most_negative = most_negative or {}
        self.positive = positive or {}
        self.negative = negative or {}
        self.url = url
