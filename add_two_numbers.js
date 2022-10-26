let l1 = [2, 4, 3];
let l2 = [5, 6, 4];

function addTwoNumbers(list1, list2) {
  list1 = parseInt(list1.map((number) => number.toString()).join(""));
  list2 = parseInt(list2.map((number) => number.toString()).join(""));
  list3 = (list1 + list2).toString();
  result = [];
  for (number of list3) {
    result.unshift(parseInt(number));
  }
  return result;
}

console.log(addTwoNumbers(l1, l2));
