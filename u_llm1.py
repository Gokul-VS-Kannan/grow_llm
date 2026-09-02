import ollama



def ask_model(question, personality = 'helpful assistant', model='qwen3:0.6b'):
    messages = [
        {
            'role':'system',
            'content':f'You are a {personality}, keep answers short and clear.'
        },
        {
            'role':'user',
            'content':question
        }
    ]

    response = ollama.chat(
        model=model,
        messages=messages
    )

    return response['message'],['content']


question = 'why should you learn python?'

r1 = ask_model(question,'friendly teacher who use simple examples')
print(r1)

r2 = ask_model(question,'comedian who use sarcastic jocks')
print(r2)