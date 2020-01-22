#!/bin/sh

# Take a screenshot
scrot -o screen_locked.png

# Pixellate it 10x
mogrify -scale 10% -scale 1000% screen_locked.png

# Lock screen displaying this image.
i3lock -i screen_locked.png
