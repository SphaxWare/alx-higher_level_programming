#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes(url)) {
        count++;
      }
    });
    console.log(count);
  }
});
