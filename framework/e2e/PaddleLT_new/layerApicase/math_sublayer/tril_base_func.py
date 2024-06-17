import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: tril_base
    api简介: 返回输入矩阵 input 的下三角部分，其余部分被设为0。 矩形的下三角部分被定义为对角线上和下方的元素
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, ):
        """
        forward
        """
        out = paddle.tril(x,  )
        return out



def create_inputspec(): 
    inputspec = ( 
        paddle.static.InputSpec(shape=(-1, -1, -1, -1), dtype=paddle.float32, stop_gradient=False), 
    )
    return inputspec

def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([7, 6, 3, 3]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([7, 6, 3, 3]).astype('float32'), )
    return inputs

