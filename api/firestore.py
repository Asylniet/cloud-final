from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Enable offline data persistence (caching)
db.enable_network()

# Example of reading from Firestore
doc_ref = db.collection('events').document('event_id')
doc = doc_ref.get()