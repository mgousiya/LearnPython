

class Life:
    def __init__(self,success,failure):
        self.success = success
        self.failure = failure

    def lesson(self):
        print("If you get success you won in life")
        print("If you get failure you are a looser")

Span = Life("Won","Failure")

print(Span.success)
Span.lesson()
print(Span.failure)