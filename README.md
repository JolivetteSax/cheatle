# cheatle
Cheating at wordle

Takes 3 parameters, opt out with the * 

if you do all stars it'll generate all possible combinations then truncate them to a max of 15

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
