# Star_Char
Below are the instruction to build docker image and to run the container.

1. > git clone https://github.com/zigzagktz/Videa.git

2. > cd ./Videa

3. > sudo docker build -t 'videa' .

4. > sudo docker run -p 8080:8080 videa

5. > go to localhost:8080, localhost:8080/films, localhost:8080/characters 

possible issues 
- if you are runnning docker on windows, then I would recommend running this docker on Linux system. Becuase windows have firewall and port forwarding issues due to the docker running inside a virtual machine under the hood. 
- you do not have docker installed. If yes, please install docker
- your port 8080 is already in use. If that is the case, do this --> sudo docker run -p 80:8080 videa and go to localhost:80
- make sure you are making a http request and not https request
- make sure you are in Videa directory after git clone before you run docker build

