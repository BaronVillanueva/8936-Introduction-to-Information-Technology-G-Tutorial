'''celsius = 10
print("Celsius\tFahrenheit")
while celsius <=30:
 f = (9/5 * celsius) + 32
 print("{0:^6}\t{1:^10.0f}".format(celsius, f))
 celsius += 5
 
##: is format, ^ center, ^6 means six characters
##.0f means no decimal place

count = 0
phrase = input("Enter a phrase: ").lower()
vowels = ['a','e','i','o','u']
while i in vowels:
    if i in phrase:
        count+=1

print("Phrase has ", i, " vowels")

'''
vowel = "aeiou"
phrase = input("Enter a phrase: ").lower()
vowelcounter = 0
for letter in phrase:
    if letter in vowel:
        vowelcounter+=1
print(f"There are {vowelcounter} vowels.")
