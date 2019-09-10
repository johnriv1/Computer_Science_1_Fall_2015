def get_words(description):
    allword = set()
    description = description.replace('.', ' ')
    description = description.replace(',', ' ')
    description = description.replace('(', ' ')
    description = description.replace(')', ' ')
    description = description.replace('"', ' ')
    description = description.lower()
    description = description.split(' ')
    for word in description:
        if len(word) >= 4 and str.isalpha(word):
            allword.add(word)
    print allword

if __name__ == '__main__':
    
    f = open('wrpi.txt')
    line = f.read()
    line = line.split('|')
    descr = line[1]
    
    get_words(descr)