# express-lambda

The question I'm trying to answer is:

> Should you run Express on AWS Lambda?

Pros:
- Reuse express

Cons:
- Complexity

When you should?

- Great for prototyping

When you shouldn't?

- AWS Lambda has a maxmium of 1000 concurrent connections

# Design Decision

- `app.js`: your express code lives here
- `server.js`: this is the code to run the server
- `handler.js`: this is the lambda handler

This allows you to run `server.js` locally:

```sh
node src/server.js
```

Then when deployed, the lambda's will fire via `src/handler.js`

Pros:
- For local development, you don't have to wrap the complexity of express within serverless
