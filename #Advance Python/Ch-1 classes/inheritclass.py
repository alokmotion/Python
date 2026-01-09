from firstclass import llm


class chatbot(llm):
    def __init__(self, model, query):
        self.model = model
        self.query = query
        llm.__init__(self,query)

    def greet(self):
        return f"Hello, I am {self.model}, your chatbot."
    

obj_inheritance = chatbot("GPT-4", "Explain Inheritance in Python")

print(obj_inheritance.greet())