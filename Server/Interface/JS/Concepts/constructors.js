/*
Constructors are a way  to define the 'shape' of an object,
meaning we can optionally define some attributes/methods
saving us time in redefining them later.
*/

function createPerson(name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function() {
    console.log(`Hi! I'm ${this.name}.`);
  }
  return obj;
}

var out = createPerson("erik");
out.introduceSelf();
