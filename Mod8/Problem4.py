#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
#by commas. Write a program that reads the poll.txt file
#Count how many votes "yea" or "nay" received and print the results.

yea_count = 0
nay_count = 0
with open('poll.txt', 'r') as file:
    poll = file.read()
    votes = poll.strip().split(',')
    # ^ strips whitespace before and after string
    for vote in votes:
        vote = vote.strip()
        # ^ again to remove white space inbetween entries
        if vote == 'yea':
            yea_count += 1
        elif vote == 'nay':
            nay_count += 1
print(f'Here are the results of the proposal:\nThere were {yea_count} in favour.\nThere were {nay_count} in opposition.')
