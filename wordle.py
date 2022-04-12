import random

def create_list(lines):
    i = 0
    list = []
    for l in lines:
        item = []
        list.append(item)
        item[:0] = l
        i = i + 1
    return list

def result_is_valid(result):
    if (len(result)!=5):
        return False
    for j in range(5):
        if (result[j] == 'b' or result[j] == 'g' or result[j] == 'y'):
            pass
        else:
            return False
    return True

def delete_words_with_letter(list,letter):
    i = 0
    while (i < len(list)):
        item = list[i]
        if letter in item:
            list.remove(item)
            i = i - 1
        i = i + 1
    return list

def delete_words_with_letter_in_position(list,letter,pos):
    i = 0
    while (i < len(list)):
        item = list[i]
        if item[pos] == letter:
            list.remove(item)
            i = i - 1
        i = i + 1
    return list

def delete_words_without_letter_in_position(list,letter,pos):
    i = 0
    while (i < len(list)):
        item = list[i]
        if item[pos] != letter:
            list.remove(item)
            i = i - 1
        i = i + 1
    return list

def delete_words_without_letter(list,letter):
    i = 0
    while (i < len(list)):
        item = list[i]
        if letter not in item:
            list.remove(item)
            i = i - 1
        i = i + 1
    return list

def delete_words_with_letter_in_positions(list,letter,positions):
    i = 0
    for pos_i in positions:
        if pos_i == 'b':
            list = delete_words_with_letter_in_position(list,letter,i)
        i = i + 1
    return list

def reduce_list(list,word,result):
    i = 0
    checked_letters = []
    for result_i in result:
        letter = word[i]
        if (result_i == 'g'):
            list = delete_words_without_letter_in_position(list,letter,i)
            checked_letters.append(letter)
        i = i + 1
    i = 0
    for result_i in result:
        letter = word[i]
        if (result_i == 'y'):
            list = delete_words_with_letter_in_position(list,letter,i)
            list = delete_words_without_letter(list,letter)
            checked_letters.append(letter)
        i = i + 1
    i = 0
    for result_i in result:
        letter = word[i]
        if letter in checked_letters:
            if (result_i == 'b'):
                list = delete_words_with_letter_in_positions(list,letter,result)
        else:
            if (result_i == 'b'):
                list = delete_words_with_letter(list,letter)
        i = i + 1
    return list

def word_is_valid(word,lines):
    if word in lines:
        return True
    return False

def recommended_word(list):
    val = random.randint(0,len(list)-1)
    return (''.join(list[val]).upper())

def print_words(list):
    list2 = list.copy()
    for a in range(len(list2)):
        list2[a] = ''.join(list2[a]).upper()
    print(list2)

def main():
    with open('bank.txt') as f:
        lines = f.readlines()
    i = 0
    while (i < len(lines)):
        lines[i] = lines[i].replace('\n','')
        i = i + 1
    list = create_list(lines)
    done = False
    it = 0
    while (done==False):
        it = it + 1
        if it == 7:
            print('FAILED to solve Wordle.')
            return
        if len(list) != 1:
            print('==> There are ' + str(len(list)) + ' current possible words.')
            if (it != 1):
                print_words(list)
        if (it > 1):
            r_w = recommended_word(list)
            if len(list) == 1:
                print('===> The SOLUTION is: ' + r_w)
            else:
                print('===> A POSSIBLE word is: ' + r_w)
        word = input('Try # ' + str(it) +' >> Insert word: ').lower()
        if word_is_valid(word,lines) == False:
            print('ERROR: Not a valid word.')
            it = it - 1
        else:
            keep_asking = True
            while (keep_asking == True):
                result = input('Insert result [B,Y,G]: ').lower()
                if result == 'ggggg':
                    print('DONE. Wordle is solved.')
                    return
                if result_is_valid(result):
                    keep_asking = False
                    list = reduce_list(list,word,result)
                else:
                    print('ERROR: Not a valid result. Must be five charecters and only B, Y, and G characters.')

main()
