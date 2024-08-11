#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  makeRequest(characters, 0);
});

function makeRequest (characters, index) {
  if (index === characters.length) return;
  request(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    makeRequest(characters, index + 1);
  });
}
