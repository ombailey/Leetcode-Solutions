const isPalindrome = (string) => {
  string = string.replace(/[^a-zA-Z0-9]/gi, "").toLowerCase();
  let reverse = string.split("").reverse().join("");
  return reverse === string;
};

console.log(isPalindrome("ab_a"));
