total_document_count = 1999
total_ham_train = 1001
total_spam_train = 998

file_num_ham = 1
file_num_spam = 1

vocabulary_ham = {}
count_ham = 0

vocabulary_spam = {}
count_spam = 0

while True:
    next_number = '{0:0{width}}'.format(file_num_ham, width=5)

    try:
        with open(f'test/test-ham-{next_number}.txt', 'r') as f:

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
        with open(f'test/test-spam-{next_number}.txt', 'r') as f:

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


