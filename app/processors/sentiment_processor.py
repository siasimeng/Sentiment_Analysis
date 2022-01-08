import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sklearn
from plotly.offline import plot
import plotly.graph_objs as go

from app.processors.preprocessing import preprocess
from app.obj.result import Result

class SentimentProcessor:
    
    def __init__(self):
        with open('app/processors/vectoriser.pickle', 'rb') as file:
            self.vectoriser = pickle.load(file)
    
        # Load the LR Model.
        with open('app/processors/Sentiment-LR.pickle', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, comments):
        finaldata = []
       
        processed_comments = []
        for x in comments:
            x = preprocess.sentiment_preprocess(x)
            x = ' '.join(x)
            processed_comments.append(x)
    
    
        commentsdata = self.vectoriser.transform(processed_comments)
        sentiment = self.model.predict(commentsdata)
    
        # print(model.classes_)
        sentiment_prob = self.model.predict_proba(commentsdata)
    
        for index,tweet in enumerate(comments):
            if sentiment[index] == 1:
                sentiment_probFinal = sentiment_prob[index][1]
            else:
                sentiment_probFinal = sentiment_prob[index][0]
            
            sentiment_probFinal2 = "{}%".format(round(sentiment_probFinal*100,2))
            finaldata.append((tweet, sentiment[index], sentiment_probFinal2))
           
        # Convert the list into a Pandas DataFrame.
        df = pd.DataFrame(finaldata, columns = ['comments','sentiment', 'probability'])
        df = df.replace([-1,1], ["Negative","Positive"])
        return df

    def process_sentiment(self, comment_list, url):
        result = Result()
        df = self.predict(comment_list)
        positive = round(np.count_nonzero(df['sentiment'] == "Positive")/len(df['sentiment'])*100,2)
        negative = round(np.count_nonzero(df['sentiment'] == "Negative")/len(df['sentiment'])*100,2)
        result.positive = positive
        result.negative = negative

        pos_df = df.loc[df['sentiment'] == "Positive"]
        pos_df = pos_df.sort_values('probability',ascending = False).head(5)
        pos_df = pos_df[['comments', 'probability']]
        result.most_positive = pos_df.set_index('comments').T.to_dict('list')

        neg_df = df.loc[df['sentiment'] == "Negative"]
        neg_df = neg_df.sort_values('probability',ascending = False).head(5)
        neg_df = neg_df[['comments', 'probability']]
        result.most_negative = neg_df.set_index('comments').T.to_dict('list')

        result.url = url
        return result
