#!/usr/bin/node

const { dict } = require('./101-data');

const userIdsByOccurrence = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userIdsByOccurrence[occurrence]) {
    userIdsByOccurrence[occurrence] = [];
  }

  userIdsByOccurrence[occurrence].push(userId);
}

console.log(userIdsByOccurrence);
