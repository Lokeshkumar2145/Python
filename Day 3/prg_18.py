'''Write a Python program to check whether an alphabet is a vowel or consonant.
'''

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
else:
    print("%s is a consonant." % l)
	