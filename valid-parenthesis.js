const isValid = (string) => {
  let s = [];
  let output = true;
  let index = 0;
  let opens = "([{";
  let closes = ")]}";

  while (index < string.length && output) {
    let sym = string[index];
    if (opens.includes(sym)) {
      s.push(sym);
    } else {
      if (s.length === 0) {
        output = false;
      } else {
        let top = s.pop();
        if (opens.indexOf(top) != closes.indexOf(sym)) {
          output = false;
        }
      }
    }
    index++;
  }

  if (output && s.length === 0) {
    return true;
  } else {
    return false;
  }
};

console.log(isValid("({[})"));
