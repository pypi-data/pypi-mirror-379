import tensorflow as tf
# from keras import regularizers
from keras import ops
from TFDWT.DWT1DFB import DWT1D, IDWT1D
from tensorflow.keras.layers import Concatenate

def dwt(x, level=3, Ψ='haar'):
    """ Multilevel 1D DWT
    
        TFDWT: Fast Discrete Wavelet Transform TensorFlow Layers.
        Copyright (C) 2025 Kishore Kumar Tarafdar

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
    subbands = []
    current = x
    channels_in = x.shape[-1]

    for _ in range(level):
        w = DWT1D(wave=Ψ)(current)
        lowpass = w[:, :, :channels_in]
        highpass = w[:, :, channels_in:]
        subbands.append(highpass)
        current = lowpass
    subbands.append(current)
    return subbands


def idwt(subbands, level=3, Ψ='haar'):
    """ Multilevel 1D IDWT
    
        TFDWT: Fast Discrete Wavelet Transform TensorFlow Layers.
        Copyright (C) 2025 Kishore Kumar Tarafdar

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
    *highpasses, lowpass = subbands  # unpack: [H1, H2, ..., Hn, ln]
    
    current = lowpass
    for H in reversed(highpasses):
        current = IDWT1D(wave=Ψ)(Concatenate()([current, H]))
    
    return current

if __name__=='__main__':
    batch_size, N, channels = 1, 32, 2
    x = tf.random.normal((batch_size, N, channels))
    x.shape
    level = 4
    subbands = dwt(x, level=level)
    print([_.shape for _ in subbands])
    x_rec = idwt(subbands, level=level)
    print(np.allclose(x,x_rec, atol=1e-9))