class Logic:
    # このファイルのみ提出してください
    # この中に解答を記述してください
    @staticmethod
    def sort(array):
        for i in range(1, len(array)):
            compair_num = array[i]  # 注目する要素の保持
            j = i - 1  # 比較対象の要素のindex
            while j >= 0 and array[j] > compair_num:  # 比較対象要素の方が大きい場合
                array[j + 1] = array[j]  # 右にシフト
                j -= 1  # 比較対象のインデックスを下げる
            array[j + 1] = compair_num  # 注目する要素の代入

        return array