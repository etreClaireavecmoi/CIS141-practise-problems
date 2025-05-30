#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
#it. Write a Python program that:
#- Reads the file
#- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#- Counts how many times each word appears
#- Creates a dictionary of the words and their counts
#- Print the dictionary to the console

#note, I tried this with a french song and it was quite tricky. I've included a second instance of the program with
#song_lyrics2.txt for a primarily english song for easier testing. 

allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789 éèàùçôêâîûëïüœ'
#this ended up being complicated with a french song, so ^ this brute force method was suggested as a way to filter out punctuation.

tracked_words = {}
with open('song_lyrics.txt', 'r') as file:
    lyrics = file.read().lower()
    filtered_lyrics = ''
    for i in lyrics:
        if i in allowed_chars:
            filtered_lyrics += i
    final_lyrics = filtered_lyrics.split()
    for i in range(5):
        word = input('What word would you like to track the count of? ')
        word = word.lower()
        count = final_lyrics.count(word)
        tracked_words[word] = count
    
print('\nHere are the words you tracked, along with how often they occured in the song!')
print(tracked_words)

'''
tracked_words = {}
with open('song_lyrics2.txt', 'r') as file:
    lyrics = file.read().lower()
    filtered_lyrics = ''
    for i in lyrics:
        if i in allowed_chars:
            filtered_lyrics += i
    final_lyrics = filtered_lyrics.split()
    for i in range(5):
        word = input('What word would you like to track the count of? ')
        word = word.lower()
        count = final_lyrics.count(word)
        tracked_words[word] = count
    
print('\nHere are the words you tracked, along with how often they occured in the song!')
print(tracked_words)
'''
