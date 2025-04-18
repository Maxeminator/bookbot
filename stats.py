def get_book_words(text):
    text=text.split()
    counter=0
    for word in text:
        counter+=1
    return counter
# or use len(text) <-prefered

def get_book_symbols(text):
    text=text.lower()
    symbols={}
    for char in text:
        if char not in symbols:
            symbols[char]=0
        symbols[char]+=1
        
    return symbols

def sorting(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    chars_list=[]
    for symbol, num in dictionary.items():
        char_dict={"char":symbol, "num": num}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sorting)
    return chars_list
