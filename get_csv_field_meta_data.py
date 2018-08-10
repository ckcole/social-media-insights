import csv, os

field_lengths = {}
nullable = []
first = True
for file in os.listdir('data'):
    filename = os.path.abspath('data/' + file)

    with open(filename, 'r') as f:
        print filename
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if first:
                for key in row:
                    field_lengths[key] = len(row[key])
                first = False
            else:
                for key in row:
                    if key not in nullable and row[key] in ('', None):
                        print '{} IS NULLABLE'.format(key)
                        nullable.append(key)
                        continue
                    if len(row[key]) > field_lengths[key]:
                        print 'Updating {} in the {}th row from {} to {}'.format(key, i, len(row[key]), field_lengths[key])
                        field_lengths[key] = len(row[key])


#TODO:  create tables and push with SQLALCHEMY or with .SQL Files?
'''
outcome:
nullable = ['post_type', 'region', 'content', 'account_type', 'external_author_id']
field_lengths =  {'account_category': 12,
 'account_type': 10,
 'author': 15,
 'content': 938,
 'language': 19,
 'post_type': 11,
 'region': 25,

 'external_author_id': 17,  #TODO: why is this 17?  should be like 10
 'followers': 6,  #TODO: these three MEDIUMINT
 'following': 5,
 'updates': 6

 'retweet': 1,
 'new_june_2018': 1,
 
 'harvested_date': 16,  #TODO: m/d/y or d/m/y  ????
 'publish_date': 16,
 
 }
'''

'''
# varchar
{'account_category': 'LeftTroll',
 'account_type': 'left',
 'author': 'BLMSOLDIER',
 'post_type': 'RETWEET',
 'language': 'English',
 'region': 'United States',
 'content': 'Retweeted Citizen TV Kenya (@citizentvkenya):  Koome: This court won\xe2\x80\x99t sit next week but will ask president to... https://t.co/v64E7IFOw2',
 
 # int
 'external_author_id': '1685173321',
 'followers': '712',
 'following': '694',
 'updates': '4845'

# str Date
############## format_str = '%m/%d/%Y %H:%M'
##############  I think use DATETIME over TIMESTAMP,  or maybe unix?
 'harvested_date': '3/7/2017 10:27',
 'publish_date': '3/7/2017 10:27',

# bool as int
 'new_june_2018': '0',
 'retweet': '1',}
 '''