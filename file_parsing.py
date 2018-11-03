def load_string(file_path):
    try:
        with open(file_path) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        print("[myScript] - Error: Could not open %s\n" % file_path)
        return -1


def parse_values(string_from_text):
    if not "00" in string_from_text:
        return string_from_text.split()
    else:
        raise ValueError('Someone has 100pts!')


def load_values(file_path):
    string_from_text = load_string(file_path)
    return parse_values(string_from_text)


