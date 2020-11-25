#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) /* 带参数形式 */
{
    printf("******************** ./crackme xxxxxx  ********************\n");
    if (argc == 1) {
    	printf("please input password!!!\n");
    	return -1;
    } else if (argc != 2) {
    	printf("only need one parameter\n");
    	return -1;
    }
    char a = 'A';
    char b = 'c';
    char c = '1';

    if (strlen(argv[1]) != 3) {
    	printf("wrong password\n");
    	return -1;
    }
    if (argv[1][0] != a || argv[1][1] != b || argv[1][2] != c) {
    	printf("wrong password\n");
	return -1;
    }
    printf("pass, Let's celebrate\n");

    return 0;
}
