class llm():
    def __init__(self,query):
        self.query = query


    def openAI(query):
        print(f"Hey I am Open AI and you asked me {query}")

    def claude(query):
        print(f"Hey I am Claude and you asked me {query}")


    def llama(query):
        print(f"Hey I am Llama and you asked me {query}")

 

boj1 = llm.openAI("who are you")



if __name__ == "__main__":
    boj2 = llm("What is your name?")
    llm.openAI(boj2.query)