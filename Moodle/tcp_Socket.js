// A client for the date server.
//This client should be used for Moodle integration to show up the data on a page
// Example usage:
//
//   node dateclient.js 10.0.1.40
//
// Source-Code: https://cs.lmu.edu/~ray/notes/jsnetexamples/

const net = require('net');

const client = new net.Socket();
client.connect({ port: 59090, host: process.argv[2] });
client.on('data', (data) => {
  console.log(data.toString('utf-8'));
});