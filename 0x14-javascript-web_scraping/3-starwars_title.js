#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
