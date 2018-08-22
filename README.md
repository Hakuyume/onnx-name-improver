# ONNX name improver

This script renames variables in an ONNX file.

## Usage

```
$ pip3 intall onnx
$ python3 rename.py <src.onnx> <dest.onnx>
```

## Example result

Input

```
node list
node num is 40
0:Conv
        input0: 140326425860192
        input1: /conv1_1/W
        input2: /conv1_1/b
        output0: 140326201104648
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1 
1:Relu
        input0: 140326201104648
        output0: 140326201105432
2:Conv
        input0: 140326201105432
        input1: /conv1_2/W
        input2: /conv1_2/b
        output0: 140326201105544
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1 
3:Relu
        input0: 140326201105544
        output0: 140326201105600
4:MaxPool
        input0: 140326201105600
        output0: 140326429223512
        attribute0: kernel_shape ints: 2 2 
        attribute1: pads ints: 0 0 
        attribute2: strides ints: 2 2 
5:Conv
        input0: 140326429223512
        input1: /conv2_1/W
        input2: /conv2_1/b
        output0: 140326150903064
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1
```

Output

```
node list
node num is 40
0:Conv
        input0: Input_0
        input1: /conv1_1/W
        input2: /conv1_1/b
        output0: Conv_0
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1 
1:Relu
        input0: Conv_0
        output0: Relu_0
2:Conv
        input0: Relu_0
        input1: /conv1_2/W
        input2: /conv1_2/b
        output0: Conv_1
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1 
3:Relu
        input0: Conv_1
        output0: Relu_1
4:MaxPool
        input0: Relu_1
        output0: MaxPool_0
        attribute0: kernel_shape ints: 2 2 
        attribute1: pads ints: 0 0 
        attribute2: strides ints: 2 2 
5:Conv
        input0: MaxPool_0
        input1: /conv2_1/W
        input2: /conv2_1/b
        output0: Conv_2
        attribute0: dilations ints: 1 1 
        attribute1: kernel_shape ints: 3 3 
        attribute2: pads ints: 1 1 1 1 
        attribute3: strides ints: 1 1
```
