import pandas as pd

print('in libs')

def get_words_containing_symbols(df, word):
#     word = 'happy'
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
    



def get_match_count_pos(sec_w, try_w):
    min_len = min(len(sec_w), len(try_w))
    try_w_trunc = try_w[0:min_len]
    sec_w_trunc = sec_w[0:min_len]
    d = pd.DataFrame({'sec':list(sec_w_trunc), 'try': list(try_w_trunc)})
    pos_match = len(d[d['sec'] == d['try']])
    count_match = len(list(set(sec_w) & set(try_w)))
    return (try_w, count_match, pos_match)