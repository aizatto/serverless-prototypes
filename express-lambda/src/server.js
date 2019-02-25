const PORT = process.env.PORT || 3000;

const app = require('./app.js');

app.listen(PORT, () => {
  // eslint-disable-next-line no-console
  console.info(`Env: ${process.env.NODE_ENV}`);
  // eslint-disable-next-line no-console
  console.info(`Open in your browser http://localhost:${PORT}`);
});
