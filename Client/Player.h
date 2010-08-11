//
// Player definition file. Initializes currentPlayer as main character. Can and should
// be used for displaying other player characters on screen
//

#ifndef PLAYER_H
#define PLAYER_H

#include "SpriteID.h"
#include "Timer.h"
#include "SpriteBank.h"

class Player
{
    public:
        Player();
        void draw(SDL_Surface* dest, int x, int y);

        enum Sex
        {
            MALE, FEMALE
        };
        enum Race
        {
            ASIAN, BLACK, WHITE
        };

        Sex sex();
        void setSex(Sex s);
        Race race();
        void setRace(Race r);
        int orientation();
        void setOrientation(int o);
        int action();
        void setAction(int a);


        int hauberk;

    private:
        Sex _sex;
        Race _race;
        int _orientation;
        int _action; // running, standing, etc

        unsigned int player_sprite_id;
        unsigned int player_animation_id;

        void resetTimerAndFrames();
        Timer playerTimer;
        int currentFrame;
        int framesCount;
};

#endif // PLAYER_H