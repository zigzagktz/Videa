# Star_Char
Below are the instruction to build docker image and to run the container.

git clone https://github.com/zigzagktz/Videa.git

cd ./Videa

sudo docker build -t 'videa' .

sudo docker run -p 8080:8080 videa

go to localhost:8080, localhost:8080/films, localhost:8080/characters 

possible issues 
    - if you are runnning docker on windows, then I would recommend running this docker on Linux system. 
    - you do not have docker installed. If yes, please install docker
    - your port 8080 is already in use. If that is the case, do this --> sudo docker run -p 80:8080 videa and go to localhost:80
    - make sure you are making a http request and not https request

