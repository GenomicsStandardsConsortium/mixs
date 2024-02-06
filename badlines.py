import argparse
import re

def contains_special_characters(line):
    # Regular expression pattern to match any character other than letters, numbers, or whitespace
    pattern = r'[^-:;_a-zA-Z0-9\s\%\=\#\@\>\<\~\&\!\:\;\*\+\'\"\,\.\?\^\$\|\\\/\]\[\}\{\)\(]'
    return re.search(pattern, line)

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if contains_special_characters(line):
                print(line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for lines containing special characters.")
    parser.add_argument("file_path", help="Path to the input file")
    args = parser.parse_args()
    main(args.file_path)

