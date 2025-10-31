import os
from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
llm = ChatGroq(model ="llama-3.1-8b-instant", temperature =0.7)
memory = ConversationBufferMemory()
prompt = PromptTemplate(
    input_variables=["input", "history"],
    template ="You are a helping assistant. Who help other to answer frequently asked questions. Don't Provide them the wrong answers. First check if your answer is right or not. The user's question is : {input}. The Conversational History is : {history}\n Answer: "
)

model = ConversationChain(
    llm =llm,
    memory =memory,
    prompt =prompt  
)





@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = model.invoke({"input": user_input})
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)


# response =model.invoke({"input": "Tell me what is Kubernetes"})
# print(response)

#work when run locally
# print("How can I assist you today?, Type 'q' or 'e' to exit.")
# while True:
#     user_input =input("User: ")
#     if user_input.lower() in ['q','e']:
#         print("Ending the Conversation. Hope you get your query solved.")
#         break
#     response =model.invoke({"input": user_input})
#     print("Assistant: ", response['response'])