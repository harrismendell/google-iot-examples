const functions = require('firebase-functions');
const cors = require('cors')({ origin: true });
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);
var db = admin.firestore();

const TOPIC = 'test-topic-name';
const DEVICE_COLLECTION = 'devices';

exports.pubsubToFirestore = functions.pubsub.topic(TOPIC_NAME).onPublish((message) => {
  console.log('Received message', message);
  const messageBody = message.data ? Buffer.from(message.data, 'base64').toString() : null;
  let data;
  try {
    data = JSON.parse(messageBody)
  } catch (e) {
    throw new Error('Expecting JSON payload')
  }
  const attributes = message.attributes;
  const deviceId = attributes.deviceId;
  console.log('Processing data ', data, deviceId);

  // Set data in the document
  db.collection(DEVICE_COLLECTION).doc(deviceId).set({
    lastMessage: {
      time: data.time
    }
  }, { merge: true })
  return data;
});
