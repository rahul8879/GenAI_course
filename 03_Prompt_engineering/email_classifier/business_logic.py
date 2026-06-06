import json
from dotenv import load_dotenv
from openai import OpenAI
import os
import time
load_dotenv()


client = OpenAI()


def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def load_prompt(filename):
    path = os.path.join('prompt', filename)
    with open(path, 'r') as f:
        return f.read()
    



def classify_with_cot(subject,body,sender):
    template = load_prompt('classify_cot.md')
    prompt = template.format(subject=subject,sender=sender,body=body)
    result = call_llm(prompt)
    category, urgency = None, None
    for line in result.split('\n'):
        if 'CATEGORY:' in line:
            category = line.split(':')[1].strip()
        if 'URGENCY:' in line:
            urgency = line.split(':')[1].strip()

    return {
        'category': category,
        'urgency': urgency,
        'full_output': result
    }
                
from collections import Counter

def classify_with_self_consitency(email, n_runs=5):
    template = load_prompt('classify_cot.md')
    results = []
    traces = []
    for i in range(n_runs):
        prompt = template.format(subject=email['subject'], body=email['body'], sender=email['sender'])
        result = call_llm(prompt)
        traces.append(result)
        for line in result.split('\n'):
            if 'CATEGORY:' in line:
                results.append(line.replace('CATEGORY:', '').strip())

    votes = Counter(results)
    winner = votes.most_common(1)[0][0]
    print(f"Winner: {winner}")
    confidence = votes.most_common(1)[0][1] / n_runs
    urgency = None

    for line in traces[0].split('\n'):
        if 'URGENCY:' in line:
            urgency = line.replace('URGENCY:', '').strip()


    return {
        'category': winner,
        'urgency': urgency,
        'confidence': confidence


    }
    

email={
    "subject": "Can't login ",
    "body": "Our entire team can't login.  paid for annual plan last week. Board demo in 3 hours.entire team cant login",
    "sender": "rtiwari@rbyteao.com"
    
    }


result = classify_with_self_consitency(email)
# category=[]
# for r in result:
#     for line in r.split('\n'):
#         if 'CATEGORY:' in line:
#             category.append(line.split(':')[1].strip())
print(result)


# subject = input("Enter the subject: ")
# body = input("Enter the body: ")
# sender = input("Enter the sender: ")

# output = classify_with_cot(subject=subject,body=body,sender=sender)
# print(output)