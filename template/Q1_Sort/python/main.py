import logic


def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sorted_array = logic.Logic().sort(array)
    # 結果出力
    [print(i) for i in sorted_array]


if __name__ == '__main__':
    main()
