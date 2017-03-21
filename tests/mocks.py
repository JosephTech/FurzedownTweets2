class status:
    def __init__(self, text, user):
        self.text = text
        self.author = author(user)

class author:
    def __init__(self, userName):
        self.userName = userName

    @property
    def screen_name(self):
        return self.userName