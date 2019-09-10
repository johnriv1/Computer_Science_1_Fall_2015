def parse_line(string):
    tuple_elements = string.split('/', 3)
    if tuple_elements[0].isdigit() and tuple_elements[1].isdigit() and tuple_elements[2].isdigit():
        int1 = int(tuple_elements[0])
        int2 = int(tuple_elements[1])
        int3 = int(tuple_elements[2])
        string_element = tuple_elements[3]
        return (int1, int2, int3, string_element)

print parse_line("12/3/4/Here is some random text, like 5/4=3")
