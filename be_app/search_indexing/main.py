import inflect
from .utils import split_words

p = inflect.engine()

PRODUCTS_SEARCH_INDEX = {

}


def add_word_to_index(word, document_id):
  if word.strip() == '' or word is None :
    return

  word = p.singular_noun(word) if p.singular_noun(word) != False else word
  if word not in PRODUCTS_SEARCH_INDEX:
    PRODUCTS_SEARCH_INDEX[word] = []
  
  PRODUCTS_SEARCH_INDEX[word].append(document_id)


def search_word_in_index(word):
  word = p.singular_noun(word) if p.singular_noun(word) != False else word
  return PRODUCTS_SEARCH_INDEX.get(word, None)


def add_list_to_index(list_of_words, document_id):
  splitted_words = split_words(list_of_words)
  for word in splitted_words:
    add_word_to_index(word, document_id)


def search_index(sentence):
  splitted_words = split_words([sentence])
  obj_list = []
  for word in splitted_words:
    matches = search_word_in_index(word)
    if matches:
      obj_list.extend(matches)

  return set(obj_list)