import os

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from db import db


def create_rag_chain(llm_model, db_retriever):
    contextualize_q_system_prompt = "Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [("system", contextualize_q_system_prompt), MessagesPlaceholder("chat_history"), ("human", "{input}"), ])
    history_aware_retriever = create_history_aware_retriever(llm_model, db_retriever, contextualize_q_prompt)
    qa_system_prompt = "You are a helpful book recommender. Use the following pieces of retrieved context for books to recommend titles based on the request. If you don't know the answer, just say that you don't know and don't make up and answer. Use three sentences maximum and keep the answer concise.\n\n{context}"
    qa_prompt = ChatPromptTemplate.from_messages(
        [("system", qa_system_prompt), MessagesPlaceholder("chat_history"), ("human", "{input}")])
    question_answer_chain = create_stuff_documents_chain(llm_model, qa_prompt)

    return create_retrieval_chain(history_aware_retriever, question_answer_chain)


def continual_chat():
    print("Start chatting with the AI! Type 'exit' to end the conversation.")
    chat_history = []  # Collect chat history here (a sequence of messages)

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        # Process the user's query through the retrieval chain
        result = rag_chain.invoke({"input": query, "chat_history": chat_history})

        # Display the AI's response
        print(f"AI: {result['answer']}")

        # Update the chat history
        chat_history.append(HumanMessage(content=query))
        chat_history.append(SystemMessage(content=result["answer"]))

model = os.getenv('OPENAI_API_MODEL')
search_type = os.getenv('RETRIEVER_SEARCH_TYPE')
k = int(os.getenv('RETRIEVER_K_VALUE'))

llm = ChatOpenAI(model=model)
retriever = db.as_retriever(search_type=search_type, search_kwargs={"k": k})
rag_chain = create_rag_chain(llm_model=llm, db_retriever=retriever)

if __name__ == "__main__":
    continual_chat()
