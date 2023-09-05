# https://leetcode.com/problems/vowel-spellchecker

import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        lower_words = {}
        without_vowel = {}
        for word in wordlist:
            if word.lower() in lower_words:
                lower_words[word.lower()].append(word)
            else:
                lower_words[word.lower()] = [word]

            vowels = "aeiouAEIOU"
            if re.sub(rf'[{vowels}]', "!", word).lower() in without_vowel:
                without_vowel[re.sub(rf'[{vowels}]', "!",
                                     word).lower()].append(word)
            else:
                without_vowel[re.sub(rf'[{vowels}]', "!", word).lower()] = [
                    word]

        correct = []
        for query in queries:
            if query in wordlist:
                correct.append(query)
            elif query.lower() in lower_words:
                correct.append(lower_words[query.lower()][0])
            elif re.sub(rf'[{vowels}]', "!", query).lower() in without_vowel:
                correct.append(without_vowel[re.sub(
                    rf'[{vowels}]', "!", query).lower()][0])
            else:
                correct.append("")
        return correct
