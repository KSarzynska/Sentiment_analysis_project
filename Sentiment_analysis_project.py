import nltk
from collections import Counter
from nltk.corpus import gutenberg
import sys
from colorama import Fore, Back, Style

# Welcome screen
name = input(Fore.CYAN + "Hello :) What is your name? ")

def welcome():
    print(Fore.CYAN + "Hi " + name + "!" + " Welcome to my sentiment analyzer!\n"
    "To use it, you need to upload your text and wait for the results :)\n"
    "You also have the option of downloading the results (also in the form of a graph) and comparing two texts.\n\n"
    "Please choose what you want to do. \n"
    "1 – Analyze/Compare\n"
    "2 – See negative wordlist\n"
    "3 – See positive wordlist\n"
    "4 - See the stoplist\n"
    "5 - Keyword based sentence search\n"
    "6 - Download texts\n"
    "7 - Exit")
welcome()

def choosing_number_again():
    print(Fore.CYAN + "\nPlease, choose what you want to do next:\n" + "1 – Analyze/Compare\n" + "2 – See negative wordlist\n" + "3 – See positive wordlist\n" + "4 - See the stoplist\n" + "5 - Keyword based sentence search\n" + "6 - Download texts\n" + "7 - Exit")

def keywords_analysis():
    try:
        file1 = input("Enter a file name. Please use a path ending with the '.txt' extension! ")
        plik1 = open(file1, 'r', encoding="utf8")
        plik1_content = plik1.read()
        plik1.close()
    except Exception:
        file1 = input("\nWrong file name. Please use a path ending with the '.txt' extension! ")
        plik1 = open(file1, 'r', encoding="utf8")
        plik1_content = plik1.read()
        plik1.close()
    text = plik1_content

    import re
    s = re.split(r'[.?!:]+', text)
    for word in s:
        word.lstrip("\n")
    keyword = input("Please enter your keyword!\n")
    def search(word, sentences):
            return [i for i in sentences if re.search(r'\b%s\b' % word, i)]
    print(search(keyword, s))

def open_stoplist(files):
    pliks = open(files, 'r', encoding="utf8")
    print(pliks.read())
    pliks.close()

def downloading_texts():
    print("Here's the list of titles you can choose from: \n")
    for title in (nltk.corpus.gutenberg.fileids()):
        print(title)
    try:
        chosen_title = input("What title do you choose? Please copy and paste the title with .txt\n")
        title1 = open(chosen_title, 'w', encoding="utf8")
        sample1 = gutenberg.raw(chosen_title)
        title1.write(sample1)
        title1.close()
        print("\nYou can find your text on your computer!\n")
    except Exception:
        chosen_title = input("You have entered wrong file name! Please copy and paste the title with .txt\n")
        title1 = open(chosen_title, 'w', encoding="utf8")
        sample1 = gutenberg.raw(chosen_title)
        title1.write(sample1)
        title1.close()
        print("\nYou can find your text on your computer!\n")
    def yes_no():
        another = input("Do you want to download another text? (yes/no)\n")
        if another == "yes" or another == "Yes" or another == "YES":
           downloading_texts()
        elif another == "no" or another == "No" or another == "NO":
           choosing_number_again()
        else:
           print("Please choose yes/no!")
           yes_no()
    yes_no()

def main_screen_function():
    main_screen = input(Fore.CYAN + "Do you want to go back to the main screen? (yes/no)\n")
    if main_screen == "yes" or main_screen == "Yes" or main_screen == "YES":
         choosing_number_again()
    elif main_screen == "no" or main_screen == "No" or main_screen == "NO":
        print(Fore.CYAN + "Thank you for using my tool! See you next time :)")
        sys.exit(0)
    else:
        print("Please choose yes/no!")
        main_screen_function()

def exit_screen_f():
    exit_screen = input(Fore.CYAN + "Are yu sure that you want to exit? (yes/no)\n")
    if exit_screen == "no" or exit_screen == "No" or exit_screen == "NO":
        choosing_number_again()
    elif exit_screen == "yes" or exit_screen == "Yes" or exit_screen == "YES":
        print(Fore.CYAN + "Thank you for using my tool! See you next time :)")
        sys.exit(0)
    else:
        print("Please choose yes/no!")
        exit_screen_f()


# Choosing number
def general():
    def choosing_no():
        number = int(input())
        #ANALYSIS/COMPARISON:
        if number == 1:
            file1 = input("Enter a file name. Please use a path ending with the '.txt' extension! ")
            #ENTERING FILE NAME:
            try:
                plik1 = open(file1, 'r', encoding="utf8")
                plik1_content = plik1.read()
                print(plik1.read())
                plik1.close()
            except Exception:
                file1 = input("\nWrong file name. Please use a path ending with the '.txt' extension! ")
                plik1 = open(file1, 'r', encoding="utf8")
                plik1_content = plik1.read()
                print(plik1.read())
                plik1.close()

            do_you_wanna0 = input("\nDo you want to compare it with another text? (yes/no)\n")

            # ANALYZING TWO TEXTS
            if do_you_wanna0 == "yes" or do_you_wanna0 == "Yes" or do_you_wanna0 == "YES":
                try:
                    file2 = input("Enter a file name. Please use a path ending with the '.txt' extension! ")
                    plik2 = open(file2, 'r', encoding="utf8")
                    plik2_content = plik2.read()
                    print(plik2.read())
                    plik1.close()
                except Exception:
                    file2 = input("\nWrong file name. Please use a path ending with the '.txt' extension! ")
                    plik2 = open(file2, 'r', encoding="utf8")
                    plik2_content = plik2.read()
                    print(plik2.read())
                    plik1.close()
                print("\n")
                do_you_wanna = input("Do you want to analyze these texts? (yes/no)\n ")
                if do_you_wanna == "yes" or do_you_wanna == "Yes" or do_you_wanna == "YES":
                    stoplist_question = input("\nDo you want to use stoplist function? \n")

                    #ANALYSIS OF TWO TEXTS WITH A STOPLIST
                    if stoplist_question == "yes" or do_you_wanna0 == "Yes" or do_you_wanna0 == "YES":
                        text1 = plik1_content
                        text2 = plik2_content
                        punc = "—”!()-[]{}';:\,<>./?@#$%^&*_~–"
                        for ele in text1:
                            if ele in punc:
                                text1 = text1.replace(ele, "")
                        for ele in text2:
                            if ele in punc:
                                text2 = text2.replace(ele, "")

                                # TOKENIZATION OF TWO TEXTS
                        if len(text1) > 0:
                            tokens_text1 = nltk.word_tokenize(text1)
                            for i in range(len(tokens_text1)):
                                tokens_text1[i] = tokens_text1[i].lower()

                                # DELETING STOPLIST ELEMENTS TEXT1
                            files = r"C:\Users\kasia\Desktop\Projekt programowanie\stoplist.txt"
                            pliks = open(files, 'r', encoding="utf8")
                            stoplist = pliks.read()
                            stoplist = stoplist.split()
                            pliks.close()
                            minus1_stoplist = []
                            for w in tokens_text1:
                                if w not in stoplist:
                                    minus1_stoplist.append(w)
                            dic1_stoplist = {}
                            for i in range(len(minus1_stoplist)):
                                dic1_stoplist[minus1_stoplist[i]] = minus1_stoplist.count(minus1_stoplist[i])
                            if len(text2) > 0:
                                tokens_text2 = nltk.word_tokenize(text2)
                                for i in range(len(tokens_text2)):
                                    tokens_text2[i] = tokens_text2[i].lower()

                                    # DELETING STOPLIST ELEMENTS TEXT2
                                files = r"C:\Users\kasia\Desktop\Projekt programowanie\stoplist.txt"
                                pliks = open(files, 'r', encoding="utf8")
                                stoplist = pliks.read()
                                stoplist = stoplist.split()
                                pliks.close()
                                minus2_stoplist = []
                                for w in tokens_text2:
                                    if w not in stoplist:
                                        minus2_stoplist.append(w)
                                dic2_stoplist = {}
                                for i in range(len(minus2_stoplist)):
                                    dic2_stoplist[minus2_stoplist[i]] = minus2_stoplist.count(minus2_stoplist[i])

                            # SENTIMENT ANALYSIS FOR TWO TEXTS
                            do_you_wanna_chart2 = input("\nDo you want to see the results (You can also download it)?\n")
                            if do_you_wanna_chart2 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":

                                # CREATING POSITIVE LIST
                                filep = r"C:\Users\kasia\Desktop\Projekt programowanie\positive.txt"
                                plikp = open(filep, 'r', encoding="utf8")
                                positive = plikp.read().split()
                                plikp.close()

                                # CREATING NEGATIVE LIST
                                filen = r"C:\Users\kasia\Desktop\Projekt programowanie\negative.txt"
                                plikn = open(filen, 'r', encoding="utf8")
                                negative = plikn.read().split()
                                plikn.close()

                                # FINDING COMMON ELEMENTS POSITIVE TEXT1
                                try:
                                    number_of_common_positive1 = int(input("\nHow many of the most common positive words do you want to see (text1)? (number)\n"))
                                    minus1_stoplist_as_set = set(minus1_stoplist)
                                    intersection1 = minus1_stoplist_as_set.intersection(positive)
                                except:
                                    number_of_common_positive1 = int(input("\nPlease choose a number!\n"))
                                    minus1_stoplist_as_set = set(minus1_stoplist)
                                    intersection1 = minus1_stoplist_as_set.intersection(positive)

                                uncommon_positive_1 = []
                                for row in minus1_stoplist:
                                    uncommon_positive_1.append(row)
                                for element in intersection1:
                                    try:
                                        while True:
                                            uncommon_positive_1.remove(element)
                                    except ValueError:
                                        pass
                                common_positive1_new = []
                                for row in minus1_stoplist:
                                    common_positive1_new.append(row)
                                for element1 in uncommon_positive_1:
                                    if element1 in common_positive1_new:
                                        common_positive1_new.remove(element1)
                                counter_common_positive1_new = Counter(common_positive1_new)
                                dictionary_positive1 = dict(
                                    counter_common_positive1_new.most_common(number_of_common_positive1))
                                dictionary_positive1_touple = [[k, v] for k, v in dictionary_positive1.items()]

                                # FINDING COMMON ELEMENTS NEGATIVE TEXT1
                                try:
                                    number_of_common_negative1 = int(input("\nHow many of the most common negative words do you want to see? (text1) (number)\n"))
                                    minus1_stoplist_as_set1 = set(minus1_stoplist)
                                    intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                except:
                                    number_of_common_negative1 = int(input("\nPlease choose a number!\n"))
                                    minus1_stoplist_as_set1 = set(minus1_stoplist)
                                    intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                uncommon_negative_1 = []
                                for row in minus1_stoplist:
                                    uncommon_negative_1.append(row)
                                for element in intersection1:
                                    try:
                                        while True:
                                            uncommon_negative_1.remove(element)
                                    except ValueError:
                                        pass
                                common_negative1_new = []
                                for row in minus1_stoplist:
                                    common_negative1_new.append(row)
                                for element1 in uncommon_negative_1:
                                    if element1 in common_negative1_new:
                                        common_negative1_new.remove(element1)
                                counter_common_negative1_new = Counter(common_negative1_new)
                                dictionary_negative1 = dict(
                                    counter_common_negative1_new.most_common(number_of_common_negative1))
                                dictionary_negative1_touple = [[k, v] for k, v in dictionary_negative1.items()]
                                result = 0
                                for element in positive:
                                    if element in minus1_stoplist:
                                        result += 1
                                for element in negative:
                                    if element in minus1_stoplist:
                                        result -= 1
                                if result < 1:
                                    print("\nEmotional charge of the text: Negative\n")
                                elif result == 0:
                                    print("\nEmotional charge of the text: Neutral\n")
                                else:
                                    print("\nEmotional charge of the text: Positive\n")
                                percent_positive1 = len(common_positive1_new) / len(minus1_stoplist) * 100
                                percent_negative1 = len(common_negative1_new) / len(minus1_stoplist) * 100
                                print("Percent of positive words:", round(percent_positive1, 2), "%")
                                print("Percent of negative words:", round(percent_negative1, 2), "%")
                                print("Positive words: ", *dictionary_positive1_touple, sep="\n")
                                print("\nNegative words: ", *dictionary_negative1_touple, sep="\n")

                                # FINDING COMMON ELEMENTS POSITIVE TEXT2
                                try:
                                    number_of_common_positive2 = int(input("\nHow many of the most common positive words do you want to see (text2)? (number)\n"))
                                    minus2_stoplist_as_set = set(minus2_stoplist)
                                    intersection2 = minus2_stoplist_as_set.intersection(positive)
                                except:
                                    number_of_common_positive2 = int(input("\nPlease choose a number!\n"))
                                    minus2_stoplist_as_set = set(minus2_stoplist)
                                    intersection2 = minus2_stoplist_as_set.intersection(positive)
                                uncommon_positive_2 = []
                                for row in minus2_stoplist:
                                    uncommon_positive_2.append(row)
                                for element in intersection2:
                                    try:
                                        while True:
                                            uncommon_positive_2.remove(element)
                                    except ValueError:
                                        pass
                                common_positive2_new = []
                                for row in minus2_stoplist:
                                    common_positive2_new.append(row)
                                for element2 in uncommon_positive_2:
                                    if element2 in common_positive2_new:
                                        common_positive2_new.remove(element2)
                                counter_common_positive2_new = Counter(common_positive2_new)
                                dictionary_positive2 = dict(
                                    counter_common_positive2_new.most_common(number_of_common_positive2))
                                dictionary_positive2_touple = [[k, v] for k, v in dictionary_positive2.items()]

                                # FINDING COMMON ELEMENTS NEGATIVE TEXT2
                                try:
                                    number_of_common_negative2 = int(input("\nHow many of the most common negative words do you want to see? (text2) (number)\n"))
                                    minus2_stoplist_as_set2 = set(minus2_stoplist)
                                    intersection2 = minus2_stoplist_as_set2.intersection(negative)
                                except:
                                    number_of_common_negative2 = int(input("\nPlease choose a number!\n"))
                                    minus2_stoplist_as_set2 = set(minus2_stoplist)
                                    intersection2 = minus2_stoplist_as_set2.intersection(negative)

                                uncommon_negative_2 = []
                                for row in minus2_stoplist:
                                    uncommon_negative_2.append(row)
                                for element in intersection2:
                                    try:
                                        while True:
                                            uncommon_negative_2.remove(element)
                                    except ValueError:
                                        pass
                                common_negative2_new = []
                                for row in minus2_stoplist:
                                    common_negative2_new.append(row)
                                for element2 in uncommon_negative_2:
                                    if element2 in common_negative2_new:
                                        common_negative2_new.remove(element2)
                                counter_common_negative2_new = Counter(common_negative2_new)
                                dictionary_negative2 = dict(
                                    counter_common_negative2_new.most_common(number_of_common_negative2))
                                dictionary_negative2_touple = [[k, v] for k, v in dictionary_negative2.items()]
                                result2 = 0
                                for element in positive:
                                    if element in minus2_stoplist:
                                        result2 += 1
                                for element in negative:
                                    if element in minus2_stoplist:
                                        result2 -= 1
                                if result2 < 1:
                                    print("\nEmotional charge of the text2: Negative\n")
                                elif result2 == 0:
                                    print("\nEmotional charge of the text2: Neutral\n")
                                else:
                                    print("\nEmotional charge of the text: Positive\n")
                                percent_positive2 = len(common_positive2_new) / len(minus2_stoplist) * 100
                                percent_negative2 = len(common_negative2_new) / len(minus2_stoplist) * 100
                                print("Percent of positive words in text2:", round(percent_positive2, 2), "%")
                                print("Percent of negative words in text2:", round(percent_negative2, 2), "%")
                                print("\nPositive words in text2: ", *dictionary_positive2_touple, sep="\n")
                                print("\nNegative words in text2: ", *dictionary_negative2_touple, sep="\n")

                                # DOWNLOADING THE RESULTS FOR TWO TEXTS
                                do_you_wanna_download1 = input("\nDo you want to download the results?\n")
                                if do_you_wanna_download1 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":
                                    download_results_text1_2 = open("Results_text1_2(stoplist).txt", 'w')

                                    download_results_text1_2.write(
                                        "Thank you for using my tool. Here are your results: \n\nText1\nMost common positive words:\n")
                                    for key, value in dictionary_positive1.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText2\nMost common positive words:\n")
                                    for key, value in dictionary_positive2.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText1\nMost common negative words:\n ")
                                    for key, value in dictionary_negative1.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText2\nMost common negative words:\n")
                                    for key, value in dictionary_negative2.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write(
                                        "\nText1\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                    download_results_text1_2.write(str(result))

                                    download_results_text1_2.write(
                                        "\nText2\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                    download_results_text1_2.write(str(result2))

                                    download_results_text1_2.write("\nText1\nPositive words (%):\n")
                                    download_results_text1_2.write(str(round(percent_positive1, 2)))

                                    download_results_text1_2.write("\nText2\nPositive words (%):\n")
                                    download_results_text1_2.write(str(round(percent_positive2, 2)))

                                    download_results_text1_2.write("\nText1\nNegative words (%):\n")
                                    download_results_text1_2.write(str(round(percent_negative1, 2)))

                                    download_results_text1_2.write("\nText2\nNegative words (%):\n")
                                    download_results_text1_2.write(str(round(percent_negative2, 2)))

                                    download_results_text1_2.close()

                                    # CREATING POSITIVE CHARTS FOR TWO TEXTS
                                    words1 = []
                                    numbers1 = []
                                    words2 = []
                                    numbers2 = []
                                    for i in dictionary_positive1.values():
                                        numbers1.append(i)
                                    for i in dictionary_positive1.keys():
                                        words1.append(i)
                                    for i in dictionary_positive2.values():
                                        numbers2.append(i)
                                    for i in dictionary_positive2.keys():
                                        words2.append(i)

                                    import pygal
                                    from pygal.style import Style

                                    yourCustomStyle1 = Style(background='transparent', colors=['#006400'])
                                    line_chart1 = pygal.Bar(style=yourCustomStyle1)
                                    line_chart1.title = 'Positive words in the text1 and their frequency'
                                    line_chart1.x_labels = map(str, words1)
                                    line_chart1.add('Number of words', numbers2)
                                    line_chart1.render_to_file("positive_word_frequency_text1(stoplist).svg")

                                    yourCustomStyle2 = Style(background='transparent', colors=['#FF0000'])
                                    line_chart2 = pygal.Bar(style=yourCustomStyle2)
                                    line_chart2.title = 'Positive words in the text2 and their frequency'
                                    line_chart2.x_labels = map(str, words2)
                                    line_chart2.add('Number of words', numbers2)
                                    line_chart2.render_to_file("positive_word_frequency_text2(stoplist).svg")

                                    # CREATING NEGATIVE CHARTS FOR TWO TEXTS
                                    words1 = []
                                    numbers1 = []
                                    words2 = []
                                    numbers2 = []
                                    for i in dictionary_negative1.values():
                                        numbers1.append(i)
                                    for i in dictionary_negative1.keys():
                                        words1.append(i)
                                    for i in dictionary_negative2.values():
                                        numbers2.append(i)
                                    for i in dictionary_negative2.keys():
                                        words2.append(i)

                                    yourCustomStyle1 = Style(background='transparent', colors=['#006400'])
                                    line_chart1 = pygal.Bar(style=yourCustomStyle1)
                                    line_chart1.title = 'Negative words in the text and their frequency'
                                    line_chart1.x_labels = map(str, words1)
                                    line_chart1.add('Number of words1', numbers1)
                                    line_chart1.render_to_file("negative_word_frequency_text1(stoplist).svg")
                                    print("You can find the results on your computer!\n",
                                          "Positive chart: positive_word_frequency_text1(stoplist).svg\n",
                                          "Negative chart: negative_word_frequency_text1(stoplist).svg\n")

                                    yourCustomStyle2 = Style(background='transparent', colors=['#FF0000'])
                                    line_chart2 = pygal.Bar(style=yourCustomStyle2)
                                    line_chart2.title = 'Negative words in the text and their frequency'
                                    line_chart2.x_labels = map(str, words2)
                                    line_chart2.add('Number of words2', numbers2)
                                    line_chart2.render_to_file("negative_word_frequency_text2(stoplist).svg")
                                    print(
                                        "Positive chart: positive_word_frequency_text2(stoplist).svg\n",
                                        "Negative chart: negative_word_frequency_text2(stoplist).svg\n",
                                        "The results: Results_text1_2(stoplist).txt")
                                else:
                                    choosing_number_again()
                                    choosing_no()

                    # ANALYSIS WITHOUT A STOPLIST FOR TWO
                    else:
                        text1 = plik1_content
                        text2 = plik2_content
                        punc = "—”!()-[]{}';:\,<>./?@#$%^&*_~–"
                        for ele in text1:
                            if ele in punc:
                                text1 = text1.replace(ele, "")
                        for ele in text2:
                            if ele in punc:
                                text2 = text2.replace(ele, "")
                                # TOKENIZATION
                        if len(text1) > 0:
                            tokens_text1 = nltk.word_tokenize(text1)
                            for i in range(len(tokens_text1)):
                                tokens_text1[i] = tokens_text1[i].lower()
                        if len(text1) > 0:
                            tokens_text2 = nltk.word_tokenize(text2)
                            for i in range(len(tokens_text2)):
                                tokens_text2[i] = tokens_text2[i].lower()

                            # SENTIMENT ANALYSIS FOR TWO WOS
                            do_you_wanna_chart2 = input(
                                "\nDo you want to see the results (You can also download it)?\n")
                            if do_you_wanna_chart2 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":

                                # CREATING POSITIVE LIST WOS
                                filep = r"C:\Users\kasia\Desktop\Projekt programowanie\positive.txt"
                                plikp = open(filep, 'r', encoding="utf8")
                                positive = plikp.read().split()
                                plikp.close()

                                # CREATING NEGATIVE LIST WOS
                                filen = r"C:\Users\kasia\Desktop\Projekt programowanie\negative.txt"
                                plikn = open(filen, 'r', encoding="utf8")
                                negative = plikn.read().split()
                                plikn.close()

                                # FINDING COMMON ELEMENTS POSITIVE TEXT1 WOS
                                try:
                                    number_of_common_positive1 = int(input("\nHow many of the most common positive words do you want to see (text1)? (number)\n"))
                                    minus1_stoplist_as_set = set(tokens_text1)
                                    intersection1 = minus1_stoplist_as_set.intersection(positive)
                                except:
                                    number_of_common_positive1 = int(input("\nPlease choose a number!\n"))
                                    minus1_stoplist_as_set = set(tokens_text1)
                                    intersection1 = minus1_stoplist_as_set.intersection(positive)

                                uncommon_positive_1 = []
                                for row in tokens_text1:
                                    uncommon_positive_1.append(row)
                                for element in intersection1:
                                    try:
                                        while True:
                                            uncommon_positive_1.remove(element)
                                    except ValueError:
                                        pass
                                common_positive1_new = []
                                for row in tokens_text1:
                                    common_positive1_new.append(row)
                                for element1 in uncommon_positive_1:
                                    if element1 in common_positive1_new:
                                        common_positive1_new.remove(element1)
                                counter_common_positive1_new = Counter(common_positive1_new)
                                dictionary_positive1 = dict(
                                    counter_common_positive1_new.most_common(number_of_common_positive1))
                                dictionary_positive1_touple = [[k, v] for k, v in dictionary_positive1.items()]

                                # FINDING COMMON ELEMENTS NEGATIVE TEXT1 WOS
                                try:
                                    number_of_common_negative1 = int(input("\nHow many of the most common negative words do you want to see? (text1) (number)\n"))
                                    minus1_stoplist_as_set1 = set(tokens_text1)
                                    intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                except:
                                    number_of_common_negative1 = int(input("\nPlease choose a number!\n"))
                                    minus1_stoplist_as_set1 = set(tokens_text1)
                                    intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                uncommon_negative_1 = []
                                for row in tokens_text1:
                                    uncommon_negative_1.append(row)
                                for element in intersection1:
                                    try:
                                        while True:
                                            uncommon_negative_1.remove(element)
                                    except ValueError:
                                        pass
                                common_negative1_new = []
                                for row in tokens_text1:
                                    common_negative1_new.append(row)
                                for element1 in uncommon_negative_1:
                                    if element1 in common_negative1_new:
                                        common_negative1_new.remove(element1)
                                counter_common_negative1_new = Counter(common_negative1_new)
                                dictionary_negative1 = dict(
                                    counter_common_negative1_new.most_common(number_of_common_negative1))
                                dictionary_negative1_touple = [[k, v] for k, v in dictionary_negative1.items()]
                                result = 0
                                for element in positive:
                                    if element in tokens_text1:
                                        result += 1
                                for element in negative:
                                    if element in tokens_text1:
                                        result -= 1
                                if result < 1:
                                    print("\nEmotional charge of the text: Negative\n")
                                elif result == 0:
                                    print("\nEmotional charge of the text: Neutral\n")
                                else:
                                    print("\nEmotional charge of the text: Positive\n")
                                percent_positive1 = len(common_positive1_new) / len(tokens_text1) * 100
                                percent_negative1 = len(common_negative1_new) / len(tokens_text1) * 100
                                print("Percent of positive words:", round(percent_positive1, 2), "%")
                                print("Percent of negative words:", round(percent_negative1, 2), "%")
                                print("Positive words: ", *dictionary_positive1_touple, sep="\n")
                                print("\nNegative words: ", *dictionary_negative1_touple, sep="\n")

                                # FINDING COMMON ELEMENTS POSITIVE TEXT2 WOS
                                try:
                                    number_of_common_positive2 = int(input("\nHow many of the most common positive words do you want to see (text2)? (number)\n"))
                                    minus2_stoplist_as_set = set(tokens_text2)
                                    intersection2 = minus2_stoplist_as_set.intersection(positive)
                                except:
                                    number_of_common_positive2 = int(input("\nPlease choose a number!\n"))
                                    minus2_stoplist_as_set = set(tokens_text2)
                                    intersection2 = minus2_stoplist_as_set.intersection(positive)
                                uncommon_positive_2 = []
                                for row in tokens_text2:
                                    uncommon_positive_2.append(row)
                                for element in intersection2:
                                    try:
                                        while True:
                                            uncommon_positive_2.remove(element)
                                    except ValueError:
                                        pass
                                common_positive2_new = []
                                for row in tokens_text2:
                                    common_positive2_new.append(row)
                                for element2 in uncommon_positive_2:
                                    if element2 in common_positive2_new:
                                        common_positive2_new.remove(element2)
                                counter_common_positive2_new = Counter(common_positive2_new)
                                dictionary_positive2 = dict(
                                    counter_common_positive2_new.most_common(number_of_common_positive2))
                                dictionary_positive2_touple = [[k, v] for k, v in dictionary_positive2.items()]

                                # FINDING COMMON ELEMENTS NEGATIVE TEXT2 WOS
                                try:
                                    number_of_common_negative2 = int(input("\nHow many of the most common negative words do you want to see? (text2) (number)\n"))
                                    minus2_stoplist_as_set2 = set(tokens_text2)
                                    intersection2 = minus2_stoplist_as_set2.intersection(negative)
                                except:
                                    number_of_common_negative2 = int(input("\nPlease choose a number!\n"))
                                    minus2_stoplist_as_set2 = set(tokens_text2)
                                    intersection2 = minus2_stoplist_as_set2.intersection(negative)
                                uncommon_negative_2 = []
                                for row in tokens_text2:
                                    uncommon_negative_2.append(row)
                                for element in intersection2:
                                    try:
                                        while True:
                                            uncommon_negative_2.remove(element)
                                    except ValueError:
                                        pass
                                common_negative2_new = []
                                for row in tokens_text2:
                                    common_negative2_new.append(row)
                                for element2 in uncommon_negative_2:
                                    if element2 in common_negative2_new:
                                        common_negative2_new.remove(element2)
                                counter_common_negative2_new = Counter(common_negative2_new)
                                dictionary_negative2 = dict(
                                    counter_common_negative2_new.most_common(number_of_common_negative2))
                                dictionary_negative2_touple = [[k, v] for k, v in dictionary_negative2.items()]
                                result2 = 0
                                for element in positive:
                                    if element in tokens_text2:
                                        result2 += 1
                                for element in negative:
                                    if element in tokens_text2:
                                        result2 -= 1
                                if result2 < 1:
                                    print("\nEmotional charge of the text2: Negative\n")
                                elif result2 == 0:
                                    print("\nEmotional charge of the text2: Neutral\n")
                                else:
                                    print("\nEmotional charge of the text: Positive\n")
                                percent_positive2 = len(common_positive2_new) / len(tokens_text2) * 100
                                percent_negative2 = len(common_negative2_new) / len(tokens_text2) * 100
                                print("Percent of positive words in text2:", round(percent_positive2, 2), "%")
                                print("Percent of negative words in text2:", round(percent_negative2, 2), "%")
                                print("Positive words in text2: ", *dictionary_positive2_touple, sep="\n")
                                print("\nNegative words in text2: ", *dictionary_negative2_touple, sep="\n")

                                # DOWNLOADING THE RESULTS FOR TWO TEXTS WOS
                                do_you_wanna_download1 = input("\nDo you want to download the results?\n")
                                if do_you_wanna_download1 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":
                                    download_results_text1_2 = open("Results_text1_2.txt", 'w')

                                    download_results_text1_2.write(
                                        "Thank you for using my tool. Here are your results: \n\nText1\nMost common positive words:\n")
                                    for key, value in dictionary_positive1.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText2\nMost common positive words:\n")
                                    for key, value in dictionary_positive2.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText1\nMost common negative words:\n ")
                                    for key, value in dictionary_negative1.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write("\nText2\nMost common negative words:\n")
                                    for key, value in dictionary_negative2.items():
                                        download_results_text1_2.write('%s:%s\n' % (key, value))

                                    download_results_text1_2.write(
                                        "\nText1\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                    download_results_text1_2.write(str(result))

                                    download_results_text1_2.write(
                                        "\nText2\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                    download_results_text1_2.write(str(result2))

                                    download_results_text1_2.write("\nText1\nPositive words (%):\n")
                                    download_results_text1_2.write(str(round(percent_positive1, 2)))

                                    download_results_text1_2.write("\nText2\nPositive words (%):\n")
                                    download_results_text1_2.write(str(round(percent_positive2, 2)))

                                    download_results_text1_2.write("\nText1\nNegative words (%):\n")
                                    download_results_text1_2.write(str(round(percent_negative1, 2)))

                                    download_results_text1_2.write("\nText2\nNegative words (%):\n")
                                    download_results_text1_2.write(str(round(percent_negative2, 2)))

                                    download_results_text1_2.close()

                                    # CREATING POSITIVE CHARTS FOR TWO TEXTS WOS
                                    words1 = []
                                    numbers1 = []
                                    words2 = []
                                    numbers2 = []
                                    for i in dictionary_positive1.values():
                                        numbers1.append(i)
                                    for i in dictionary_positive1.keys():
                                        words1.append(i)

                                    for i in dictionary_positive2.values():
                                        numbers2.append(i)
                                    for i in dictionary_positive2.keys():
                                        words2.append(i)

                                    import pygal
                                    from pygal.style import Style
                                    yourCustomStyle1 = Style(background='transparent', colors=['#006400'])
                                    line_chart1 = pygal.Bar(style=yourCustomStyle1)
                                    line_chart1.title = 'Positive words in the text1 and their frequency'
                                    line_chart1.x_labels = map(str, words1)
                                    line_chart1.add('Number of words', numbers2)
                                    line_chart1.render_to_file("positive_word_frequency_text1.svg")

                                    yourCustomStyle2 = Style(background='transparent', colors=['#FF0000'])
                                    line_chart2 = pygal.Bar(style=yourCustomStyle2)
                                    line_chart2.title = 'Positive words in the text2 and their frequency'
                                    line_chart2.x_labels = map(str, words2)
                                    line_chart2.add('Number of words', numbers2)
                                    line_chart2.render_to_file("positive_word_frequency_text2.svg")

                                    # CREATING NEGATIVE CHART FRO TWO TEXTS WOS
                                    words1 = []
                                    numbers1 = []
                                    words2 = []
                                    numbers2 = []
                                    for i in dictionary_negative1.values():
                                        numbers1.append(i)
                                    for i in dictionary_negative1.keys():
                                        words1.append(i)
                                    for i in dictionary_negative2.values():
                                        numbers2.append(i)
                                    for i in dictionary_negative2.keys():
                                        words2.append(i)
                                    import pygal
                                    from pygal.style import Style

                                    yourCustomStyle = Style(background='transparent', colors=['#FF0000'])
                                    line_chart1 = pygal.Bar(style=yourCustomStyle)
                                    line_chart1.title = 'Negative words in text1 and their frequency'
                                    line_chart1.x_labels = map(str, words1)
                                    line_chart1.add('Number of words1', numbers1)
                                    line_chart1.render_to_file("negative_word_frequency_text1.svg")

                                    yourCustomStyle = Style(background='transparent', colors=['#006400'])
                                    line_chart2 = pygal.Bar(style=yourCustomStyle)
                                    line_chart2.title = 'Negative words in text2 and their frequency'
                                    line_chart2.x_labels = map(str, words2)
                                    line_chart2.add('Number of words2', numbers2)
                                    line_chart2.render_to_file("negative_word_frequency_text2.svg")
                                    print("You can find the results on your computer!\n",
                                          "Positive chart: positive_word_frequency_text1.svg\n",
                                          "Negative chart: negative_word_frequency_text1.svg\n",
                                          "Positive chart: positive_word_frequency_text2.svg\n",
                                          "Negative chart: negative_word_frequency_text2.svg\n",
                                          "The results: Results_text1_2.txt")
                                else:
                                    choosing_number_again()
                                    choosing_no()



                # ANALYZING JUST ONE TEXT
            else:
                print(plik1_content)
                print("\n")
                do_you_wanna = input("Do you want to analyze this text? (yes/no)\n ")
                if do_you_wanna == "yes" or do_you_wanna == "Yes" or do_you_wanna == "YES":
                    def analyzing_one(file1):
                        plik1 = open(file1, 'r', encoding="utf8")
                        plik1.close()
                        stoplist_question = input("\nDo you want to use stoplist function? \n")
                        if stoplist_question == "yes" or do_you_wanna0 == "Yes" or do_you_wanna0 == "YES":
                            text1 = plik1_content
                            punc = "—”!()-[]{}';:\,<>./?@#$%^&*_~–"
                            for ele in text1:
                                if ele in punc:
                                    text1 = text1.replace(ele, "")

                                    #TOKENIZATION
                            if len(text1) > 0:
                                tokens_text1 = nltk.word_tokenize(text1)
                                for i in range(len(tokens_text1)):
                                    tokens_text1[i] = tokens_text1[i].lower()

                                    #DELETING STOPLIST ELEMENTS
                                files = r"C:\Users\kasia\Desktop\Projekt programowanie\stoplist.txt"
                                pliks = open(files, 'r', encoding="utf8")
                                stoplist = pliks.read()
                                stoplist = stoplist.split()
                                pliks.close()
                                minus1_stoplist = []
                                for w in tokens_text1:
                                    if w not in stoplist:
                                        minus1_stoplist.append(w)
                                dic1_stoplist = {}
                                for i in range(len(minus1_stoplist)):
                                    dic1_stoplist[minus1_stoplist[i]] = minus1_stoplist.count(minus1_stoplist[i])

                                #SENTIMENT ANALYSIS
                                do_you_wanna_chart2 = input("\nDo you want to see the results (You can also download it)?\n")
                                if do_you_wanna_chart2 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":
                                    #POSITIVE LIST
                                    filep = r"C:\Users\kasia\Desktop\Projekt programowanie\positive.txt"
                                    plikp = open(filep, 'r', encoding="utf8")
                                    positive = plikp.read().split()
                                    plikp.close()

                                    #NEGATIVE LIST
                                    filen = r"C:\Users\kasia\Desktop\Projekt programowanie\negative.txt"
                                    plikn = open(filen, 'r', encoding="utf8")
                                    negative = plikn.read().split()
                                    plikn.close()

                                    #FINDING COMMON ELEMENTS POSITIVE
                                    try:
                                        number_of_common_positive1 = int(input("\nHow many of the most common positive words do you want to see? (number)\n"))
                                        minus1_stoplist_as_set = set(minus1_stoplist)
                                        intersection1 = minus1_stoplist_as_set.intersection(positive)
                                    except:
                                        number_of_common_positive1 = int(input("\nPlease choose a number!\n"))
                                        minus1_stoplist_as_set = set(minus1_stoplist)
                                        intersection1 = minus1_stoplist_as_set.intersection(positive)
                                    uncommon_positive_1 = []
                                    for row in minus1_stoplist:
                                        uncommon_positive_1.append(row)
                                    for element in intersection1:
                                        try:
                                            while True:
                                                uncommon_positive_1.remove(element)
                                        except ValueError:
                                            pass
                                    common_positive1_new = []
                                    for row in minus1_stoplist:
                                        common_positive1_new.append(row)
                                    for element1 in uncommon_positive_1:
                                        if element1 in common_positive1_new:
                                            common_positive1_new.remove(element1)
                                    counter_common_positive1_new = Counter(common_positive1_new)
                                    dictionary_positive1 = dict(counter_common_positive1_new.most_common(number_of_common_positive1))
                                    dictionary_positive1_touple = [[k, v] for k, v in dictionary_positive1.items()]

                                    #FINDING COMMON ELEMENTS NEGATIVE
                                    try:
                                        number_of_common_negative1 = int(input("\nHow many of the most common negative words do you want to see? (number)\n"))
                                        minus1_stoplist_as_set1 = set(minus1_stoplist)
                                        intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                    except:
                                        number_of_common_negative1 = int(input("\nPlease choose a number!\n"))
                                        minus1_stoplist_as_set1 = set(minus1_stoplist)
                                        intersection1 = minus1_stoplist_as_set1.intersection(negative)
                                    uncommon_negative_1 = []
                                    for row in minus1_stoplist:
                                        uncommon_negative_1.append(row)
                                    for element in intersection1:
                                        try:
                                            while True:
                                                uncommon_negative_1.remove(element)
                                        except ValueError:
                                            pass
                                    common_negative1_new = []
                                    for row in minus1_stoplist:
                                        common_negative1_new.append(row)
                                    for element1 in uncommon_negative_1:
                                        if element1 in common_negative1_new:
                                            common_negative1_new.remove(element1)
                                    counter_common_negative1_new = Counter(common_negative1_new)
                                    dictionary_negative1 = dict(counter_common_negative1_new.most_common(number_of_common_negative1))
                                    dictionary_negative1_touple = [[k, v] for k, v in dictionary_negative1.items()]
                                    result = 0
                                    for element in positive:
                                        if element in minus1_stoplist:
                                            result += 1
                                    for element in negative:
                                        if element in minus1_stoplist:
                                            result -= 1
                                    if result < 1:
                                        print("\nEmotional charge of the text: Negative\n")
                                    elif result == 0:
                                        print("\nEmotional charge of the text: Neutral\n")
                                    else:
                                        print("\nEmotional charge of the text: Positive\n")
                                    percent_positive1 = len(common_positive1_new) /len(minus1_stoplist) * 100
                                    percent_negative1 = len(common_negative1_new) /len(minus1_stoplist) * 100
                                    print("Percent of positive words:", round(percent_positive1,2), "%")
                                    print("Percent of negative words:", round(percent_negative1,2), "%")
                                    print("Positive words: ",*dictionary_positive1_touple, sep = "\n")
                                    print("\nNegative words: ",*dictionary_negative1_touple, sep = "\n")

                                    #DOWNLOADING THE RESULTS
                                    do_you_wanna_download1 = input("\nDo you want to download the results?\n")
                                    if do_you_wanna_download1 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":
                                        download_results_text1 = open("Results_text1(stoplist).txt", 'w')
                                        download_results_text1.write("Thank you for using my tool. Here are your results: \n\nMost common positive words:\n")
                                        for key, value in dictionary_positive1.items():
                                            download_results_text1.write('%s:%s\n' % (key, value))
                                        download_results_text1.write("\nMost common negative words:\n ")
                                        for key, value in dictionary_negative1.items():
                                            download_results_text1.write('%s:%s\n' % (key, value))
                                        download_results_text1.write("\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                        download_results_text1.write(str(result))
                                        download_results_text1.write("\nPositive words (%):\n")
                                        download_results_text1.write(str(round(percent_positive1, 2)))
                                        download_results_text1.write("\nNegative words (%):\n")
                                        download_results_text1.write(str(round(percent_negative1, 2)))
                                        download_results_text1.close()

                                        #CREATING POSITIVE CHART
                                        words = []
                                        numbers = []
                                        for i in dictionary_positive1.values():
                                            numbers.append(i)
                                        for i in dictionary_positive1.keys():
                                            words.append(i)
                                        import pygal
                                        line_chart = pygal.Bar()
                                        line_chart.title = 'Positive words in the text and their frequency'
                                        line_chart.x_labels = map(str, words)
                                        line_chart.add('Number of words', numbers)
                                        line_chart.render_to_file("positive_word_frequency_text1(stoplist).svg")

                                        #CREATING NEGATIVE CHART
                                        words1 = []
                                        numbers1 = []
                                        for i in dictionary_negative1.values():
                                            numbers1.append(i)
                                        for i in dictionary_negative1.keys():
                                            words1.append(i)
                                        import pygal
                                        line_chart = pygal.Bar()
                                        line_chart.title = 'Negative words in the text and their frequency'
                                        line_chart.x_labels = map(str, words1)
                                        line_chart.add('Number of words', numbers1)
                                        line_chart.render_to_file("negative_word_frequency_text1(stoplist).svg")
                                        print("You can find the results on your computer!\n","Positive chart: positive_word_frequency_text1(stoplist).svg\n", "Negative chart: negative_word_frequency_text1(stoplist).svg\n", "The results: Results_text1(stoplist).txt")
                                    else:
                                        print("Please, choose again:\n" + "1 – Analyze/Compare\n" + "2 – See negative wordlist\n" + "3 – See positive wordlist\n" + "4 - See the stoplist" + "5 - Exit")
                                        choosing_no()
                                else:
                                    print("Thank you for using my tool! See you next time :)")

                        #WITHOUT A STOPLIST
                        else:
                            text1 = plik1_content
                            punc = "—”!()-[]{}';:\,<>./?@#$%^&*_~–"
                            for ele in text1:
                                if ele in punc:
                                    text1 = text1.replace(ele, "")

                                    # TOKENIZATION
                            if len(text1) > 0:
                                tokens_text1 = nltk.word_tokenize(text1)
                                for i in range(len(tokens_text1)):
                                    tokens_text1[i] = tokens_text1[i].lower()

                                # SENTIMENT ANALYSIS WOS
                                do_you_wanna_chart2 = input(
                                    "\nDo you want to see the results (You can also download it)?\n")
                                if do_you_wanna_chart2 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":

                                    # POSITIVE LIST
                                    filep = r"C:\Users\kasia\Desktop\Projekt programowanie\positive.txt"
                                    plikp = open(filep, 'r', encoding="utf8")
                                    positive = plikp.read().split()
                                    plikp.close()

                                    # NEGATIVE LIST
                                    filen = r"C:\Users\kasia\Desktop\Projekt programowanie\negative.txt"
                                    plikn = open(filen, 'r', encoding="utf8")
                                    negative = plikn.read().split()
                                    plikn.close()

                                    # FINDING COMMON ELEMENTS POSITIVE WOS
                                    try:
                                        number_of_common_positive1 = int(input("\nHow many of the most common positive words do you want to see? (number)\n"))
                                        tokens_text1_as_set = set(tokens_text1)
                                        intersection1 = tokens_text1_as_set.intersection(positive)
                                    except:
                                        number_of_common_positive1 = int(input("\nPlease choose a number!\n"))
                                        tokens_text1_as_set = set(tokens_text1)
                                        intersection1 = tokens_text1_as_set.intersection(positive)
                                    uncommon_positive_1 = []
                                    for row in tokens_text1:
                                        uncommon_positive_1.append(row)
                                    for element in intersection1:
                                        try:
                                            while True:
                                                uncommon_positive_1.remove(element)
                                        except ValueError:
                                            pass
                                    common_positive1_new = []
                                    for row in tokens_text1:
                                        common_positive1_new.append(row)
                                    for element1 in uncommon_positive_1:
                                        if element1 in common_positive1_new:
                                            common_positive1_new.remove(element1)
                                    counter_common_positive1_new = Counter(common_positive1_new)
                                    dictionary_positive1 = dict(
                                        counter_common_positive1_new.most_common(number_of_common_positive1))
                                    dictionary_positive1_touple = [[k, v] for k, v in dictionary_positive1.items()]

                                    # FINDING COMMON ELEMENTS NEGATIVE WOS
                                    number_of_common_negative1 = int(input(
                                        "\nHow many of the most common negative words do you want to see? (number)\n"))
                                    tokens_text1_as_set1 = set(tokens_text1)
                                    intersection1 = tokens_text1_as_set1.intersection(negative)
                                    uncommon_negative_1 = []
                                    for row in tokens_text1:
                                        uncommon_negative_1.append(row)
                                    for element in intersection1:
                                        try:
                                            while True:
                                                uncommon_negative_1.remove(element)
                                        except ValueError:
                                            pass
                                    common_negative1_new = []
                                    for row in tokens_text1:
                                        common_negative1_new.append(row)
                                    for element1 in uncommon_negative_1:
                                        if element1 in common_negative1_new:
                                            common_negative1_new.remove(element1)
                                    counter_common_negative1_new = Counter(common_negative1_new)
                                    dictionary_negative1 = dict(
                                        counter_common_negative1_new.most_common(number_of_common_negative1))
                                    dictionary_negative1_touple = [[k, v] for k, v in dictionary_negative1.items()]
                                    result = 0
                                    for element in positive:
                                        if element in tokens_text1:
                                            result += 1
                                    for element in negative:
                                        if element in tokens_text1:
                                            result -= 1
                                    if result < 1:
                                        print("\nEmotional charge of the text: Negative\n")
                                    elif result == 0:
                                        print("\nEmotional charge of the text: Neutral\n")
                                    else:
                                        print("\nEmotional charge of the text: Positive\n")
                                    percent_positive1 = len(common_positive1_new) / len(tokens_text1) * 100
                                    percent_negative1 = len(common_negative1_new) / len(tokens_text1) * 100
                                    print("Percent of positive words:", round(percent_positive1, 2), "%")
                                    print("Percent of negative words:", round(percent_negative1, 2), "%")
                                    print("Positive words: ", *dictionary_positive1_touple, sep="\n")
                                    print("\nNegative words: ", *dictionary_negative1_touple, sep="\n")

                                    # DOWNLOADING THE RESULTS WOS
                                    do_you_wanna_download1 = input("\nDo you want to download the results?\n")
                                    if do_you_wanna_download1 == "yes" or do_you_wanna_chart2 == "Yes" or do_you_wanna_chart2 == "YES":
                                        download_results_text1 = open("Results_text1_with_stoplist.txt", 'w')
                                        download_results_text1.write(
                                            "Thank you for using my tool. Here are your results: \n\nMost common positive words:\n")
                                        for key, value in dictionary_positive1.items():
                                            download_results_text1.write('%s:%s\n' % (key, value))
                                        download_results_text1.write("\nMost common negative words:\n ")
                                        for key, value in dictionary_negative1.items():
                                            download_results_text1.write('%s:%s\n' % (key, value))
                                        download_results_text1.write(
                                            "\nEmotional charge of the text (minus - negative, plus - positive, 0 - neutral):\n")
                                        download_results_text1.write(str(result))
                                        download_results_text1.write("\nPositive words (%):\n")
                                        download_results_text1.write(str(round(percent_positive1, 2)))
                                        download_results_text1.write("\nNegative words (%):\n")
                                        download_results_text1.write(str(round(percent_negative1, 2)))
                                        download_results_text1.close()

                                        # CREATING POSITIVE CHART WOS
                                        words = []
                                        numbers = []
                                        for i in dictionary_positive1.values():
                                            numbers.append(i)
                                        for i in dictionary_positive1.keys():
                                            words.append(i)
                                        import pygal
                                        line_chart = pygal.Bar()
                                        line_chart.title = 'Positive words in the text and their frequency'
                                        line_chart.x_labels = map(str, words)
                                        line_chart.add('Number of words', numbers)
                                        line_chart.render_to_file("positive_word_frequency_text1_with_stoplist.svg")

                                        # CREATING NEGATIVE CHART WOS
                                        words1 = []
                                        numbers1 = []
                                        for i in dictionary_negative1.values():
                                            numbers1.append(i)
                                        for i in dictionary_negative1.keys():
                                            words1.append(i)
                                        import pygal
                                        line_chart = pygal.Bar()
                                        line_chart.title = 'Negative words in the text and their frequency'
                                        line_chart.x_labels = map(str, words1)
                                        line_chart.add('Number of words', numbers1)
                                        line_chart.render_to_file("negative_word_frequency_text1_with_stoplist.svg")
                                        print("You can find the results on your computer!\n",
                                              "Positive chart: positive_word_frequency_text1_with_stoplist.svg\n",
                                              "Negative chart: negative_word_frequency_text1_with_stoplist.svg\n",
                                              "The results: Results_text1_with_stoplist.txt")
                                    else:
                                        choosing_number_again()
                                        choosing_no()
                                else:
                                    print(Fore.CYAN + "Thank you for using my tool! See you next time :)")

                    analyzing_one(file1)

                else:
                    choosing_number_again()
                    choosing_no()


        # OPENING NEGATIVE LIST:
        elif number == 2:
            filen = r"C:\Users\kasia\Desktop\Projekt programowanie\negative.txt"
            plikn = open(filen, 'r', encoding="utf8")
            print(plikn.read())
            plikn.close()
            print("\n")
            main_screen_function()
            choosing_no()
        # OPENING POSITIVE LIST:
        elif number == 3:
            filep = r"C:\Users\kasia\Desktop\Projekt programowanie\positive.txt"
            plikp = open(filep, 'r', encoding="utf8")
            print(plikp.read())
            plikp.close()
            print("\n")
            main_screen_function()
            choosing_no()

        # OPENING A STOPLIST:
        elif number == 4:
            files = r"C:\Users\kasia\Desktop\Projekt programowanie\stoplist.txt"
            open_stoplist(files)
            print("\n")
            main_screen_function()
            choosing_no()

        elif number == 7:
            exit_screen_f()
            choosing_no()

        elif number == 5:
            keywords_analysis()
            choosing_number_again()
            choosing_no()

        elif number == 6:
            downloading_texts()
            choosing_no()

        else:
            print(Fore.RED + "Please choose from 1 to 4 :)")
            choosing_no()
    choosing_no()
general()





