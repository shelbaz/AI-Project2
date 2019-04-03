import re
import math

total_document_count = 1999
total_ham_train = 1001
total_spam_train = 998

prob_ham = total_ham_train/total_document_count
prob_spam = total_spam_train/total_document_count

file_num_ham = 1
file_num_spam = 1

vocabulary_ham = {}
count_ham = 0

vocabulary_spam = {}
count_spam = 0

vocab_size = 59953
total_count_spam = 850106
total_count_ham = 557066

# while True:
#     next_number = '{0:0{width}}'.format(file_num_ham, width=5)

#     try:
#         with open(f'test/test-ham-{next_number}.txt', 'r', encoding='latin-1') as f:

#             content = f.read().lower()
#             raw_tokens = re.split('[^a-zA-Z]', content)
#             tokens = [x for x in raw_tokens if x != '']

#             for token in tokens:
#                 count_ham += 1

#                 if vocabulary_ham.get(token):
#                     vocabulary_ham[token] += 1
#                 else:
#                     vocabulary_ham[token] = 1
#     except FileNotFoundError:
#         print(f'Done with {file_num_ham} ham files.')
#         break

#     file_num_ham += 1

# while True:
#     next_number = '{0:0{width}}'.format(file_num_spam, width=5)

#     try:
#         with open(f'test/test-spam-{next_number}.txt', 'r', encoding='latin-1') as f:

#             content = f.read().lower()
#             raw_tokens = re.split('[^a-zA-Z]', content)
#             tokens = [x for x in raw_tokens if x != '']

#             for token in tokens:
#                 count_spam += 1

#                 if vocabulary_spam.get(token):
#                     vocabulary_spam[token] += 1
#                 else:
#                     vocabulary_spam[token] = 1
                

#     except FileNotFoundError:
#         print(f'Done with {file_num_spam} spam files.')
#         break

#     file_num_spam += 1

def naive_classifier():
    final_file = []
    classification_ham = {}
    classification_spam = {}

    with open('model.txt', 'r') as f1:
        lines = f1.readlines()
        for line in lines:
            info  = line.split('  ')
            word = info[1]
            conditional_prob_ham = info[3]
            conditional_prob_spam = info[5]
            classification_ham[word] = remove_exp(conditional_prob_ham)
            classification_spam[word] = remove_exp(conditional_prob_spam)
    
    while True:
        next_number = '{0:0{width}}'.format(file_num_ham, width=5)

        try:
            line_count = file_len(f'test/test-ham-{next_number}.txt')
            with open(f'test/test-ham-{next_number}.txt', 'r', encoding='latin-1') as f:
                content = f.read().lower()
                raw_tokens = re.split('[^a-zA-Z]', content)
                tokens = [x for x in raw_tokens if x != '']

                score_ham = math.log10(float(prob_ham))
                score_spam = math.log10(float(prob_spam))

                for token in tokens:
                    if classification_ham.get(token):
                        score_ham = score_ham + math.log10(float(classification_ham[token]))
                    else:
                        new_cond_prob_ham = (0.5)/(total_count_ham + vocab_size*0.5 + 0.5)
                        score_ham = score_ham + math.log10(float(new_cond_prob_ham))
                    
                    if classification_spam.get(token):
                        score_spam = score_spam + math.log10(float(classification_spam[token]))
                    else:
                        new_cond_prob_spam = (0.5)/(total_count_spam + vocab_size*0.5 + 0.5)
                        score_spam = score_spam + math.log10(float(new_cond_prob_spam))
                    
                filename = 'test-ham-{next_number}.txt'
                final_classification = 'ham' if score_ham > score_spam else 'spam'
                actual_classification = 'ham'
                correct = 'right' if final_classification == actual_classification else 'wrong'
                final_file.append(
                    f'{line_count}  {filename}  {final_classification}  {score_ham}  {score_spam}  {actual_classification}  {correct}\n')
        
        except FileNotFoundError:
            print(f'Done with {file_num_ham} ham files.')
            break

    print('Done processing the hams.')

    while True:
        next_number = '{0:0{width}}'.format(file_num_spam, width=5)

        try:
            line_count = file_len(f'test/test-spam-{next_number}.txt')
            with open(f'test/test-spam-{next_number}.txt', 'r', encoding='latin-1') as f:
                content = f.read().lower()
                raw_tokens = re.split('[^a-zA-Z]', content)
                tokens = [x for x in raw_tokens if x != '']

                score_ham = math.log10(float(prob_ham))
                score_spam = math.log10(float(prob_spam))

                print('score_ham' + str(score_ham))
                print('score_spam'+ str(score_spam))
                
                for token in tokens:
                    if classification_ham.get(token):
                        score_ham = score_ham + math.log10(float(classification_ham[token]))
                    else:
                        new_cond_prob_ham = (0.5)/(total_count_ham + vocab_size*0.5 + 0.5)
                        score_ham = score_ham + math.log10(float(new_cond_prob_ham))
                    
                    if classification_spam.get(token):
                        score_spam = score_spam + math.log10(float(classification_spam[token]))
                    else:
                        new_cond_prob_spam = (0.5)/(total_count_spam + vocab_size*0.5 + 0.5)
                        score_spam = score_spam + math.log10(float(new_cond_prob_spam))

                score_ham = math.log10(score_ham)
                score_spam = math.log10(score_spam)
                filename = 'test-spam-{next_number}.txt'
                final_classification = 'ham' if score_ham > score_spam else 'spam'
                actual_classification = 'spam'
                correct = 'right' if final_classification == actual_classification else 'wrong'
                final_file.append(
                    f'{line_count}  {filename}  {final_classification}  {score_ham}  {score_spam}  {actual_classification}  {correct}\n')

        except FileNotFoundError:
            print(f'Done with {file_num_spam} spam files.')
            break

    print('Done processing the spams.')

    with open('classifier.txt', 'w') as myfile:
        for line in final_file:
            myfile.write(f'{line}')


def remove_exp(number):
    value = str(number)
    value2 = value.replace(',', '.')
    answer = float(value2)
    answer = format(answer, '.9f')
    return answer

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

naive_classifier()
