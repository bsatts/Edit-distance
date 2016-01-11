import os
import sys

def edit_distance(s1, s2):
    """
    Computes the edit distance between string s1 and s2
    """
    if len(s1) < len(s2):
        return edit_distance(s2, s1)
    m = len(s1)
    n = len(s2)
    #Initialize dynamic programming matrix
    d = [[0 for _ in range(n+1)] for _ in range(m+1)]

    #Cost for prefixes of s1 being reduced to ""
    for i in range(1, m+1):
        d[i][0] = i

    #Costs for prefixes of s2 being reduced to ""
    for i in range(1, n+1):
        d[0][i] = i

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s1[i-1] == s2[j-1]:   #No edit
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1, #deletion
                              d[i][j-1] + 1, #insertion
                              d[i-1][j-1] + 1) #substitution)
    return d[m][n]
 

def main():
    s1 = "Levenshtein"
    s2 = "Levenshten"
    print edit_distance(s1, s2)







if __name__ == '__main__':
    main()