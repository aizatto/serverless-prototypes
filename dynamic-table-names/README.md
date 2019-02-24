The goal of this repository is to get the DynamoDB table names to be shorter when developing locally, and expanded whenever deployed.

For example:

Locally:

- PETS_TABLE: pets
- USERS_TABLE: users

Deployed:

- PETS_TABLE: service-stage-pets
- USERS_TABLE: service-stage-users

The trouble though is that the config.js file will need to be called in each repositories `serverless.yml`

Also note, that it reads from the `provider.stage`

```sh
SLS_DEBUG=* sls invoke local --function hello
```

Notes:
- https://serverless.com/framework/docs/providers/aws/guide/variables#reference-properties-in-serverlessyml
- https://serverless.com/framework/docs/providers/aws/guide/variables/#reference-variables-in-javascript-files
