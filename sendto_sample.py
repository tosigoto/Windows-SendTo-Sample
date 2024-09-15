import sys


def main(path_list):
    imax = len(path_list)
    for i, path in enumerate(path_list, 1):
        print(f"[path {i} / {imax}]: {path}")


if __name__ == "__main__":
    print("-" * 20)
    print("Windows-SendTo-Sample")
    print("-" * 20)

    main(sys.argv[1:])

    print("End")
