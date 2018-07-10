# -*- coding: utf-8 -*-
from __future__ import unicode_literals # za naša slova
import tweepy, urllib, json, random, schedule, time, sys, os

response = urllib.urlopen("https://baza-podataka.herokuapp.com/quotes/")
# SETUP TWEEPY (from env variables)
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

# FUNKCIJE

def filtriraj(quotes):
    f = open("fajl.txt", 'r+')
    objavljeno = f.readlines()
    sr_citati = [q for q in quotes if q["sr"]]
    if len(objavljeno) >= len(sr_citati):
        f.truncate(0)
    return [q for q in quotes if q["sr"] and not q["_id"] in objavljeno]

def sacuvaj(id):
    with open("fajl.txt", "a") as fajl:
        fajl.write(id + "\n")

def dajIzreku(quotes):
    citat = random.choice(quotes)
    sacuvaj(citat["_id"])
    tekst = citat["sr"]
    autor = citat["author"]
    return """"{0}"
    — {1}""".format(tekst, autor)

def objavi(api):
    filtrirano = filtriraj(json.load(response))
    izreka = dajIzreku(filtrirano)
    if len(izreka) <= 280:
        api.update_status(status=izreka)
        print(izreka)
    else:
        objavi(api)

# INIT

objavi(api)

schedule.every(30).minutes.do(objavi)

while 1:
    schedule.run_pending()
    time.sleep(1)
