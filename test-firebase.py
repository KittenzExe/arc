import firebase_admin
from firebase_admin import credentials,firestore
cd = credentials.Certificate({
  "type": "service_account",
  "project_id": "arc-data-base",
  "private_key_id": "57729cc1ce4f367212f3e59b32adf27b37906e19",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCm9orkircmE4oY\n6+eUaTRMxg7seQGdaxpyYy/Cvz6mPv7LdfpeloXUnxsNd/yJsjCwVjvCcvZqZq3Y\n00+0C4TxU4ubyo34BJdNlKXm6fyvm757/A8cpTgv9znb9vNzEro9GFlTZ9XxYjFF\nXqNyVsUjJQN2XwT66sN6yiwGuiwX0AsXCgO3RCC1skR4QDeCaXbEM9VO/CHrmjdw\nwLKj755/5Ht5MnI9JCqQJP221NyD67wK7Pv/YqsLIEojY4wMlZyc+hstg2Y76x7B\naK7duNyXJHQPm7oQ5grtoEK+oS4SdrlCjPnOtAFkiikdYEOJutJis+w0Q3Fp50In\ne8iUD4tJAgMBAAECgf8VXdqc00aXG8BNmOL1nhhKmAJuALzfzi86EVpUFMJyoRdd\nPe1VPvPnVjsADMxTO4M/mWxvSlh+kPydBcrqfLHPao1HlBuocEsPgpZnIkqZ3R1A\ngKcc+p8b+K1O3togKI4bbC3q+6eLOZoOw624grl3wwHxVYNE6pHlPwujUMFlPuWW\ncfjESm9y2cf1HBzJClAAZk7UYadIhnNQOmkfMMH3i/9tWffjqHoqJ0g6/QJC7/i2\n4vYIIDxomQjO/P/8asYqn9A3LfYu0qb6GGszTc+gANbwSReVaDN5xBwitVMZEAat\n1HcfkJKLW1bHC8T2Xvnya+eAs9KoSYzDhP1g3FECgYEA1kxS+XVyoHSYrssmACgO\n50xvrCOlPjzdmy7XOGDKctFApCyAmx46o6w/LF2gsJYOIY9y6wlbaWtunN+njl0y\nanIVoUnSPTZqhwqIzwn4HHLq+ndhy8BUPExGvEUcZ8zBmrxPNzZicBttpUKWZnH6\nU3ehsnSuwcWkovJ8XWLM+3ECgYEAx3QhOF+OY9Vf5G2T2pS+Is8r2qhk9naNrOFq\nWLcIobSbahr+IlCgg5Ggy2soiM/UJWq8zVChn6frTqEPRNWYwAhYg091K4RjmeZ8\n4d3pVHQr5jPiq5XtFcjxf23i2soB753U6wHt1EYGEr55OaRfvg3g3NZ0koveQtCm\nD+ijsVkCgYEAgAg7rqTX5jujGRNwUbmdJd3J/muRhzywHc3/ccSKT8zrNOsNrx+B\nY1Y+rBAIOFh+etiMjRYbEkHIZVtObUULIQOmHqXPQRkoziOiFyhanwydjSUUPbpb\n2WatAEC+NtnjdcI6Bb+tUlNgz9KXrv870vBvoAIMguLFeUEswlKMK1ECgYA1k1gp\nEGHrJzGu5lBE8pdwOj4JahpUqdu8iIBMfD3xUdY9VirVhNrY/JE4kvw8Y7cUpes5\nK2N+w1hNsq2rS8TQMG22N+29Vr56ZJM/CKDYcqwoFd/ZP1iD9YoJNLcvFfwXJUpA\nJjCASJ7xAgEGHsUpBAlWyLRfePqm7+zrcQ4nYQKBgQCxIYJVn9Jh3A4PomIA0VWE\nayGFXq3kHMHJ0YOo/xc2GifOjEUKACrOWkOnvQnh+WvijhJdUt5PVXZWfxU4j4Uy\nvrCdiiXnlRyddT56kYluIgsBJN+2ThQ0rCLweuB+L4KbTZKdmvKIc3evgrKaCcvr\niRXuBGvrnPkEn+r7MDobHg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-1vqh2@arc-data-base.iam.gserviceaccount.com",
  "client_id": "112266744488263067593",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1vqh2%40arc-data-base.iam.gserviceaccount.com"
})
# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.
firebase_admin.initialize_app(cd)
datab = firestore.client()
doc_ref = datab.collection(u'users').document(u'test1')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
    sID = (f"{doc.to_dict()}")
    print(sID[0:5])
else:
    print(u'No such document!')