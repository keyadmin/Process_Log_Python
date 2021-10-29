import re
def check_string_in_file(file_name, string_to_search):
    # Open the file in read only mode
    reg = "^{}".format(string_to_search)
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        counts = 0
        for rder in read_obj:
            isTrue = re.match(reg, rder)
            if isTrue:
        # For each line, check if line contains the string  
                counts=counts+1
    return counts



#print(check_string_in_file('fileprces.txt','coc_coc_browser'))
