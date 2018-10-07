# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from bothub_client.decorators import command

from bothub import telegram_alpha as telegram
from bothub.response import template, bird_emoji, senti_emoji

import requests
import json


class Bot(BaseBot):
    @command('start')
    def command_handler(self, event, content, args):
        self.send_message(template('start') + ' ' + bird_emoji())

    @channel()
    def default_handler(self, event, context):
        intent = self.detect_intent(event, context)
        if intent == 'intent.bird.gen':
            self.send_message(template('one_sec'))
            url = self.gen_bird_pic(event['content'])
            self.send_message(template('here_you_go'))
            if event['channel'] == 'telegram':
                telegram.send_photo(event, context, url)
            else:
                self.send_message(url)
        else:
            senti_score = self.sentiment_score(event['content'])
            emoji = senti_emoji(senti_score)
            self.send_message(emoji)

    def detect_intent(self, event, conext):
        text = event['content']
        text = text.lower()
        if text.find('bird') >= 0:
            return 'intent.bird.gen'
        else:
            return 'intent.fallback'

    def api_key(self):
        return self.get_project_data().get('api_key')

    def gen_bird_pic(self, caption):
        url = 'https://c4jn3eek1c.execute-api.us-east-1.amazonaws.com/Prod/bird'
        headers = { 'content-type': 'application/json', 'x-api-key': self.api_key() }
        payload = { 'caption': caption }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        return r.json()['url']

    def sentiment_score(self, message):
        url = 'https://jzn2o2euj2.execute-api.us-east-1.amazonaws.com/Prod/sentiment'
        headers = { 'content-type': 'application/json', 'x-api-key': self.api_key() }
        payload = { 'message': message }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        return r.json()['sentiment']


