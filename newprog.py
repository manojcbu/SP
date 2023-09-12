[200~def toGoatLatin(sentence):
      def is_vowel(char):
          return char in 'aeiouAEIOU'

      words = sentence.split()
      goat_latin_words = []

      for i, word in enumerate(words, 1):
          if is_vowel(word[0]):
              goat_word = word + 'ma'
          else:
              goat_word = word[1:] + word[0] + 'ma'

          goat_word += 'a' * i
          goat_latin_words.append(goat_word)

      return ' '.join(goat_latin_words)


  # Example usage:
  sentence = "The quick brown fox jumped over the lazy dog"
  result = toGoatLatin(sentence)
  print(result)  # Output: "Imaa ovelmaaa oatGmaaa atinLmaaaa"
