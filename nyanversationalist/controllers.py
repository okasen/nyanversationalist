import numpy
import pandas
import pickle

import sklearn
from sklearn.model_selection import train_test_split

import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot

STOPWORDS_SET = set(stopwords.words("english"))


def clean_words(row) -> str:
    words_filtered = [e.lower() for e in row if len(e) >= 3]
    cleaned_stopless_words = " ".join([word for word in words_filtered
                                       if "http" not in word
                                       and not (word.startswith("#") or word.startswith("@"))
                                       and word != "RT"
                                       and word not in STOPWORDS_SET
                                       ])
    return cleaned_stopless_words


def get_words_without_sentiment(words) -> list:
    tweets = []
    for row in words:
       cleaned_words = clean_words(row)
       tweets.append(cleaned_words)
    return tweets


def get_words_and_sentiments_from_tweets(train) -> list:
    tweets = []
    for _,  row in train.iterrows():
        words_filtered = [e.lower() for e in row.text.split() if len(e) >= 3]
        words_cleaned = [word for word in words_filtered
                         if 'http' not in word
                         and not word.startswith('@')
                         and not word.startswith('#')
                         and word != 'RT']
        words_without_stopwords = [word for word in words_cleaned if not word in STOPWORDS_SET]
        tweets.append((words_without_stopwords, row.sentiment))
    return tweets


def get_words_for_features(tweets) -> list:
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def wordcloud_draw(words, color="black") -> None:
    wordcloud = WordCloud(stopwords=STOPWORDS_SET,
                          background_color=color,
                          width=2500,
                          height=2000
                          ).generate(words)
    pyplot.figure(1, figsize=(13, 13))
    pyplot.imshow(wordcloud)
    pyplot.axis("off")
    pyplot.show()


def get_word_features(wordlist) -> dict:
    wordlist = nltk.FreqDist(wordlist)
    features = wordlist.keys()
    return features


def extract_features_from_document(tweets) -> dict:
    document_words = set(tweets)
    features = {}
    for word in word_features:
        features[f"contains({word})"] = (word in document_words)
    return features


sentiment_data = pandas.read_csv("Sentiment.csv")

sentiment_data = sentiment_data[["text", "sentiment"]]

train, test = train_test_split(sentiment_data, test_size=0.1)

train = train[train.sentiment != "Neutral"]

train_pos = train[train["sentiment"] == "Positive"]

train_pos = train_pos["text"]

train_neut = train[train["sentiment"] == "Neutral"]

train_neut = train_neut["text"]

train_neg = train[train["sentiment"] == "Negative"]

train_neg = train_neg["text"]

tweets = get_words_and_sentiments_from_tweets(train=train)

test_pos = test[ test['sentiment'] == 'Positive']
test_pos = test_pos['text']

test_neg = test[ test['sentiment'] == 'Negative']
test_neg = test_neg['text']

word_features = get_word_features(get_words_for_features(tweets))



training_new_set = True
if training_new_set:
    print("getting ready")
    training_set = nltk.classify.apply_features(extract_features_from_document, tweets)
    print("and readier...")
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("ready to check!")

    with open("sentiment_classifier.pickle", "wb") as f:
        pickle.dump(classifier, f)
else:
    f = open('sentiment_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

success = 0
failures = 0
for _,tweet in test.iterrows():
    classified = classifier.classify(extract_features_from_document(tweet.text.split()))
    print(classified)
    print(tweet.sentiment)
    if classified == tweet.sentiment:
        success += 1
    else:
        failures += 1

print(success / (success + failures))