import numpy as np

a = np.array([
    [
        [
            [
                [
                    [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8]
                    ],
                    [
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
                    ]
                ],
                [
                    [
                        [17, 18, 19, 20],
                        [21, 22, 23, 24]
                    ],
                    [
                        [25, 26, 27, 28],
                        [29, 30, 31, 32]
                    ]
                ]
            ]
        ]
    ]
]
)

print(f"Element is the  : {a[0,0,0,1,1,1,3]}")
print(f"Dimention : {a.ndim}")
print(f"Shape : {a.shape}")
print(f"Size: {a.size}")  
print(f"Data type: {a.dtype}")  
print(f"Total memoray used are : {a.nbytes}bytes")