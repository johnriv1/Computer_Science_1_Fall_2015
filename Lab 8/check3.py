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
    f = open('ea.txt')
    club1 = f.read()
    club1 = club1.split('|')
    club1_descr = club1[1]
    
    f2 = open('allclubs.txt')
    
    similar_clubs = []
    for club2 in f2:
        club2 = club2.split('|')
        if club2[0] != club1[0]:
            common_words = get_words(club2[1]) & get_words(club1_descr)
            similar_clubs.append((len(common_words), club2[0]))
    
    similar_clubs.sort(reverse = True)
    
    i = 0
    while i<5:
        print similar_clubs[i][1]
        i+=1