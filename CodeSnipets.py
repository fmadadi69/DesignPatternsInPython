def merge_dictionaries(*dics):
    merged_dic = dict()
    for dic in dics:
        merged_dic.update(dic)

    return merged_dic


print(merge_dictionaries({1: 10, 's': 11, 'sara': 'samad'}, {'ali': 'sara', 1: 'salam', 'sara': 20}))


def merge_dictionaries_2(*dics):
    mereged_dic = {key: value for d in dics for key, value in d.items()}
    return mereged_dic


print(merge_dictionaries_2({1: 10, 's': 11, 'sara': 'samad'}, {'ali': 'sara', 1: 'salam', 'sara': 20}))


def merge_dictionaries_3(dic1 , dic2):
    return {**dic1, **dic2}


print(merge_dictionaries_3({1: 10, 's': 11, 'sara': 'samad'}, {'ali': 'sara', 1: 'salam', 'sara': 20}))

