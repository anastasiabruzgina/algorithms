from random import randint

n = int(input('количество цифр в первом массиве: '))
m = int(input('количество цифр во втором массиве: '))

first = [randint(1, n) for i in range(1, n + 1)]
second = [randint(1, m) for i in range(1, m + 1)]

def medians(nums1, nums2=[]):
    massive = sorted(nums1 + nums2)
    if len(massive) % 2 == 1:
        return massive[len(massive) // 2]
    else:
        return (0.5 * (massive[len(massive) // 2 - 1] + massive[len(massive) // 2]))
    
medians(first, second)

def test():
    nums1 = [1, 3]
    nums2 = [2]
    result = 2
    if medians(nums1, nums2) == result:
        print('Первый тест пройден')
    else:
        print('Первый тест завален')
       
    nums3 = [1,2]
    nums4 = [3,4]
    result2 = 2.5
    if medians(nums3, nums4) == result2:
        print('Второй тест пройден')
    else:
        print('Второй тест завален')
     
    nums5 = [0, 0]
    nums6 = [0, 0]
    result3 = 0
    if medians(nums5, nums6) == result3:
        print('Третий тест пройден')
    else:
        print('Третий тест завален')
         
    nums3 = [0, 0]
    nums4 = [0, 0]
    result2 = 0
    if medians(nums3, nums4) == result2:
        print('Четвертый тест пройден')
    else:
        print('Четвертый тест завален')
          
    nums3 = [0, 0]
    nums4 = [0, 0]
    result2 = 0
    if medians(nums3, nums4) == result2:
        print('Пятый тест пройден')
    else:
        print('Пятый тест завален')
