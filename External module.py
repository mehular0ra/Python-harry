import re

tweet = """Our #COVID19 vaccination analysis "#CoWIN: Really Winning? Analysing Inequity in India’s Vaccination Response"  
Blog https://precog.iiit.ac.in/blog/2022/02/15/co-win-really-winning-analysing-inequity-in-indias-vaccination-response/ 
Full paper https://arxiv.org/abs/2202.04433 
w/ @hemanklamba @meghaarora42 @tanvi141 @Avinash_2468 @mehulma67701972 
#academictwitter Findings🧵"""


def Tokenizer(inp = None):
    word_regex=r"#\S+|@\S+|Dr\.|Mr\.|Mrs\.|[0-9]+\.[0-9]+|\w*'t|\w*'s|\w+|'|,|\.|\w*'t\b|\(|\)|\\|\/|-|!\s+"
    url_regex = r"https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}"
    word_regex = url_regex + r"|" + word_regex
    
    hash_regex = r"#\S+"
    mention_regex = r"@\S+"

    ret = re.findall(word_regex, inp)
    # ret = re.sub(url_regex, "<URL>", str(ret))
    # ret = re.sub(hash_regex, "<HASHTAG>", str(ret)) 
    # ret = re.sub(mention_regex, "<MENTION>", str(ret)) 
    return ret


re_tweet = Tokenizer(tweet)
print(re_tweet)
