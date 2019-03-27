import re
import sys

file_num_ham = 1
file_num_spam = 1

vocabulary_ham = {}
count_ham = 0

vocabulary_spam = {}
count_spam = 0

while True:
    next_number = '{0:0{width}}'.format(file_num_ham, width=5)

    try:
        with open(f'train/train-ham-{next_number}.txt', 'r') as f:

            content = f.read().lower()
            raw_tokens = re.split('[^a-zA-Z]', content)
            tokens = [x for x in raw_tokens if x != '']

            for token in tokens:
                count_ham += 1

                if vocabulary_ham.get(token):
                    vocabulary_ham[token] += 1
                else:
                    vocabulary_ham[token] = 1
    except FileNotFoundError:
        print(f'Done with {file_num_ham} ham files.')
        break

    file_num_ham += 1

while True:
    next_number = '{0:0{width}}'.format(file_num_spam, width=5)

    try:
        with open(f'train/train-spam-{next_number}.txt', 'r') as f:

            content = f.read().lower()
            raw_tokens = re.split('[^a-zA-Z]', content)
            tokens = [x for x in raw_tokens if x != '']

            for token in tokens:
                count_spam += 1

                if vocabulary_spam.get(token):
                    vocabulary_spam[token] += 1
                else:
                    vocabulary_spam[token] = 1
    except FileNotFoundError:
        print(f'Done with {file_num_spam} spam files.')
        break

    file_num_spam += 1

delta = 0.5
vocabulary_size = len(list(vocabulary_ham.keys()) + list(set(list(vocabulary_spam.keys())) - set(list(vocabulary_ham.keys()))))

with open('model.txt', 'w') as f:
    merged_vocab = []

    for word, freq_ham in vocabulary_ham.items():
        freq_spam = vocabulary_spam.pop(word, 0)

        prob_ham = (freq_ham + delta) / (count_ham + delta*vocabulary_size)
        prob_spam = (freq_spam + delta) / (count_spam + delta*vocabulary_size)

        merged_vocab.append(f'{word}  {freq_ham + delta}  {float("{0:.3g}".format(prob_ham))}  {freq_spam + delta}  {float("{0:.3g}".format(prob_spam))}\n')

    for word, freq_spam in vocabulary_spam.items():
        if vocabulary_ham.get(word):
            print('We screwed up.')
            sys.exit()
        
        freq_ham = 0

        prob_ham = (freq_ham + delta) / (count_ham + delta*vocabulary_size)
        prob_spam = (freq_spam + delta) / (count_spam + delta*vocabulary_size)

        merged_vocab.append(f'{word}  {freq_ham + delta}  {float("{0:.3g}".format(prob_ham))}  {freq_spam + delta}  {float("{0:.3g}".format(prob_spam))}\n')
        
    sorted_vocab = sorted(merged_vocab)

    vocab_counter = 0

    for string in sorted_vocab:
        vocab_counter += 1

        f.write(f'{vocab_counter}  {string}')
