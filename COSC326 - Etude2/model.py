import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer

IN_SYLLABLES = "data/30000_common_syllables.csv"
TEST_SYLLABLES = "data/6000_syllables.csv"

OUT_MODEL = "pickle/model.pkl"
OUT_VECTORIZER = "pickle/vectorizer.pkl"

print(f"Generating model using dataset: {IN_SYLLABLES}")

df = pd.read_csv(IN_SYLLABLES, header=None, names=["word", "syllables"])
df = df.dropna()

vectorizer = CountVectorizer(analyzer="char", ngram_range=(1, 2))
vectorizer.fit(df["word"])

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


def create_variables(df: pd.DataFrame) -> pd.DataFrame:
    newDf = pd.DataFrame()
    newDf["syllables"] = df["syllables"]
    newDf["wordLength"] = df["word"].str.len()
    newDf["AsContained"] = df["word"].str.count("a")
    newDf["EsContained"] = df["word"].str.count("e")
    newDf["OsContained"] = df["word"].str.count("o")
    newDf["UsContained"] = df["word"].str.count("u")
    newDf["IsContained"] = df["word"].str.count("i")
    newDf["YsContained"] = df["word"].str.count("y")
    newDf["vowelCount"] = (
        newDf["AsContained"]
        + newDf["EsContained"]
        + newDf["OsContained"]
        + newDf["UsContained"]
        + newDf["IsContained"]
        + newDf["YsContained"]
    )
    newDf["startsInVowel"] = df["word"].apply(lambda x: x[0] in vowels)
    newDf["endsInVowel"] = df["word"].apply(is_vowel)
    newDf["finalLetter"] = df["word"].apply(get_last)
    newDf["diphthongs"] = df["word"].apply(count_diphthongs)
    newDf["triphthongs"] = df["word"].apply(count_triphthongs)
    newDf["hiatus"] = df["word"].apply(lambda x: "ia" in x)
    newDf["prefix"] = df["word"].apply(get_prefix)
    newDf["suffix"] = df["word"].apply(get_suffix)

    cvMatrix = vectorizer.transform(df["word"])
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

    return newDf.dropna()


variablesDataFrame = create_variables(df)
X = variablesDataFrame.drop("syllables", axis=1)
y = variablesDataFrame[["syllables"]]

dt = DecisionTreeClassifier(random_state=1, criterion="entropy")
dt = dt.fit(X, y)

print("Finished training model")

print(f"Testing model accuracy using: {TEST_SYLLABLES}")

testDF = pd.read_csv(
    TEST_SYLLABLES, header=None, names=["word", "syllables"]
)
testDF = testDF.dropna()
testDataFrame = create_variables(testDF)
y_score = testDataFrame[["syllables"]]
testDataFrame = testDataFrame.drop("syllables", axis=1)

print(f"Accuracy: {100 * dt.score(testDataFrame, y_score)}")

print(f"Dumping vectorizer to: {OUT_VECTORIZER}")

pickle.dump(vectorizer, open(OUT_VECTORIZER, "wb"))

print("Finished dumping vectorizer")

print(f"Dumping model to: {OUT_MODEL}")

pickle.dump(dt, open(OUT_MODEL, "wb"))

print("Finished dumping model")
