most_common_delimeters = ['-', ',', '.', ':', ' ', '(', ')']

def split_words(list_of_words):
  return_list = []
  for word in list_of_words:
    delimeter = [delimeter for delimeter in most_common_delimeters if delimeter in word]
    if len(delimeter) > 0:
      splitted = word.split(delimeter[0])
      return_list.extend(split_words(splitted))
    else:
      return_list.append(word)

  return [word for word in return_list if word != '']

