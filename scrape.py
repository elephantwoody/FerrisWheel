import requests
from bs4 import BeautifulSoup

def tweets_a ():
    r_a = requests.get("https://twitter.com/search?q=%23Abortion&src=typd&")
    r_a.content
    soup = BeautifulSoup(r_a.content, "html.parser")

    a = ""
    i_a = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        a += "%s. " % i_a
        a += tweets.find('p').text + ("\n")
        i_a = i_a + 1

        if i_a >= 6:
            break

    return a

def tweets_b ():
    r_b = requests.get("https://twitter.com/search?q=%23PlannedParenthood&src=typd&")
    r_b.content
    soup = BeautifulSoup(r_b.content, "html.parser")

    b = ""
    i_b = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        b += "%s. " % i_b
        b += tweets.find('p').text + ("\n")
        i_b = i_b + 1

        if i_b >= 6:
            break

    return b

def tweets_c ():
    r_c = requests.get("https://twitter.com/search?q=%23ReligiousFreedom&src=typd&")
    r_c.content
    soup = BeautifulSoup(r_c.content, "html.parser")

    c = ""
    i_c = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        c += "%s. " % i_c
        c += tweets.find('p').text + ("\n")
        i_c = i_c + 1

        if i_c >= 6:
            break

    return c

def tweets_d ():
    r_d = requests.get("https://twitter.com/search?q=%23GayMarriage&src=typd&")
    r_d.content
    soup = BeautifulSoup(r_d.content, "html.parser")

    d = ""
    i_d = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        d += "%s. " % i_d
        d += tweets.find('p').text + ("\n")
        i_d = i_d + 1

        if i_d >= 6:
            break

    return d

def tweets_e ():
    r_e = requests.get("https://twitter.com/search?q=%23GenderIdentity&src=typd&")
    r_e.content
    soup = BeautifulSoup(r_e.content, "html.parser")

    e = ""
    i_e = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        e += "%s. " % i_e
        e += tweets.find('p').text + ("\n")
        i_e = i_e + 1

        if i_e >= 6:
            break

    return e

def tweets_f ():
    r_f = requests.get("https://twitter.com/search?q=%23LGBTAdoption&src=typd&")
    r_f.content
    soup = BeautifulSoup(r_f.content, "html.parser")

    f = ""
    i_f = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        f += "%s. " % i_f
        f += tweets.find('p').text + ("\n")
        i_f = i_f + 1

        if i_f >= 6:
            break

    return f

def tweets_g ():
    r_g = requests.get("https://twitter.com/search?q=%23DeathPenalty&src=typd&")
    r_g.content
    soup = BeautifulSoup(r_g.content, "html.parser")

    g = ""
    i_g = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        g += "%s. " % i_g
        g += tweets.find('p').text + ("\n")
        i_g = i_g + 1

        if i_g >= 6:
            break

    return g

def tweets_h ():
    r_h = requests.get("https://twitter.com/search?q=%23SafeSpaces&src=typd&")
    r_h.content
    soup = BeautifulSoup(r_h.content, "html.parser")

    h = ""
    i_h = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        h += "%s. " % i_h
        h += tweets.find('p').text + ("\n")
        i_h = i_h + 1

        if i_h >= 6:
            break

    return h

def tweets_i ():
    r_i = requests.get("https://twitter.com/search?q=%23FirstAmendment&src=typd&")
    r_i.content
    soup = BeautifulSoup(r_i.content, "html.parser")

    i = ""
    i_i = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        i += "%s. " % i_i
        i += tweets.find('p').text + ("\n")
        i_i = i_i + 1

        if i_i >= 6:
            break

    return i

def tweets_j ():
    r_j = requests.get("https://twitter.com/search?q=%23GovernmentMandates&src=typd&")
    r_j.content
    soup = BeautifulSoup(r_j.content, "html.parser")

    j = ""
    i_j = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        j += "%s. " % i_j
        j += tweets.find('p').text + ("\n")
        i_j = i_j + 1

        if i_j >= 6:
            break

    return j

def tweets_k ():
    r_k = requests.get("https://twitter.com/search?q=%23WorkplaceDiversity&src=typd&")
    r_k.content
    soup = BeautifulSoup(r_k.content, "html.parser")

    k = ""
    i_k = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        k += "%s. " % i_k
        k += tweets.find('p').text + ("\n")
        i_k = i_k + 1

        if i_k >= 6:
            break

    return k

def tweets_l ():
    r_l = requests.get("https://twitter.com/search?q=%23WomenInCombat&src=typd&")
    r_l.content
    soup = BeautifulSoup(r_l.content, "html.parser")

    l = ""
    i_l = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        l += "%s. " % i_l
        l += tweets.find('p').text + ("\n")
        i_l = i_l + 1

        if i_l >= 6:
            break

    return l

def tweets_m ():
    r_m = requests.get("https://twitter.com/search?q=%23MaritalRape&src=typd&")
    r_m.content
    soup = BeautifulSoup(r_m.content, "html.parser")

    m = ""
    i_m = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        m += "%s. " % i_m
        m += tweets.find('p').text + ("\n")
        i_m = i_m + 1

        if i_m >= 6:
            break

    return m

def tweets_n ():
    r_n = requests.get("https://twitter.com/search?q=%23Euthanasia&src=typd&")
    r_n.content
    soup = BeautifulSoup(r_n.content, "html.parser")

    n = ""
    i_n = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        n += "%s. " % i_n
        n += tweets.find('p').text + ("\n")
        i_n = i_n + 1

        if i_n >= 6:
            break

    return n

def tweets_o ():
    r_o = requests.get("https://twitter.com/search?q=%23ConfederateFlag&src=typd&")
    r_o.content
    soup = BeautifulSoup(r_o.content, "html.parser")

    o = ""
    i_o = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        o += "%s. " % i_o
        o += tweets.find('p').text + ("\n")
        i_o = i_o + 1

        if i_o >= 6:
            break

    return o

def tweets_p ():
    r_p = requests.get("https://twitter.com/search?q=%23Niqab&src=typd&")
    r_p.content
    soup = BeautifulSoup(r_p.content, "html.parser")

    p = ""
    i_p = 1

    for tweets in soup.findAll('div', {"class":"content"}):
        p += "%s. " % i_p
        p += tweets.find('p').text + ("\n")
        i_p = i_p + 1

        if i_p >= 6:
            break

    return p
