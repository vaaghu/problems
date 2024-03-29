/*
Create a function, or show a built-in function, to count the number of non-overlapping occurrences of a substring inside a string.

The function should take two arguments:

the first argument being the string to search, and
the second a substring to be searched for.
It should return an integer count.

The matching should yield the highest number of non-overlapping matches.

In general, this essentially means matching from left-to-right or right-to-left */


function countSubstring(str, subStr) {
    for(let i =0;i<subStr.length;i++){
        if(!/[a-z,A-Z]/.test(subStr[i])){
            subStr = subStr.slice(0,i)+`[${subStr[i]}]`+subStr.slice(i+1,);
            i+=2;
        }
    }
    return str.match(new RegExp(subStr,"g")).length;
  }

  countSubstring("a*b*a*baba","a*")
