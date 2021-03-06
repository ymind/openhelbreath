# missing messages
# 0x0BE5, 0x0BE6, 0x0BE7, 0x0BE8, 0x0BEA
DEF_NOTIFY_SPAWNEVENT = 0x0BAA
DEF_NOTIFY_QUESTCOUNTER = 0x0BE2
DEF_NOTIFY_HELDENIANSTART = 0x0BEA
DEF_NOTIFY_HELDENIANCOUNT = 0x0BEC
DEF_NOTIFY_HELDENIANEND = 0x0BE7

DEF_MSGTYPE_CONFIRM = 0x0F14
DEF_MSGTYPE_REJECT = 0x0F15

MSGID_REQUEST_INITPLAYER = 0x05040205
MSGID_RESPONSE_INITPLAYER = 0x05040206

MSGID_REQUEST_INITDATA = 0x05080404
MSGID_RESPONSE_INITDATA = 0x05080405

MSGID_COMMAND_MOTION = 0x0FA314D5
MSGID_RESPONSE_MOTION = 0x0FA314D6
MSGID_EVENT_MOTION = 0x0FA314D7
MSGID_EVENT_LOG = 0x0FA314D8
MSGID_EVENT_COMMON = 0x0FA314DB
MSGID_COMMAND_COMMON = 0x0FA314DC

DEF_COMMONTYPE_ITEMDROP = 0x0A01
DEF_COMMONTYPE_EQUIPITEM = 0x0A02
DEF_COMMONTYPE_REQ_LISTCONTENTS = 0x0A03
DEF_COMMONTYPE_REQ_PURCHASEITEM = 0x0A04
DEF_COMMONTYPE_GIVEITEMTOCHAR = 0x0A05
DEF_COMMONTYPE_JOINGUILDAPPROVE = 0x0A06
DEF_COMMONTYPE_JOINGUILDREJECT = 0x0A07
DEF_COMMONTYPE_DISMISSGUILDAPPROVE = 0x0A08
DEF_COMMONTYPE_DISMISSGUILDREJECT = 0x0A09
DEF_COMMONTYPE_RELEASEITEM = 0x0A0A
DEF_COMMONTYPE_TOGGLECOMBATMODE = 0x0A0B
DEF_COMMONTYPE_SETITEM = 0x0A0C
DEF_COMMONTYPE_MAGIC = 0x0A0D
DEF_COMMONTYPE_REQ_STUDYMAGIC = 0x0A0E
DEF_COMMONTYPE_REQ_TRAINSKILL = 0x0A0F
DEF_COMMONTYPE_REQ_GETREWARDMONEY = 0x0A10
DEF_COMMONTYPE_REQ_USEITEM = 0x0A11
DEF_COMMONTYPE_REQ_USESKILL = 0x0A12
DEF_COMMONTYPE_REQ_SELLITEM = 0x0A13
DEF_COMMONTYPE_REQ_REPAIRITEM = 0x0A14
DEF_COMMONTYPE_REQ_SELLITEMCONFIRM = 0x0A15
DEF_COMMONTYPE_REQ_REPAIRITEMCONFIRM = 0x0A16
DEF_COMMONTYPE_REQ_GETFISHTHISTIME = 0x0A17
DEF_COMMONTYPE_TOGGLESAFEATTACKMODE = 0x0A18
DEF_COMMONTYPE_REQ_CREATEPORTION = 0x0A19
DEF_COMMONTYPE_TALKTONPC = 0x0A1A
DEF_COMMONTYPE_REQ_SETDOWNSKILLINDEX = 0x0A1B
DEF_COMMONTYPE_REQ_GETOCCUPYFLAG = 0x0A1C
DEF_COMMONTYPE_REQ_GETHEROMANTLE = 0x0A1D
DEF_COMMONTYPE_EXCHANGEITEMTOCHAR = 0x0A1E
DEF_COMMONTYPE_SETEXCHANGEITEM = 0x0A1F
DEF_COMMONTYPE_CONFIRMEXCHANGEITEM = 0x0A20
DEF_COMMONTYPE_CANCELEXCHANGEITEM = 0x0A21
DEF_COMMONTYPE_QUESTACCEPTED = 0x0A22
DEF_COMMONTYPE_BUILDITEM = 0x0A23
DEF_COMMONTYPE_GETMAGICABILITY = 0x0A24

DEF_COMMONTYPE_REQ_GETOCCUPYFIGHTZONETICKET = 0x0A25
DEF_COMMONTYPE_BANGUILD = 0x0A26

DEF_COMMONTYPE_REQUEST_ACCEPTJOINPARTY = 0x0A30
DEF_COMMONTYPE_REQUEST_JOINPARTY = 0x0A31
DEF_COMMONTYPE_RESPONSE_JOINPARTY = 0x0A32
DEF_COMMONTYPE_REQUEST_ACTIVATESPECABLTY = 0x0A40
DEF_COMMONTYPE_REQUEST_CANCELQUEST = 0x0A50
DEF_COMMONTYPE_REQUEST_SELECTCRUSADEDUTY = 0x0A51
DEF_COMMONTYPE_REQUEST_MAPSTATUS = 0x0A52
DEF_COMMONTYPE_REQUEST_HELP = 0x0A53

DEF_COMMONTYPE_SETGUILDTELEPORTLOC = 0x0A54
DEF_COMMONTYPE_GUILDTELEPORT = 0x0A55
DEF_COMMONTYPE_SUMMONWARUNIT = 0x0A56
DEF_COMMONTYPE_SETGUILDCONSTRUCTLOC = 0x0A57

MSGID_NOTIFY = 0x0FA314D0

DEF_NOTIFY_ITEMOBTAINED = 0x0B01
DEF_NOTIFY_QUERY_JOINGUILDREQPERMISSION = 0x0B02
DEF_NOTIFY_QUERY_DISMISSGUILDREQPERMISSION = 0x0B03
DEF_NOTIFY_WAITFORGUILDOPERATION = 0x0B04
DEF_NOTIFY_CANNOTCARRYMOREITEM = 0x0B05
DEF_NOTIFY_ITEMPURCHASED = 0x0B06
DEF_NOTIFY_HP = 0x0B07
DEF_NOTIFY_NOTENOUGHGOLD = 0x0B08
DEF_NOTIFY_KILLED = 0x0B09
DEF_NOTIFY_EXP = 0x0B0A
DEF_NOTIFY_GUILDDISBANDED = 0x0B0B
DEF_NOTIFY_EVENTMSGSTRING = 0x0B0C
DEF_NOTIFY_CANNOTJOINMOREGUILDSMAN = 0x0B0D
DEF_NOTIFY_NEWGUILDSMAN = 0x0B0E
DEF_NOTIFY_DISMISSGUILDSMAN = 0x0B0F
DEF_NOTIFY_MAGICSTUDYSUCCESS = 0x0B10
DEF_NOTIFY_MAGICSTUDYFAIL = 0x0B11
DEF_NOTIFY_SKILLTRAINSUCCESS = 0x0B12
DEF_NOTIFY_SKILLTRAINFAIL = 0x0B13
DEF_NOTIFY_MP = 0x0B14
DEF_NOTIFY_SP = 0x0B15
DEF_NOTIFY_LEVELUP = 0x0B16
DEF_NOTIFY_ITEMLIFESPANEND = 0x0B17
DEF_NOTIFY_LIMITEDLEVEL = 0x0B18
DEF_NOTIFY_ITEMTOBANK = 0x0B19
DEF_NOTIFY_PKPENALTY = 0x0B1A
DEF_NOTIFY_PKCAPTURED = 0x0B1B
DEF_NOTIFY_ENEMYKILLREWARD = 0x0B1C
DEF_NOTIFY_GIVEITEMFIN_ERASEITEM = 0x0B1D
DEF_NOTIFY_DROPITEMFIN_ERASEITEM = 0x0B1F
DEF_NOTIFY_ITEMDEPLETED_ERASEITEM = 0x0B20
DEF_NOTIFY_NEWDYNAMICOBJECT = 0x0B21
DEF_NOTIFY_DELDYNAMICOBJECT = 0x0B22
DEF_NOTIFY_SKILL = 0x0B23
DEF_NOTIFY_SERVERCHANGE = 0x0B24
DEF_NOTIFY_SETITEMCOUNT = 0x0B25
DEF_NOTIFY_CANNOTITEMTOBANK = 0x0B26
DEF_NOTIFY_MAGICEFFECTON = 0x0B27
DEF_NOTIFY_MAGICEFFECTOFF = 0x0B28
DEF_NOTIFY_TOTALUSERS = 0x0B29
DEF_NOTIFY_SKILLUSINGEND = 0x0B2A
DEF_NOTIFY_SHOWMAP = 0x0B2B
DEF_NOTIFY_CANNOTSELLITEM = 0x0B2C
DEF_NOTIFY_SELLITEMPRICE = 0x0B2D
DEF_NOTIFY_CANNOTREPAIRITEM = 0x0B2E
DEF_NOTIFY_REPAIRITEMPRICE = 0x0B2F
DEF_NOTIFY_ITEMREPAIRED = 0x0B30
DEF_NOTIFY_ITEMSOLD = 0x0B31
DEF_NOTIFY_PLAYERONGAME = 0x0B33
DEF_NOTIFY_PLAYERNOTONGAME = 0x0B34
DEF_NOTIFY_WHISPERMODEON = 0x0B35
DEF_NOTIFY_WHISPERMODEOFF = 0x0B36
DEF_NOTIFY_PLAYERPROFILE = 0x0B37
DEF_NOTIFY_TRAVELERLIMITEDLEVEL = 0x0B38
DEF_NOTIFY_HUNGER = 0x0B39

DEF_NOTIFY_TOBERECALLED = 0x0B40
DEF_NOTIFY_TIMECHANGE = 0x0B41
DEF_NOTIFY_PLAYERSHUTUP = 0x0B42
DEF_NOTIFY_ADMINUSERLEVELLOW = 0x0B43
DEF_NOTIFY_CANNOTRATING = 0x0B44
DEF_NOTIFY_RATINGPLAYER = 0x0B45
DEF_NOTIFY_NOTICEMSG = 0x0B46
DEF_NOTIFY_EVENTFISHMODE = 0x0B47
DEF_NOTIFY_FISHCHANCE = 0x0B48
DEF_NOTIFY_DEBUGMSG = 0x0B49
DEF_NOTIFY_FISHSUCCESS = 0x0B4A
DEF_NOTIFY_FISHFAIL = 0x0B4B
DEF_NOTIFY_FISHCANCELED = 0x0B4C
DEF_NOTIFY_WHETHERCHANGE = 0x0B4D
DEF_NOTIFY_SERVERSHUTDOWN = 0x0B4E
DEF_NOTIFY_REWARDGOLD = 0x0B4F
DEF_NOTIFY_IPACCOUNTINFO = 0x0B50
DEF_NOTIFY_SAFEATTACKMODE = 0x0B51
DEF_NOTIFY_SUPERATTACKLEFT = 0x0B52
DEF_NOTIFY_NOMATCHINGPORTION = 0x0B53
DEF_NOTIFY_LOWPORTIONSKILL = 0x0B54
DEF_NOTIFY_PORTIONFAIL = 0x0B55
DEF_NOTIFY_PORTIONSUCCESS = 0x0B56
DEF_NOTIFY_NPCTALK = 0x0B57
DEF_NOTIFY_ADMINIFO = 0x0B58
DEF_NOTIFY_DOWNSKILLINDEXSET = 0x0B59
DEF_NOTIFY_ENEMYKILLS = 0x0B5A
DEF_NOTIFY_ITEMPOSLIST = 0x0B5B
DEF_NOTIFY_ITEMRELEASED = 0x0B5C
DEF_NOTIFY_NOTFLAGSPOT = 0x0B5D
DEF_NOTIFY_OPENEXCHANGEWINDOW = 0x0B5E
DEF_NOTIFY_SETEXCHANGEITEM = 0x0B5F
DEF_NOTIFY_CANCELEXCHANGEITEM = 0x0B60
DEF_NOTIFY_EXCHANGEITEMCOMPLETE = 0x0B61
DEF_NOTIFY_CANNOTGIVEITEM = 0x0B62
DEF_NOTIFY_GIVEITEMFIN_COUNTCHANGED = 0x0B63
DEF_NOTIFY_DROPITEMFIN_COUNTCHANGED = 0x0B64
DEF_NOTIFY_ITEMCOLORCHANGE = 0x0B65
DEF_NOTIFY_QUESTCONTENTS = 0x0B66
DEF_NOTIFY_QUESTABORTED = 0x0B67
DEF_NOTIFY_QUESTCOMPLETED = 0x0B68
DEF_NOTIFY_QUESTREWARD = 0x0B69

DEF_NOTIFY_BUILDITEMSUCCESS = 0x0B70
DEF_NOTIFY_BUILDITEMFAIL = 0x0B71
DEF_NOTIFY_OBSERVERMODE = 0x0B72
DEF_NOTIFY_GLOBALATTACKMODE = 0x0B73
DEF_NOTIFY_DAMAGEMOVE = 0x0B74
DEF_NOTIFY_FORCEDISCONN = 0x0B75
DEF_NOTIFY_FIGHTZONERESERVE = 0x0B76
DEF_NOTIFY_NOGUILDMASTERLEVEL = 0x0B77
DEF_NOTIFY_SUCCESSBANGUILDMAN = 0x0B78
DEF_NOTIFY_CANNOTBANGUILDMAN = 0x0B79

DEF_NOTIFY_RESPONSE_CREATENEWPARTY = 0x0B80
DEF_NOTIFY_QUERY_JOINPARTY = 0x0B81

# DEF_NOTIFY_SUCCESSBANGUILDMAN 0x0B82

DEF_NOTIFY_ENERGYSPHERECREATED = 0x0B90
DEF_NOTIFY_ENERGYSPHEREGOALIN = 0x0B91
DEF_NOTIFY_SPECIALABILITYENABLED = 0x0B92
DEF_NOTIFY_SPECIALABILITYSTATUS = 0x0B93
DEF_NOTIFY_CRUSADE = 0x0B94
DEF_NOTIFY_LOCKEDMAP = 0x0B95
DEF_NOTIFY_DUTYSELECTED = 0x0B96
DEF_NOTIFY_MAPSTATUSNEXT = 0x0B97
DEF_NOTIFY_MAPSTATUSLAST = 0x0B98
DEF_NOTIFY_HELP = 0x0B99
DEF_NOTIFY_HELPFAILED = 0x0B9A
DEF_NOTIFY_METEORSTRIKECOMING = 0x0B9B
DEF_NOTIFY_METEORSTRIKEHIT = 0x0B9C
DEF_NOTIFY_GRANDMAGICRESULT = 0x0B9D
DEF_NOTIFY_NOMORECRUSADESTRUCTURE = 0x0B9E
DEF_NOTIFY_CONSTRUCTIONPOINT = 0x0B9F

DEF_NOTIFY_TCLOC = 0x0BA0
DEF_NOTIFY_CANNOTCONSTRUCT = 0x0BA1
DEF_NOTIFY_PARTY = 0x0BA2
DEF_NOTIFY_ITEMATTRIBUTECHANGE = 0x0BA3
DEF_NOTIFY_GIZONITEMUPGRADELEFT = 0x0BA4
DEF_NOTIFY_GIZONITEMCANGE = 0x0BA5
DEF_NOTIFY_REQGUILDNAMEANSWER = 0x0BA6
DEF_NOTIFY_FORCERECALLTIME = 0x0BA7
DEF_NOTIFY_ITEMUPGRADEFAIL = 0x0BA8

DEF_NOTIFY_NOMOREAGRICULTURE = 0x0BB0
DEF_NOTIFY_AGRICULTURESKILLLIMIT = 0x0BB1
DEF_NOTIFY_AGRICULTURENOAREA = 0x0BB2
DEF_NOTIFY_SETTING_SUCCESS = 0x0BB3
DEF_NOTIFY_SETTING_FAILED = 0x0BB4
DEF_NOTIFY_STATECHANGE_SUCCESS = 0x0BB5
DEF_NOTIFY_STATECHANGE_FAILED = 0x0BB6

DEF_NOTIFY_SLATE_CREATESUCCESS = 0x0BC1
DEF_NOTIFY_SLATE_CREATEFAIL = 0x0BC2

DEF_NOTIFY_NORECALL = 0x0BD1
DEF_NOTIFY_APOCGATESTARTMSG = 0x0BD2
DEF_NOTIFY_APOCGATEENDMSG = 0x0BD3
DEF_NOTIFY_APOCGATEOPEN = 0x0BD4
DEF_NOTIFY_APOCGATECLOSE = 0x0BD5
DEF_NOTIFY_ABADDONKILLED = 0x0BD6
DEF_NOTIFY_APOCFORCERECALLPLAYERS = 0x0BD7
DEF_NOTIFY_SLATE_INVINCIBLE = 0x0BD8
DEF_NOTIFY_SLATE_MANA = 0x0BD9

DEF_NOTIFY_SLATE_EXP = 0x0BE0
DEF_NOTIFY_SLATE_STATUS = 0x0BE1
DEF_NOTIFY_MONSTERCOUNT = 0x0BE3
DEF_NOTIFY_RESURRECTPLAYER = 0x0BE9
DEF_NOTIFY_HELDENIANTELEPORT = 0x0BE6
DEF_NOTIFY_0BE8 = 0x0BE8

MSGID_ADMINSETTINGSCONFIGURATIONCONTENTS = 0x0FA314D3
MSGID_SETTINGSCONFIGURATIONCONTENTS = 0x0FA314D4
MSGID_ITEMCONFIGURATIONCONTENTS = 0x0FA314D9
MSGID_NPCCONFIGURATIONCONTENTS = 0x0FA314DA
MSGID_MAGICCONFIGURATIONCONTENTS = 0x0FA314DB
MSGID_SKILLCONFIGURATIONCONTENTS = 0x0FA314DC
MSGID_PLAYERITEMLISTCONTENTS = 0x0FA314DD
MSGID_PORTIONCONFIGURATIONCONTENTS = 0x0FA314DE
MSGID_PLAYERCHARACTERCONTENTS = 0x0FA40000
MSGID_QUESTCONFIGURATIONCONTENTS = 0x0FA40001
MSGID_BUILDITEMCONFIGURATIONCONTENTS = 0x0FA40002
MSGID_DUPITEMIDFILECONTENTS = 0x0FA40003
MSGID_NOTICEMENTFILECONTENTS = 0x0FA40004
MSGID_UPDATECONFIGFILES = 0x0FA40005
MSGID_NPCITEMCONFIGCONTENTS = 0x0FA40006

# WLServer 0x0FA40007
# Teleport 0x0FA40008
# ApocalypeSchedule 0x0FA40009
# HeldinianSchedule 0x0FA40010

MSGID_COMMAND_CHECKCONNECTION = 0x03203203
MSGID_COMMAND_CHATMSG = 0x03203204

MSGID_REQUEST_REGISTERGAMESERVER = 0x0512A3F4
MSGID_RESPONSE_REGISTERGAMESERVER = 0x0512A3F5
MSGID_REQUEST_REGISTERDBSERVER = 0x0512A3F6
MSGID_RESPONSE_REGISTERDBSERVER = 0x0512A3F7
MSGID_REQUEST_REGISTERGAMESERVERSOCKET = 0x0512A3F8
MSGID_RESPONSE_REGISTERGAMESERVERSOCKET = 0x0512A3F9

MSGID_REQUEST_LOGIN = 0x0FC94201
MSGID_REQUEST_CREATENEWACCOUNT = 0x0FC94202
MSGID_RESPONSE_LOG = 0x0FC94203
MSGID_REQUEST_CREATENEWCHARACTER = 0x0FC94204
MSGID_REQUEST_ENTERGAME = 0x0FC94205
MSGID_RESPONSE_ENTERGAME = 0x0FC94206
MSGID_REQUEST_DELETECHARACTER = 0x0FC94207
MSGID_REQUEST_CREATENEWGUILD = 0x0FC94208
MSGID_RESPONSE_CREATENEWGUILD = 0x0FC94209
MSGID_REQUEST_DISBANDGUILD = 0x0FC9420A
MSGID_RESPONSE_DISBANDGUILD = 0x0FC9420B
MSGID_REQUEST_HELDENIAN_WINNER = 0x3D001240

MSGID_REQUEST_UPDATEGUILDINFO_NEWGUILDSMAN = 0x0FC9420C
MSGID_REQUEST_UPDATEGUILDINFO_DELGUILDSMAN = 0x0FC9420D

MSGID_REQUEST_CIVILRIGHT = 0x0FC9420E
MSGID_RESPONSE_CIVILRIGHT = 0x0FC9420F

MSGID_REQUEST_CHANGEPASSWORD = 0x0FC94210
MSGID_RESPONSE_CHANGEPASSWORD = 0x0FC94211

DEF_LOGRESMSGTYPE_CONFIRM = 0x0F14
DEF_LOGRESMSGTYPE_REJECT = 0x0F15
DEF_LOGRESMSGTYPE_PASSWORDMISMATCH = 0x0F16
DEF_LOGRESMSGTYPE_NOTEXISTINGACCOUNT = 0x0F17
DEF_LOGRESMSGTYPE_NEWACCOUNTCREATED = 0x0F18
DEF_LOGRESMSGTYPE_NEWACCOUNTFAILED = 0x0F19
DEF_LOGRESMSGTYPE_ALREADYEXISTINGACCOUNT = 0x0F1A
DEF_LOGRESMSGTYPE_NOTEXISTINGCHARACTER = 0x0F1B
DEF_LOGRESMSGTYPE_NEWCHARACTERCREATED = 0x0F1C
DEF_LOGRESMSGTYPE_NEWCHARACTERFAILED = 0x0F1D
DEF_LOGRESMSGTYPE_ALREADYEXISTINGCHARACTER = 0x0F1E
DEF_LOGRESMSGTYPE_CHARACTERDELETED = 0x0F1F
DEF_LOGRESMSGTYPE_PASSWORDCHANGESUCCESS = 0x0A00
DEF_LOGRESMSGTYPE_PASSWORDCHANGEFAIL = 0x0A01
DEF_LOGRESMSGTYPE_NOTEXISTINGWORLDSERVER = 0x0A02

DEF_ENTERGAMEMSGTYPE_NEW = 0x0F1C
DEF_ENTERGAMEMSGTYPE_NOENTER_FORCEDISCONN = 0x0F1D
DEF_ENTERGAMEMSGTYPE_CHANGINGSERVER = 0x0F1F

DEF_ENTERGAMERESTYPE_PLAYING = 0x0F20
DEF_ENTERGAMERESTYPE_REJECT = 0x0F21
DEF_ENTERGAMERESTYPE_CONFIRM = 0x0F22
DEF_ENTERGAMERESTYPE_FORCEDISCONN = 0x0F23

DEF_REJECTTYPE_CHARABOVETRIALLEVEL = 0x01
DEF_REJECTTYPE_MAXREGISTEREDIPREACHED = 0x02
DEF_REJECTTYPE_GAMESERVERNOTONLINE = 0x03
DEF_REJECTTYPE_DATADIFFERENCE = 0x04
DEF_REJECTTYPE_MAXSERVERUSERLIMITREACHED = 0x06
DEF_REJECTTYPE_WORLDSERVERISFULL = 0x07
DEF_REJECTTYPE_LOGINERROR = 0x08

MSGID_REQUEST_PLAYERDATA = 0x0C152210
MSGID_RESPONSE_PLAYERDATA = 0x0C152211
MSGID_RESPONSE_SAVEPLAYERDATA_REPLY = 0x0C152212
MSGID_REQUEST_SAVEPLAYERDATA = 0x0DF3076F
MSGID_REQUEST_SAVEPLAYERDATA_REPLY = 0x0DF30770
MSGID_REQUEST_SAVEPLAYERDATALOGOUT = 0x0DF3074F
MSGID_REQUEST_NOSAVELOGOUT = 0x0DF30750


MSGID_REQUEST_RETRIEVEITEM = 0x0DF30751
MSGID_RESPONSE_RETRIEVEITEM = 0x0DF30752

MSGID_REQUEST_FULLOBJECTDATA = 0x0DF40000

MSGID_GUILDNOTIFY = 0x0DF30760
DEF_GUILDNOTIFY_NEWGUILDSMAN = 0x1F00

MSGID_REQUEST_TELEPORT = 0x0EA03201
MSGID_REQUEST_CITYHALLTELEPORT = 0x0EA03202
MSGID_REQUEST_HELDENIANTELEPORT = 0x0EA03206

MSGID_LEVELUPSETTINGS = 0x11A01000
MSGID_DYNAMICOBJECT = 0x12A01001

MSGID_GAMESERVERALIVE = 0x12A01002
MSGID_ADMINUSER = 0x12A01003

MSGID_GAMESERVERDOWN = 0x12A01004
MSGID_TOTALCLIENTS = 0x12A01005

MSGID_ENTERGAMECONFIRM = 0x12A01006

MSGID_REQUEST_FIGHTZONE_RESERVE = 0x12A01007
MSGID_RESPONSE_FIGHTZONE_RESERVE = 0x12A01008

DEF_MSGID_ANNOUNCEACCOUNT = 0x13000000

MSGID_ACCOUNTINFOCHANGE = 0x13000001
MSGID_IPINFOCHANGE = 0x13000002

MSGID_GAMESERVERSHUTDOWNED = 0x14000000
MSGID_ANNOUNCEACCOUNTNEWPASSWORD = 0x14000010

MSGID_REQUEST_IPIDSTATUS = 0x14E91200
MSGID_RESPONSE_IPIDSTATUS = 0x14E91201
MSGID_REQUEST_ACCOUNTCONNSTATUS = 0x14E91202
MSGID_RESPONSE_ACCOUNTCONNSTATUS = 0x14E91203
MSGID_REQUEST_CLEARACCOUNTCONNSTATUS = 0x14E91204
MSGID_RESPONSE_CLEARACCOUNTCONNSTATUS = 0x14E91205

MSGID_REQUEST_FORCEDISCONECTACCOUNT = 0x15000000
MSGID_REQUEST_NOCOUNTINGSAVELOGOUT = 0x15000001

MSGID_OCCUPYFLAGDATA = 0x167C0A30
MSGID_REQUEST_SAVEARESDENOCCUPYFLAGDATA = 0x167C0A31
MSGID_REQUEST_SAVEELVINEOCCUPYFLAGDATA = 0x167C0A32

MSGID_ARESDENOCCUPYFLAGSAVEFILECONTENTS = 0x17081034
MSGID_ELVINEOCCUPYFLAGSAVEFILECONTENTS = 0x17081035

MSGID_REQUEST_SETITEMPOS = 0x180ACE0A

MSGID_BWM_INIT = 0x19CC0F82
MSGID_BWM_COMMAND_SHUTUP = 0x19CC0F84

MSGID_SENDSERVERSHUTDOWNMSG = 0x20000000
MSGID_ITEMLOG = 0x210A914D
MSGID_GAMEMASTERLOG = 0x210A914E

MSGID_REQUEST_NOTICEMENT = 0x220B2F00
MSGID_RESPONSE_NOTICEMENT = 0x220B2F01

MSGID_REGISTER_WORLDSERVER = 0x23AA210E
MSGID_REGISTER_WORLDSERVERSOCKET = 0x23AA210F
MSGID_REGISTER_WORLDSERVER_GAMESERVER = 0x23AB211F

MSGID_REQUEST_CHARINFOLIST = 0x23AB2200
MSGID_RESPONSE_CHARINFOLIST = 0x23AB2201

MSGID_REQUEST_REMOVEGAMESERVER = 0x2400000A
MSGID_REQUEST_CLEARACCOUNTSTATUS = 0x24021EE0

MSGID_REQUEST_SETACCOUNTINITSTATUS = 0x25000198
MSGID_REQUEST_SETACCOUNTWAITSTATUS = 0x25000199

MSGID_REQUEST_CHECKACCOUNTPASSWORD = 0x2654203A
MSGID_WORLDSERVERACTIVATED = 0x27049D0C

MSGID_REQUEST_PANNING = 0x27B314D0
MSGID_RESPONSE_PANNING = 0x27B314D1

MSGID_REQUEST_RESTART = 0x28010EEE
MSGID_RESPONSE_REGISTER_WORLDSERVERSOCKET = 0x280120A0

MSGID_REQUEST_BLOCKACCOUNT = 0x2900AD10
MSGID_IPTIMECHANGE = 0x2900AD20
MSGID_ACCOUNTTIMECHANGE = 0x2900AD22
MSGID_REQUEST_IPTIME = 0x2900AD30
MSGID_RESPONSE_IPTIME = 0x2900AD31

MSGID_REQUEST_SELLITEMLIST = 0x2900AD30

MSGID_REQUEST_ALL_SERVER_REBOOT = 0x3AE8270A
MSGID_REQUEST_EXEC_1DOTBAT = 0x3AE8370A
MSGID_REQUEST_EXEC_2DOTBAT = 0x3AE8470A
MSGID_MONITORALIVE = 0x3AE8570A

MSGID_COLLECTEDMANA = 0x3AE90000
MSGID_METEORSTRIKE = 0x3AE90001

MSGID_SERVERSTOCKMSG = 0x3AE90013

GSM_REQUEST_FINDCHARACTER = 0x01
GSM_RESPONSE_FINDCHARACTER = 0x02
GSM_GRANDMAGICRESULT = 0x03
GSM_GRANDMAGICLAUNCH = 0x04
GSM_COLLECTEDMANA = 0x05
GSM_BEGINCRUSADE = 0x06
GSM_ENDCRUSADE = 0x07
GSM_MIDDLEMAPSTATUS = 0x08
GSM_SETGUILDTELEPORTLOC = 0x09
GSM_CONSTRUCTIONPOINT = 0x0A
GSM_SETGUILDCONSTRUCTLOC = 0x0B
GSM_CHATMSG = 0x0C
GSM_WHISPERMSG = 0x0D
GSM_DISCONNECT = 0x0E
GSM_REQUEST_SUMMONPLAYER = 0x0F
GSM_REQUEST_SHUTUPPLAYER = 0x10
GSM_RESPONSE_SHUTUPPLAYER = 0x11
GSM_REQUEST_SETFORCERECALLTIME = 0x12
GSM_BEGINAPOCALYPSE = 0x13
GSM_ENDAPOCALYPSE = 0x14
GSM_REQUEST_SUMMONGUILD = 0x15
GSM_REQUEST_SUMMONALL = 0x16
GSM_ENDHELDENIAN = 0x17
GSM_STARTHELDENIAN = 0x19
# 2.06
DEF_COMMONTYPE_REQ_CHANGEPLAYMODE = 0x0A60
DEF_NOTIFY_CHANGEPLAYMODE = 0x0BA9

# Party Code
MSGID_PARTYOPERATION = 0x3C00123A
DEF_PARTYSTATUS_PROCESSING = 1
DEF_PARTYSTATUS_NULL = 0
DEF_PARTYSTATUS_CONFIRM = 2

# Upgrade code
DEF_COMMONTYPE_UPGRADEITEM = 0x0A58
DEF_ITEMLOG_UPGRADESUCCESS = 30
DEF_ITEMLOG_UPGRADEFAIL = 29
DEF_COMMONTYPE_REQGUILDNAME = 0x0A59

# Log Msg
MSGID_GAMEITEMLOG = 0x210A914F

# Crusade
DEF_CRUSADELOG_ENDCRUSADE = 1
DEF_CRUSADELOG_STARTCRUSADE = 2
DEF_CRUSADELOG_SELECTDUTY = 3
DEF_CRUSADELOG_GETEXP = 4
MSGID_GAMECRUSADELOG = 0x210A914C

# NPC drops
DEF_ITEMSPREAD_RANDOM = 1
DEF_ITEMSPREAD_FIXED = 2
MAX_NPCITEMDROP = 25

# Slates
DEF_COMMONTYPE_REQ_CREATESLATE = 0x0A61
DEF_NOTIFY_SLATECLEAR = 99

# PK
DEF_PKLOG_REDUCECRIMINAL = 1
DEF_PKLOG_BYPLAYER = 2
DEF_PKLOG_BYPK = 3
DEF_PKLOG_BYENERMY = 4
DEF_PKLOG_BYNPC = 5
DEF_PKLOG_BYOTHER = 6

# Ressurection
DEF_REQUEST_RESURRECTPLAYER_NO = 0x0FC94215
DEF_REQUEST_RESURRECTPLAYER_YES = 0x0FC94214