// A test server to test the JavaScript client
//This client should be used for Moodle integration to show up the data on a page
// Example usage:
//
//   node dateclient.js 10.0.1.40
//
// Source-Code: https://cs.lmu.edu/~ray/notes/jsnetexamples/


const net = require('net');

// A use-once date server. Clients get the date on connection and that's it!
const server = net.createServer((socket) => {
  socket.end(`${new Date()}\n`);
});

server.listen(59090);