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

    data["date"] = Number(data["date"]);
    data["tm"] = Number(data["tm"]);
    data["hm"] = Number(data["hm"]);
    data["li"] = Number(data["li"]);

    // Push the new message into the Realtime Database using the Firebase Admin SDK.
    const ref = await fireStore.collection('values').add(data);

    data.id = ref.id;
    response.json(data);
});

exports.setInfo = functions.https.onRequest(async (request, response) => {

    let data: any = {};
    Object.assign(data, request.query);

    for (let key in data) {
        data[key] = Number(data[key]);
    }

    // Push the new message into the Realtime Database using the Firebase Admin SDK.
    const ref = await fireStore.collection('infos').add(data);

    data.id = ref.id;
    response.json(data);
});

exports.update = functions.https.onRequest(async (request, response) => {
    fireStore.collection('values').get()
        .then(function (querySnapshot: any) {
            querySnapshot.forEach(function (doc: any) {
                // doc.data() is never undefined for query doc snapshots
                console.log(doc.id, " => ", doc.data());
                let up: any = {};
                up["date"] = Number(doc.data().date);
                up["tm"] = Number(doc.data().tm);
                up["hm"] = Number(doc.data().hm);
                if (doc.data().li) {
                    up["li"] = Number(doc.data().li);
                }
                doc.ref.update(up);
            });
        });
});
