# Star Wars API
### Algorithm
### API
### JavaScript

__The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, APIinteraction, and asynchronous programming in JavaScript.__

## Mock Technical Interview
## Requirements

- Allowed editors:
	- vi
	- vim
	- emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant.
- Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

## More Info

- Install Node 10
*$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -$ sudo apt-get install -y nodejs*
- Install semi-standard
*$ sudo npm install semistandard --global*
- Install request module and use it
*$ sudo npm install request --global$ export NODE_PATH=/usr/lib/node_modules*

## Tasks

0. Star Wars Characters

	- Write a script that prints all characters of a Star Wars movie:
	- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
	- Display one character name per line in the same order as the “characters” list in the /films/ endpoint
	- You must use the Star wars API
