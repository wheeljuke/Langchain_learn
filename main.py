from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model="mistral", temperature = 0.0)


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
    
    Keep the keywords count equal or less than 5.
    
    Only output the whole JSON file and nothing else, no dialogue.
    """),
    ("user", "{input}")
])

from langchain_core.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()

chain = flashcardgen | llm #| output_parser

print(chain.invoke({"input": """
1. 眼的移動由6條骨骼肌控制，即上斜肌（Superior oblique）、下斜肌（Inferior oblique）、上直肌（Superior rectus）、下直肌（Inferior rectus）、內直肌（Medial rectus）和外直肌(Lateral rectus）。這些肌肉協調運動可以使眼球移動，以掃描視野中的物體，保持對焦於目標，並調整眼睛的焦點以適應環境變化rectus）。這些肌肉協調運可以使眼球移動，以掃描視野中的物體，保持對焦於目標，並調整眼睛的焦點以適應環境變化。
2. 物的或頭部在移動時，眼的移動可以獨立於物體移動之外，使得視網膜上的影像能夠穩定地維持在中央小窩這一區域中，即黃斑中心凹（fovea centralis）。這樣做有助於提高對細微差別的分辨能力，尤其是在低視野的情況下。
3. 這些肌肉不僅能控制眼球運動，還能參與視覺調適（accommodation）過程，這是指眼睛改變其晶體曲率，以調整焦點以更好地適應距離變化。當人眼這些肌肉不僅能控制眼球運動，還能參與視覺調適（accommodation）過程，這是指眼睛改變其晶體曲率，以調整焦點以更好地適應距離變化。當人眼從遠處看近物時，會透過睫狀肌和睫狀小帶的收縮作用來增加眼的屈光力，使得影像能夠清晰聚焦在黃斑中心凹。
總之，眼球的運動是由一系列肌肉協調控制的，這些肌肉不僅能移動眼球以對應環境中的物體，還能參與視覺功能的許多其他方面，包括維持穩定清晰的視野以及實現視覺遠處看近物時，會透過睫狀肌和睫狀小帶的收縮作用來增加眼的屈光力，使得影像能夠清晰聚焦在黃斑中心凹。總之，眼球的運動是由一系列肌肉協調控制的，這些肌肉不僅能移動眼球以對應環境中的物體，還能參與視覺功能的許多其他方面，包括維持穩定清晰的視野以及實現視覺調適。
"""}))

#print(llm.invoke("why is the sky blue"))
