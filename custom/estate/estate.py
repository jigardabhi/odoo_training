import xmlrpc.client

db = "emp1234"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print ("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

# to_confrim_ids = models.execute_kw(db, uid, password, 'estate.property', 'search', [[('garden_orientation', '=', 'north')]])
# print ("\n\nto_confrim_id ::: ", to_confrim_ids)