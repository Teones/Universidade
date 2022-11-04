# GROUP_1: TARCIO ELYAKIN, KEVIN SANTOS, PABLO ODILON, ARTHUR SANTANA.
# GROUP_2: ?

def remove_repeated_elements_from_array(array):
    array = sorted(map(
        lambda x: x[1],
        filter(lambda x: x[1] not in array[:x[0]], enumerate(array))))
    return array


def read_different_angles(angles):
    angles = angles.lower().split(' ')
    characters = ['g', 'm', 's']
    alphabet = []
    # creating the alphabet
    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))

    # remove g,m,s from alphabet
    [alphabet.remove(characters[i]) for i in range(len(characters))]

    # analyzing if there is any wrong letter
    index_remove = []
    for i in range(len(alphabet)):
        for j in range(len(angles)):
            if alphabet[i] in angles[j]:
                index_remove.append(angles[j])

    index_remove = remove_repeated_elements_from_array(index_remove)

    # removing wrong indexes
    [angles.remove(index_remove[i]) for i in range(len(index_remove))]

    # check and remove elements that can be a number
    index_remove = []
    for i in range(len(angles)):
        if angles[i].isdigit():
            index_remove.append(angles[i])

    index_remove = remove_repeated_elements_from_array(index_remove)
    [angles.remove(index_remove[i]) for i in range(len(index_remove))]

    # correcting a missing number
    for i in range(len(angles)):
        for j in range(len(angles[i])):
            if not angles[i][j].isdigit():
                if not angles[i][j - 1].isdigit():
                    change_angle_list = list(angles[i])
                    change_angle_list.insert(j, '0')
                    change_angle_list = ''.join(change_angle_list)
                    angles[i] = change_angle_list

    return angles


def tuples_referring_to_each_angle(string):
    characters = ['g', 'm', 's']

    if characters[0] not in string:
        string = f'0g{string}'

    if characters[1] not in string:
        string = f"{string[:string.index('g') + 1]}0m{string[string.index('g') + 1:]}"

    if characters[2] not in string:
        string = f"{string[:string.index('m') + 1]}0s"

    string = list(string)
    for i in range(len(string)):
        if str(string[i]).isdigit():
            ...
        else:
            if string[i] == string[-1]:
                string[i] = ''
            else:
                string[i] = ' '

    string = tuple(list(map(int, ''.join(string).split(' '))))

    return string


def create_dictionary(angles):
    listangles = read_different_angles(angles)
    dictionary = []
    for i in range(len(listangles)):
        dictionary.append(
            {
                'Chave': listangles[i],
                'Valor': tuples_referring_to_each_angle(listangles[i])
            }
        )

    return dictionary


"""
to create your list of keys (dictionary) just 
call the "create_dictionary()" function and 
pass the arguments you want: 

For example: 

    " 
        myDict = create_dictionary('12g 5m 12g2ms') 
        print(myDict)  
          
        OUTPUT:
          
        [
          {'Chave': '12g', 'Valor': (12, 0, 0)}, 
          {'Chave': '5m', 'Valor': (0, 5, 0)}, 
          {'Chave': '12g2m0s', 'Valor': (12, 2, 0)}
        ]
      
      "
    
NOTE: note that in the example above there is an 
argument which does not have a number followed by 
letters, but only a letter. however, our algorithm 
takes care of correcting it for you. A "0" is added 
before the letter that does not have a number.

"""

# Now it's up to you, carry on...
# TIP: Create a function to transform everything in
# seconds perform the calculation and transform it
# back into degrees minutes and seconds.


def sum_and_average_of_all_angles(array):
    ...
