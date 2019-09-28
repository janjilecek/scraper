# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        self.content = None
        self.soup = None
        self.samples = None
        self.lastSample = None
        self.numbers = None

    def download(self):
        result = requests.get("https://www.korunka.eu/vysledky")
        if result.status_code == 200:
            self.content = result.content
        else:
            raise Exception("Download: Could not fetch data.")

    def findSoupSamples(self):
        self.soup = BeautifulSoup(self.content, "html.parser")
        self.samples = self.soup.find('div', {'class': 'lotteryResultsView'})

    def getLastSample(self):
        allSamples = self.samples.findAll('div', {'class': 'flex'})
        lastSample = None
        for lotterySample in allSamples:
            lotterySample = lotterySample.find('div', {'class': 'lotteryResult'})
            if lotterySample is None:
                break
            lastSample = lotterySample
        self.lastSample = lastSample.parent

    def extractDataFromSample(self):
        resultList = []
        dayTimeString = self.lastSample.find('h4').text
        numbers = self.lastSample.findAll('div', {'class': 'lotteryResult'})
        for number in numbers:
            resultList.append(number.text.strip().encode('ascii', 'ignore'))
        self.numbers = (dayTimeString, resultList)

    def getPreparedMessage(self):
        stringToSend = ""
        stringToSend += "Vecerni:" if "Ve" in self.numbers[0] else "Odpoledni:"  # remove accents hack
        stringToSend += u' '.join(self.numbers[1]).encode('utf-8').strip()
        return stringToSend

    def run(self):
        self.download()
        self.findSoupSamples()
        self.getLastSample()
        self.extractDataFromSample()
        self.getPreparedMessage()
