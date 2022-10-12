import numpy as np

arr1=np.ones((5,10))*5
print(arr1)
print()

arr2=np.arange(1,26).reshape(5,5)
print(arr2)
print()

arr3=np.arange(10,51,2)
print(arr3)
print()

arr4=np.eye(3)*8
print(arr4)
print()

arr5=np.arange(0,1,0.01).reshape((10,10))
print(arr5)
print()

arr6=np.linspace(0, 1, 50)
print(arr6)
print()

arr7=arr2.flatten()[12:24]
print(arr7)
print()

arr8=arr2[0:3, 4].reshape((3,1))
print(arr8)
print()

arr9=np.sum(arr2[3:5, 0:5])
print(arr9)
print()

tensor = np.random.randint(0, 100, (np.random.randint(10), np.random.randint(10)))
print(tensor)