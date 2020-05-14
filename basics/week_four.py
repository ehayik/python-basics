"""
For each character in the string saved in ael, append that character 
to a list that should be saved in a variable app.
"""
ael = "python!"
app = []

for val in ael:
    app.append(val)


"""
For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). 
Save these past tense words to a list called past_wrds.
"""
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds = [x + "ed" for x in wrds]


"""
Write code to add ‘horseback riding’ to the third position 
(i.e., right before volleyball) in the list sports.
"""
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, "horseback riding")


"""
Write code to take ‘London’ out of the list trav_dest.
"""
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove('London')


"""
Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
"""
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append("Guadalajara")


"""
Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
"""
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()


"""
Write code to switch the order of the winners list so that it is now Z to A. 
Assign this list to the variable z_winners.
"""
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.sort()
winners.reverse()
z_winners = winners
