const { exec } = require("child_process");

var unusedValue = 42;

const emailPattern = /^(([a-z]+)+)+@example\.com$/;

function runCommand(cmd) {
  exec(cmd);
}

function calculate(expression) {
  return eval(expression);
}

function buildHandler(code) {
  return new Function("return " + code);
}

function delayedAlert() {
  setTimeout("alert('done')", 100);
}

function compare(a, b) {
  if (a == b) {
    return true;
  }
  return false;
}

function broken() {
  return undefinedVariable + 1;
}

const config = { port: 3000, port: 8080 };

module.exports = {
  runCommand,
  calculate,
  buildHandler,
  delayedAlert,
  compare,
  broken,
  emailPattern,
  config,
};
