#/bin/sh
cd "$HOME/Documents/Learning/reverse"

/usr/local/Cellar/binutils/2.35.1/bin/readelf -all --dyn-syms -u -W -x .got -p .strtab cc/1.exe > output/1.exe.elf
/usr/local/Cellar/binutils/2.35.1/bin/readelf -all --dyn-syms -u -W -x .got -p .strtab cc/2.so > output/2.so.elf
/usr/local/Cellar/binutils/2.35.1/bin/readelf -all --dyn-syms -u -W -p .strtab cc/m.o > output/m.o.elf
/usr/local/Cellar/binutils/2.35.1/bin/readelf -all --dyn-syms -u -W -x .got -p .strtab cc/m > output/m.elf

/usr/local/Cellar/binutils/2.35.1/bin/objdump -d -x -T -t -r -w -z --sym cc/1.exe > output/1.exe.dump
/usr/local/Cellar/binutils/2.35.1/bin/objdump -d -x -T -t -r -w -z --sym cc/2.so > output/2.so.dump
/usr/local/Cellar/binutils/2.35.1/bin/objdump -d -x -t -r -w -z --sym cc/m.o > output/m.o.dump
/usr/local/Cellar/binutils/2.35.1/bin/objdump -d -x -T -t -r -w -z --sym cc/m > output/m.dump
