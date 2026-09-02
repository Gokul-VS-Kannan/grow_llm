"""
plan for clling an LLM

goal send a request to the ollama model, get a response
"""

# 1 import the ollama library for talking to the model
import ollama
#2 define what model we want to use
#3 create the message in the formate model expects (as dictionary)
#4 send the message to the model
#5 get back the response
#6 extract the test from it
#7 return the text


response = ollama.chat(
    model = "qwen3:0.6b",
    messages= [
        {
            'role':'user',
            'content':'What is python programming language? Explain in 1 sentences.',
        }
    ]
)

# print(response)

answer = response['message'],['content']
print(answer)