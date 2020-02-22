import * as functions from 'firebase-functions';

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

const fireStore = admin.firestore()

// // Start writing Firebase Functions
// // https://firebase.google.com/docs/functions/typescript
//
exports.setValue = functions.https.onRequest(async (request, response) => {

    let data: any = {};
    Object.assign(data, request.query);
    // Push the new message into the Realtime Database using the Firebase Admin SDK.
    const ref = await fireStore.collection('values').add(data);

    data.id = ref.id;
    response.json(data);
});
