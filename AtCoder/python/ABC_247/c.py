# わからなかったので答えを見てコードを理解する
def S(n):
    if n == 1:
        return [1]
    else:
        print(S(n-1)+[n]+S(n-1))
        return n
        # return S(n - 1) + [n] + S(n - 1)


def main():
    # 入力値nの受け取り
    N = int(input())
    # S関数の戻り値を出力&S関数呼び出し

    print(*S(N))


main()
