def most_frequent(string):
    dict1 ={}
    for letter in string:
        if letter in dict1.keys():
            dict1[letter] += 1
        else:
            dict1[letter] = 1
    print("Output:",end='')
    print(dict1)
    print("Sorted Output:",sorted(dict1.items(), key = lambda t :t[1]))
most_frequent("Mississippi")