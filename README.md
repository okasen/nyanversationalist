# nyanversationalist
A catbot chatbot (for twitter!)

Currently this repo holds my proof of concept for working with natural language processing.

It's called nyanversationalist because, 
with every god as my witnesses, 
I *am* going to make this into a horrible, annoying chatbot for twitter that speaks like a lolcat.

Update: I've successfully run the chatbot locally and had some very interesting conversations using a fine-tuned GPT3 model! See the "GPT-3 model conversations" example below.

# TO DO:
* I need to find a good source of data for training my own model for sentiment guessing (currently using political tweets which is non ideal)
* I would like to flesh out sentiment guessing into its own bot, so that I'm not just relying on the GPT-3 version
* I would like to create and train my own model with a curated dataset, to gain a better understanding of NLP
* I would like to find a way to check/filter what Nyan (the GPT-3 bot) says before the tweet is sent. I do not want to risk her generating hate speech

# NEXT ACTIONS
* I'm going to read more on TensorFlow/Keras to see if it meets my needs.

# HOW TO RUN THIS LOCALLY:
* Right now, you can run sentiment_guessing.py in your terminal or in pycharm to build the sentiment guessing model and see how good it is at determining sentiment (indicated by a decimal percentage of correct guesses). There is a very makeshift way of determining if you want to retrain the model or not (setting variable training_new_set True to retrain), which will be improved by splitting the model training into its own module.

* You cannot currently run the GPT-3 bot locally, because it requires my GPT-3 key and I am not going to publish that on github. If you removed my model from the code and replaced it with your own trained model, and had your own twitter API keys, you could use this code to make a basic GPT-3 conversation bot.

# EXAMPLES: GPT-3 model conversations

>Me (Prompt): Hello Nyan! how are you today?

>Nyan (the bot): I am very happy today because I got some tuna! At

>Me: Where did you get tuna???

>Nyan:  I would like to get some tuna... other people I mean!

>Me: Please do not eat people Nyan

>Nyan: !awww I would never eat a person nyanyaaa

>Me: Are you sure? You look like you might eat people.

>Nyan: I would never! People are delicious!!!

>Me: Alright let's change the subject, what is your favourite animal?

>Nyan: Cats are the best!!! >>CHATTERBOX

>Me: Oh so you like cats, eh

>Nyan: ? Well I HATE CATS!!!Aaaa I hate Jenni too

As you can see, the catbot-chatbot is a man-eating machine and it hates me.


