import json
from difflib import get_close_matches
dict_data = json.load(open('data.json'))

def get_def(word):
    word = word.lower()
    if word in dict_data:
        return word,dict_data[word]
    elif word.title() in dict_data:
        return word.title(),dict_data[word.title()]
    elif word.upper() in dict_data:
        return word.upper(),dict_data[word.upper()]
    elif len(get_close_matches(word,dict_data.keys()))>0:
        close_matches = get_close_matches(word,dict_data.keys(),cutoff=0.75)
        if len(close_matches)>0:
            print('Did you mean any of these outputs?')
            for i in range(0,len(close_matches)):
                print('{}. {}'.format(i+1,close_matches[i]))
            user_ip = input('Press select a number form the above options or N for non of the above : ')
            if user_ip.isdigit() and int(user_ip)<=len(close_matches):
                return get_def(close_matches[int(user_ip)-1])
            else:
                return 'Try another word or incorrect selection'
        else:
           return 'The word does not exist.' 
    else:
        return 'The word does not exist.'

search_word = input("Enter the word to search for its definition : ")
results = get_def(search_word)
if type(results)==tuple:
    print('\nWord : {} \nDefinition :-'.format(results[0]))
    [print(expl) for expl in results[1]] if type(results[1]) == list else print(results[1])
    print('\n')
else:
     print(results)