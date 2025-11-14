class IntegerNFA:
    def __init__(self):
        # State definitions for combined NFA
        self.transitions = {
            'start': {
                '0': ['zero'],
                '1': ['dec'], '2': ['dec'], '3': ['dec'], '4': ['dec'],
                '5': ['dec'], '6': ['dec'], '7': ['dec'], '8': ['dec'], '9': ['dec']
            },
            'zero': {
                '0': ['zero'],  # Allow multiple leading zeros
                'o': ['oct_prefix'], 'O': ['oct_prefix'],
                'x': ['hex_prefix'], 'X': ['hex_prefix']
            },
            'dec': {
                '0': ['dec'], '1': ['dec'], '2': ['dec'], '3': ['dec'], '4': ['dec'],
                '5': ['dec'], '6': ['dec'], '7': ['dec'], '8': ['dec'], '9': ['dec']
            },
            'oct_prefix': {
                '0': ['oct'], '1': ['oct'], '2': ['oct'], '3': ['oct'],
                '4': ['oct'], '5': ['oct'], '6': ['oct'], '7': ['oct']
            },
            'oct': {
                '0': ['oct'], '1': ['oct'], '2': ['oct'], '3': ['oct'],
                '4': ['oct'], '5': ['oct'], '6': ['oct'], '7': ['oct']
            },
            'hex_prefix': {
                '0': ['hex'], '1': ['hex'], '2': ['hex'], '3': ['hex'], '4': ['hex'],
                '5': ['hex'], '6': ['hex'], '7': ['hex'], '8': ['hex'], '9': ['hex'],
                'a': ['hex'], 'b': ['hex'], 'c': ['hex'], 'd': ['hex'], 'e': ['hex'], 'f': ['hex'],
                'A': ['hex'], 'B': ['hex'], 'C': ['hex'], 'D': ['hex'], 'E': ['hex'], 'F': ['hex']
            },
            'hex': {
                '0': ['hex'], '1': ['hex'], '2': ['hex'], '3': ['hex'], '4': ['hex'],
                '5': ['hex'], '6': ['hex'], '7': ['hex'], '8': ['hex'], '9': ['hex'],
                'a': ['hex'], 'b': ['hex'], 'c': ['hex'], 'd': ['hex'], 'e': ['hex'], 'f': ['hex'],
                'A': ['hex'], 'B': ['hex'], 'C': ['hex'], 'D': ['hex'], 'E': ['hex'], 'F': ['hex']
            }
        }

        self.accept_states = {'zero', 'dec', 'oct', 'hex'}
        self.start_state = 'start'

    def recognize(self, input_string):

       # Check if valid Python string literal

        if not input_string:
            return False, None

        current_states = {self.start_state}

        for char in input_string:
            next_states = set()
            for state in current_states:
                if state in self.transitions and char in self.transitions[state]:
                    next_states.update(self.transitions[state][char])

            if not next_states:
                return False, None

            current_states = next_states

        # Check if any final state is an accept state
        accepted_states = current_states.intersection(self.accept_states)
        if accepted_states:
            # Checks type of integer
            if 'hex' in accepted_states:
                return True, 'hexinteger'
            elif 'oct' in accepted_states:
                return True, 'octinteger'
            elif 'dec' in accepted_states or 'zero' in accepted_states:
                return True, 'decinteger'

        return False, None


def process_test_file(input_filename, output_filename):
    """
    Process test file in format: "input_string expected_result"
    Write results to output file with pass/fail indication
    """
    nfa = IntegerNFA()

    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        outfile.write("Input\tExpected\tActual\tType\tResult\n")
        outfile.write("=" * 70 + "\n")

        for line in infile:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Parse input: "string expected_result"
            parts = line.split()
            if len(parts) < 2:
                continue

            test_input = parts[0]
            expected = parts[1].lower()  # 'accept' or 'reject'

            is_valid, literal_type = nfa.recognize(test_input)
            actual = 'accept' if is_valid else 'reject'
            result = 'PASS' if actual == expected else 'FAIL'

            type_str = literal_type if literal_type else 'N/A'

            outfile.write(f"{test_input}\t{expected}\t{actual}\t{type_str}\t{result}\n")


def interactive_mode():
    """
    Interactive mode for testing individual strings
    """
    nfa = IntegerNFA()
    print("Python Integer Literal Recognizer")
    print("=" * 50)
    print("Recognizes: decinteger, octinteger, hexinteger")
    print("Enter 'quit' to exit\n")

    while True:
        user_input = input("Enter a string to test: ").strip()

        if user_input.lower() == 'quit':
            break

        is_valid, literal_type = nfa.recognize(user_input)

        if is_valid:
            print(f"✓ ACCEPT - Valid {literal_type}")
        else:
            print(f"✗ REJECT - Not a valid integer literal")
        print()


def main():
    import sys

    if len(sys.argv) > 1:
        # File-based testing mode
        input_file = sys.argv[1] if len(sys.argv) > 1 else 'in_ans.txt'
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'out.txt'

        print(f"Processing test file: {input_file}")
        print(f"Writing results to: {output_file}")

        try:
            process_test_file(input_file, output_file)
            print("Testing complete!")
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            print("\nSwitching to interactive mode...")
            interactive_mode()
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()