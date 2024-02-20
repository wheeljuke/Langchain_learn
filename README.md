# Langchain_learn
This is a prototype for flashcard creation from PDF files, using langchain and open source llms. Output can be displayed using the print(deck) command or use the internal csv output function

## Env
MBP 2021 M1 Pro 16G Ram

## Future work
1. Create a card format in Anki to accept this ["flashcard_index", "flashcard_topic", "flashcard_question", "flashcard_answer", "flashcard_keyword"] format
1-1. Index should be ingnored, the others should be filled into their respective fields.
2. Clozer for llm unsupervised traning could be a good option for flashcard generation.
