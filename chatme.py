import warnings
import pickle
import json
import random
import tensorflow
import tflearn
import numpy
from nltk.stem.lancaster import LancasterStemmer
import nltk
from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False  # to disable warnings
# nltk.download('punkt')
# nltk.download('popular')
stemmer = LancasterStemmer()


Unknown = [
    "i am lost!",
    "i Seriously have No idea about What your talking...",
    "Sorry but i can't get you",
    "Can you help me understand better?"]

with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def Respond_To_Command(inp):
    # print(inp)
    results = model.predict([bag_of_words(inp.lower(), words)])
    results_index = numpy.argmax(results)
    # rx = list(results[0] < 0.04)
    # print(rx)
    if results[0][results_index] < 0.66:
        intent = "Unknown"
        return random.choice(Unknown), intent

    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
            intent = tg['tag']

    return random.choice(responses), intent


# def chat():
#     print("Start talking with the bot (type quit to stop)!")
#     # print(responses)
#     while True:
#         inp = input("You: ")
#         if inp.lower() == "quit":
#             break

#         results = model.predict([bag_of_words(inp, words)])
#         results_index = numpy.argmax(results)
#         if results[0][results_index] < 0.66:
#             print(results[0][results_index])
#             print(random.choice(Unknown))
#             intent = "Unknown"
#             continue

#         tag = labels[results_index]

#         for tg in data["intents"]:
#             if tg['tag'] == tag:
#                 responses = tg['responses']
#                 intent = tg['tag']

#         print(random.choice(responses), intent, results[0][results_index])


# chat()
