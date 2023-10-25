#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, responce, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dat = data.characters;
  for (const i of dat) {
    request.get(i, function (error, responce, bod) {
      if (error) {
        console.log(error);
      }
      const data2 = JSON.parse(bod);
      console.log(data2.name);
    });
  }
});
