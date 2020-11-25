class axx{
	public:
	int a{10};
	axx(int a):a(a){}; 
	template<typename T> T foo(T b, T c) {
    		return b+c;
	}
};
static axx ss(0x5a);
int main(int argc, char **argv) {
	if (argc != 10) {
		axx *x = new axx(5);
		int b=10;
		int c=15;
		x->foo(b, c);
	}
	return 0;
}
