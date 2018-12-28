#Write a function called censor that takes two strings, text and word, as input.
#It should return the text with the word you chose replaced with asterisks.
#For example:
#censor("this hack is wack hack", "hack")
#should return:
#"this **** is wack ****"
#Assume your input strings won't contain punctuation or upper case letters.
#The number of asterisks you put should correspond to the number of letters in the censored word.


def censor(text,word):
  text = text.split(" ")
  for char in range(0,len(text)):
    if text[char]==word:
      text[char] = len(text[char]) * "*"
    else:
      text[char]=text[char]
  
  text = " ".join(text)
  return text
