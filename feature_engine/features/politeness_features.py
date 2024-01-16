"""
file: politeness_features.py
---
Defines a feature that calls the PolitenessStrategies from ConvoKit
and returns them as 21 columns (for each message).

Link to Politness Documentation: https://convokit.cornell.edu/documentation/politenessStrategies.html
Link to ConvoKit GitHub examples: https://github.com/CornellNLP/ConvoKit/tree/master/examples/politeness-strategies

You should follow the samples to create the appropriate imports, process the data, and call the function.
"""

import convokit
import spacy
from convokit import PolitenessStrategies

"""
function: get_politeness_strategies
(Chat-level function)

This gets the politeness annotations of each message, with some fields 
including HASHEDGE, Factuality, Deference, Gratitude, Apologizing, etc.
"""
def get_politeness_strategies(text):

     '''
     @TODO : Add your Implementation of the feature here! Good Luck :)
     '''

     ps = PolitenessStrategies()
     spacy_nlp = spacy.load('en_core_web_sm', disable=['ner'])
     utt = ps.transform_utterance(text, spacy_nlp=spacy_nlp)
     return utt.meta['politeness_strategies']
