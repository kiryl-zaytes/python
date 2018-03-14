__author__ = 'kiryl_zayets'

def bad_hash(key,numberOfBuckets):
    codeOfFirstLetter = ord(key[0])
    buck = codeOfFirstLetter % numberOfBuckets
    return buck

def hash_function(func,keys,size):
    results = [0]*size
    keys_used = []
    for key in keys:
        if key not in keys_used:
            hr=func(key,size)
            results[hr]+=1
            keys_used.append(key)
    return results

def hash_string(key,buckets):
    hash = 0
    for letter in key:
        hash = (hash + ord(letter))%buckets
    return hash

def createBuckets(nBuckets):
    buckets = []
    for i in range(0,nBuckets-1):
        buckets.append([])
    return buckets

def getBucket(hTable,key):
    return hTable[hash_string(key,len(hTable))]

def hashTableAdd(hTable,key,valueToAdd):
    return getBucket(hTable,key).append([key,valueToAdd])

hTable = createBuckets(10)
hashTableAdd(hTable,'test',23)
hashTableAdd(hTable,'1test',24)
hashTableAdd(hTable,'3test',24)
hashTableAdd(hTable,'3test',25)
bucket=getBucket(hTable,'test')

print(hTable)
print(bucket)


