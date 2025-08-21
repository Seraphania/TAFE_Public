from datetime import datetime

class Post:
    def __init__(self, content): # called by user,py
        self.content = content
        self.timestamp = datetime.today()

    def display_post(self):
        post = f"{self.content} \n {self.timestamp}"
        print(post)