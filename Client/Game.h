//
// Main window initialization and game loop
//

#ifndef GAME_H
#define GAME_H

#include "Logger.h"
#include "Socket.h"
#include "NetMessages.h"
#include "GlobalDef.h"

#include "Window.h"
#include "Mouse.h"
#include "SpriteBank.h"
#include "SoundBank.h"
#include "Font.h"
#include "Map.h"

#include "Player.h"
#include "PlayGroundScene.h"
#include "LoadingScene.h"
#include "MenuScene.h"
#include "ExitScene.h"
#include "SignupScene.h"
#include "SelectServerScene.h"
#include "LoginScene.h"
#include "VersionNotMatchScene.h"
#include "SelectCharScene.h"
#include "CreateNewCharScene.h"

class Game: public Event
{
	public:
		static Game& getInstance()
		{
			static Game instance;
			return instance;
		}

		int onExecute();
		bool onInitialize();
		void onLoop();
		void onDraw();
		void onEvent(SDL_Event* eventSource);
		void onKeyDown(SDLKey sym, SDLMod mod, Uint16 unicode);
		void onExit();
		void onQuit();
		void onCleanup();
		void changeScene(Scene* newScene);
		void drawFPS(SDL_Surface* dest);
		static void drawVersion(SDL_Surface* dest);

		Mouse mouseCursor;

		std::string login;
		std::string password;

	private:
		Game();
		Game(const Game &);
		Game& operator =(const Game&);
        bool initializeFonts();

		Window mainWindow;
		Scene* currentScene;
		Scene* previousScene;
		bool running;
};

#endif // GAME_H
