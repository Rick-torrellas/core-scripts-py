@echo off
set carpeta=Peliculas
echo Bienvenidos al buscador de pelis, para que no existan repetidas y esas goeboah.
if exist %carpeta% (cd %carpeta%) else (echo No existe donde buscar, osea no existe la carpeta %carpeta% ale)
:inicio
set /p Peli=Que Pelicula Quieres busca ale?
for %%G in ("%Peli%*") do set "peli=%%G"
if exist "%peli%" (echo Existe %peli% & echo Abriendo imagen... & timeout /T 2 & start "" "%peli%") else (echo No exista la pelicula %peli%)
call :inicio
