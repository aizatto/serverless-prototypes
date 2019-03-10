export function verify(event) {
  // Your verify token. Should be a random string.
  let VERIFY_TOKEN = "c9218247-0272-4362-acf5-765eabaa8af9";

  // Parse the query params
  let mode = event.queryStringParameters['hub.mode'];
  let token = event.queryStringParameters['hub.verify_token'];
  let challenge = event.queryStringParameters['hub.challenge'];

  // Checks the mode and token sent is correct
  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    // Responds with the challenge token from the request
    return {
      statusCode: 200,
      body: challenge,
    }
  } else {
    // Responds with '403 Forbidden' if verify tokens do not match
    return {
      statusCode: 403,
    }
  }
}

export function webhook(event) {
  const body = JSON.parse(event.body);
  body.entry.map((entry) => {
    entry.messaging.map((message) => {
      if (message.sender.id !== '2510354708994619') {
        return;
      }
    });
  });

  return {
    statusCode: 200
  };
}
