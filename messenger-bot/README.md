# Notes

- https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start
- https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup
- https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages
- https://serverless.com/blog/building-a-facebook-messenger-chatbot-with-serverless/

# `event`

```json
{
  "resource": "/",
  "path": "/",
  "httpMethod": "POST",
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "deflate, gzip",
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Desktop-Viewer": "true",
    "CloudFront-Is-Mobile-Viewer": "false",
    "CloudFront-Is-SmartTV-Viewer": "false",
    "CloudFront-Is-Tablet-Viewer": "false",
    "CloudFront-Viewer-Country": "US",
    "Content-Type": "application/json",
    "Host": "nefyrq8jv2.execute-api.ap-southeast-1.amazonaws.com",
    "User-Agent": "facebookexternalua",
    "Via": "1.1 5afc8eca980390e71a86518c6f90001a.cloudfront.net (CloudFront)",
    "X-Amz-Cf-Id": "h6t9nujnNm8wQY8s1IIlmzZNpP-KCOUFIUIElHiEKR0frsMtpvzhIQ==",
    "X-Amzn-Trace-Id": "Root=1-5c84e584-0cf209c8fa58c7769f419606",
    "X-Forwarded-For": "66.220.149.2, 52.46.17.18",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https",
    "X-Hub-Signature": "sha1=fa08ff54136c5d52576f641419c7d25b9fc28bb8"
  },
  "multiValueHeaders": {
    "Accept": [
      "*/*"
    ],
    "Accept-Encoding": [
      "deflate, gzip"
    ],
    "CloudFront-Forwarded-Proto": [
      "https"
    ],
    "CloudFront-Is-Desktop-Viewer": [
      "true"
    ],
    "CloudFront-Is-Mobile-Viewer": [
      "false"
    ],
    "CloudFront-Is-SmartTV-Viewer": [
      "false"
    ],
    "CloudFront-Is-Tablet-Viewer": [
      "false"
    ],
    "CloudFront-Viewer-Country": [
      "US"
    ],
    "Content-Type": [
      "application/json"
    ],
    "Host": [
      ".execute-api.ap-southeast-1.amazonaws.com"
    ],
    "User-Agent": [
      "facebookexternalua"
    ],
    "Via": [
      "1.1 5afc8eca980390e71a86518c6f90001a.cloudfront.net (CloudFront)"
    ],
    "X-Amz-Cf-Id": [
      "h6t9nujnNm8wQY8s1IIlmzZNpP-KCOUFIUIElHiEKR0frsMtpvzhIQ=="
    ],
    "X-Amzn-Trace-Id": [
      "Root=1-5c84e584-0cf209c8fa58c7769f419606"
    ],
    "X-Forwarded-For": [
      "66.220.149.2, 52.46.17.18"
    ],
    "X-Forwarded-Port": [
      "443"
    ],
    "X-Forwarded-Proto": [
      "https"
    ],
    "X-Hub-Signature": [
      "sha1=fa08ff54136c5d52576f641419c7d25b9fc28bb8"
    ]
  },
  "queryStringParameters": null,
  "multiValueQueryStringParameters": null,
  "pathParameters": null,
  "stageVariables": null,
  "requestContext": {
    "resourceId": "f8a90azip8",
    "resourcePath": "/",
    "httpMethod": "POST",
    "extendedRequestId": "WUjMvFoiSQ0FjGw=",
    "requestTime": "10/Mar/2019:10:23:00 +0000",
    "path": "/dev/",
    "accountId": "",
    "protocol": "HTTP/1.1",
    "stage": "dev",
    "domainPrefix": "",
    "requestTimeEpoch": 1552213380789,
    "requestId": "7b47bec4-431e-11e9-b684-1be8671286f0",
    "identity": {
      "cognitoIdentityPoolId": null,
      "accountId": null,
      "cognitoIdentityId": null,
      "caller": null,
      "sourceIp": "66.220.149.2",
      "accessKey": null,
      "cognitoAuthenticationType": null,
      "cognitoAuthenticationProvider": null,
      "userArn": null,
      "userAgent": "facebookexternalua",
      "user": null
    },
    "domainName": "",
    "apiId": ""
  },
  "body": "{\"object\":\"page\",\"entry\":[{\"id\":\"397934987666525\",\"time\":1552213380295,\"messaging\":[{\"sender\":{\"id\":\"2510354708994619\"},\"recipient\":{\"id\":\"397934987666525\"},\"timestamp\":1552132131692,\"message\":{\"mid\":\"HUTLBVmKCp6FMLQYDW8BPAZ_KnduFT-02tQJjqX3GqoI-mGLHHZgJG0FHyJ8ynxVrzPuI4v6AgAhZokQ4pNvOA\",\"seq\":1443915,\"text\":\"2019\\/03\\/09 7:48:48 PM - W10\\/D6 Saturday\"}}]}]}",
  "isBase64Encoded": false
}
```

