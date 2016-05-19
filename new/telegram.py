#-*- coding: utf-8 -*-
#Classes declaradas a partir da API do telegram

#Standard imports
import json

class Hangman (object):
    def __init__(self, message):
        self.message_id       = message['message_id']
        self.from             = User(message['from'])
        self.chat             = Chat(message['chat'])
        self.reply_to_message = Hangman(message.get('reply_to_message')) if message.get('reply_to_message') else None
        self.text             = message.get('text')
        self.location         = Location(message.get('location')) if message.get('location') else None
        self.left_chat_member = User(message.get('left_chat_member')) if message.get('left_chat_member') else None

        if self.text:
            #if self.text.startswith('@ccuem_bot'):
            #    self.text = self.text[11:]
            if self.text.startswith('@PlayHangmanBot'):
                self.text = self.text[15:]
            if not self.text.startswith('/admin'):
                self.text = self.text.lower()

class User(object):
    def __init__(self, user):
        self.id         = user['id']
        self.first_name	= user['first_name']
        self.last_name  = user.get('last_name')
        self.username   = user.get('username')

class Chat(object):
    def __init__(self, chat):
        self.id         = chat['id']
        self.type       = chat['type']
        self.title      = chat.get('title')
        self.username   = chat.get('username')
        self.first_name = chat.get('first_name')
        self.last_name  = chat.get('last_name')

class Location(object):
    def __init__(self,location):
        self.longitude = location['longitude']
        self.latitude  = location['latitude']
