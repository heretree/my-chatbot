import os

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.schema import HumanMessage
from utils import get_api_keys

config = get_api_keys("api_keys.yaml")
os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
os.environ["PROMPTLAYER_API_KEY"] = config["PROMPTLAYER_API_KEY"]

class MyChatBot():
    def __init__(self, model="gpt-4", temperature=0.1, verbose=False):
        self.verbose=verbose
        self.chat = PromptLayerChatOpenAI(
            pl_tags=["langchain", "chater"], 
            model=model,
            temperature=temperature
        )
        self.conversation = ConversationChain(
            llm=self.chat,
            verbose=self.verbose
        )
        return
    
    def ask(self, input):
        response = self.conversation.run(input)
        return response
        