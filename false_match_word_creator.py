import re

false_words_file = open('false_words.txt', 'r').read().split(',')
false_words = [w.strip(' ') for w in false_words_file]
false_words = [w for w in false_words if w !='']
print len(false_words), false_words
#import_length = len(false_words_file)

correct_words_file = open('correct_words.txt', 'r').read().split(',')
correct_words = [w.strip(' ') for w in correct_words_file]
correct_words = [w for w in correct_words if w !='']
print len(correct_words), correct_words

# file with sentiment list word and text word match
file = open('matches.txt', 'r').read().split('\n')


# initialize raw input variable
p = ''


for r in file:
    r1, r2 = r.split('\t')[0].strip(' '), r.split('\t')[1].strip(' ')
    r1 = re.sub('^\W+|\W+$', '', r1)
    if p == 'esc': break
    if any(w in r1 for w in false_words) == False and any(w in r1 for w in correct_words) == False and r1 != r2:
        undecided = True
        while undecided == True:
            print ''
            print r1, '    ', 'matched with:    ', r2
            p = raw_input('y: accept matched, n: exclude matched, or type exclusion: to add variant')
            if p == "y":
                print r1
                correct_words.append(r1)
                undecided = False
            if p == 'n':
                false_words.append(r1)
                undecided = False
            if p == 'esc': break
            elif p != 'y' and p != 'n' and p!= 'esc':
                conf = raw_input('are you sure you want to add    %s    to the list? y if yes, any other will reset input' % p)
                if conf == 'y':
                    false_words.append(p)
                    undecided = False
                else: undecided = True


false_words_file_write = open('false_words.txt', 'w')
for w in false_words: false_words_file_write.write(w + ', ')

correct_words_file_write = open('correct_words.txt', 'w')
for w in correct_words: correct_words_file_write.write(w + ', ')

