#include <stdio.h>
#include <string.h>
#include <locale.h>

#define N 50 

int main(){
	setlocale(LC_ALL,"portuguese");

	char s1[N] = {"May "};
        char s2[N] = {"team"};

	printf("str1: %s\n", s1);
        printf("str1: %s\n", s2);
	
	strcat(s1,s2);

	puts(s1);
}

