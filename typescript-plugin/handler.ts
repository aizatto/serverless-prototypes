const pkg = require('typescript/package.json');

export const hello = async (event, context) => {
  console.log(`TypeScript Version: ${pkg.version}`);
  return {
    statusCode: 200,
    body: JSON.stringify({
      pkg,
    }),
  };
};
