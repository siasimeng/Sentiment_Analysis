# Method to load the models from pickle file
def load_models():  
       
    # Load the vectoriser.
    with open('vectoriser.pickle', 'rb') as file:
      vectoriser = pickle.load(file)
    
    # Load the LR Model.
    with open('Sentiment-LR.pickle', 'rb') as file:
      LRmodel = pickle.load(file)
    
    return vectoriser, LRmodel


# Method to perform tfidf vectorizer on unseen data and then using the model loaded from pickle file to predict 
# whether positive or negative and also the probability along with it.
def predict(vectoriser, model, text):
    finaldata = []
    
    
    processed_text = []
    for x in text:
        x = preprocess(x)
        x = ' '.join(x)
        processed_text.append(x)
    
    
    textdata = vectoriser.transform(processed_text)
    sentiment = model.predict(textdata)
    
    # print(model.classes_)
    sentiment_prob = model.predict_proba(textdata)
    
    for index,tweet in enumerate(text):
        if sentiment[index] == 1:
            sentiment_probFinal = sentiment_prob[index][1]
        else:
            sentiment_probFinal = sentiment_prob[index][0]
            
        sentiment_probFinal2 = "{}%".format(round(sentiment_probFinal*100,2))
        finaldata.append((tweet, sentiment[index], sentiment_probFinal2))
           
    # Convert the list into a Pandas DataFrame.
    df = pd.DataFrame(finaldata, columns = ['text','sentiment', 'Probability(Confidence Level)'])
    df = df.replace([-1,1], ["Negative","Positive"])
    return df
