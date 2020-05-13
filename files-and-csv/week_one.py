
"""
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable num.
"""
with open("travel_plans.txt") as travel_plans:
    num = len(travel_plans.read())


"""
We have provided a file called emotion_words.txt that contains 
lines of words that describe emotions. Find the total number of words 
in the file and assign this value to the variable num_words.
"""
with open("emotion_words.txt") as emotion_words:
    num_words = len(emotion_words.read().split())


"""
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
"""
with open("school_prompt.txt") as school_prompt:
    num_lines = len(school_prompt.readlines())


"""
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
"""
with open("school_prompt.txt") as school_prompt:
    beginning_chars = school_prompt.read()[:30]

"""
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
"""    
with open("school_prompt.txt") as school_prompt:
    three = [x.split()[2] for x in school_prompt.readlines()]


"""
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
"""
with open("emotion_words.txt") as emotion_words:
    emotions = [x.split()[0] for x in emotion_words.readlines()]

"""
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, 
then add the word to a list called p_words.
"""
with open("school_prompt.txt") as school_prompt:
    p_words = [w for line in school_prompt.readlines() for word in line.split() if 'p' in word]    
