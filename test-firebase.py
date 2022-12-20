import firebase_admin
from firebase_admin import credentials,firestore
cd = credentials.Certificate("arc-data-base-firebase-adminsdk-1vqh2-57729cc1ce.json")
# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.
firebase_admin.initialize_app(cd)
datab = firestore.client()
usersref = datab.collection(u'users').document(u'test1')
doc = usersref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')