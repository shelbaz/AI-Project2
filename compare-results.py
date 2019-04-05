baseline_right = 0
baseline_wrong = 0

stopword_right = 0
stopword_wrong = 0

wordlength_right = 0
wordlength_wrong = 0

with open('baseline-result.txt', 'r') as f:
    baseline = f.read().split('\n')
    baseline.remove('')
    baseline = [e.split(' ')[-1] for e in baseline]

    for x in baseline:
        if x == 'right':
            baseline_right += 1
        else:
            baseline_wrong += 1

    print(f'Baseline accuracy: {baseline_right / (baseline_right + baseline_wrong)}\n')

with open('stopword-result.txt', 'r') as f:
    stopword = f.read().split('\n')
    stopword.remove('')
    stopword = [e.split(' ')[-1] for e in stopword]

    for x in stopword:
        if x == 'right':
            stopword_right += 1
        else:
            stopword_wrong += 1

    print(f'Stopword accuracy: {stopword_right / (stopword_right + stopword_wrong)}\n')

with open('wordlength-result.txt', 'r') as f:
    wordlength = f.read().split('\n')
    wordlength.remove('')
    wordlength = [e.split(' ')[-1] for e in wordlength]

    for x in wordlength:
        if x == 'right':
            wordlength_right += 1
        else:
            wordlength_wrong += 1

    print(f'Wordlength accuracy: {wordlength_right / (wordlength_right + wordlength_wrong)}\n')
