import sys
import utils.json_fns as fns
import utils.input as input


def main():
    if len(sys.argv) > 1:
        operation = sys.argv[1:][0]
        match operation:
            case 'read':
                fns.read_from_json()
            case 'write':
                msg = input.get_input()
                fns.write_to_json(msg)
    else:
        print("no operator")

