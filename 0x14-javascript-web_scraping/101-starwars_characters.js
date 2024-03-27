#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  const fetchCharactersInOrder = async () => {
    for (let i = 0; i < charactersUrls.length; i++) {
      try {
        const characterUrl = charactersUrls[i];
        const character = await fetchCharacter(characterUrl);
        console.log(character.name);
      } catch (error) {
        console.error('Error fetching character details:', error);
      }
    }
  };

  const fetchCharacter = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  };

  fetchCharactersInOrder();
});
