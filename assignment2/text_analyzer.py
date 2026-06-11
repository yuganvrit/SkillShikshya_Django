def analyze_text(text):
    print('word_count: ', len(text))

    word_without_spaces  = 0
    frequent_word = {}
    sentence = 0
    for i in text.lower():

        #counts word without spaces.
        if i != " ":
            word_without_spaces +=1

            #counts no. of sentence.
            if i in '?.!':
                sentence += 1

            print("No of sentences split by ?!. is: ", sentence)

            #gets the most frequent word
            if frequent_word.get(i) is None:
                frequent_word[i] = 1
            else:
                frequent_word[i] += 1
    print('total character count without spaces: ', word_without_spaces)   
    
   
    maximum_word = -1
    for key, value in frequent_word.items():
        # print(key, value)
        if maximum_word < value:
            maximum_word = value
            most_used_word = key

    print('frequent word: ', most_used_word)

    
    
analyze_text('santosh is a good boy. is he is a very excellent boy? wow! i doubt this is good.')


