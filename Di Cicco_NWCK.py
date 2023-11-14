'''
Rosalind NWCK exercise by Di Cicco Cecilia
'''
# Distances in trees

# Defining the function tree distance
def tree_distance(T, x, y):
    X = T.find(x)
    Y = T.find(y)
    t = [i for i in T[min(X, Y):max(X, Y)] if i in [')', '(', ',']]
    brackets = ''
    for i in t:
        brackets += i
    while '(,)' in brackets:
        brackets = brackets.replace('(,)', '')
    if brackets.count('(') == len(brackets):
        return len(brackets)
    elif brackets.count(')') == len(brackets):
        return len(brackets)
    elif brackets.count(',') == len(brackets):
        return 2
    else:
        return brackets.count(')') + brackets.count('(') + 2
    


if __name__ == '__main__':

    # Creating a new file that stores the result
    file_result = 'result_NWCK.txt'
    with open('rosalind_nwck.txt', 'r') as input_file:
        TREE = [line.strip().replace(';', '') for line in input_file.readlines() if len(line.strip()) > 0]

    with open(file_result, 'w') as result:
        for i in range(0, len(TREE), 2):
            T = TREE[i]
            x, y = TREE[i + 1].split(' ')
            distance = tree_distance(T, x, y)
            result.write(f"{distance} ")

    print(file_result)