from sqlalchemy.orm import mapper, relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
from sqlalchemy.sql import exists
from sqlalchemy.sql.expression import *
from sqlalchemy import MetaData, Table, Column, DateTime, SmallInteger, Integer, String, ForeignKey, create_engine

import time, random, os, re, datetime
from Helpers import PutLogFileList, PutLogList
from GlobalDef import AccountInfo, DEF, Logfile
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class Account(Base):
	__tablename__ = "account"
	AccountID = Column(Integer, primary_key = True)
	Name = Column(String(10), nullable = False, unique = True)
	Password = Column(String(10), nullable = False)
	Mail = Column(String(50), nullable = False)
	Quiz = Column(String(45))
	Answer = Column(String(20))
	SignupDate = Column(DateTime(), nullable = False)
	BlockDate = Column(DateTime())
	IpAddress = Column(String(15), nullable = False)
	
	def __init__(self, name, password, mail, quiz, answer, address):
		self.Name = name
		self.Password = password
		self.Mail = mail
		self.Quiz = quiz
		self.Answer = answer
		self.SignupDate = datetime.datetime.now()
		self.IpAddress = address
		
	def __repr__(self):
		return "<User('%s', '%s', '%s')>" % (str(self.AccountID), self.Name, self.Password)
	@staticmethod
	def ByName(session, name):
		try:
			return session.query(Account).\
				filter(Account.Name == name).\
				one()
		except NoResultFound:
			return False
	@staticmethod
	def Match( session, name, pwd):
		try:
			return session.query(Account).\
				filter(_and(Account.Name == name, Account.Password == pwd)).\
				one()
		except NoResultFound:
			return False
		
class Character(Base):
	__tablename__ = "character"
	AccountID = Column(Integer, ForeignKey("account.AccountID"))
	CharacterID = Column(Integer, primary_key = True)
	CharName = Column(String(10), nullable = False, unique = True)
	ID1 = Column(Integer, default = 0)
	ID2 = Column(Integer, default = 0)
	ID3 = Column(Integer, default = 0)
	Level = Column(Integer, default = 1)
	Strength = Column(Integer, default = 10)
	Dexterity = Column(Integer, default = 10)
	Intelligence = Column(Integer, default = 10)
	Magic = Column(Integer, default = 10)
	Vitality = Column(Integer, default = 10)
	Charisma = Column(Integer, default = 10)
	Luck = Column(Integer, default = 0)
	Experience = Column(Integer, default = 0)
	Gender = Column(SmallInteger, default = 0)
	Skin = Column(SmallInteger, default = 0)
	HairStyle = Column(SmallInteger, default = 0)
	HairColor = Column(SmallInteger, default = 0)
	Underwear = Column(SmallInteger, default = 0)
	ApprColor = Column(Integer, default = 0)
	Appr1 = Column(Integer, default = 0)
	Appr2 = Column(Integer, default = 0)
	Appr3 = Column(Integer, default = 0)
	Appr4 = Column(Integer, default = 0)
	Nation = Column(String(10), default = "NONE")
	MapLoc = Column(String(10), default = "default")
	LocX = Column(SmallInteger, default = 0)
	LocY = Column(SmallInteger, default = 0)
	Profile = Column(String(255))
	AdminLevel = Column(SmallInteger, default = 0)
	Contribution = Column(Integer, default = 0)
	LeftSpecialTime = Column(Integer, default = 0)
	LockedMapName = Column(String(10), default = "")
	LockedMapTime = Column(Integer, default = 0)
	CreateDate = Column(DateTime)
	BlockDate = Column(DateTime)
	GuildName = Column(String(20))
	GuildID = Column(Integer, default = -1)
	GuildRank = Column(Integer, default = -1)
	FightNum = Column(SmallInteger, default = 0)
	FightDate = Column(SmallInteger, default = 0)
	FightTicket = Column(SmallInteger, default = 0)
	QuestNum = Column(SmallInteger, default = 0)
	QuestID = Column(SmallInteger, default = 0)
	QuestCount = Column(SmallInteger, default = 0)
	QuestRewType = Column(SmallInteger, default = 0)
	QuestRewAmmount = Column(SmallInteger, default = 0)
	QuestCompleted = Column(SmallInteger, default = 0)
	EventID = Column(Integer, default = 0)
	WarCon = Column(Integer, default = 0)
	CruJob = Column(Integer, default = 0)
	CruID = Column(Integer, default = 0)
	CruConstructPoint = Column(SmallInteger, default = 0)
	Popularity = Column(Integer, default = 0)
	HP = Column(Integer, default = 0)
	MP = Column(Integer, default = 0)
	SP = Column(Integer, default = 0)
	EK = Column(Integer, default = 0)
	PK = Column(Integer, default = 0)
	RewardGold = Column(Integer, default = 0)
	DownSkillID = Column(Integer, default = -1)
	Hunger = Column(SmallInteger, default = 100)
	LeftSAC = Column(Integer, default = 0)
	LeftShutupTime = Column(Integer, default = 0)
	LeftPopTime = Column(Integer, default = 0)
	LeftForceRecallTime = Column(Integer, default = 0)
	LeftFirmStaminarTime = Column(Integer, default = 0)
	LeftDeadPenaltyTime = Column(Integer, default = 0)
	MagicMastery = Column(String(100), default = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
	PartyID = Column(Integer, default = 0)
	GizonItemUpgradeLeft = Column(Integer, default = 0)

	Account = relationship(Account, backref = backref("CharList", order_by = Level))
	def __init__(self, CharName, Gender, SkinColor,
				 HairStyle, HairColor, UnderColor, Str, Dex, Int, Mag, Vit, Chr):
		self.CharName = CharName
		self.Gender = int(Gender)
		self.Skin = int(SkinColor)
		self.HairStyle = int(HairStyle)
		self.HairColor = int(HairColor)
		self.Underwear = int(UnderColor)
		self.Strength = Str
		self.Dexterity = Dex
		self.Intelligence = Int
		self.Magic = Mag
		self.Vitality = Vit
		self.Charisma = Chr
		
	def __repr__(self):
		return "<Character(CharName = '%s', Level = '%d')>" % (self.CharName, self.Level)

class DatabaseDriver:
	def Initialize(self, URL):
		self.engine = None
		self.Session = None
		try:
			self.engine = create_engine(URL, echo = False)
			Base.metadata.create_all(self.engine)
		except ArgumentError:
			return False
		self.Session = sessionmaker(bind = self.engine)
		return True
	
	def session(self):
		return self.Session()
	
	def CreateNewCharacter(self, Packet):
		"""
			Create new character given Packet
			Packet:
				MsgType
				PlayerName
				AccountName
				AccountPassword
				WS
				Gender
				SkinCol
				HairStyle
				HairCol
				UnderCol
				Str
				Vit
				Dex
				Int
				Mag
				Agi
		"""
		session = self.Session()
		try:
			acc = session.query(Account).\
					filter(and_(Account.Name == Packet.AccountName, Account.Password == Packet.AccountPassword)).\
					one()
		except NoResultFound:
			return False
		
		if len(acc.CharList) >= 4:
			return False
		
		new_char = Character(Packet.PlayerName, Packet.Gender, Packet.SkinCol, Packet.HairStyle, Packet.HairCol, Packet.UnderCol,
							 Packet.Str, Packet.Dex, Packet.Int, Packet.Mag, Packet.Vit, Packet.Chr)
		
		acc.CharList += [new_char]
		try:
			session.commit()
			return True
		except:
			session.rollback()
			return False