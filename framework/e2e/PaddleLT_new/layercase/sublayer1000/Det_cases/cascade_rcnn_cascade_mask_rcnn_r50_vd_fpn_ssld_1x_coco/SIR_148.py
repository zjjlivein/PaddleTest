# api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.input.one_hot||method:unsqueeze||api:paddle.tensor.manipulation.expand_as||api:paddle.tensor.search.nonzero||api:paddle.tensor.manipulation.gather_nd||api:paddle.tensor.manipulation.reshape||method:cast||method:unsqueeze||api:paddle.nn.functional.loss.binary_cross_entropy_with_logits
import paddle
import unittest
import numpy as np


class LayerCase(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        self.parameter_0 = self.create_parameter(
           shape=[80],
           dtype=paddle.float32,
        )
        self.parameter_1 = self.create_parameter(
           shape=[80, 256, 1, 1],
           dtype=paddle.float32,
        )
    def forward(
        self,
        var_0,    # (shape: [4, 256, 28, 28], dtype: paddle.float32, stop_gradient: False)
        var_1,    # (shape: [4], dtype: paddle.int32, stop_gradient: True)
        var_2,    # (shape: [4, 28, 28], dtype: paddle.int32, stop_gradient: True)
        var_3,    # (shape: [4], dtype: paddle.float32, stop_gradient: True)
    ):
        var_4 = paddle.nn.functional.conv._conv_nd(var_0, self.parameter_1, bias=self.parameter_0, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_5 = paddle.nn.functional.input.one_hot(var_1, 80)
        var_6 = var_5.unsqueeze([2, 3])
        var_7 = paddle.tensor.manipulation.expand_as(var_6, var_4)
        var_8 = paddle.tensor.search.nonzero(var_7)
        var_9 = paddle.tensor.manipulation.gather_nd(var_4, var_8)
        var_10 = paddle.tensor.manipulation.reshape(var_9, [4, 28, 28])
        var_11 = var_2.cast('float32')
        var_12 = var_3.unsqueeze([1, 2])
        var_13 = paddle.nn.functional.loss.binary_cross_entropy_with_logits(var_10, var_11, weight=var_12, reduction='mean')
        return var_13


def create_paddle_inputs():
    inputs = (
        paddle.rand(shape=[4, 256, 28, 28], dtype=paddle.float32),
        paddle.randint(low=0, high=10, shape=[4], dtype=paddle.int32),
        paddle.randint(low=0, high=10, shape=[4, 28, 28], dtype=paddle.int32),
        paddle.rand(shape=[4], dtype=paddle.float32),
    )
    return inputs


def create_numpy_inputs():
    inputs = (
        np.random.random(size=[4, 256, 28, 28]).astype('float32'),
        np.random.randint(low=0, high=10, size=[4], dtype='int32'),
        np.random.randint(low=0, high=10, size=[4, 28, 28], dtype='int32'),
        np.random.random(size=[4]).astype('float32'),
    )
    return inputs


class TestLayer(unittest.TestCase):
    def setUp(self):
        self.inputs = create_paddle_inputs()
        self.net = LayerCase()
    def train(self, net, to_static, with_prim=False, with_cinn=False):
        if to_static:
            paddle.set_flags({'FLAGS_prim_all': with_prim})
            if with_cinn:
                build_strategy = paddle.static.BuildStrategy()
                build_strategy.build_cinn_pass = True
                net = paddle.jit.to_static(net, build_strategy=build_strategy, full_graph=True)
            else:
                net = paddle.jit.to_static(net, full_graph=True)
        paddle.seed(123)
        outs = net(*self.inputs)
        return outs
    def test_ast_prim_cinn(self):
        st_out = self.train(self.net, to_static=True)
        cinn_out = self.train(self.net, to_static=True, with_prim=True, with_cinn=True)
        for st, cinn in zip(paddle.utils.flatten(st_out), paddle.utils.flatten(cinn_out)):
            np.testing.assert_allclose(st.numpy(), cinn.numpy(), atol=1e-8)


if __name__ == '__main__':
    unittest.main()