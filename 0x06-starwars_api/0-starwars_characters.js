#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;
      for (const character of characters) {
        const characterBody = await getCharacter(character);
        console.log(characterBody.name);
      }
    }
  }
});

async function getCharacter (character) {
  return new Promise((resolve, reject) => {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        if (response.statusCode === 200) {
          const characterBody = JSON.parse(body);
          resolve(characterBody);
        } else {
          reject(
            Error('Request failed with status code: ' + response.statusCode)
          );
        }
      }
    });
  });
}
