# Python Scripts for Holberton Projects

---

## Required things

* sudo apt-get install pip
* pip install mechanize
* pip install beautifulsoup4

**NOTE: This program only works with python2, make sure your alias is 'python2'.**
---

## Description

Automating file template creation for Holberton projects, below is the chart of files that it will automate. The program will first ask you for your header file name, skip it by leaving it blank and pressing enter. Then it will ask if you want to include holberton's putchar file. Finally, it will then create a directory with the correct project name with all the project files in it.

| C Projects  | Python Projects | Javascript |
| ------------- | ------------- | ------------- |
| C Templates | Py Templates | Coming Soon |
| Header file | C files |  Coming Soon |
| Putchar file | Header files |  Coming Soon |
| Main.c files | Coming soon |  Coming Soon |
| README.md | Coming soon |  Coming Soon |

## Instructions

**Install required things above**

**Setting User Information:** Enter in your Holberton intranet username and password as well as your Github name, username, and profile link in the [auth_data.json](./auth_data.json) file.

**Setting Alias:** Type cd in terminal, then open up '.bashrc' with your text editor. then enter in the alias corresponding with the ones that you want to use (alias name totally up to you if you want to change them).

Example alias below each file in this readme.

---

### [Holberton Proj. Scraper Python](./project-scraper_py.py)
* alias hopy='python2 /DIRECTORY/project-scraper_py.py'
* takes 1 argument: the project url

### [Holberton Proj. Scraper C](./holberton-project-scraper.py)
* alias hos='python2 /DIRECTORY/holberton-project-scraper.py'
* takes 1 argument: the project page url
* then asks for the header file name, skip by leaving blank and press enter
* then asks if you want _putchar.c, type 'y' or 'n'

### [Auth Data](./auth_data.json)
* Store your user/pass in here

### [Holberton README.md Template](./holberton-read_t.py)
* alias hotr='python2 /DIRECTORY/holberton-read_t.py'

---
## Example of hos

[![Watch the video](https://i.imgur.com/3gVa0Qq.png)](https://puu.sh/C5Ogn/2e531610a2.mp4)
Click the image to watch a video version.
---

## Author
* **Derrick Gee** - [kai-dg](https://github.com/kai-dg)

---

## Contributors
* **Brennan D Baraban** - [bdbaraban](https://github.com/bdbaraban)
