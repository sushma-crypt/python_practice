#acronyms = {}

#acronyms['LOL'] = 'laugh out load'
#acronyms['IDK'] = "I don't know"
#acronyms['TBH'] = 'to be honest'
#print(acronyms['TBH'])

acronyms = {'LOL': 'laugh out loud',
             'IDK': "I dont know",
             'TBH': 'to be honest'}
sentence = 'IDK' + ' What hapened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)