# Serverless Prototypes

Goal:
- Isolate larger goals of a serverless projects into smaller easier to deploy prototypes
- Helps with isolation and reproducability

Other serverless apss:

- https://github.com/aizatto/build.my
- https://github.com/aizatto/url-shortener

See my Serverless notes:

- https://www.aizatto.com/notes/serverless

# Simple Template

What I use to create templates:

```sh
serverless create --template hello-world --path $PATH
```

TypeScript:
```sh
serverless create --template aws-nodejs-typescript --path $PATH
```

# Keywords

- Prototypes
- Toys
- Tests
- Proof of Concepts

# Useful URLs

- https://github.com/serverless/examples

# Handler arguments

## event

### ses

```js
{
  Records: [
    {
      eventSource: 'aws:ses',
      eventVersion: '1.0',
      ses: {
        mail: {
          messageId
        }
      }
    }
  ]
}
```

### context

```sh
{
  awsRequestId: '839130a2-ac26-4993-8cf1-10fa1f587880',
  callbackWaitsForEmptyEventLoop: true,
  done: [Function: done],
  fail: [Function: fail],
  functionName: 'dynamic-table-names-prod-hello',
  functionVersion: '$LATEST',
  getRemainingTimeInMillis: [Function: getRemainingTimeInMillis],
  invokedFunctionArn: 'arn:aws:lambda:us-east-1:320184668102:function:dynamic-table-names-prod-hello',
  invokeid: '839130a2-ac26-4993-8cf1-10fa1f587880',
  logGroupName: '/aws/lambda/dynamic-table-names-prod-hello',
  logStreamName: '2019/02/24/[$LATEST]0ca719531827422dae1de8faa81f9069',
  memoryLimitInMB: '128',
  succeed: [Function: succeed]
}
```

### process.env:

```js
{
  AWS_ACCESS_KEY_ID: '',
  AWS_DEFAULT_REGION: 'us-east-1',
  AWS_EXECUTION_ENV: 'AWS_Lambda_nodejs8.10',
  AWS_LAMBDA_FUNCTION_MEMORY_SIZE: '128',
  AWS_LAMBDA_FUNCTION_NAME: 'dynamic-table-names-prod-hello',
  AWS_LAMBDA_FUNCTION_VERSION: '$LATEST',
  AWS_LAMBDA_LOG_GROUP_NAME: '/aws/lambda/dynamic-table-names-prod-hello',
  AWS_LAMBDA_LOG_STREAM_NAME: '2019/02/24/[$LATEST]0ca719531827422dae1de8faa81f9069',
  AWS_REGION: 'us-east-1',
  AWS_SECRET_ACCESS_KEY: '_',
  AWS_SESSION_TOKEN: '_',
  AWS_XRAY_CONTEXT_MISSING: 'LOG_ERROR',
  AWS_XRAY_DAEMON_ADDRESS: '169.254.79.2:2000',
  LAMBDA_RUNTIME_DIR: '/var/runtime',
  LAMBDA_TASK_ROOT: '/var/task',
  LANG: 'en_US.UTF-8',
  LD_LIBRARY_PATH: '/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib',
  NODE_PATH: '/opt/nodejs/node8/node_modules:/opt/nodejs/node_modules:/var/runtime/node_modules:/var/runtime:/var/task:/var/runtime/node_modules',
  PATH: '/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin',
  PETS_TABLE: 'dynamic-table-names-dev-pets',
  TZ: ':UTC',
  USERS_TABLE: 'dynamic-table-names-dev-users',
  _AWS_XRAY_DAEMON_ADDRESS: '169.254.79.2',
  _AWS_XRAY_DAEMON_PORT: '2000',
  _HANDLER: 'handler.hello',
  _X_AMZN_TRACE_ID: 'Root=1-5c72ccab-55bb7ee4ae8a47049a23dec4;Parent=4613ca99476ef7a7;Sampled=0'
}
```
