#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const complete = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.complete === true) {
        if (complete[task.userId] === undefined) {
          complete[task.userId] = 1;
        } else {
          complete[task.userId]++;
        }
      }
    }
    console.log(complete);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
