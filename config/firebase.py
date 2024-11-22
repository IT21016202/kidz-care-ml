from datetime import datetime

import firebase_admin
from firebase_admin import credentials, storage
from firebase_admin import db

date_now = datetime.now()

# Firebase Configuration
GOOGLE_APPLICATION_CREDENTIALS = ''
FIREBASE_STORAGE_BUCKET = ''
FIREBASE_DATABASE_NAME = ''
FIREBASE_DATABASE_URL = ''

# Initialize Firebase
cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'storageBucket': FIREBASE_STORAGE_BUCKET,
    'databaseURL': FIREBASE_DATABASE_URL
})

firebase_ref = db.reference(FIREBASE_DATABASE_NAME)
# kids_ref = firebase_ref.child('kids')
alert_ref = db.reference('alert')
# alert_ref = firebase_ref.child('alert')
# attendance_ref = firebase_ref.child('attendance')
attendance_ref = db.reference('attendance')

# If Saving Images, Initialize Firebase Storage bucket
firebase_bucket = storage.bucket()
