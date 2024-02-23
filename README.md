# Langchain_learn
This is a prototype for flashcard creation from PDF files, using langchain and open source llms. Output can be displayed using the print(deck) command or use the internal csv output function.

## Structure
1. Main.py for the main program.
2. Ollama with mistral downloaded running in serve mode(type in ollama serve in mac terminal).
3. Move your PDF file of choice into the same folder of main.py(currently test.pdf will be read).
4. Output csv is called output.csv and will appear in the same folder as main.py after execution.

## Env
MBP 2021 M1 Pro 16G Ram
Python 3.13

## Future work
~~1. Create a card format in Anki to accept this ["flashcard_index", "flashcard_topic", "flashcard_question", "flashcard_answer", "flashcard_keyword"] format.~~
~~1-1. Index should be ingnored, the others should be filled into their respective fields.~~
2. Clozer for llm unsupervised traning could be a good option for flashcard generation.
3. Possibly restructure chunking by pages into a vector database.
4. Improve the prompt even more to reduce format conflict with JSON, and increase question specificity to remove odd questions.
