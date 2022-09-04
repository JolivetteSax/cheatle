#inspired by https://github.com/regexer/wordler

from bottle import request, response, run
from bottle import post, get, put, delete
import json
import re


from nltk.corpus import words as nltk_words
dictionary = dict.fromkeys(nltk_words.words(), None)
print("Dictionary size: " + str(len(dictionary)))

def is_english_word(word):
  try:
    x = dictionary[word.lower()]
    return True
  except KeyError:
    #print(word + " is not a word")
    return False

@get('/')
@get('/<known>')
@get('/<known>/<missplaced>')
@get('/<known>/<missplaced>/<missing>')
def handler(known = '*', missplaced = '*', missing = '*'):
    results = ['']

    matrix = [[], [], [], [], []]

    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    #For test/debug
    #possible = 'AB';

    if missing != '*':
      possible = re.sub(f'[{missing}]', '', possible)

    if known == '*':
      known = '_____'

    if missplaced == '*':
      missplaced = '_____'

    if len(known) != 5:
      raise ValueError('Improper length of wordle')

    #Generate first pass possible matrix of results
    for i in range(0,5):
      if known[i] != '_':
        matrix[i] = [known[i]]
      elif missplaced[i] != '_':
        matrix[i] = re.sub(f'[{missplaced[i]}]', '', possible)
      else:
        matrix[i] = possible

    # Generate word lists from matrix
    for listing in matrix:
      concats = []
      for existing in results:
        for letter in listing:
          concats.append(existing + letter);
      results = concats

    # Remove all words which do not contain misplaced chars

    required = re.sub('[_]', '', missplaced)
    if len(required) > 0:
      elim = []
      for word in results:
        if re.search(f'[{required}]', word):
          elim.append(word)

      results = elim;

    # and all strings which are not real words
    elim = []
    for word in results:
      if is_english_word(word):
        elim.append(word)
    results = elim

    if len(results) > 15:
      print("truncated long list")
      del results[15:]

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'known': known, 'missplaced': missplaced, 
    'missing': missing, 'results': results })

if __name__ == '__main__':
    run(host = '127.0.0.1', port = 8000)
