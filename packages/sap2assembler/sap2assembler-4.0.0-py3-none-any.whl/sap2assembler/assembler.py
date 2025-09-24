import re
import os

class Mnemonic:
    def __init__(self, name, num_bytes, opcode):
        self.name = name
        self.num_bytes = num_bytes
        self.opcode = opcode

class PseudoInstruction:
    def __init__(self, instruction):
        self.instruction = instruction

class Label:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Label({self.name}, {self.address})"

class Macro:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class AssemblerError(Exception):
    pass

def parse_ascii(text):
    return [format(ord(c), '08b') for c in text][1:-1]

def handle_macros(text: str) -> str:
    # 1. Extract all macros
    macro_pattern = re.compile(r'(\.macro\s+(\w+)\s*?\n.*?\.endmacro)', re.DOTALL)
    macros = {}

    # Find all macros and store their body
    for match in macro_pattern.finditer(text):
        full_block = match.group(1)
        name = match.group(2)
        body_lines = full_block.splitlines()[1:-1]  # skip .macro/.endmacro
        macros[name] = body_lines

        # 2. Delete the macro definition from text
        text = text.replace(full_block, '')

    # 3. Replace macro calls with their body
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped in macros:
            # Preserve indentation of the macro call
            indent = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
            expanded = [indent + l for l in macros[stripped]]
            # Replace the macro call line with the expanded body
            lines[i:i+1] = expanded
            i += len(expanded)  # skip over the newly inserted lines
        else:
            i += 1

    # Join back into a single string
    result = "\n".join(lines)
    return result


class SAP2Assembler:
    def __init__(self):
        self.mnemonics = {}
        self.pseudo_instructions = {}
        self.instructions_accepting_labels = []
        self.line_numbers_sanitized = {}
        self.num_address_bits = 16
        self.init_assembler_variables()
        self.assembled_bytes = [self.mnemonics["nop"].opcode for i in range(1<<self.num_address_bits)]
        self.address = 0
        self.labels = {}

    def init_assembler_variables(self):
        self.mnemonics = {
            'add b': Mnemonic('add b', 1, '10000000'),
            'add c': Mnemonic('add c', 1, '10000001'),
            'adi': Mnemonic('adi', 2, '11000110'),
            'ana b': Mnemonic('ana b', 1, '10100000'),
            'ana c': Mnemonic('ana c', 1, '10100001'),
            'ani': Mnemonic('ani', 2, '11100110'),
            'call': Mnemonic('call', 3, '11001101'),
            'cmp b': Mnemonic('cmp b', 1, '10111000'),
            'cmp c': Mnemonic('cmp c', 1, '10111001'),
            'cpi': Mnemonic('cpi', 2, '11111110'),
            'dcr a': Mnemonic('dcr a', 1, '00111101'),
            'dcr b': Mnemonic('dcr b', 1, '00000101'),
            'dcr c': Mnemonic('dcr c', 1, '00001101'),
            'hlt': Mnemonic('hlt', 1, '01110110'),
            'inr a': Mnemonic('inr a', 1, '00111100'),
            'inr b': Mnemonic('inr b', 1, '00000100'),
            'inr c': Mnemonic('inr c', 1, '00001100'),
            'in': Mnemonic('in', 2, '11011011'),
            'jmp': Mnemonic('jmp', 3, '11000011'),
            'jm': Mnemonic('jm', 3, '11111010'),
            'jnz': Mnemonic('jnz', 3, '11000010'),
            'jz': Mnemonic('jz', 3, '11001010'),
            'lda': Mnemonic('lda', 3, '00111010'),
            'mov a, b': Mnemonic('mov a, b', 1, '01111000'),
            'mov a, c': Mnemonic('mov a, c', 1, '01111001'),
            'mov b, a': Mnemonic('mov b, a', 1, '01000111'),
            'mov b, c': Mnemonic('mov b, c', 1, '01000001'),
            'mov c, a': Mnemonic('mov c, a', 1, '01001111'),
            'mov c, b': Mnemonic('mov c, b', 1, '01001000'),
            'mvi a': Mnemonic('mvi a', 2, '00111110'),
            'mvi b': Mnemonic('mvi b', 2, '00000110'),
            'mvi c': Mnemonic('mvi c', 2, '00001110'),
            'nop': Mnemonic('nop', 1, '00000000'),
            'ora b': Mnemonic('ora b', 1, '10110000'),
            'ora c': Mnemonic('ora c', 1, '10110001'),
            'ori': Mnemonic('ori', 2, '11110110'),
            'out': Mnemonic('out', 2, '11010011'),
            'ret': Mnemonic('ret', 1, '11001001'),
            'sta': Mnemonic('sta', 3, '00110010'),
            'sub b': Mnemonic('sub b', 1, '10010000'),
            'sub c': Mnemonic('sub c', 1, '10010001'),
            'sui': Mnemonic('sui', 2, '11010110'),
            'xra b': Mnemonic('xra b', 1, '10101000'),
            'xra c': Mnemonic('xra c', 1, '10101001'),
            'xri': Mnemonic('xri', 2, '11101110'),
        }

        self.pseudo_instructions = {'.org': PseudoInstruction(".org"),
                                    '.word': PseudoInstruction(".word"),
                                    '.byte': PseudoInstruction(".byte"),
                                    '.ascii': PseudoInstruction(".ascii"),}

        self.instructions_accepting_labels = ["jmp", "jm", "jnz", "jz", "call"]

    def sanitize_mnemonics(self):
        mnemonics = {}
        for mnemonic_name, mnemonic in self.mnemonics.items():
            mnemonics[mnemonic_name.replace(" ", "").replace("\t", "")] = mnemonic
        self.mnemonics = mnemonics

    def pad_assembled_bytes(self):
        n = (1 << self.num_address_bits)
        self.assembled_bytes += ["00000000"] * (n - len(self.assembled_bytes)) if len(self.assembled_bytes) < n else self.assembled_bytes[:n]

    def write_assembled_bytes(self, n_bytes, row, hex_output, file):
        content = ""
        for address in range(n_bytes):
            if not hex_output:
                if address % row == 0:
                    content += f"{hex(address)[2:].zfill(int(self.num_address_bits / 4))}: {self.assembled_bytes[address]}" + "" if address % n_bytes != n_bytes - 1 else "\n"
                    pass
                else:
                    content += f" {self.assembled_bytes[address]}" + ("" if address % row != row - 1 else "\n")

            else:
                if address % row == 0:
                    content += f"{hex(address)[2:].zfill(int(self.num_address_bits / 4))}: {hex(int(self.assembled_bytes[address], 2))[2:].zfill(2)}" + ("" if address % n_bytes != n_bytes - 1 else "\n")

                else:
                    content += f" {hex(int(self.assembled_bytes[address], 2))[2:].zfill(2)}" + ("" if address % row != row - 1 else "\n")

        with open(file, "w") as f:
            f.write(content)

    def print_assembled_bytes(self, n_bytes, row, hex_output):
        for address in range(n_bytes):
            if not hex_output:
                if address % row == 0:
                    print(f"{hex(address)[2:].zfill(int(self.num_address_bits / 4))}: {self.assembled_bytes[address]}", end="" if address % n_bytes != n_bytes-1 else "\n")
                    pass
                else:
                    print(f" {self.assembled_bytes[address]}", end="" if address % row != row-1 else "\n")

            else:
                if address % row == 0:
                    print(f"{hex(address)[2:].zfill(int(self.num_address_bits / 4))}: {hex(int(self.assembled_bytes[address], 2))[2:].zfill(2)}", end="" if address % n_bytes != n_bytes-1 else "\n")
                    pass
                else:
                    print(f" {hex(int(self.assembled_bytes[address], 2))[2:].zfill(2)}", end="" if address % row != row-1 else "\n")

    def increment_address(self, li, line):
        self.address += 1
        if self.address > (1<<self.num_address_bits) - 1:
            raise AssemblerError(f"Error in line {self.line_numbers_sanitized[li]}, ({line}), address exceeds {(1<<self.num_address_bits) - 1}")

    def add_bytes(self, bytes_to_add, li, line):
        for byte in bytes_to_add:
            self.assembled_bytes[self.address] = byte
            self.increment_address(li, line)

    def add_byte(self, byte, li, line):
        self.assembled_bytes[self.address] = byte
        self.increment_address(li, line)

    def jump_to(self, address_bytes, li, line):
        address = "".join(address_bytes[::-1])
        address = int(address, 2)
        self.address = address - 1
        self.increment_address(li, line)

    def sanitize_lines(self, lines):
        line_number = 0
        sanitized_lines = []

        string_pattern = re.compile(r'(["\'])(?:\\.|(?!\1).)*\1')  # matches "..." or '...' including escaped quotes
        include_pattern = re.compile(r'\.include\s*<([^>]+)>')

        comment_free_lines = []
        for line in lines:
            if line.startswith(";"):
                print()
                continue
            comment_free_lines.append(line)

        lines = comment_free_lines
        # --- expand includes first ---
        while True:
            new_lines = []
            modified = False

            for line in lines:
                match = include_pattern.search(line)
                if match:
                    filename = match.group(1)
                    if not os.path.exists(filename):
                        raise FileNotFoundError(f"Included file '{filename}' not found.")

                    with open(filename, "r") as f:
                        file_contents = f.read().splitlines()

                    # Insert included file contents in place of the .include line
                    new_lines.extend(file_contents)
                    modified = True
                else:
                    new_lines.append(line)

            lines = new_lines
            if not modified:  # stop if no more .include left
                break


        # run macros AFTER includes
        lines = handle_macros("\n".join(lines)).split("\n")

        for idx, line in enumerate(lines):
            def remove_outside_strings(s):
                result = []
                last_end = 0
                for m in string_pattern.finditer(s):
                    result.append(s[last_end:m.start()].replace(" ", "").replace("\t", ""))
                    result.append(m.group())
                    last_end = m.end()
                result.append(s[last_end:].replace(" ", "").replace("\t", ""))
                return ''.join(result)

            stripped_line = remove_outside_strings(line)

            if stripped_line != "":
                self.line_numbers_sanitized[line_number] = idx
                line_number += 1
                sanitized_lines.append(stripped_line.lower())

        return sanitized_lines

    def parse_operand(self, operand, li, mnemonic_name, line):
        for label_name, label in self.labels.items():
            if operand.startswith(label_name):
                if mnemonic_name not in self.instructions_accepting_labels:
                    raise AssemblerError(f"Error in line {self.line_numbers_sanitized[li]}, ({line}), mnemonic {mnemonic_name} doesn't accept labels as operands.")
                operand = "$" + label.address
        if operand.startswith("#"):
            operand = operand[1:]
            if not set(operand) <= {"0", "1"}:
                raise AssemblerError(f"Invalid operand {operand} on line {self.line_numbers_sanitized[li]}, ({line}), # must only contain binary.")
            operand = operand.rjust((len(operand)+7)//8*8, "0")
            operand_bytes = [operand[max(i-8, 0):i] for i in range(len(operand), 0, -8)]
            return operand_bytes
        elif operand.startswith("$"):
            operand = operand[1:]
            try:
                hex_operand = operand
                operand = int(operand, 16)
                if len(hex_operand) % 2:
                    hex_operand = "0" + hex_operand
                bytes_list = [int(hex_operand[i:i+2], 16) for i in range(0, len(hex_operand), 2)]
                bytes_list.reverse()
                return [f"{byte:08b}" for byte in bytes_list]
            except ValueError:
                raise AssemblerError(f"Invalid operand {operand} on line {self.line_numbers_sanitized[li]}, ({line}), $ must only contain hex.")

        return None

    def resolve_labels(self, lines):
        address = 0
        for li, line in enumerate(lines):
            if ":" in line:
                label = line.split(":")[0].strip()
                self.labels[label] = Label(label, hex(address)[2:].zfill(int(self.num_address_bits / 4)))
                address += 1

            else:
                for mnemonic_name, mnemonic in self.mnemonics.items():
                    if line.startswith(mnemonic_name):
                        address += mnemonic.num_bytes
                        break

                for pseudo_instruction in self.pseudo_instructions:
                    if line.startswith(pseudo_instruction):
                        if pseudo_instruction == ".org":
                            address = self.parse_operand(line.split(".org")[1], li, ".org", line)
                            address = "".join(address[::-1])
                            address = int(address, 2)

                        elif pseudo_instruction == ".word":
                            address += 2

                        elif pseudo_instruction == ".byte":
                            address += 1

                        elif pseudo_instruction == ".ascii":
                            ascii_bytes = parse_ascii(line.split(".ascii")[1])
                            address += len(ascii_bytes)
                        break

    def assemble(self, text, file_to_write=None, print_output=False, n_bytes=256, row=8, hex_output=True):
        self.address = 0
        self.assembled_bytes = [self.mnemonics["nop"].opcode for i in range(1<<self.num_address_bits)]
        self.sanitize_mnemonics()
        lines = text.split("\n")
        lines = self.sanitize_lines(lines)
        self.resolve_labels(lines)
        for li, line in enumerate(lines):
            found_label = False
            found_pseudo_instruction = False
            for mnemonic_name, mnemonic in self.mnemonics.items():
                for label in self.labels:
                    if line.startswith(label) and ":" in line:
                        found_label = True
                        break
                    elif line.startswith(label) and not ":" in line:
                        raise AssemblerError(f"Error in line {self.line_numbers_sanitized[li]}, ({line}), label {label} cannot be called.")

                if found_label:
                    break

                for pseudo_instruction in self.pseudo_instructions:
                    if line.startswith(pseudo_instruction):
                        if pseudo_instruction == ".org":
                            address = self.parse_operand(line.split(".org")[1], li, ".org", line)
                            self.jump_to(address, li, line)
                            found_pseudo_instruction = True

                        elif pseudo_instruction == ".word":
                            operand = self.parse_operand(line.split(".word")[1], li, ".word", line)
                            if len(operand) > 2:
                                raise AssemblerError(f"Error in line {self.line_numbers_sanitized[li]}, ({line}), .word takes 2 bytes.")
                            self.add_bytes(operand, li, line)
                            found_pseudo_instruction = True

                        elif pseudo_instruction == ".byte":
                            operand = self.parse_operand(line.split(".byte")[1], li, ".byte", line)
                            if len(operand) > 1:
                                raise AssemblerError(f"Error in line {self.line_numbers_sanitized[li]}, .byte takes 1 byte.")
                            self.add_bytes(operand, li, line)
                            found_pseudo_instruction = True

                        elif pseudo_instruction == ".ascii":
                            text = line.split(".ascii")[1]
                            ascii_bytes = parse_ascii(text)
                            self.add_bytes(ascii_bytes, li, line)
                            found_pseudo_instruction = True

                if found_pseudo_instruction:
                    break

                if line.startswith(mnemonic_name):
                    self.add_byte(mnemonic.opcode, li, line)
                    if mnemonic.num_bytes != 1 and line.replace(mnemonic_name, "") != "":
                        operand = line.replace(mnemonic_name, "")
                        operand_bytes = self.parse_operand(operand, li, mnemonic_name, line)
                        if len(operand_bytes) != mnemonic.num_bytes-1:
                            raise AssemblerError(f"Error on line {self.line_numbers_sanitized[li]}, ({line}), operand must be {mnemonic.num_bytes-1} bytes")
                        self.assembled_bytes += operand_bytes
                        self.add_bytes(operand_bytes, li, line)

                    elif mnemonic.num_bytes != 1 and line.replace(mnemonic_name, "") == "":
                        raise AssemblerError(f"Error on line {self.line_numbers_sanitized[li]}, ({line}), mnemonic {mnemonic.name} takes an operand of "
                                             f"{mnemonic.num_bytes-1} bytes but none were given.")

                    elif mnemonic.num_bytes == 1 and line.replace(mnemonic_name, "") != "":
                        raise AssemblerError(f"Error on line {self.line_numbers_sanitized[li]}, ({line}), mnemonic {mnemonic.name} does not take an operand.")

                    break

        self.pad_assembled_bytes()
        if print_output:
            self.print_assembled_bytes(n_bytes, row, hex_output)

        if file_to_write is not None:
            self.write_assembled_bytes(n_bytes, row, hex_output, file_to_write)

    def assemble_from_file(self, file_to_assemble, file_to_write=None, print_output=False, n_bytes=256, row=8, hex_output=True):
        with open(file_to_assemble, "r") as f:
            content = f.read()

        self.assemble(content, file_to_write=file_to_write, print_output=print_output, n_bytes=n_bytes, row=row, hex_output=hex_output)
