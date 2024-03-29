import pytest
from main import LFUCache as Solution 

def assert_unorderedList(result, expected):
  assert result == expected

def controller(operations,values):
  output = []
  solution = None
  for i in range(len(operations)):
    match operations[i]:
      case "LFUCache":
        solution = Solution(capacity=values[i][0])
        output.append(None)
      case "put":
        output.append(solution.put(key = values[i][0], value= values[i][1]))
      case "get":
        output.append(solution.get(key = values[i][0]))
  return output

# Test cases

def test_case_1():
  expected = [None,None,None,1,None,-1,3,None,-1,3,4]
  result = controller(operations=["LFUCache","put","put","get","put","get","get","put","get","get","get"],
                      values = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]] )
  assert_unorderedList(result, expected)

def test_case_2():
  expected = [None,None,None,2,1,2,None,None,-1,2,1,4]
  result = controller(operations = ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"],
                      values = [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]])
  assert_unorderedList(result, expected)
