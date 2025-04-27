import PySimpleGUI as sg

PARTITION_TEXT = "http://jhsjk.people.cn"

# ("WORD", 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)
OCCUR_KEYWORDS = [
    ["人民", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["团结", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["我们的", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["国家", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["民族", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["奋斗", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["伟大", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["责任", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["梦想", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["中国梦", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["复兴", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["伟大", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["家梦想", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["中华民族伟大复兴的中国梦", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["社会主义核心价值观", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["遗产", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["人格", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["斗争", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["中华民族伟大复兴的", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["人民对美好生活的向往, 就是我们的奋斗目标", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# ("WORD", 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)
# describes occurrences of words with a keyword. Most probably with: 中国梦
OCCUR_WITH_KEYWORD = [
    ["人民", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["团结", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["我们的", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["国家", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["民族", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["奋斗", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["伟大", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["责任", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["梦想", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["复兴", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["伟大", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["家梦想", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["中华民族伟大复兴的中国梦", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["社会主义核心价值观", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["遗产", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["人格", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["斗争", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["中华民族伟大复兴的", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

ARTICLES_SUM = 0

CONTEXT_ITERATIONS = 0

ALL_SPEECHES = []
ALL_ARTICLES = []


def split_alternative(raw_text):
    speeches = []
    articles = []
    counter = 0
    speeches_counter = 0
    global ARTICLES_SUM

    text = raw_text
    splitted = text.splitlines()

    while counter < len(splitted):
        builder = ""
        if PARTITION_TEXT in splitted[counter]:
            articles.append(splitted[counter])
            counter += 1
            while PARTITION_TEXT not in splitted[counter]:
                counter += 1
                try:
                    builder += "\n" + splitted[counter]
                except IndexError:
                    speeches.append(builder.replace(splitted[counter - 1], ""))
                    return speeches, articles
            speeches.append(builder.replace(splitted[counter - 1], ""))
            speeches_counter += 1
        else:
            counter += 1
    return speeches, articles


def print_occur_keywords(occur_keywords):
    for i in range(0, len(occur_keywords)):
            print(f"""({occur_keywords[i][0]}, {occur_keywords[i][1]}, {occur_keywords[i][2]}, {occur_keywords[i][3]}, {occur_keywords[i][4]}, {occur_keywords[i][5]}, {occur_keywords[i][6]}, {occur_keywords[i][7]}, {occur_keywords[i][8]}, {occur_keywords[i][9]}, {occur_keywords[i][10]}, {occur_keywords[i][11]}, {occur_keywords[i][12]}, {occur_keywords[i][13]})""")
    print("\n")


def find_keywords(speeches, articles, year, result):
    if year == 2024: index = 13
    elif year == 2023: index = 12
    elif year == 2022: index = 11
    elif year == 2021: index = 10
    elif year == 2020: index = 9
    elif year == 2019: index = 8
    elif year == 2018: index = 7
    elif year == 2017: index = 6
    elif year == 2016: index = 5
    elif year == 2015: index = 4
    elif year == 2014: index = 3
    elif year == 2013: index = 2
    elif year == 2012: index = 1
    else: index = -1

    for j in range(0, len(speeches)):
        speech = speeches[j]
        for i in range(0, len(result)):
            keyword = result[i][0]
            occurrences = speech.count(keyword)
            result[i][index] += occurrences


def select_speeches_containing_keyword(speeches, keyword):
    result = []
    for speech in speeches:
        if keyword in speech:
            result.append(speech)
    return result


def find_context(all_speeches, all_articles, word, offset):
    global CONTEXT_ITERATIONS
    try:
        speech = all_speeches[CONTEXT_ITERATIONS]
        article = all_articles[CONTEXT_ITERATIONS]
    except IndexError:
        return "Tested all the strings.", "Please restart application."
    split = speech.split(word)
    builder = ""
    for k in range(0, len(split) - 1):
        try:
            tidy_before = split[k].replace("\n", "").replace("\r", "").replace("\r\n", "").replace("\n\n", "")[-offset:]
            tidy_after = split[k + 1].replace("\n", "").replace("\r", "").replace("\r\n", "").replace("\n\n", "")[:offset]
            found_context = tidy_before + word + tidy_after
            builder = builder + "Context: " + found_context + "\n"
        except IndexError:
            continue
    CONTEXT_ITERATIONS += 1
    if builder == "":
        if CONTEXT_ITERATIONS < len(all_speeches):
            return find_context(all_speeches, all_articles, word, offset)
        else:
            return "Tested all the strings.", "Please restart application."
    else:
        return article, builder


def execute():
    speeches = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
#    speeches = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
#    articles = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    articles = ["", "", "", "", "", "", "", "", "", "", "", "", ""]

    speech_2024 = open("Speeches/Speeches_2024")
    speech_2023 = open("Speeches/Speeches_2023")
    speech_2022 = open("Speeches/Speeches_2022")
    speech_2021 = open("Speeches/Speeches_2021")
    speech_2020 = open("Speeches/Speeches_2020")
    speech_2019 = open("Speeches/Speeches_2019")
    speech_2018 = open("Speeches/Speeches_2018")
    speech_2017 = open("Speeches/Speeches_2017")
    speech_2016 = open("Speeches/Speeches_2016")
    speech_2015 = open("Speeches/Speeches_2015")
    speech_2014 = open("Speeches/Speeches_2014")
    speech_2013 = open("Speeches/Speeches_2013")
    speech_2012 = open("Speeches/Speeches_2012")

    speeches[0], articles[0] = split_alternative(speech_2024.read())
    speeches[1], articles[1] = split_alternative(speech_2023.read())
    speeches[2], articles[2] = split_alternative(speech_2022.read())
    speeches[3], articles[3] = split_alternative(speech_2021.read())
    speeches[4], articles[4] = split_alternative(speech_2020.read())
    speeches[5], articles[5] = split_alternative(speech_2019.read())
    speeches[6], articles[6] = split_alternative(speech_2018.read())
    speeches[7], articles[7] = split_alternative(speech_2017.read())
    speeches[8], articles[8] = split_alternative(speech_2016.read())
    speeches[9], articles[9] = split_alternative(speech_2015.read())
    speeches[10], articles[10] = split_alternative(speech_2014.read())
    speeches[11], articles[11] = split_alternative(speech_2013.read())
    speeches[12], articles[12] = split_alternative(speech_2012.read())

    number_of_articles = 0
    for i in range(1, len(articles) - 1):
        number_of_articles = number_of_articles + len(articles[i])

    find_keywords(speeches[0], articles[0], 2024, OCCUR_KEYWORDS)
    find_keywords(speeches[1], articles[1], 2023, OCCUR_KEYWORDS)
    find_keywords(speeches[2], articles[2], 2022, OCCUR_KEYWORDS)
    find_keywords(speeches[3], articles[3], 2021, OCCUR_KEYWORDS)
    find_keywords(speeches[4], articles[4], 2020, OCCUR_KEYWORDS)
    find_keywords(speeches[5], articles[5], 2019, OCCUR_KEYWORDS)
    find_keywords(speeches[6], articles[6], 2018, OCCUR_KEYWORDS)
    find_keywords(speeches[7], articles[7], 2017, OCCUR_KEYWORDS)
    find_keywords(speeches[8], articles[8], 2016, OCCUR_KEYWORDS)
    find_keywords(speeches[9], articles[9], 2015, OCCUR_KEYWORDS)
    find_keywords(speeches[10], articles[10], 2014, OCCUR_KEYWORDS)
    find_keywords(speeches[11], articles[11], 2013, OCCUR_KEYWORDS)
    find_keywords(speeches[12], articles[12], 2012, OCCUR_KEYWORDS)

    for i in range(0, 12):
        speeches[i] = select_speeches_containing_keyword(speeches[i], "中国梦")

    find_keywords(speeches[0], articles[0], 2024, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[1], articles[1], 2023, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[2], articles[2], 2022, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[3], articles[3], 2021, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[4], articles[4], 2020, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[5], articles[5], 2019, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[6], articles[6], 2018, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[7], articles[7], 2017, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[8], articles[8], 2016, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[9], articles[9], 2015, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[10], articles[10], 2014, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[11], articles[11], 2013, OCCUR_WITH_KEYWORD)
    find_keywords(speeches[12], articles[12], 2012, OCCUR_WITH_KEYWORD)

    speech_2024 = open("Speeches/Speeches_2024")
    speech_2023 = open("Speeches/Speeches_2023")
    speech_2022 = open("Speeches/Speeches_2022")
    speech_2021 = open("Speeches/Speeches_2021")
    speech_2020 = open("Speeches/Speeches_2020")
    speech_2019 = open("Speeches/Speeches_2019")
    speech_2018 = open("Speeches/Speeches_2018")
    speech_2017 = open("Speeches/Speeches_2017")
    speech_2016 = open("Speeches/Speeches_2016")
    speech_2015 = open("Speeches/Speeches_2015")
    speech_2014 = open("Speeches/Speeches_2014")
    speech_2013 = open("Speeches/Speeches_2013")
    speech_2012 = open("Speeches/Speeches_2012")

    speeches[0], articles[0] = split_alternative(speech_2024.read())
    speeches[1], articles[1] = split_alternative(speech_2023.read())
    speeches[2], articles[2] = split_alternative(speech_2022.read())
    speeches[3], articles[3] = split_alternative(speech_2021.read())
    speeches[4], articles[4] = split_alternative(speech_2020.read())
    speeches[5], articles[5] = split_alternative(speech_2019.read())
    speeches[6], articles[6] = split_alternative(speech_2018.read())
    speeches[7], articles[7] = split_alternative(speech_2017.read())
    speeches[8], articles[8] = split_alternative(speech_2016.read())
    speeches[9], articles[9] = split_alternative(speech_2015.read())
    speeches[10], articles[10] = split_alternative(speech_2014.read())
    speeches[11], articles[11] = split_alternative(speech_2013.read())
    speeches[12], articles[12] = split_alternative(speech_2012.read())

    global ALL_SPEECHES, ALL_ARTICLES
    ALL_SPEECHES = speeches[0] + speeches[1] + speeches[2] + speeches[3] + speeches[4] + speeches[5] + speeches[6] + speeches[7] + speeches[8] + speeches[9] + speeches[10] + speeches[11] + speeches[12]
    ALL_ARTICLES = articles[0] + articles[1] + articles[2] + articles[3] + articles[4] + articles[5] + articles[6] + articles[7] + articles[8] + articles[9] + articles[10] + articles[11] + articles[12]
#    article, context = find_context(ALL_SPEECHES, ALL_ARTICLES, "中国梦", 5)

#    print(f"found article: {article}")
#    print(f"found context:\n{context}")

    print(f"{number_of_articles} analyzed articles.")
    print("OCCURRENCES OF ALL THE WORDS AMONG THE YEARS")
    print_occur_keywords(OCCUR_KEYWORDS)
    print("OCCURRENCES OF ALL THE WORDS IN SPEECHES CONTAINING THE WORD 中国梦")
    print_occur_keywords(OCCUR_WITH_KEYWORD)


if __name__ == "__main__":
    execute()

