def same_by(func_filter, data):
    answer = list(map(func_filter, data))
    # for i in range(len(answer)):
    #     if answer[0] != answer[i]:
    #         return False
    # return True
    return len(set(answer)) == 1 # all, any

values = [0, 2, 10, 6, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
