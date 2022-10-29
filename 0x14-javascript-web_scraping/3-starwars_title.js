#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request(apiUrl + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const resJson = JSON.parse(body);
    console.log(resJson.title);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
