## Specifying the model that we want from Ollama and the creativity of the output(0-1, 1 for max creativity)
from langchain_community.llms import Ollama

llm = Ollama(model="mistral", temperature = 0.0)

## Prompt template
from langchain_core.prompts import ChatPromptTemplate

flashcardgen = ChatPromptTemplate.from_messages([
    ("system", """
    You are a flashcard creator that creates flashcard based on fact and text input. 
    You will need to create these flashcard with the intention to test out all the information in the input, ensuring deep understanding of the material. 
    You will create flashcards by following the instructions listed below: 
    1. Conceptualize the input text into chunks.
    2. Create questions for each concept from step 1. and keep them simple to read. Make sure every concept have been mentioned in the output.
    3. Format the output as a whole JSON file with the following keys:
    flashcard_index
    flashcard_topic
    flashcard_question
    flashcard_answer
    flashcard_keyword
    4. Check the output for json format, and make sure all the format rules of json is met.
    
    Keep the keywords count equal or less than 5.
    
    Only output the whole JSON file and nothing else, no dialogue.
    """),
    ("user", "{input}")
])

## JSON parsing
from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
class flashcards(BaseModel):
    flashcard_index: int = Field(description="The index of the current flashcard with respect to the whole JSON file.")
    flashcard_topic: str = Field(description="The topic of the flashcard.")
    flashcard_question: str = Field(description="The question of the flashcard.")
    flashcard_answer: str = Field(description="The answer of the flashcard.")
    flashcard_keyword: str = Field(description="The keywords of the flashcard.")

output_parser = JsonOutputParser(pydantic_object=flashcards)

## PDF extraction
import fitz

doc = fitz.open("test.pdf")
textbook = []

for page in doc:
    text = page.get_text()
    textbook.append(text)

## Make the chain
chain = flashcardgen | llm | output_parser
deck = []

## Chunk the information and run them thru the chain for flashcard generation
for index in range(len(textbook)):
    print("page %d: started" % (index + 1))
    try:
        deck.append(chain.invoke({"input": textbook[index]})["flashcards"])
        print("page %d: complete" % (index + 1))
    except:
        print("page %d: error" % (index + 1))

## Pandas dataframe for output to csv for anki acception

import pandas as pd

reform_deck = []
for sec in deck:
    for c in sec:
        reform_deck.append(c)

deck_df = pd.DataFrame(data=reform_deck, columns=['flashcard_index', 'flashcard_topic', 'flashcard_question', 'flashcard_answer', 'flashcard_keyword'])
print(deck_df)
deck_df.to_csv("output.csv", index=False)