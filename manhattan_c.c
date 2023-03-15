#include <stdio.h>

int main() {	
  
  	double x0, y0, x1, y1;
  	double dif_x, dif_y;
  	int distance;
  	
  	printf("PROGRAM MENGHITUNG JARAK MANHATTAN by FIKRI DEAN\n");

	printf("Insert x0 = ");
	scanf("%lf", &x0);
	
	printf("\nInsert y0 = ");
	scanf("%lf", &y0);
  
 	printf("\nInsert x1 = ");
	scanf("%lf", &x1);
  
    printf("\nInsert y1 = ");
	scanf("%lf", &y1);
	
	printf("\n\nx0 = %lf \n", x0);
	printf("y0 = %lf \n", y0);
	printf("x1 = %lf \n", x1);
	printf("y1 = %lf \n", y1);
	
	printf("\nCalculating... \n");
	
	dif_x = x1 - x0;
	dif_y = y1 - y0;
	
	if(dif_x < 0) {
		dif_x = - dif_x;
	}
	
	if(dif_y < 0) {
		dif_y = - dif_y;
	}
	
	printf("\n%lf \n", dif_x);
	printf("%lf \n", dif_y);
	
	distance = (int) dif_x + (int) dif_y;
	
	printf("\nHasil jarak Manhattan = %d", distance);
  
  	return 0;
}
