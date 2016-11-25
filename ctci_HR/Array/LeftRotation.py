def array_left_rotation(a, n, k):
    b = []
    for i in range(0,n,1):
        j = (i+k)%n
        b.append(a[j])
    return b
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))