def parse_line(string):
    tuple_elements = string.split('/', 3)
    if tuple_elements[0].isdigit() and tuple_elements[1].isdigit() and tuple_elements[2].isdigit():
        int1 = int(tuple_elements[0])
        int2 = int(tuple_elements[1])
        int3 = int(tuple_elements[2])
        string_element = tuple_elements[3]
        return (int1, int2, int3, string_element)
    
def get_line(fname,parno,lineno):
    f = open('%s.txt' %(fname))
    lno = 0
    pno = 0
    skip = False
    previous_line = ''
    for line in f:
        if line == '\n':
            skip = True
        else:
            skip = False
        
        if skip:
            previous_line = line   
            continue
        else:
            lno += 1
            if pno == 0:
                pno += 1
            elif previous_line == '\n' and line != '\n':
                pno += 1
                lno = 1     
        previous_line = line
        if lno == int(lineno) and pno == int(parno):
            return line


if __name__ == "__main__":

    fname = raw_input('Please file number ==> ')
    parno = raw_input('Please enter paragraph number ==> ')
    lineno = raw_input('Please enter the line number ==> ')
    
    print (get_line(fname,parno,lineno)).strip('\n')