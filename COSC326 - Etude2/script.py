import pickle
import sys
import pandas as pd

IN_MODEL = "pickle/model.pkl"
IN_VECTORIZER = "pickle/vectorizer.pkl"

model = pickle.load(open(IN_MODEL, "rb"))
vectorizer = pickle.load(open(IN_VECTORIZER, "rb"))

prefixes = [
    "ab",
    "ad",
    "an",
    "ante",
    "anti",
    "auto",
    "be",
    "bi",
    "centi",
    "circum",
    "co",
    "de",
    "deca",
    "di",
    "dia",
    "dis",
    "em",
    "en",
    "endo",
    "epi",
    "eu",
    "ex",
    "extra",
    "fore",
    "giga",
    "hemi",
    "hepta",
    "hetero",
    "hexa",
    "homo",
    "hyper",
    "hypo",
    "il",
    "im",
    "in",
    "infra",
    "inter",
    "intra",
    "ir",
    "iso",
    "kilo",
    "macro",
    "mega",
    "micro",
    "milli",
    "mis",
    "mono",
    "nano",
    "neo",
    "non",
    "nona",
    "octa",
    "omni",
    "pan",
    "para",
    "penta",
    "peri",
    "poly",
    "post",
    "pre",
    "pro",
    "re",
    "retro",
    "semi",
    "sub",
    "super",
    "tele",
    "tera",
    "tetra",
    "therm",
    "trans",
    "tri",
    "un",
    "uni",
]
suffixes = [
    "a",
    "ability",
    "able",
    "ably",
    "ac",
    "acean",
    "aceous",
    "ad",
    "ade",
    "aemia",
    "age",
    "aholic",
    "al",
    "algia",
    "all",
    "amine",
    "an",
    "ana",
    "ance",
    "ancy",
    "androus",
    "andry",
    "ane",
    "ant",
    "ar",
    "arch",
    "archy",
    "ard",
    "arian",
    "arium",
    "art",
    "ary",
    "ase",
    "ate",
    "athon",
    "ation",
    "ative",
    "ator",
    "atory",
    "biont",
    "biosis",
    "blast",
    "bot",
    "cade",
    "caine",
    "carp",
    "carpic",
    "carpous",
    "cele",
    "cene",
    "centric",
    "cephalic",
    "cephalous",
    "cephaly",
    "chore",
    "chory",
    "chrome",
    "cide",
    "clast",
    "clinal",
    "cline",
    "clinic",
    "coccus",
    "coel",
    "coele",
    "colous",
    "cracy",
    "crat",
    "cratic",
    "cratical",
    "cy",
    "cyte",
    "dale",
    "derm",
    "derma",
    "dermatous",
    "dom",
    "drome",
    "dromous",
    "ean",
    "eaux",
    "ectomy",
    "ed",
    "ee",
    "eer",
    "ein",
    "eme",
    "emia",
    "en",
    "ence",
    "enchyma",
    "ency",
    "ene",
    "ent",
    "eous",
    "er",
    "ergic",
    "ergy",
    "es",
    "escence",
    "escent",
    "ese",
    "esque",
    "ess",
    "est",
    "et",
    "eth",
    "etic",
    "ette",
    "ey",
    "facient",
    "faction",
    "fer",
    "ferous",
    "fic",
    "fication",
    "fid",
    "florous",
    "fold",
    "foliate",
    "foliolate",
    "form",
    "fuge",
    "ful",
    "fy",
    "gamous",
    "gamy",
    "gate",
    "gen",
    "gene",
    "genesis",
    "genetic",
    "genic",
    "genous",
    "geny",
    "gnathous",
    "gon",
    "gony",
    "gram",
    "graph",
    "grapher",
    "graphy",
    "gyne",
    "gynous",
    "gyny",
    "hood",
    "ia",
    "ial",
    "ian",
    "iana",
    "iasis",
    "iatric",
    "iatrics",
    "iatry",
    "ibility",
    "ible",
    "ic",
    "icide",
    "ician",
    "ick",
    "ics",
    "id",
    "ide",
    "ie",
    "ify",
    "ile",
    "in",
    "ine",
    "ing",
    "ion",
    "ious",
    "isation",
    "ise",
    "ish",
    "ism",
    "ist",
    "istic",
    "istical",
    "istically",
    "ite",
    "itious",
    "itis",
    "ity",
    "ium",
    "ive",
    "ix",
    "ization",
    "ize",
    "i-",
    "kin",
    "kinesis",
    "kins",
    "latry",
    "le",
    "lepry",
    "less",
    "let",
    "like",
    "ling",
    "lite",
    "lith",
    "lithic",
    "log",
    "logue",
    "logic",
    "logical",
    "logist",
    "logy",
    "ly",
    "lyse",
    "lysis",
    "lyte",
    "lytic",
    "lyze",
    "mancy",
    "mania",
    "meister",
    "ment",
    "mer",
    "mere",
    "merous",
    "meter",
    "metric",
    "metrics",
    "metry",
    "mire",
    "mo",
    "morph",
    "morphic",
    "morphism",
    "morphous",
    "most",
    "mycete",
    "mycin",
    "nasty",
    "ness",
    "nik",
    "nomy",
    "nomics",
    "o",
    "ode",
    "odon",
    "odont",
    "odontia",
    "oholic",
    "oic",
    "oid",
    "ol",
    "ole",
    "oma",
    "ome",
    "omics",
    "on",
    "one",
    "ont",
    "onym",
    "onymy",
    "opia",
    "opsis",
    "opsy",
    "or",
    "orama",
    "ory",
    "ose",
    "osis",
    "otic",
    "otomy",
    "ous",
    "para",
    "parous",
    "path",
    "pathy",
    "ped",
    "pede",
    "penia",
    "petal",
    "phage",
    "phagia",
    "phagous",
    "phagy",
    "phane",
    "phasia",
    "phil",
    "phile",
    "philia",
    "philiac",
    "philic",
    "philous",
    "phobe",
    "phobia",
    "phobic",
    "phone",
    "phony",
    "phore",
    "phoresis",
    "phorous",
    "phrenia",
    "phyll",
    "phyllous",
    "plasia",
    "plasm",
    "plast",
    "plastic",
    "plasty",
    "plegia",
    "plex",
    "ploid",
    "pod",
    "pode",
    "podous",
    "poieses",
    "poietic",
    "pter",
    "punk",
    "rrhagia",
    "rrhea",
    "ric",
    "ry",
    "s",
    "scape",
    "scope",
    "scopy",
    "scribe",
    "script",
    "sect",
    "sepalous",
    "ship",
    "some",
    "speak",
    "sperm",
    "sphere",
    "sporous",
    "st",
    "stasis",
    "stat",
    "ster",
    "stome",
    "stomy",
    "taxis",
    "taxy",
    "tend",
    "th",
    "therm",
    "thermal",
    "thermic",
    "thermy",
    "thon",
    "thymia",
    "tion",
    "tome",
    "tomy",
    "tonia",
    "trichous",
    "trix",
    "tron",
    "trophic",
    "trophy",
    "tropic",
    "tropism",
    "tropous",
    "tropy",
    "tude",
    "ture",
    "ty",
    "ular",
    "ule",
    "ure",
    "urgy",
    "uria",
    "uronic",
    "urous",
    "valent",
    "virile",
    "vorous",
    "ward",
    "wards",
    "ware",
    "ways",
    "wear",
    "wide",
    "wise",
    "worthy",
    "xor",
    "y",
    "yl",
    "yne",
    "zilla",
    "zoic",
    "zoon",
    "zygous",
    "zyme",
]
vowels = "aeiouy"

is_vowel = lambda x: x[-1] in vowels


def get_prefix(x: str) -> int:
    x = x.casefold()
    for i, v in enumerate(prefixes):
        if x.startswith(v.casefold()):
            return i
    return -1


def get_suffix(x: str) -> int:
    x = x.casefold()
    for i, v in enumerate(suffixes):
        if x.endswith(v.casefold()):
            return i
    return -1


def count_diphthongs(x: str) -> int:
    count = 0
    for i in range(len(x) - 2):
        if (
            x[i] in vowels
            and x[i + 1] in vowels
            and x[i + 2] not in vowels
        ):
            count += 1
    return count


def count_triphthongs(x: str) -> int:
    count = 0
    for i in range(len(x) - 2):
        if x[i] in vowels and x[i + 1] in vowels and x[i + 2] in vowels:
            count += 1
    return count


def get_last(x: str) -> int:
    i = x[-1]
    if i == "a":
        return 1
    if i == "o":
        return 2
    if i == "e":
        return 3
    if i == "u":
        return 4
    if i == "i":
        return 5
    if i == "y":
        return 6
    else:
        return 0


def count_syllables(inputWord: str) -> int:
    newDf = pd.DataFrame()
    inputLen = len(inputWord)
    newDf["wordLength"] = [inputLen]
    newDf["AsContained"] = inputWord.count("a")
    newDf["EsContained"] = inputWord.count("e")
    newDf["OsContained"] = inputWord.count("o")
    newDf["UsContained"] = inputWord.count("u")
    newDf["IsContained"] = inputWord.count("i")
    newDf["YsContained"] = inputWord.count("y")
    newDf["vowelCount"] = (
        newDf["AsContained"]
        + newDf["EsContained"]
        + newDf["OsContained"]
        + newDf["UsContained"]
        + newDf["IsContained"]
        + newDf["YsContained"]
    )
    newDf["startsInVowel"] = inputWord[0] in vowels
    newDf["endsInVowel"] = is_vowel(inputWord)
    newDf["finalLetter"] = get_last(inputWord)
    newDf["diphthongs"] = count_diphthongs(inputWord)
    newDf["triphthongs"] = count_triphthongs(inputWord)
    newDf["hiatus"] = "ia" in inputWord
    newDf["prefix"] = get_prefix(inputWord)
    newDf["suffix"] = get_suffix(inputWord)

    cvMatrix = vectorizer.transform([inputWord])
    vectorizerDf = pd.DataFrame(
        cvMatrix.todense(), columns=vectorizer.get_feature_names_out()
    )
    newDf = pd.concat(
        [
            newDf.reset_index(drop=True),
            vectorizerDf.reset_index(drop=True),
        ],
        axis=1,
    )

    return model.predict(newDf)[0]


def main() -> None:
    for line in sys.stdin:
        print(count_syllables(line.strip()))


if __name__ == "__main__":
    main()
