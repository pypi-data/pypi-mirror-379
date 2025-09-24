
import argparse
from sap2assembler import SAP2Assembler

__version__ = "4.0.0"

def main():
    parser = argparse.ArgumentParser(
        prog="sap2assembler",
        description="SAP-2 Assembler CLI"
    )

    # Options
    parser.add_argument("-a", metavar="file", help="Specify the input assembly file to assemble")
    parser.add_argument("-o", metavar="file", help="Specify the output file to write machine code", default=None)
    parser.add_argument("-rw", metavar="width", type=int, default=16, help="Set the row width for output (default is 16)")
    parser.add_argument("-b", metavar="bytes", type=int, default=256, help="Set the number of bytes to write to the file or print (default is 256)")
    parser.add_argument("-p", action="store_true", help="Print the assembled data to the console")
    parser.add_argument("-hd", action="store_true", help="Output data in hex format (instead of binary)")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--version-info", action="store_true", help="Show version info")

    args = parser.parse_args()

    fileToWrite = args.o if args.o else None
    fileToAssemble = args.a if args.a else ""
    row_width = args.rw
    print_data = args.p
    hex_data = args.hd
    n_bytes = args.b

    if not fileToAssemble and not args.version and not args.version_info:
        return print("type 'sap2assembler -h' for help")

    if args.version:
        return print(__version__)

    if args.version_info:
        return print("Efficiency Update.")

    assembler = SAP2Assembler()
    assembler.assemble_from_file(
        fileToAssemble,
        fileToWrite,
        print_data,
        n_bytes,
        row_width,
        hex_data
    )

    return None
