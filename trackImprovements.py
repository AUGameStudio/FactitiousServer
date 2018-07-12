import json

with open('improvementPks.json') as f:
    persons = sorted(json.load(f),key=lambda p:p['games'])

def trackImprovements():
    tabs = {}
    for p in persons:
        numG = p['games']
        if not numG in tabs:
            tabs[numG]= {'totP':0, 'avg_score':0, 'avg_time':0, 'sum_scores':[0 for i in range(numG)], 'sum_times':[0 for i in range(numG)]}
            print 'numG',numG
        d = tabs[numG]
        d['totP'] += 1
    return tabs

        
