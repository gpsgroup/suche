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

You will have to rename above file to big.txt and place it in the scripts directory for seeding.


To use the search engine, first of all, you have to crawl the web pages. First of all, add a new URL
(reddit.com or bbc.com) to admin/indexer/sucheurl/ (sucheurl table). Then, call the crawler from

    http://127.0.0.1:8000/crawler/crawlpage

After the web page is crawled, index it by calling

    http://127.0.0.1:8000/crawler/operatedata

After you index the webpage, it will extract more URLs and you can repeat the
crawl process as long as you want.
