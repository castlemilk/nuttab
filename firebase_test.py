from firebase import firebase
import time
import json
import os
start_time = time.time()
firebase = firebase.FirebaseApplication('https://nutritiondb-3314c.firebaseio.com/', None)
# result = firebase.get('/itemList', None)
result = firebase.get('/v1/USDA_DB/27053', None)
# print ("got %d items " % len(result))
#with open(os.path.join(os.getcwd(),'USDA_DB.json')) as f:
#    db_dict = json.load(f)
#    print "pushing large dict.."
#    result = firebase.put('v1/','USDA_DB', db_dict, params={'print':'silent'})

# result = firebase.delete('v1/','USDA_DB')
# print result
print("--- request completed in %s seconds ---" % (time.time() - start_time))
for code, info in result['nutrients'].iteritems():
    print code,
    print info['name']
