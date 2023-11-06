#include <stdio.h>
#include <string.h>
#include <locale.h>

#define N 50 

int main(){
	setlocale(LC_ALL,"portuguese");

	char s[N];
	int i;
	
	printf("Seus dados:\n");
	gets(s);
	i = strlen(s);
	printf("\nTexto:%d\n\n", i);

	printf("Conteudo:\n");

	puts(s);

}

































