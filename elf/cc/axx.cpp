class axx{
        public:
        int a{10};
        axx(int a):a(a){};
        template<typename T> T foo(T b, T c) {
                return b+c;
        }
};

int ad(int d) {
	axx *x = new axx(1);
	return x->foo(d, 1);
}
