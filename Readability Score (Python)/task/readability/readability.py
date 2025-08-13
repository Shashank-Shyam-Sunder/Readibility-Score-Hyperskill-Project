# Write your code here
if __name__ == "__main__":
    import argparse
    import math
    import re
    import nltk

    from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize

    ### STEP 1: Parsing the file name from the command line interface using argparse module of Python
    parser = argparse.ArgumentParser(description="Please mention the text file name while running the script"
                                                 "in the terminal as python <script_name.py> <file_name.txt> <longman_words.txt>")
    parser.add_argument("file_name1", help="The text file name")
    parser.add_argument("file_name2", help="The Longman words file")

    args = parser.parse_args()
    file_name1 = args.file_name1
    file_name2 = args.file_name2

    ### STEP 2: Reading the text from the file
    file = open(file_name1, "r")
    text = file.read()
    file.close()
    print(f"Text: {text}")

    file = open(file_name2, "r")
    longman_words = set(word.strip() for word in file if word.strip())
    file.close()
    # print(f"Text: {longman_words}")
    # print(type(longman_words))
    # longman_words = [word.lower() for word in longman_words.split()]

    words = re.findall(r"\b\w+\b", text)
    difficult_words = 0
    for word in words:
        # if re.search(word, longman_words, flags=re.IGNORECASE):
        if word in longman_words:
            pass
        else:
            difficult_words += 1

    # words_all = re.findall(r"\b\w+\b", text)
    # syllables_count = 0
    #
    # for word in words_all:
    #     if not re.search(r"[aeiouyAEIOUY]", word):
    #         syllables_count += 1  # assume 1 syllable for vowel-less word
    #         continue
    #
    #     match = re.findall(r"[aeiouyAEIOUY]", word)
    #
    #     if len(match) == 1:
    #         syllables_count += 1
    #     else:
    #         syllables_word_count = len(match)
    #         match_2_vowles = len(re.findall(r"[aeiouyAEIOUY]{2}", word))
    #         if match_2_vowles:
    #             syllables_word_count -= match_2_vowles
    #         match_3_vowels = len(re.findall(r"[aeiouyAEIOUY]{3}", word))
    #         if match_3_vowels:
    #             syllables_word_count += match_3_vowels
    #         syllables_count += syllables_word_count
    #
    #     if word.endswith("e"):
    #         syllables_count -= 1

    import pyphen

    def count_syllables(text, lang='en_US'):
        dic = pyphen.Pyphen(lang=lang)
        words = text.split()
        syllable_count = 0

        for word in words:
            hyphenated = dic.inserted(word)
            if hyphenated:
                syllable_count += hyphenated.count('-') + 1
            else:
                syllable_count += 1  # fallback

        return syllable_count


    syllables_count = count_syllables(text)

    ### STEP 3: Counting the number of characters in the text except \n, \s and \t characters
    text_clean = text.replace(" ", "").replace("\n", "").replace("\t", "")
    no_char = len(text_clean)

    ### STEP 4: Tokenize the text data into sentences using sent_tokenize and then into words using regexp_tokenize from ntlk library
    ###         to count the number of sentences and words in the sentences
    sentences = sent_tokenize(text)
    no_words_dict = {}
    for _ in range(len(sentences)):
        words = regexp_tokenize(sentences[_], "[0-9A-z']+")
        no_words = len(words)
        no_words_dict[_+1] = no_words

    no_words_total = sum(list(no_words_dict.values()))

    ## Printing the number of characters, sentences and words
    print(f"Characters: {no_char}")
    print(f"Sentences: {len(sentences)}")
    print(f"Words: {no_words_total}")
    print(f"Difficult Words: {difficult_words}")
    print(f"Syllables: {syllables_count}")

    ### STEP: 5 Computing the Automated readability index for English texts designed to gauge the understanding of a text.
    ## STEP: 5.1 Creating the score dictionary for further mapping of the score to the Age range
    score_dict = {}
    for _ in range(1,14):
        score_dict[_] = f"{_+4}-{_+5}"
    score_dict[14] = "18-22"

    ## STEP: 5.2 Computing the score Automated readability index
    score = 4.71 * no_char / no_words_total + 0.5 * no_words_total / len(sentences) - 21.43
    score = math.ceil(score)

    ## STEP 5.3 Computing the score of the Flesch-Kincaid readability test
    score_fk = 0.39 * (no_words_total / len(sentences)) + 11.8 * (syllables_count/no_words_total) - 15.59
    score_fk = math.ceil(score_fk)

    ### STEP 5.4 Counting the Dale-Chall Readability Index
    score_dc = 0.1579 * difficult_words / no_words_total * 100 + 0.0496 * no_words_total / len(sentences)

    if difficult_words/len(words) < 0.05:
        score_dc = score_dc
        score_dc =  math.ceil(score_dc)
    else:
        score_dc = score_dc + 3.6365
        score_dc = math.ceil(score_dc)

    print()
    # print(f"Automated Readability Index: {score} (this text should be understood by {score_dict[score]} year olds).")
    print(f"Automated Readability Index: {score} (about the {score_dict[score]} year olds).")
    print(f"Flesch–Kincaid Readability Test: {score_fk} (about the {score_dict[score_fk]} year olds).")
    print(f"Dale-Chall Readability Index: {score_dc}. The text can be understood by {score_dict[score_dc]} year olds.")
    avg_age_to_read = score_dict[score] + " " + score_dict[score_fk] + " " + score_dict[score_dc]
    age_numbers = re.findall(r"\b\d+\b", avg_age_to_read)
    age_numbers = [int(_) for _ in age_numbers]
    average_age = round((sum(age_numbers) / len(age_numbers)),1)
    print()
    print(f"This text should be understood in average by {average_age} year olds.")