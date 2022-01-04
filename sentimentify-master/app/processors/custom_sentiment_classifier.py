import nltk
from nltk.corpus import movie_reviews


class CustomSentimentClassifier:

    def __init__(self):
        self.classifier = self._train()

    def _get_feature_dictionary(self, words):
        return {word: True for word in words}

    def _train(self):
        # Separate dataset based on positive and negative movie reviews
        features_positive = [(self._get_feature_dictionary(movie_reviews.words(fileids=[f])), 'Positive') for f in movie_reviews.fileids('pos')]
        features_negative = [(self._get_feature_dictionary(movie_reviews.words(fileids=[f])), 'Negative') for f in movie_reviews.fileids('neg')]

        # Create combined dataset and train Naive Bayes Classifier
        training_features = features_positive + features_negative
        classifier = nltk.NaiveBayesClassifier.train(training_features)

        return classifier

    def polarity_scores(self, comment):
        # Get distribution of probability of each classification
        probability_distribution = self.classifier.prob_classify(self._get_feature_dictionary(comment.split()))
        predicted_sentiment = probability_distribution.max()
        probability = round(probability_distribution.prob(predicted_sentiment), 4)
        # Return in the same form as vaderSentiment library
        return {'compound': (probability if predicted_sentiment == 'Positive' else probability * -1)}

