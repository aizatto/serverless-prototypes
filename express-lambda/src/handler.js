const serverless = require("serverless-http");

const app = require('./app.js');
const express = serverless(app);

module.exports = { express }
