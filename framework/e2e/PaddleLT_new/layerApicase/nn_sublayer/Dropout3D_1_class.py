import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: Dropout3D_1
    api简介: 3维Dropout
    """

    def __init__(self):
        super(LayerCase, self).__init__()
        self.func = paddle.nn.Dropout3D(p=1.0, )

    def forward(self, data, ):
        """
        forward
        """
        out = self.func(data, )
        return out



def create_inputspec(): 
    inputspec = ( 
        paddle.static.InputSpec(shape=(-1, -1, -1, -1, -1), dtype=paddle.float32, stop_gradient=False), 
    )
    return inputspec

def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([2, 3, 10, 10, 10]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([2, 3, 10, 10, 10]).astype('float32'), )
    return inputs
