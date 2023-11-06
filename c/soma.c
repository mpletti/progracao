#include <stdio.h> 



int main(){
	int a, b, soma, subtr, mult, divis;

	printf("valor 1: \n");
	scanf("%d", &a);
	printf("valor 2: \n");
	scanf("%d", &b);

	soma = a + b;
	subtr = a - b;
	mult = a * b;
	divis = a / b;

	printf("Resultados:\n");
	printf("soma: %d.\n", soma);
        printf("sub: %d.\n", subtr);
        printf("mult: %d.\n", mult);
        printf("div: %d.\n", divis);
}
