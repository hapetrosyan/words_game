import pandas as pd

# df = pd.read_csv('C:/Q_C_Hakob/github/words_game/words_list.txt')
df = pd.read_csv('C:/Q_C_Hakob/github/words_game/words_10k.txt')

def get_match_list(df, word):
    word = set(word)
    wc = len(word)
    i = 0
    word =''.join(word)
    lst = pd.DataFrame(columns=['word', 'len'])
    for dict_word in df['a']:
        try:
            if len(dict_word) >= wc:
                if len(list(set(dict_word) & set(word))) == wc:
        #             print(word, dict_word)
                    lst = lst.append({'word': dict_word, 'len': len(dict_word)}, ignore_index=True)
        except:
            continue
    return(lst.sort_values('len', ascending=True)['word'])


    print(get_match_list(df, 'physically'))