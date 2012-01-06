# -*- coding: utf-8 -*-
# module SkypeApi

import sys;
from time import sleep;

import Skype;

def AccountOnChange (self, property_name):
	global loggedIn;
	if property_name == 'status':
		if self.status == 'LOGGED_IN':
			loggedIn = True;
			print('Login complete.');

def ParticipantOnChange (self, property_name):
	if property_name == 'voice_status':

		# It makes sense to only display 'joined call' and 'left call'
		# feedback messages for people other than ourselves.
		if self.identity != accountName:
			if self.voice_status == 'SPEAKING':
				print(self.identity + ' has joined the call.');

			if self.voice_status == 'VOICE_STOPPED':
				print(self.identity + ' has left the call.');

		if (self.identity == accountName) and (self.voice_status == 'VOICE_STOPPED'):
			global isCallFinished;
			isCallFinished = True;

	# This property enables you to have neat voice activity indicators in your UI.
	if property_name == 'sound_level':
		print(self.identity + ' sound level: ' + str(self.sound_level));

class SkypeApi:
	
	def __init__(self, skypename, password):
		global loggedIn;
		global isCallFinished;

		self.skypename = skypename;

		loggedIn = False;
		isCallFinished = False;

		Skype.Account.OnPropertyChange = AccountOnChange;
		Skype.isLiveSessionUp = False;
		Skype.liveSession = 0;

		Skype.Participant.OnPropertyChange = ParticipantOnChange;

		self.MySkype = Skype.GetSkype('DeveloperKeyPair.pem');

		self.account = self.MySkype.GetAccount(skypename);
		print('Logging in with ' + skypename);
		self.account.LoginWithPassword(password, False, False);
		while loggedIn == False:
			sleep(1);

	def call(self, callTargets):
		global isCallFinished;

		self.liveConversation = self.MySkype.GetConversationByParticipants(callTargets, True, False);
		callParticipants = self.liveConversation.GetParticipants('ALL');
		if len(callParticipants) > 0:
			for P in callParticipants:
				if P.identity != self.skypename:
					print('Calling ' + P.identity + '..');

		isCallFinished = False;
		self.liveConversation.RingOthers(callTargets, False, '');

	def endcall(self):
		global isCallFinished;

		self.liveConversation.LeaveLiveSession(False);
		while not isCallFinished:
			sleep(1);

	def stop(self):
		self.MySkype.stop();
	
#api = SkypeApi('mushroom_conf', 'mushroom0')
#api.call([ 'jwebkr' ])

