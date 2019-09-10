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
    return allword

if __name__ == '__main__':
    
    f = open('wrpi.txt')
    line = f.read()
    line = line.split('|')
    descr = line[1]
    
    f2 = open('qc.txt')
    line2 = f2.read()
    line2 = line2.split('|')
    descr2 = line2[1]
    
    common = get_words(descr) & get_words(descr2)
    only_in_club1= get_words(descr).difference(get_words(descr2))
    only_in_club2= get_words(descr2).difference(get_words(descr))
    
    print common
    print only_in_club1
    print only_in_club2