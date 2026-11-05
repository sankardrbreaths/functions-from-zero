import wikipedia

# Business logic
def get_summary(name, length=1):
    return wikipedia.summary(name, sentences=length)