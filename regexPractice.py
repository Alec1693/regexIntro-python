import re

##Basic Patterns
pattern = r"Cookie"
sequence = "Cookie"

if re.match(pattern,sequence):
    print("Match!")
else:
    print("Not a match!")

##The r at the start of r"Cookie" is called a raw string literal. It changes how the string literal is interpreted
##Such literals are stored as they appear
##For example, \ (backslash) is just a backslash when prefixed with an 'r' rather than being interpreted
##as an escape sequence

##A period . matches any single character except the newline character
re.search(r'Co.k.e','Cookie').group()
#Cookie

##A caret ^ matches the start of the string
re.search(r'^Eat',"Eat cake!").group()
#Eat

##However, the code below will not give the same result
##re.search(r'^eat',"Let's eat cake!").group()

## A $ matches the end of string
re.search(r'cake$',"Cake! Let's eat cake").group()
#cake

##The next search will return the NONE value, because cake isn't at the end of the string
##re.search(r'cake$',"Cake! Let's eat cake on our way home!").group()

##[abc] - matches a or b or c
##[a-zA-Z0-9] - matches any letter from (a to z) or (A to Z) or (0 to 9)
##Characters that are not within the range can be matched by complementing the set. If the first
##character of the set is ^, all the characters that are ot in that set will be matched
re.search(r'[0-6]','Number: 5').group()
#5

##Matches any character except 5
re.search(r'Number: [^5]','Number: 0').group()
#Number: 0
##This will not match and hence a NONE value will be returned
#re.search(r'Number: [^5]','Number:5').group()

##Backslash \
##If the character following the backslash \ is a recognized escape character, then the special meaning of
##the term is taken
##Scenario 1 - This treats '\s' as an escape character, '\s' defines a space
re.search(r'Not a\sregular character','Not a regular character').group()
#Not a regular character
##Scenario 2 - '\' is treated as an ordinary character, because '\r' is not a recognized escape character
re.search(r'Just a \regular character','Just a \regular character').group()
#Just a \regular character
##Scenario 3 - \s is escaped using an extra \ so it's interpreted as a literal string \s
#re.search(r'Just a \\sregular character','Just a \regular character').group()
#Just a \\sregular charater

##There is a predefined set of special sequences that begin with \ and are also very helpful when performing search
##and match
##\w - Lowercase w matches any single letter,digit,or underscore
##\W - matches any character not part of \w (lowercase w)
print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())

##Matches any character except single letter, digit, or underscore
print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

## Uppercase W won't match single letter, digit
print("Uppercase W won't match, and return:", re.search(r'Co\Wk\We', 'Cookie'))

##Lowercase \s matches a single white space character like space,newline,tab,return
print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
##Upercase \S matches any character not part of \s
print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

##Lowercase \d matches decimal digit 0-9
print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())
#How many cookies do you want?  100
##Uppercase \D matches any character that is not a decimal digit
print("How many cookies do you want? ", re.search(r'\D+', '100 cookies').group())
#How many cookies do you want?   cookies

##The + symbol used after the \d is used for repetition.
##\t lowercase t matches tab
##\n lowercase n matches newline
##\r matches return
##\A matches only the start of the string. Works across multiple lines as well
##\Z matches only at the end of the string
##^ and \A are effectively, and so are $ and \Z.. Except when dealing with MultiLine mode

##\b matches only the beginning or end of the word
# Example for \t
print("\\t (TAB) example: ", re.search(r'Eat\tcake', 'Eat    cake').group())
# Example for \b
print("\\b match gives: ",re.search(r'\b[A-E]ookie', 'Cookie').group())

##+ checks if the preceding character appears one or more times starting from that position
re.search(r'Co+kie', 'Cooookie').group()
#'Cooookie'

##* checks if the preceding character appears zero or more times starting from that position
# Checks for any occurrence of a or o or both in the given sequence
re.search(r'Ca*o*kie', 'Cookie').group()
#'Cookie'

##? Checks if the preceding character appears exactly zero or one time starting from that position
# Checks for exactly zero or one occurrence of a or o or both in the given sequence
re.search(r'Colou?r', 'Color').group()
#'Color'

##Check for an exact number of sequence repetition
#{x} repeat exactly x nuber of times
#{x,} repeat at least x times ore more
#{x,y} repeat at least x times but no more than y times
re.search(r'\d{9,10}', '0987654321').group()
#'0987654321'
#The + and * qualifies are said to be greedy

##Group feature of regular expressions allows you to pick up parts of the matching text. Parts of a regular expression
##pattern bounded by parenthesis() are called groups. The () does not change what the expression matches, but rather
##forms groups within the matched sequence. You have been using group() function all along. Th plain match.group()
##without any argument is still the whoe matched text as usual
statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)

##Another way of doing the same thing with the usage of <> brackets instead. This will let you create named groups
##Syntax for creating name group is (?P<name>...)
statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
if statement:
  print("Email address:", match.group('email'))
  print("Username:", match.group('username'))
  print("Host:", match.group('host'))

##when a special character matches as much of the search sequence as possible, it is said to be a 'Greedy' match
##it is normal behavior of regex, but not always desired
pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*>', heading).group()
#'<h1>TITLE</h1>'
#the partern <.*> matched the whole string, However if you only wantedto match the first <h1> tag you couldve used
#a greedy qualifier *? that matches as little text as possible
heading  = r'<h1>TITLE</h1>'
re.match(r'<.*?>', heading).group()
#'<h1>'


