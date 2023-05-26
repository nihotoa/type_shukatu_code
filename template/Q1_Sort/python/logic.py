class Logic:
    # このファイルのみ提出してください
    # この中に解答を記述してください
    @staticmethod
    def sort(array):
        n = len(array)
        for i in range(n): #fixされた数
            for j in range(0, n - i - 1): #操作を行う回数分ループ
                focus_index = -(j+1)
                if array[focus_index-1] > array[focus_index]: #右の要素が小さい時
                    array[focus_index-1], array[focus_index] = array[focus_index], array[focus_index-1] #入れ替え

        return array