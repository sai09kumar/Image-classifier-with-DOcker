@echo off
docker load -i ai-image-gui.tar
docker run -it --rm ai-image-gui
pause
