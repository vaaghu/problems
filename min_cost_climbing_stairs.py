# https://leetcode.com/problems/min-cost-climbing-stairs
class Node:
  def __init__(self,cost):
    self.stepOne = None
    self.stepTwo = None
    self.cost = cost or 0
  def __str__(self):
    return f" {self.stepOne and self.stepOne.cost }<{self.cost}>{self.stepTwo and self.stepTwo.cost} "
minCost = 0
def minCostClimbingStairs(cost):
  cost = cost + [0]
  print(cost)
  temp = Node(0)
  minCost = -1
  def add(temp,index,minCost):
    if (index>=len(cost)):
      # print(index, temp.cost)
      return temp.cost if minCost == -1 or minCost > temp.cost else minCost
    tempCost2 = None
    
    temp.stepOne = Node(cost[index]+temp.cost)
    if minCost == -1 or minCost >= (cost[index]+temp.cost):
      tempCost = add(temp.stepOne,index+1,minCost)
    else:
      tempCost = minCost
    if index+1 < len(cost):
      if tempCost >= (cost[index+1]+temp.cost):
        temp.stepTwo = Node(cost[index+1]+temp.cost)
        tempCost2 = add(temp.stepTwo,index+2,tempCost)
    print(tempCost,tempCost2,minCost,"cost")
    if tempCost2 != None and tempCost2 < tempCost:
      tempCost = tempCost2
    
    if tempCost < minCost or minCost == -1:
      minCost = tempCost

    print(index,temp,minCost)
    return minCost
  
  minCost = add(temp,0,minCost)
  print("\n",minCost)
  return minCost
minCostClimbingStairs([1,100,1,1,100,1,100])
minCostClimbingStairs([10,15,20,0])
# minCostClimbingStairs([841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275,259,872,630,965,978,109,56,523,851,887,91,544,598,963,305,481,959,560,454,883,50,216,732,572,511,156,177,831,122,667,548,978,771,880,922,777,990,498,525,317,469,151,874,202,519,139,670,341,514,469,858,913,94,849,839,813,664,163,3,802,21,634,944,901,446,186,843,742,330,610,932,614,625,169,833,4,81,55,124,294,71,24,929,534,621,543,417,534,427,327,179,90,341,949,368,692,646,290,488,145,273,617,596,82,538,751,80,616,763,826,932,184,630,478,163,925,259,237,839,602,60,786,603,413,816,278,4,35,243,64,631,405,23,638,618,829,481,877,756,482,999,973,718,157,262,752,931,882,741,40,77,535,542,879,607,879,321,46,210,116,244,830,591,285,382,925,48,497,913,203,239,696,162,623,291,525,950,27,546,293,108,577,672,354,256,3,671,998,22,989,557,424,251,923,542,243,46,488,80,374,372,334,190,817,150,742,362,196,75,193,162,645,859,758,433,903,199,289,175,303,475,818,213,576,181,668,243,297,572,549,840,161,292,719,226,338,981,345,203,655,210,65,111,746,76,935,406,646,976,567,32,726,638,674,727,861,426,297,349,464,973,341,452,826,223,805,940,458,468,967,107,345,987,553,407,916,103,324,367,864,74,946,712,596,105,194,79,634,855,703,70,170,543,208,739,632,663,880,857,824,258,743,488,659,647,470,958,492,211,927,356,488,744,570,143,674,502,589,270,80,6,463,506,556,495,713,407,229,689,280,162,454,757,565,267,575,417,948,607,269,852,938,560,24,222,580,604,800,628,487,485,615,796,384,555,226,412,445,503,810,949,966,28,768,83,213,883,963,831,390,951,378,497,440,780,209,734,290,96,398,146,56,445,880,910,858,671,164,552,686,748,738,837,556,710,787,343,137,298,685,909,828,499,816,538,604,652,7,272,729,529,343,443,593,992,434,588,936,261,873,64,177,827,172,712,628,609,328,672,376,628,441,9,92,525,222,654,699,134,506,934,178,270,770,994,158,653,199,833,802,553,399,366,818,523,447,420,957,669,267,118,535,971,180,469,768,184,321,712,167,867,12,660,283,813,498,192,740,696,421,504,795,894,724,562,234,110,88,100,408,104,864,473,59,474,922,759,720,69,490,540,962,461,324,453,91,173,870,470,292,394,771,161,777,287,560,532,339,301,90,411,387,59,67,828,775,882,677,9,393,128,910,630,396,77,321,642,568,817,222,902,680,596,359,639,189,436,648,825,46,699,967,202,954,680,251,455,420,599,20,894,224,47,266,644,943,808,653,563,351,709,116,849,38,870,852,333,829,306,881,203,660,266,540,510,748,840,821,199,250,253,279,672,472,707,921,582,713,900,137,70,912,51,250,188,967,14,608,30,541,424,813,343,297,346,27,774,549,931,141,81,120,342,288,332,967,768,178,230,378,800,408,272,596,560,942,612,910,743,461,425,878,254,929,780,641,657,279,160,184,585,651,204,353,454,536,185,550,428,125,889,436,906,99,942,355,666,746,964,936,661,515,978,492,836,468,867,422,879,92,438,802,276,805,832,649,572,638,43,971,974,804,66,100,792,878,469,585,254,630,309,172,361,906,628,219,534,617,95,190,541,93,477,933,328,984,117,678,746,296,232,240,532,643,901,982,342,918,884,62,68,835,173,493,252,382,862,672,803,803,873,24,431,580,257,457,519,388,218,970,691,287,486,274,942,184,817,405,575,369,591,713,158,264,826,870,561,450,419,606,925,710,758,151,533,405,946,285,86,346,685,153,834,625,745,925,281,805,99,891,122,102,874,491,64,277,277,840,657,443,492,880,925,65,880,393,504,736,340,64,330,318,703,949,950,887,956,39,595,764,176,371,215,601,435,249,86,761,793,201,54,189,451,179,849,760,689,539,453,450,404,852,709,313,529,666,545,399,808,290,848,129,352,846,2,266,777,286,22,898,81,299,786,949,435,434,695,298,402,532,177,399,458,528,672,882,90,547,690,935,424,516,390,346,702,781,644,794,420,116,24,919,467,543,58,938,217,502,169,457,723,122,158,188,109,868,311,708,8,893,853,376,359,223,654,895,877,709,940,195,323,64,51,807,510,170,508,155,724,784,603,67,316,217,148,972,19,658,5,762,618,744,534,956,703,434,302,541,997,214,429,961,648,774,244,684,218,49,729,990,521,948,317,847,76,566,415,874,399,613,816,613,467,191])