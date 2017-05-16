import urllib.request as request
def read_content():
    quotes = open("I:\FullStack\movie_quotes.txt")
    contents_of_file = quotes.read().split(' ')
    print(contents_of_file)
    for word in contents_of_file:
        check_profanity(word)
    quotes.close()
def check_profanity(text):
    connection = request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    if(output == "b'false'"):
        print("Curse word found")
    connection.close()
read_content()