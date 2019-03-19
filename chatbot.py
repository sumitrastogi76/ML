from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import csv

# Create a new chat bot named Charlie
chatbot = ChatBot(
                'Sumit',
                logic_adapters=[ 
                                'chatterbot.logic.MathematicalEvaluation', 
                                #'chatterbot.logic.TimeLogicAdapter'#,
                                'chatterbot.logic.BestMatch'
                ],
                preprocessors=[
                                'chatterbot.preprocessors.clean_whitespace'
                ],
                read_only=True
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
trainer = ListTrainer(chatbot)
with open("dataset.csv",'r') as csvfile:
  data =  csv.reader(csvfile,delimiter=',') 
  for row in data:
    trainer.train(row)

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
