import redis
r = redis.Redis(host='localhost', port=6379, db=0)

## set and get
r.set('foo', 'bar')
print(r.get('foo'))

## increment and decrement

r.set('count',1)

for i in range(1, 5):
  print(r.incr('count'))


# rpush, llen, and lindex

r.rpush('hispanic', 'uno')
r.rpush('hispanic', 'dos')
r.rpush('hispanic', 'tres')
r.rpush('hispanic', 'cuatro')

# print(r.get('hispanic'))

print('Lenght ' + str(r.llen('hispanic'))) ## get length

print(r.lindex('hispanic', 3)) ## get 4th item / 3 index value

