# cheatle
Cheating at wordle with python, inspired by https://github.com/regexer/wordler

Takes 3 URL params, opt out with the *
A-la: `@get('/<known>/<missplaced>/<missing>')`
Since this doesn't really use wildcards specify missing letters from the set of known/missplaced by using underscores

if you do all stars it'll generate all possible combinations then truncate them to a max of 15

If for example you choose words that don't contain an A like so: `*/*/A`

Shows the first 15 like so
"BEBED", "BEBOG", "BEBOP", "BECRY", "BECUT", "BEDEL", "BEDEN", "BEDEW", "BEDIM", "BEDIN", "BEDIP", "BEDOG", "BEDOT", "BEDUB", "BEDUR"

# Prereqs

```
pip3 install nltk
pip3 install bottle
$ python3
Python 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> nltk.download('words')
```

# Run

```
$ python3 server.py 
Dictionary size: 235892
Bottle v0.12.23 server starting up (using WSGIRefServer())...
Listening on http://127.0.0.1:8000/
Hit Ctrl-C to quit.

127.0.0.1 - - [04/Sep/2022 14:09:35] "GET /LA___/RE___/* HTTP/1.1" 200 160
127.0.0.1 - - [04/Sep/2022 14:12:53] "GET /LA___/RE___/G HTTP/1.1" 200 142
127.0.0.1 - - [04/Sep/2022 14:13:22] "GET /LA___/E_R__/G HTTP/1.1" 200 133
127.0.0.1 - - [04/Sep/2022 14:14:28] "GET /LAY__/__R_E/G HTTP/1.1" 200 79
```

## Example
```
$ curl localhost:8000/LA___/RE___/*
{"known": "LA___", "missplaced": "RE___", "missing": "*", "results": ["LACER", "LADER", "LAGER", "LAKER", "LARGE", "LARVE", "LASER", "LATER", "LAVER", "LAYER"]}

$ curl localhost:8000/LA___/RE___/G
{"known": "LA___", "missplaced": "RE___", "missing": "G", "results": ["LACER", "LADER", "LAKER", "LARVE", "LASER", "LATER", "LAVER", "LAYER"]

$ curl localhost:8000/LA___/E_R__/G
{"known": "LA___", "missplaced": "E_R__", "missing": "G", "results": ["LACER", "LADER", "LAKER", "LASER", "LATER", "LAVER", "LAYER"]}

$ curl localhost:8000/LAY__/__R_E/G
{"known": "LAY__", "missplaced": "__R_E", "missing": "G", "results": ["LAYER"]}
```

## TODO:
Algorithmic efficiency? 
Accented chars?
