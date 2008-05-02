"""
parse speech data for each representative

from: data/crawl/govtrack/speeches.xml
"""

import web
from xml.sax import make_parser, handler

class SpeechesXML(handler.ContentHandler):
    def __init__(self,callback):
        self.callback = callback
        self.current = None
        
    def startElement(self, name, attrs):
        if name == 'representative':
            self.current = web.storage(attrs)
    
    def endElement(self, name):
        if name == 'representative':
            self.callback(self.current)
        self.current = None

def callback(rep):
    if rep.get('Speeches'):
        print rep.id, rep.Speeches, rep.WordsPerSpeech

def main(callback):
    parser = make_parser()
    parser.setContentHandler(SpeechesXML(callback))
    parser.parse('../data/crawl/govtrack/us/110/repstats/speeches.xml')

if __name__ == "__main__": main(callback)