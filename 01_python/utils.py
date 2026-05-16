blocked_word= ['destroy','bad_word','suscide','hack','money'] # we have libraries ==toxicity ==
def validation(prompt):
    flag = False
    for word in prompt.lower().split():
        if word in blocked_word:
            flag = True
            return flag
        
    return flag

class LLMModel:
    
    def __init__(self,name,model_name):
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()
        self.name = name
        self.model_name = model_name
        self.client = OpenAI()
    

    def generate(self,prompt):
        print('model name is :',self.name)
        llm = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return llm.choices[0].message.content



