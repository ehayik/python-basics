# Dictionary Mechanics

"""
At the halfway point during the Rio Olympics, the United States had 70 medals, 
Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany 
had 17 medals. Create a dictionary assigned to the variable medal_count with the country 
names as the keys and the number of medals the country had as each key’s value.
"""
medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17}


"""
Given the dictionary swimmers, add an additional key-value pair to the dictionary 
with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.
"""
swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4}
swimmers['Phelps'] = 23


"""
The dictionary golds contains information about how many gold medals each country won 
in the 2016 Olympics. But today, Spain won 2 more gold medals. Update golds to reflect this information.
"""
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] = golds["Spain"] + 2


"""
Create a list of the countries that are in the dictionary golds, and assign 
that list to the variable name countries. Do not hard code this.
"""
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = golds.keys()


"""
Provided is the dictionary, medal_count, which lists countries and their respective medal count at 
the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value 
for "Belarus" to the variable belarus. Do not hardcode this.
"""
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 
                'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 
                'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 
                'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 
                'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 
                'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}

belarus = medal_count['Belarus']


# Dictionary Accumulation

"""
The dictionary Junior shows a schedule for a junior year semester. 
The key is the course name and the value is the number of credits. 
Find the total number of credits taken this semester and assign it to the variable credits. 
Do not hardcode this – use dictionary accumulation!
"""
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for val in Junior.values():
    credits += val


"""
Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
"""
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:
    freq[char] = str1.count(char)


"""
Create the dictionary characters that shows each character from the string sally and its frequency. 
Then, find the most frequent letter based on the dictionary. 
Assign this letter to the variable best_char.
"""
sally = "sally sells sea shells by the sea shore"
characters = {}

for char in sally:
    characters[char] = sally.count(char)

dict_items = characters.items()
best_char, best_value = dict_items[0]

for i in range(1, len(dict_items)):
    key, value = dict_items[i]
    if value > best_value:
        best_char, best_value = dict_items[i]

