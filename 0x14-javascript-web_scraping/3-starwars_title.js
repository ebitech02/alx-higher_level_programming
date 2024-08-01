#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const argsId = process.argv[2];

request.get(url, (error, response, body) => {
    console.log(
	error ? error.message :
	    response.statusCode === 200 ? JSON.parse(body).title :
	    console.log(body.title);)};
	   );
