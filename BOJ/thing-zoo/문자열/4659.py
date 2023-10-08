vowel = 'aeiou'

while True:
    word = input()
    if word == 'end':
        break

    count1 = 0
    count2 = 0
    contain_vowel = False
    error = False
    for i in range(len(word)):
        if word[i] in vowel:
            contain_vowel = True
            count1 += 1
            count2 = 0
        else:
            count1 = 0
            count2 += 1

        if count1 == 3 or count2 == 3:
            error = True
            break
    
        if i > 0 and word[i-1] == word[i]:
            if word[i] != 'e' and word[i] != 'o':
                error = True
                break

    if contain_vowel and not error:
        print('<' + word + '> is acceptable.')
    else:
        print('<' + word + '> is not acceptable.')