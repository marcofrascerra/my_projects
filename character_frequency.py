# This function will tell you what's the frequency of each character in a string

def frequency(string):

    answer = {}

    for i in string:

        if i in answer.keys():

            continue

        else:

            cursor = string.index(i) + 1

            counter = 1

            while cursor != len(string):

                if i == string[cursor]:

                    counter += 1

                cursor += 1

            answer.update({i: counter})

    return answer


test = "ababcc"

print(frequency(test))
