# -*- coding: utf-8 -*-

import yaml
import random

_bird_emoji = ['🐦', '🐤', '🐥', '🦆', '🦅', '🦉', '🕊', '🐓', '🦃']
_senti_emoji = {
    'pos': ['😍', '😎', '🤩', '😘', '😄', '😊'],
    'neg': ['🤥', '😤', '😠', '😡', '😱', '😰', '😥'],
    'neu': ['🙂', '🙃', '🧐', '🙄', '😴'],
}

_templates = yaml.load(open('bothub/response.yml', 'r'))

def template(key):
    return random.choice(_templates[key])

def bird_emoji():
    return random.choice(_bird_emoji)

def senti_emoji(senti_score):
    if senti_score > 0.9:
        cls = 'pos'
    elif senti_score < 0.75:
        cls = 'neg'
    else:
        cls = 'neu'
    return random.choice(_senti_emoji[cls])
