
def writeTextToFile(text):
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    FILENAME = 'file.txt'
    with open(FILENAME, 'w') as f:
        f.write(STATICKY_TEXT + text)
    
    return FILENAME

writeTextToFile('lubiku was here')