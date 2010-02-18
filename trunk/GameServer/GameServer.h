#ifndef GAMESERVER_H
#define GAMESERVER_H

#include "GateSocket.h"
#include "Threading.h"
#include "IniFile.h"
#include "Map.h"
#include "GlobalDef.h"

class GameServer
{
	private:
		GameServer() { }
		GameServer(const GameServer &);
		GameServer& operator=(const GameServer&);
	public:
		static GameServer& getInstance()
		{
			static GameServer instance;
			return instance;
		}

		CGateConnector * m_pGateConnector;	
		string m_sServerName; // server name, it is sent to gate server
		vector<string> m_sGameServerAddr; // bind address list
		int m_iGameServerPort; // bind address port (ports?)
		string m_sGateServerAddr; // login server address
		int m_iGateServerPort; // gate server port
		vector<CMap> m_pMapList;

		void Initialize();

		bool bReadMainConfig();
		bool bRegisterMap(string sMapName);
		int iGetMapIndex(string sMapName);

};
#endif
