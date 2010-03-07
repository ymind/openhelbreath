#include "App.h"

CGameState GameState;

CApp::CApp()
{
    Surf_Display = NULL;

    ScreenWidth = 640;
    ScreenHeight = 480;
    ScreenDepth = 32;
    ScreenFlags = SDL_HWSURFACE | SDL_DOUBLEBUF /*| SDL_FULLSCREEN*/;

    Running = true;

    GameState.ChangeGameState(OnLoad);

    AppName = "HelGame";

    FRAMES_PER_SECOND = 30;

    cap = false;

    frame = 0;
}

int CApp::OnExecute()
{
    if(OnInit() == false)
    {
        OnCleanup();
        return -1;
    }

    SDL_Event Event;

    fpsCounter.start();

    while(Running)
    {
        fps.start();
        while(SDL_PollEvent(&Event))
        {
            OnEvent(&Event);
            Mouse.OnEvent(&Event);

            switch(GameState.getGameStatus())
            {
            case OnMenu:
                MenuScene.OnEvent(&Event);
                break;
            case OnSelectServer:
            case OnLogin:
                LoginScene.OnEvent(&Event);
                break;
            case OnConnecting:
//                MessageBox.OnEvent(&Event);
                break;
            }
        }

        OnLoop();
        OnRender();
    }

    OnCleanup();

    return 0;
}

bool CApp::OnInit()
{
    if(SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO|SDL_INIT_TIMER) < 0)
    {
        printf("Unable to init SDL\n");
        return false;
    }

    if((Surf_Display = SDL_SetVideoMode(ScreenWidth, ScreenHeight, ScreenDepth, ScreenFlags)) == NULL)
    {
        printf("Unable to set video mode\n");
        return false;
    }

    if(Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 4096) < 0)
    {
        printf("Unable to init audio\n");
        return false;
    }

    if(!Font.OnLoad("fonts/Times_New_Roman.ttf", 14))
    {
        return false;
    }

    SDL_EnableKeyRepeat(100, 50);
    SDL_ShowCursor(0);
    SDL_WarpMouse(320, 240);

    if(!Mouse.OnLoad("sprites/interface.pak"))
    {
        return false;
    }

    if(!LoadScene.OnLoad())
    {
        return false;
    }

    SDL_WM_SetCaption(AppName.c_str(), NULL);

    return true;
}

void CApp::OnLoop()
{
    switch(GameState.getGameStatus())
    {
    case OnLoad:
        switch(LoadScene.procent)
        {
        case 0:
            if(!ExitScene.OnLoad())
            {
                GameState.ChangeGameState(OnQuit);
            }
            if(!MenuScene.OnLoad())
            {
                GameState.ChangeGameState(OnQuit);
            }
            if(!LoginScene.OnLoad())
            {
                GameState.ChangeGameState(OnQuit);
            }

            /*          if(!MessageBox.OnLoad("sprites/GameDialog.pak", 3))
                        {
                            GameState.ChangeGameState(OnQuit);
                        }

                        CSurface::Transparent(MessageBox.Surf_Dialog, 0, 123, 255);*/

            if((CSound::SoundControl.OnLoad("sounds/E14.WAV")) == -1)
            {
                GameState.ChangeGameState(OnQuit);
            }
            break;
        }
        LoadScene.OnLoop();
        break;
    case OnQuit:
        ExitScene.OnLoop();
        if(!quitTimer.is_started())
        {
            quitTimer.start();
        }
        if(quitTimer.get_ticks() > 2000)
        {
            OnExit();
        }
        break;
    }
}

void CApp::OnRender()
{
    switch(GameState.getGameStatus())
    {
    case OnLoad:
        LoadScene.OnRender(Surf_Display);
        break;
    case OnMenu:
        MenuScene.OnRender(Surf_Display);
        break;
    case OnSelectServer:
    case OnLogin:
        LoginScene.OnRender(Surf_Display);
        //Surf_Test = Font.OnRender(TestString.c_str());
        //CSurface::OnDraw(Surf_Display, Surf_Test, 175, 161);
        //SDL_FreeSurface(Surf_Test);
        break;
    case OnConnecting:
//        MessageBox.OnRender(Surf_Display);
        break;
    case OnQuit:
        ExitScene.OnRender(Surf_Display);
        break;
    }
    Mouse.OnRender(Surf_Display);

    SDL_Flip(Surf_Display);

    frame++;

    if(fpsCounter.get_ticks() > 1000)
    {
        printf("fps: %i\n", frame);

        fpsCounter.start();
        frame = 0;
    }

    if ((cap == true) && (fps.get_ticks() < 1000 / FRAMES_PER_SECOND))
    {
        SDL_Delay((1000 / FRAMES_PER_SECOND) - fps.get_ticks());
    }
}

void CApp::OnCleanup()
{
    SDL_FreeSurface(Surf_Display);

//    MessageBox.OnCleanup();
    Mouse.OnCleanup();

    Font.OnCleanup();

    CSound::SoundControl.OnCleanup();

    Mix_CloseAudio();

    SDL_Quit();
}