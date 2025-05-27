::
:: Start/Stop Mysql Server Docker
::
@echo OFF
set OPTION=%1
if %OPTION%. == start. (
    docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=Hitema2025 -p3306:3306 -vvolume_mysql:/var/lib/mysql mysql:8.4.4
) else if %OPTION%. == stop. (
     docker stop mysql 
) else (
    echo.
    echo Entrez la commande dkmysql [start^|stop]
    echo.
)

