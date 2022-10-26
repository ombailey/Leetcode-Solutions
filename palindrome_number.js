function isPalindrome(number) {
  let result = number.toString().split("").reverse();
  result = parseInt(result.join(""));
  if (result === number) {
    return true;
  } else {
    return false;
  }
}
