import spacy 

def load_file():
    with open("sample.txt","r") as f:
        text=f.readlines()

    return text

def exmaple_sentence():
    nlp=spacy.blank("en")
    nlp.add_pipe("sentencizer")
    doc = nlp("Apple is good for health. It keeps you healthy and fit.")

    for sentence in doc.sents:
        print(sentence)


if __name__ == "__main__":
    ##english
    ##this gives empty pipe and tokkenizer
    nlp=spacy.blank("en")

    # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

    # for token in doc:
    #     print(token)

    text=load_file()
    print(text)

    text=" ".join(text)
    print(text)

    docs=nlp(text)
    emails = []

    for token in docs:
        if token.like_email:
            emails.append(token.text)

    print(emails)

    exmaple_sentence()