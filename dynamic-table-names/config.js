module.exports = (serverless) => {
  const tables = {
    PETS_TABLE: 'pets',
    USERS_TABLE: 'users',
  };

  if (serverless.pluginManager.cliCommands[0] !== 'deploy') {
    return tables;
  }

  const {service, provider: { stage }} = serverless.service;

  // need to test if I don't use the provider stage
  const PREFIX = `${service}-${stage}`;

  const deployed_tables = {};
  for (const key in tables) {
    const table = tables[key];
    deployed_tables[key] = `${PREFIX}-${table}`
  }

  return deployed_tables;
}
