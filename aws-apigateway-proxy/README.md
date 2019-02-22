# API Gateway Proxy

Goal:
- Demonstrate how to setup API Gateway Proxy using Serverless


Stack:
- Serverless
- AWS API Gateway
- S3

AWS Console Links:

- https://ap-southeast-1.console.aws.amazon.com/apigateway/home?region=ap-southeast-1
- https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks?filter=active

# Deploy

```sh
SLS_DEBUG=* sls deploy
```

For some reason the API gateway isn't deploying this...

# Notes

Solution found in

- https://github.com/serverless/serverless/issues/1738#issuecomment-237926786
- https://cloudhut.io/how-to-setup-proxy-passthrough-on-api-gateway-console-cloudformation-55e923d02b9
- https://stackoverflow.com/questions/51464084/how-to-create-an-api-gateway-http-proxy-without-any-lambda-function

## Created

Created with:

```sh
serverless create --template hello-world --path aws-apigateway-proxy
```


## Fix API Gateway name

As of 2019-02-22, the API Gateways are named `$stage-$service`.

That makes it difficult to see all the stages for a particular service.

This renames it:

```yml
resources:
  Resources:
    # https://github.com/serverless/serverless/issues/2445#issuecomment-333016523
    ApiGatewayRestApi:
      Type: AWS::ApiGateway::RestApi
      Properties:
        Name: ${self:service}-${self:provider.stage}
```

- https://github.com/serverless/serverless/issues/2445#issuecomment-333016523
