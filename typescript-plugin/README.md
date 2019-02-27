Goal to compare TypeScript using:

- Plugin: https://github.com/prisma/serverless-plugin-typescript
- Template: https://github.com/serverless/serverless/tree/master/lib/plugins/create/templates/aws-nodejs-typescript 

It seems easier to use the plugin vs the template as you are not reliant on webpack.

Created with
```sh
serverless create -t aws-nodejs --path typescript-plugin
cd typescript-plugin
yarn add --dev serverless-plugin-typescript
```

Test
```sh
SLS_DEBUG=* sls invoke local --function hello
```

Notes:
- Last updated 6th January 2018
- Defined to use TypeScript `^v2.2.2`:
  - https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-2.html
  - Released: 22nd February 2017
- Pulls TypeScript `v2.9.2`
  - https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-9.html
  - https://github.com/Microsoft/TypeScript/releases/tag/v2.9.2
  - Released 14th June 2018
- Current version of TypeScript `v3.3.3333`

Pros:
- No dependency on webpack
- You can install local latest version of TypeScript

You can remove your own version of TypeScript.

Without any changes:
```sh
sls invoke local --function hello
```

Output:
```
TypeScript Version: 2.9.2
```

Installing latest version of TypeScript:

```
yarn add typescript
sls invoke local --function hello
```

Output:
```
TypeScript Version: 3.3.3333
```

What to do using Plugin:
- Add `.build` to `.gitignore`

Test remotely:
```sh
aws lambda invoke --function-name prototype-typescript-plugin-dev-hello /dev/stdout
```

# Template

Template can be created via:
```sh
serverless create -t aws-nodejs-template --path typescript-template
```

Cons:
- Dependency on WebPack
