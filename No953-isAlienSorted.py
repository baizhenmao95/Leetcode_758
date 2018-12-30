# --coding: utf-8 --
'''
算法如下：
循环，依次取相邻两词进行比较，先判断两词是否完全相同，若是，则True，进入下一轮循环。
若否，则判断前一单词是否长于后一单词
    若是，则将两词转为列表形式，对应位置一一比较，找出第一个不同的字母，比较其序号
        序号由order转成的列表的索引获取。la > lb则False，反之则True
    若前一单词短于后一单词，则先假定True，再循环，若发现la > lb的情况，则修改标记

只要发现存在False的情况，就直接跳出最外的循环，return False

'''
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        len_words = len(words)
        lorder = list(order)
        for i in range(len_words-1):
            a = list(words[i])
            b = list(words[i+1])

            la = len(a)
            lb = len(b)
            flag_eq = 1
            flag_df = 0

            if a == b:  # 判断前后两单词是否完全一样，若否，则以长度分if
                flag_eq = 0
                flag_df = 0
            elif la > lb:
                for i in range(lb):
                    if a[i] == b[i]:
                        continue
                    else:
                        flag_eq = 0
                        order_a = lorder.index(a[i])
                        order_b = lorder.index(b[i])
                        if order_a > order_b:
                            flag_df = 1
                            break
            else:
                flag_eq = 0  # 如果a与b的前端完全相同则符合要求，若有不同则会进入else，此处flag_eq = 0 只是为了编程方便
                for i in range(la):
                    if a[i] == b[i]:
                        continue
                    else:
                        order_a = lorder.index(a[i])
                        order_b = lorder.index(b[i])
                        if order_a > order_b:
                            flag_df = 1
                        else:
                            flag_df = 0
                    break
            if (flag_eq + flag_df) > 0:
                break
        if (flag_eq + flag_df) > 0:
            return False
        else:
            return True

#         初版，只能解决不同首字母的问题
#         initial = []
#         intini = []
#         lorder = list(order)
#         i = 0
#         for word in words:
#             w = list(word)
#             initial.append(w[1])
#
#         for ini in initial:
#             intini.append(lorder.index(ini))
#             i += 1
#
#         li = len(intini)
# #        max = intini[li-1]  # 此处错误，应该遍历一次数组，看看中间项是否有最大值
#         flag = 0
#         for i in range(li-1):
#             if intini[i] > intini[i+1]:
#                 flag = 1
#                 break
#
#         if flag == 0:
#             return True
#         else:
#             return False



# 以下为自己测试的用例

# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"

# words = ["iekm","tpnhnbe"]
# order = "loxbzapnmstkhijfcuqdewyvrg"

# words = ["word","person","row"]
# order = "worldabcefghijkmnpqstuvxyz"

words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"
a = Solution()
print(a.isAlienSorted(words,order))
