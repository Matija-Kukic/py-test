class Food:
    def __init__(self,Type,article):
        self.Type = Type
        self.article = article
    def __str__(self):
        return f"Food is type: {self.Type}, article {self.article}"
