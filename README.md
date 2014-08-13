# Suche
Suche is an intelligent search engine. Currently crawling only wikipedia.org, reddit.com and bbc.com, it can be modified to crawl every URL.
It is made in python using django framework.

To start the project,

    ./runserver.sh

First seed the database for spell corrector words use:
./dbseed.sh

The spell correction script must be running for the project to work properly

    ./runspell.sh

To seed the word list for the spell correction program, you need to place a file named "big.txt" in the scripts folder. 
Then, run the database seed program as

    python3 manage.py shell
    >>> from scripts.databaseSeed import run
    >>> run()

The current text source for seeding the database is

    http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

