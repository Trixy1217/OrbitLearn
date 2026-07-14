from langchain_ollama import ChatOllama

def model_smollm2():

    llm= ChatOllama(
        model="smollm2:360m",
        temperature=0,
        
    )


    return llm


oe = model_smollm2()

print(oe)