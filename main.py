import sys
import random

if __name__ == "__main__":
    print(u"カードの枚数は何枚ですか？[半角数字、0より大きい自然数]")
    n = 0
    pn = 0
    try:
        n = int(input())
    except ValueError:
        print(u"半角数字で入力してください")
        exit()
    if n <= 0:
        print(u"0より大きい自然数で入力してください")
        exit()
    print(u"人数は何人ですか？[半角数字、0より大きく26以下自然数、カードの枚数以下]")
    try:
        pn = int(input())
    except ValueError:
        print(u"半角数字で入力してください")
        exit()
    if pn <= 0 or pn > 26 or pn > n:
        print(u"0より大きく26以下でカードの枚数以下の自然数を入力してください")
        exit()
    l = [x+1 for x in range(n)]
    random.shuffle(l)
    for i in range(pn):
        sys.stdout.write("{0}={1} ".format(chr(65+i), l[i]))