import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\d":
        # for char in input_line:
        #     if not char.isdigit():
        #         return False
        # return True
        return any(char.isdigit() for char in input_line)  
    elif pattern == "\w":
        return any(char.isalnum() for char in input_line)
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == "^":
            return any(char not in pattern[2:-1] for char in input_line)
        return any(char in pattern[1:-1] for char in input_line)  
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
