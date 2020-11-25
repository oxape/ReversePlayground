#-------------------------------------------------------------------------------
# elftools example: elf_low_high_api.py
#
# A simple example that shows some usage of the low-level API pyelftools
# provides versus the high-level API while inspecting an ELF file's symbol
# table.
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
from __future__ import print_function
import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection, StringTableSection, SymbolTableIndexSection
from elftools.elf.sections import SUNWSyminfoTableSection, NoteSection, StabSection
from elftools.elf.dynamic import DynamicSection, DynamicTag

# If pyelftools is not installed, the example can also run from the root or
# examples/ dir of the source distribution.
sys.path[0:0] = ['.', '..']


def process_file(filename):
    print('Processing file:', filename)
    with open(filename, 'rb') as f:
        #.symtab #.dynsym #.strtab
        allsection_info_highlevel(f)
        # section_info_by_name(f, '.dynsym')
        # section_info_by_name(f, '.strtab')


def allsection_info_highlevel(stream):
    print('High level API...')
    elffile = ELFFile(stream)

    # Just use the public methods of ELFFile to get what we need
    # Note that section names are strings.
    num = elffile.num_sections()
    print('  %s sections' % num)
    for i in range(num):
        section = elffile.get_section(i)
        section_info_highlevel(section)


def section_info_by_name(stream, section_name):
    elffile = ELFFile(stream)
    section = elffile.get_section_by_name(section_name)
    section_info_highlevel(section)


def section_info_highlevel(section):
    if not section:
        print('  No symbol table found. Perhaps this ELF has been stripped?')
        return

    # A section type is in its header, but the name was decoded and placed in
    # a public attribute.
    print('  Section name: %s, type: %s, offset: %08x' %(
        section.name, section['sh_type'], section['sh_offset']))

    # But there's more... If this section is a symbol table section (which is
    # the case in the sample ELF file that comes with the examples), we can
    # get some more information about it.
    if isinstance(section, SymbolTableSection):
        num_symbols = section.num_symbols()
        print("  It's a symbol section with %s symbols" % num_symbols)
        for i in range(num_symbols):
            symbol = section.get_symbol(i)
            name = 'NULL'
            if len(symbol.name) > 0:
                name = symbol.name
            print("  The name of the symbol in the section is: %s index: %d" % (name, symbol['st_name']))
            print("                                                 shndx:%s vale:%08x size:%08x %s" % (
                symbol['st_shndx'], symbol['st_value'], symbol['st_size'], str(symbol['st_info'])))
    elif isinstance(section, StringTableSection):
        size = section['sh_size']
        offset = 0
        index = 0
        while True:
            value = section.get_string(offset)
            print("  index:%03d offset:%04d %s" % (index, offset, value))
            bytes_array = value.encode('utf-8')
            index += 1
            offset += len(bytes_array)+1
            if offset >= size:
                break
    elif isinstance(section, SymbolTableIndexSection):
        print('SymbolTableIndexSection')
    elif isinstance(section, SUNWSyminfoTableSection):
        print('SUNWSyminfoTableSection')
    elif isinstance(section, NoteSection):
        print('NoteSection')
    elif isinstance(section, StabSection):
        print('StabSection')
    elif isinstance(section, DynamicSection):
        num_tag = section.num_tags()
        print("  It's a dynamic section with %s tags" % num_tag)
        for i in range(num_tag):
            tag = section.get_tag(i)
            print("     %s" % str(tag))
    else:
        print(section.data().hex())


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        process_file(filename)
