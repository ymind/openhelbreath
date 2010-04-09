#ifndef MESSAGEBOX_H
#define MESSAGEBOX_H

#include "Widget.h"
#include "Font.h"
#include "Timer.h"

class ConnectingWidget: public Widget
{
	public:

		ConnectingWidget();
		~ConnectingWidget();

		void Draw(SDL_Surface *Dest);

		void OnKeyDown(SDLKey Sym, SDLMod Mod, Uint16 Unicode);

		void SetEnabled(bool Enable);
		inline bool IsEnabled() const;
		int GetState() const;
		void SetState(int State);

	private:
		Timer MessageTimer;
		bool Enabled;
		int State;
};

#endif // MESSAGEBOX_H