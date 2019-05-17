/*
printing the pattern/pyramid of number
when input is three("3")
33333
32223
32123
32223
33333
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include <stdio.h>

int main() {
  int i, j, n, k;
  int nTP;
  for (i = n; i > 2; i--) {
    nTP = n;
    for (j = 1; j < n; j++) {
      // printf("%d ",nTP);
      if (nTP >= i) {
        nTP -= 1;
      }
      printf("%d ", nTP);
    }
    for (k = 2; k < n; k++) {
      if (nTP < k) {
        nTP += 1;
      }
      printf("%d ", nTP);
    }
    printf("\n");
  }
  for (i = 2; i <= n; i++) {
    nTP = n;
    for (j = 1; j < n; j++) {
      // printf("%d ",nTP);
      if (nTP >= i) {
        nTP -= 1;
      }
      printf("%d ", nTP);
    }
    for (k = 2; k < n; k++) {
      if (nTP < k) {
        nTP += 1;
      }
      printf("%d ", nTP);
    }
    printf("\n");
  }
  return 0;
}
