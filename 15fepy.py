～ジェネレータは何に使うか～

ジェネレータの一番の使い道はメモリ使用量を減らすことです

例

import sys

a=[i for i in range(100000)]

ジェネレータ使うとき

def num(max):

   i=0

   whike i<max

   yield i

  i++

   for i in num(10):

     print(i)

(配列でメモリ使用量多く使うのでジェネレータ使ったほうがいい）

print(sys.getsizeof(a))#aのメモリ使用量(4000000)

gen=num(100000)

print(sys.getsizeof(gen))#genのメモリ使用量(10)

