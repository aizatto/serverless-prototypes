# Goal

A simple Serverless Python example demonstrating storing a Facebook Access Token into Parameter Store.

- Store Facebook Access Token in Parameter Store for reuse
- Build simple Facebook API
- Experiment with
  - Parameter Store
  - Python on Serverless
  - Facebook APIs

Stack:
  - Serverless
  - Python3
  - AWS API Gateway
  - AWS Parameter Store
  - Facebook Login


My notes on Serverless: https://www.aizatto.com/notes/serverless

# Disclaimers

I understand if another user accesses the login page, it will overwrite the Facebook Access Token. I don't expect any other users for now. As a demo and example, I still think this repository is useful.

I could have used something like AWS Cognito or Auth0, but I thought this was simpler. You'd probably want to use something like that if you were doing something in production.

# Configuration

On https://developers.facebook.com/apps/$app_id/fb-login/settings/

Products > Facebook Login > Settings

Valid OAuth Redirect URIS:

Enter your API Gateway: https://$secret.execute-api.region.amazonaws.com/prod/callback/

Visit

https://$secret.execute-api.ap-southeast-1.amazonaws.com/prod/

# Notes

```sh
aws ssm put-parameter --name "/build.my/dev/FACEBOOK_CLIENT_ID" --value $app_id --type String --region ap-southeast-1
aws ssm put-parameter --name "/build.my/dev/FACEBOOK_CLIENT_SECRET" --value $client_secret --type String --region ap-southeast-1
```

Try login flow, and see if you can get parameter

```sh
aws ssm get-parameter --name "/build.my/dev/FACEBOOK_ACCESS_TOKEN"
```

- https://ap-southeast-1.console.aws.amazon.com/systems-manager/parameters?region=ap-southeast-1
- https://aws.amazon.com/systems-manager/pricing/
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.put_parameter
- https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/
- https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html
- https://docs.python.org/3.7/library/urllib.request.html
- https://serverless.com/framework/docs/providers/aws/guide/variables/#reference-variables-using-the-ssm-parameter-store

Convert unixtime to time in CLI:

```sh
date -r $unixtime
```
