import sys


def parse_input(lines):
    k = int(lines[0])
    values = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        values[parts[0]] = int(parts[1])
    A = lines[k + 1]
    B = lines[k + 2]
    return values, A, B


def hvlcs(values, A, B):
    m = len(A)
    n = len(B)

    # build dp table
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # traceback to find the actual subsequence
    result = []
    i = m
    j = n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return dp[m][n], ''.join(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 hvlcs.py <input_file>")
        return

    # for incorrect file name
    try:
        with open(sys.argv[1], 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
        sys.exit(1)

    values, A, B = parse_input(lines)
    max_val, subseq = hvlcs(values, A, B)
    print(max_val)
    print(subseq)


if __name__ == "__main__":
    main()