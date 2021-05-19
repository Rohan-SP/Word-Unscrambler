# Rohan Patel

aTOz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']


# Checks to make sure only letters of the alphabet are in the string
def illegal_character(character_check):

    for r in character_check:
        if r not in aTOz:
            return True

    return False


# takes a word and returns the word ith characters in alphabetical order
def alpha_order(given):
    given = given.lower()
    output = ""
    for k in range(0, 26):
        for g in range(0, len(given)):
            if given[g] == aTOz[k]:
                output = output + aTOz[k]

    return output


def sequence_generator(given):

    # Makes sure int given is 16 or less since only 16 characters in  digits list
    if given > 16:
        print("given sequence integer cannot be greater than 16")
        return

    # Uses hexadecimal instead of decimal system for feature of more input string length
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    output = []
# previous
    # Lists used to track previous and current sequence lengths generated
    prev_list = []
    new_list = []

    for x in range(0, given):

        # Handles sequences of length 1 by copying all individual characters
        if x == 0:
            for y in range(0, given):
                output.append(digits[y])
                new_list.append(digits[y])

        # Handles the sequence of max length (given), by returning all character side by side
        elif x == given - 1:

            int_out = ""
            for w in range(0, given):
                int_out = int_out + digits[w]

            output.append(int_out)
            prev_list.append(int_out)
        # Handles all cases in between the first and last sequence generation
        else:
            # goes through the previous list
            for z in prev_list:
                # adds all digits after the last digit from the digits list to maintain alphabetical order when
                # translated and adds the list generated based off the previous list to the output
                for c in range(digits.index(z[len(z) - 1]) + 1, given):
                    new_list.append(z + digits[c])
                    output.append(z + digits[c])

        prev_list = new_list
        new_list = []

    return output


# takes a string and returns all possibilities of in order of alphabetical
def assign_to_sequence(stringgiven):

    if len(stringgiven) > 16:
        print("given sequence integer cannot be greater than 16")
        return "given sequence integer cannot be greater than 16"

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    stringgiven = alpha_order(stringgiven)
    int_sequence = sequence_generator(len(stringgiven))
    assigned_output = []

    # loops through each sequence generated
    for a in int_sequence:
        stringthing = ""

        # converts each digit for digits list to its corresponding value in the stringgiven
        for b in a:
            stringthing = stringthing + stringgiven[digits.index(b)]

        assigned_output.append(stringthing)

    return assigned_output


with open('language.txt', 'r') as language:
    word_list = language.readlines()

dictionary = {}

for i in range(0, len(word_list)):

    # removes the new line character if there is one at the end
    original_word = word_list[i].strip("\n")
    alphabetized_word = alpha_order(original_word)

    # adds words alphabetized as key and original as value and puts repeat values added to the already existing key
    if alphabetized_word in dictionary:
        dictionary[alphabetized_word] += ", " + original_word
    else:
        dictionary[alphabetized_word] = original_word

# After processing given txt file of words it will ask user for string of characters to unscramble
while True:
    word_given = input("\n\nGive a sequence of up to 16 letters and I'l give you words that can be made with "
                       "those letters. Type 0 to Exit\n--> ")

    # makes sure only words of length 16 or less are given
    if len(word_given) > 16:
        print("given sequence integer cannot be greater than 16")

    # Exit if 0
    elif word_given == "0":
        break

    # Checks for illegal characters
    elif illegal_character(word_given):
        print("\n\n***Please provide a string with only letters of the alphabet***\n")

    # Goes through the processes of giving the possible words from the scrambled string
    else:
        # Creates the sequences of possibles letters
        possible_words = assign_to_sequence(word_given)

        # Creates an empty output list
        output_list = []
        for i in range(0, len(possible_words) + 1):
            output_list.append("")

        # adds words to the list to be displayed to user
        for t in possible_words:
            if t in dictionary:
                output_list[len(t)] = output_list[len(t)] + dictionary[t] + ", "

        # Prints all words for the user to look at and continue
        for u in range(0, len(output_list)):
            if len(output_list[u]) != 0:
                print("\nThese are all the {} letter word(s):\n{}" .format(u, output_list[u].strip(", ")))

        # If no words can be generated from the given word
        if output_list.count("") == len(output_list):
            print("\nNo Words can be generated from \"{}\"" .format(word_given))

print("Exited.")
