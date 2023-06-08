import pandas as pd


english_to_maori_pronouns = {
    "i": "au",
    "me": "ahau",
    "you": "koe",
    "you (1 incl)": "koe",
    "he": "ia",
    "she": "ia",
    "him": "ia",
    "her": "ia",
    "we (2 excl)": "māua",
    "we (2 incl)": "tāua",
    "us (2 incl)": "tāua",
    "us (2 excl)": "māua",
    "you (2 incl)": "kōrua",
    "they (2 excl)": "rāua",
    "them (2 excl)": "rāua",
    "we (3 excl)": "mātou",
    "we (3 incl)": "tātou",
    "us (3 incl)": "tātou",
    "us (3 excl)": "mātou",
    "you (3 incl)": "koutou",
    "they (3 excl)": "rātou",
    "them (3 excl)": "rātou",
}

english_to_maori_verbs = {
    "go": "haere",
    "make": "hanga",
    "see": "kite",
    "want": 'hiahia',
    "call": "karanga",
    "ask": "pātai",
    "read": "pānui",
    "learn": "ako",
    "going": "haere",
    "making": "hanga",
    "seeing": "kite",
    "wanting": 'hiahia',
    "calling": "karanga",
    "asking": "pātai",
    "reading": "pānui",
    "learning": "ako",
    "went": "haere",
    "saw": "kite",
    "made": "hanga",
    "wanted": "hiahia",
    "called": "karanga",
    "asked": "pātai",
    "read": "pānui",
    "learned": "ako",
    "learnt": "haere",
    "wants": "hiahia"
}

english_to_maori_tense = {
    "wants": "Kei te",
    "went": "I",
    "going": "Kei te",
    "made": "I",
    "making": "Kei te",
    "saw": "I",
    "seeing": "Kei te",
    "wanted": "I",
    "want": "Kei te",
    "called": "I",
    "calling": "Kei te",
    "asked": "I",
    "asking": "Kei te",
    "read": "I",
    "reading": "Kei te",
    "learned": "I",
    "learning": "Kei te",
}


def parse_tense(sentence):
    words = sentence.split()
    tense = None
    if "will" in words:
        tense = "Ka"
    elif "am" in words:
        tense = "Kei te"
    elif "are" in words:
        tense = "Kei te"
    elif "is" in words:
        tense = "Kei te"
    else:
        for word in words:
            if word in english_to_maori_tense:
                tense = english_to_maori_tense[word]
    return tense


def parse_sentence(sentence):
    words = sentence.split()
    pronoun = None
    verb = None
    pronoun_extention = None
    incl_excl = None
    contains_incl_excl = False

    for word in words:
        if "(" in word:
            contains_incl_excl = True
            num_people = ""
            start_index = word.find("(") + 1
            for i in range(start_index, len(word)):
                if word[i] == " ":
                    "breaking loop"
                    break
                num_people += word[i]
        if "excl" in word:
            incl_excl = "excl"
        if "incl" in word:
            incl_excl = "incl"

    if contains_incl_excl == True:
        if int(num_people) == 2:
            pronoun_extention = " (2 " + incl_excl + ")"

        if int(num_people) >= 3:
            pronoun_extention = " (3 " + incl_excl + ")"

    for word in words:
        if pronoun_extention != None:
            word_with_extention = word + pronoun_extention
        if word in english_to_maori_pronouns:
            pronoun = english_to_maori_pronouns[word]
        if pronoun_extention != None and word_with_extention in english_to_maori_pronouns:
            pronoun = english_to_maori_pronouns[word_with_extention]
        if word in english_to_maori_verbs:
            verb = english_to_maori_verbs[word]
    return pronoun, verb


def translate_sentence(sentence):
    sentence = sentence.lower()
    try:
        pronoun, verb = parse_sentence(sentence)
        tense = parse_tense(sentence)
        if tense == verb:
            return verb + " " + pronoun
        else:
            return tense + " " + verb + " " + pronoun
    except TypeError:
        return "INVALID"


def main():
    while True:
        try:
            sentence = input()
            if sentence.lower() == '':
                break
        except EOFError:
            break
        sentence = sentence.lower()
        try:
            pronoun, verb = parse_sentence(sentence)
            tense = parse_tense(sentence)
            if tense == verb:
                print(verb + " " + pronoun)
            else:
                print(tense + " " + verb + " " + pronoun)
        except TypeError:
            print("INVALID")


if __name__ == "__main__":
    main()
