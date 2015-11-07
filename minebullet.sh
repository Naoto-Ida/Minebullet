#!/bin/bash

if [ -s .players ]; then
    lsof -iTCP:25565 -sTCP:ESTABLISHED > .players
else
    lsof -iTCP:25565 -sTCP:ESTABLISHED > .players && /usr/bin/python ~/minebullet/minebullet.py
fi
