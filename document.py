from typing import List

class Document:
    def __init__(self,topics: List[Topic],doc_title) -> None:
        self.topics = topics
        self.doc_title = doc_title
    
class Topic:
    def __init__(self,questions, topic_title) -> None:
        self.questions = questions
        self.topic_title = topic_title
        
class Question:
    def __init__(self,text,number,answer:Answer) -> None:
        self.text = text
        self.number = number
        self.answer = answer
        
class Answer:
    def __init__(self,text,number) -> None:
        self.text = text
        self.number = number