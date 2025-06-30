from langchain_ollama import OllamaLLM


#load model from ollama
llm = OllamaLLM(model="mistral")

print("\n welcome to ypur AI Agent")

while True:
    question = input("enter your question (or type exit to stop): ")
    if question.lower() == "exit":   #anything will be converted to lower letters like if user enters EXIT or Exit also it should accept!!
        print("Good Bye!")
        break
    response = llm.invoke(question)  #invoke - question will be passed to the model and llm is the method  we decided (mistral)
    print("AI response: ", response)

