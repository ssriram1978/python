"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
k - starting row index
m - ending row index
l - starting column index
n - ending column index
i - iterator

while k < m && l < n:
/* Print the first row from the remaining rows */
/* Print the last column from the remaining columns */
/* Print the last row from the remaining rows */
/* Print the first column from the remaining columns */
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return None

        #define start and end of row and column
        row_start=0
        row_end=len(matrix)-1
        column_start=0
        column_end=len(matrix[0])-1
        start_of_each_element_in_row=0
        #define a temporary variable named index which will be used frequently.
        index=0
        #define a list where you will be storing all the elements
        spiralList=[]
        #start a while loop
        while row_start <= row_end and column_start <= column_end:
            #1. Accumulate all the elements in the current row.
            for index in range(column_start,column_end+1,+1):
                spiralList.append(matrix[row_start][index])
            row_start+=1
            #2. Accumulate all the end elements in each row.
            # move the start column index by 1.
            column_start+=1
            for index in range(row_start,row_end+1,+1):
                spiralList.append(matrix[index][column_end])
            column_end-=1
            #3. Traverse backwards at the end row and accumulate all the elements.
            for index in range(column_end,start_of_each_element_in_row-1,-1):
                spiralList.append(matrix[row_end][index])
            #4. Walk up traversing each row from the bottom and
            # accumulate all the elements found at the starting position.
            row_end-=1
            for index in range(row_end,row_start-1,-1):
                spiralList.append(matrix[index][start_of_each_element_in_row])
            start_of_each_element_in_row+=1

        return spiralList

sol=Solution()
#list=[[8,18],[7,17],[6,16],[5,19],[4,20],[3,21]]
#list2=sorted(list,key=lambda x:x[0])
#list3=sorted(list,key=lambda x:x[1])
#print(list2)
#print(list3)
matrix=[
 [1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15],
 [16,17,18,19,20],
 [21,22,23,24,25]
]
print(sol.spiralOrder(matrix))