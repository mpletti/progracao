#include <stdio.h>
#include <string.h>
#include <locale.h>

#define N 50 

int main(){
	setlocale(LC_ALL,"portuguese");

	char hardtext[N] = {"maick1090"};
	char senha_usr[N];
	int ok;

	printf("Digite:\n");
	gets(senha_usr);

	ok = strcmp(hardtext, senha_usr);

	if(ok == 0)
	    printf("Correto\n");
	else
	    printf("Incorreto\n");

}




