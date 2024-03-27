#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }
  fs.writeFile(filepath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    }
  });
});
