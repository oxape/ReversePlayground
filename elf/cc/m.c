//#include <stdio.h>
extern int haha(int a);
const int sxx = 0x5b;
int axx = 123;
int ccc;
int main() {
	int tmp = axx+sxx;
	ccc = haha(tmp);
	//printf("c = %d\n", ccc);
	return ccc;
}
