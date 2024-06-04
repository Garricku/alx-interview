#!/usr/bin/node

const fetch = require('node-fetch');

async function getMovieData(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  const response = await fetch(apiUrl);
  const movieData = await response.json();
  return movieData;
}

async function getCharacterName(characterUrl) {
  const response = await fetch(characterUrl);
  const characterData = await response.json();
  return characterData.name;
}

async function printCharacterNames(movieId) {
  try {
    const movieData = await getMovieData(movieId);
    for (const characterUrl of movieData.characters) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Usage: ./0-starwars_characters.js movie_id', error);
  }
}

// Usage: node script.js <MovieID>
const movieId = process.argv[2];
printCharacterNames(movieId);
