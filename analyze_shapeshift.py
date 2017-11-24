import pickle
file = pickle.load(open('shapeshift.p', 'rb'))

counting= map(lambda x: x['curIn']=='ETH', file)
print 'The number of transactions that have Ethereum as the input currency: ', counting.count(True)

counting1= map(lambda x: x['curOut']=='BTC', file)
print 'The number of transactions that have Bitcoin as the output currency: ', counting1.count(True)

counting2= map(lambda x: x['curOut']=='BTC' and x['curIn']=='ZEC', file)
print 'Number of transactions that convert Zcash to Bitcoin: ', counting2.count(True)
