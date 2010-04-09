#include "Game.h"

Game::Game()
{
	Running = true;

	ChangeScene(new LoadingScene);

	Sprites.assign(DEF_MAXSPRITES, Sprite::Sprite());
}

int Game::OnExecute()
{
	if (!OnInitialize())
	{
		return -1;
	}

	SDL_Event EventHandle;

	while (Running)
	{
		while (SDL_PollEvent(&EventHandle))
		{
			OnEvent(&EventHandle);

			MouseCursor.OnEvent(&EventHandle);

			CurrentScene->OnEvent(&EventHandle);
		}

		OnLoop();

		OnDraw();

		MainWindow.Update();
	}

	OnCleanup();

	return 0;
}

bool Game::OnInitialize()
{

#ifndef __unix__
	WSADATA wsdat;
	memset(&wsdat, 0, sizeof(wsdat));
	if (WSAStartup(0x0101, &wsdat))
	{
		fprintf(stderr, "WSAStartup() failed.\n");
		return false;
	}
#endif

#ifdef DEF_FULLSCREEN
	MainWindow.Create("HelGame", 640, 480, 32, SDL_FULLSCREEN | SDL_HWSURFACE | SDL_DOUBLEBUF);
#else
	MainWindow.Create("HelGame", 640, 480, 32, SDL_HWSURFACE | SDL_DOUBLEBUF);
#endif

	MainWindow.SetKeyRepeat(5, 200);
	MainWindow.ShowCursor(false);
	MainWindow.SetCursorPos(320, 240);

#ifdef DEF_FPSLIMIT
	MainWindow.SetFpsLimit(DEF_FPSLIMIT);
#endif

	Font = TTF_OpenFont("font/VeraSe.ttf", 12);

	//Load some Sprites before Loading
	Sprites[SPRID_CURSOR].LoadFromFile("interface.pak", 0);
	Surface::SetTransparent(Sprites[SPRID_CURSOR].GetSurface(), 255, 132, 66);
	
	Sprites[SPRID_SPRFONT].LoadFromFile("SPRFONTS.PAK", 0);
	Surface::SetTransparent(Sprites[SPRID_SPRFONT].GetSurface(), 255, 255, 255);
	Sprites[SPRID_SPRFONT2].LoadFromFile("SPRFONTS.PAK", 1);
	Surface::SetTransparent(Sprites[SPRID_SPRFONT2].GetSurface(), 255, 255, 255);

	Sprites[SPRID_LOADING].LoadFromFile("New-Dialog.pak", 0);

	return true;
}

void Game::OnLoop()
{
	CurrentScene->OnLoop();
}

void Game::OnDraw()
{
	CurrentScene->Draw(MainWindow.GetSurface());

	MouseCursor.Draw(MainWindow.GetSurface());
}

void Game::OnEvent(SDL_Event *EventSource)
{
	Event::OnEvent(EventSource);
}

void Game::OnKeyDown(SDLKey Sym, SDLMod Mod, Uint16 Unicode)
{
	if (Sym == SDLK_F12)
	{
		ChangeScene(new DebugScene);
	}
}

void Game::OnExit()
{
	ChangeScene(new ExitScene);
}

void Game::OnQuit()
{
	Running = false;
}

void Game::OnCleanup()
{
	TTF_CloseFont(Font);

	MainWindow.Close();
}

void Game::ChangeScene(Scene *NewScene)
{
	delete CurrentScene;

	CurrentScene = NewScene;
}