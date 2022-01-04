class Result:
    
    def __init__(self, compound_score=None, most_positive=None, most_negative=None, url=None):
        self.compound_score = compound_score
        self.most_positive = most_positive or {}
        self.most_negative = most_negative or {}
        self.url = url
