import argparse
from collections import defaultdict

import onnx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('dest')
    args = parser.parse_args()

    model = onnx.load(args.src)

    names = {v.name: v.name for v in model.graph.initializer}
    op_counts = defaultdict(int)

    for op in model.graph.node:
        op_name = '{}_{}'.format(op.op_type, op_counts[op.op_type])
        op_counts[op.op_type] += 1

        for i in range(len(op.input)):
            if op.input[i] in names:
                op.input[i] = op.input[i]
            else:
                op.input[i] = 'Input_{}'.format(op_counts['Input'])
                op_counts['Input'] += 1

        for i in range(len(op.output)):
            if len(op.output) <= 1:
                names[op.output[i]] = op_name
            else:
                names[op.output[i]] = '{}_{}'.format(op_name, i)
            op.output[i] = names[op.output[i]]

    onnx.save(model, args.dest)


if __name__ == '__main__':
    main()
