@echo off
title Subir Proyecto a GitHub - Fabrica Visual
color 0A
echo =======================================================
echo     SUBIR PROYECTO A GITHUB - FABRICA VISUAL
echo =======================================================
echo.
echo Para continuar, primero debes crear un repositorio vacio 
echo en tu cuenta de GitHub (en https://github.com/new).
echo.
set /p username="Introduce tu usuario de GitHub: "
set /p repo="Introduce el nombre de tu repositorio (ej. fabrica-visual): "
echo.
echo Vinculando con el repositorio remoto...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/%username%/%repo%.git
git branch -M main
echo.
echo Subiendo los archivos a GitHub...
git push -u origin main
echo.
echo =======================================================
echo     PROCESO COMPLETADO!
echo =======================================================
pause
