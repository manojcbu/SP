class Solution:
    def toGoatLatin(self, sentence):
        def is_vowel(char):
            return char.lower() in ['a', 'e', 'i', 'o', 'u']

        words = sentence.split()
        result = []

        for i, word in enumerate(words, 1):
            if is_vowel(word[0]):
                result.append(word + "ma" + "a" * i)
            else:
                result.append(word[1:] + word[0] + "ma" + "a" * i)

        return " ".join(result)

solution = Solution()
result = solution.toGoatLatin("I love Python")
print(result)


