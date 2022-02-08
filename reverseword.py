# Giving an input string s, reverse the order of the words.
# Return a string of the word in reverse order concatenated by single space.


def reverseWord(s):

    i = len(s) - 1
    curWord = ''
    result = ''

    while (i >= 0):
        if (s[i] == " "):
            i -= 1
            if len(curWord) > 0:
                result += curWord
                result += ' '
                curWord = ''

        else:
            curWord = s[i] + curWord
            i -= 1

    result += curWord

    return result


word = "    the sky is blue"
print(reverseWord(word))
