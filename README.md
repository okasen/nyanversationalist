# nyanversationalist
A catbot chatbot (for twitter!)

Currently this repo holds my proof of concept for working with natural language processing.

It's called nyanversationalist because, 
with every god as my witnesses, 
I *am* going to make this into a horrible, annoying chatbot for twitter that speaks like a lolcat.

# TO DO:
* I need to find a good source of data for training the model (currently using political tweets which is non ideal)
* I need to split the code into two parts: A controller for training/retraining the model, and one for interacting with the catbot using the model (via twitter)
* I need to integrate the twitter API into this bot (for reading incoming tweets, and for sending obnoxious tweets back)
* There needs to be a mechanism for choosing a response tweet from a list based on the sentiment of the incoming tweet. This will be expanded to generate tweets using NLP in due time.

# HOW TO RUN THIS LOCALLY:
* Right now, you can run controllers.py in your terminal or in pycharm to build the model and see how good it is at determining sentiment (indicated by a decimal percentage of correct guesses). There is a very makeshift way of determining if you want to retrain the model or not (setting variable training_new_set True to retrain), which will be improved by splitting the model training into its own module.
