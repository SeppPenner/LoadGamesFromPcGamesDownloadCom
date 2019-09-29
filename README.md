# LoadGamesFromPcGamesDownloadCom

LoadGamesFromPcGamesDownloadCom is written and tested in Python 3.7.4. Its purpose is to load all posts in a structured way from https://pcgames-download.com/.
The project is no longer needed because the website went down (Probably due to DMCA takedown).
The last state of the webiste can be found under http://web.archive.org/web/20181231044556/https://pcgames-download.com/.

[![Build status](https://ci.appveyor.com/api/projects/status/che88x6i83lacy0x?svg=true)](https://ci.appveyor.com/project/SeppPenner/loadgamesfrompcgamesdownloadcom)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/LoadGamesFromPcGamesDownloadCom.svg)](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/LoadGamesFromPcGamesDownloadCom.svg)](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/LoadGamesFromPcGamesDownloadCom.svg)](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/LoadGamesFromPcGamesDownloadCom/badge.svg)](https://snyk.io/test/github/SeppPenner/LoadGamesFromPcGamesDownloadCom) 

## How does it work:

The programm scrapes the last page index from the website https://pcgames-download.com/ and iterates over all available pages to collect all posts. The data is saved as a CSV file 
under the [savedData](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/tree/master/savedData) subfolder).

Staged data / raw data will be loaded to the [loading](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/tree/master/loading) subfolder and overwritten.

The programm doesn't use threading because the website otherwise might block the IP address of the scraper in respect to DDoS attacks.

Loading the data might take a while :hourglass_flowing_sand:, so have a :coffee: or two :coffee: :coffee: or do something else in parallel: :iphone:, :telephone:, :tv:, :computer:, :toilet:

## How do you start the project:

```python
python LoadGames.py
```

## What else do you need:

BeautifulSoup 4

## Install all required pip package dependencies with
```python
pip install -r requirements.txt
```

## The result:

The result is a .csv file for the current status of the games: [2018-05-13T19-02-26-141897.csv](https://github.com/SeppPenner/LoadGamesFromPcGamesDownloadCom/tree/master/savedData/2018-05-13T19-02-26-141897.csv).

Change history
--------------

* **Version 1.0.0.0 (2019-09-29)** : Updated python version, updated requirements.
* **Version 1.0.0.0 (2018-05-13)** : 1.0 release.