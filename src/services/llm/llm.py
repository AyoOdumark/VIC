from llama_cpp import Llama
from src import models

def get_chat_history():
    try:
        _ = models.Message.find(models.Message.role == "system").all()
    except TypeError:
        system_message = models.Message(
            role="system",
            content="You are a helpful assistant"
        )
        system_message.save()
    
    chat_history = []
    primary_keys = models.Message.all_pks()
    
    for pk in primary_keys:
        chat_message = models.Message.get(pk).dict()
        chat_history.append(
            {
             "role": chat_message["role"],
             "content": chat_message["content"]
             }
        )
        
    return chat_history

def generate_response(user_input):
    llm = Llama(model_path="", n_ctx=2048)
    chat_history = get_chat_history()
    user_message = {
        "role": "user",
        "content": user_input
    }
    
    chat_history.append(user_message)

    user_message = models.Message(**user_message)
    user_message.save()
    
    output = llm.create_chat_completion(chat_history, stop=["\n"])
    
    output_message = output["choices"][0]["message"]
    
    assistant_message = models.Message(**output_message)
    assistant_message.save()
    
    return output_message["content"]