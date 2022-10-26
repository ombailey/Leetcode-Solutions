function lengthOfLongestSubstring(str) {
  let strings = [];
  let max = 0;
  let index = 1;
  for (let letter of str) {
    strings.push(letter);
    for (let i = index; i < str.length; i++) {
      while (strings.includes(letter) !== true) {
        strings.push(str[i]);
        i++;
      }
      console.log(strings);
    }
    if (strings.length > max) {
      max = strings.length;
    }
    strings = [];
    index++;
  }
  return max;
}

console.log(lengthOfLongestSubstring("pwwkew"));
