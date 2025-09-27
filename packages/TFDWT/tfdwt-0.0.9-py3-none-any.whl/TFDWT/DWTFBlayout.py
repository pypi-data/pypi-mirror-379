import tensorflow as tf
import keras
from TFDWT.DWTFilters import FetchAnalysisSynthesisFilters
from TFDWT.dwt_op import make_dwt_operator_matrix_A
# from TFDWT.DWTop import DWTop

@keras.saving.register_keras_serializable()
class DWTNDlayout(tf.keras.layers.Layer):
    """ TFDWT: Fast Discrete Wavelet Transform TensorFlow Layers.
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

    Note: if clean==True  then I/O (batch, N,..., N, channels) -> (batch, N/2,..., N/2, channels*2)
          if clean==False then I/O (batch, N,..., N, channels) -> (batch, N..., N, channels)

    DWT ND layout (mother class)  --kkt@20Jun2024"""
    def __init__(self, wave='haar', clean=True, **kwargs):
        super().__init__(**kwargs)
        self.wave = wave
        self.clean = clean  
        w = FetchAnalysisSynthesisFilters(wave)
        self.h0, self.h1 = w.analysis()
        self.L = len(self.h0)
        # self.h0 = tf.convert_to_tensor(h0, dtype=tf.float32)
        # self.h1 = tf.convert_to_tensor(h1, dtype=tf.float32)
        # self.L = self.h0.shape[0]
    
    def build(self, input_shape):
        self.N = input_shape[1]
        A = make_dwt_operator_matrix_A(self.h0,self.h1,self.N)
        # A = DWTop(self.h0,self.h1,self.N).A
        # Use analysis operator A with standard orientation (N x N)
        self.A = tf.cast(A, tf.float32)
        super().build(input_shape)
    
    def call(self, x):
        pass

    # def call(self, inputs):
    #     # inputs: (batch, N, channels)
    #     out = tf.einsum('bic,ij->bjc', inputs, self.A)
    #     if self.clean: return self.__extract_2subbands(out)
    #     else: return out

    # def __extract_2subbands(self,LH_padded):
    #     """returns 2 subbands L, H from DWT Analysis bank o/p --@k"""
    #     mid = int(LH_padded.shape[1]/2)
    #     L = LH_padded[:,:mid,:]
    #     H = LH_padded[:,mid:,:]
    #     return tf.concat([L, H], axis=-1)

    def get_config(self):
        config = super().get_config()
        config.update({
            'wave': self.wave,
            'clean': self.clean,
            # 'h0': list(self.h0),  # Converts TrackedList to regular list
            # add h1 if you also need it
            # 'h1': list(self.h1),
        })
        return config

#%%
@keras.saving.register_keras_serializable()
class IDWTNDlayout(tf.keras.layers.Layer):
    """ TFDWT: Fast Discrete Wavelet Transform TensorFlow Layers.
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
        
    Note: if clean==True  then I/O (batch, N/2,..., N/2, channels*2) -> (batch, N,..., N, channels)
          if clean==False then I/O (batch, N,..., N, channels) -> (batch, N,..., N, channels)  
    
    IDWT ND layout (mother class) --kkt@20Jun2024"""
    def __init__(self, wave='haar', clean=True, **kwargs):
        super().__init__(**kwargs)
        self.wave = wave
        self.clean = clean
        w = FetchAnalysisSynthesisFilters(wave)
        if 'bior' in wave or 'rbio' in wave:
            """BIORTHOGONAL wavelets"""
            self.h0, self.h1 = w.synthesis()
            # print(f"Biothogonal wavelet {wave}")
        else:
            """ORTHOGONAL wavelets"""
            self.h0, self.h1 = w.analysis()
        self.L = len(self.h0)

    def build(self, input_shape):
        if self.clean: self.N = int(input_shape[1] * 2)
        else: self.N = int(input_shape[1])
        A = make_dwt_operator_matrix_A(self.h0,self.h1,self.N)
        # A = DWTop(self.h0,self.h1,self.N).A
        # Use synthesis operator as A^T for consistency
        self.S = tf.cast(tf.transpose(A), tf.float32)
        super().build(input_shape)

    def call(self, inputs):
        pass


    # def call(self, inputs):
    #     # inputs: (batch, N, channels)
    #     if self.clean: inputs = self.__join_2subbands(inputs)
    #     out = tf.einsum('bic,ij->bjc', inputs, self.S)
    #     return out

    # def __join_2subbands(self, concat_subbands):
    #     """
    #     Inverts tf.concat([L, H], axis=-1) where L, H have shape (batch, mid, channels).
    #     Returns (batch, 2*mid, channels).
    #     """
    #     L, H = tf.split(concat_subbands, 2, axis=-1)
    #     return tf.concat([L, H], axis=1)

    def get_config(self):
        config = super().get_config()
        config.update({
            'wave': self.wave,
            'clean': self.clean,
            # 'h0': list(self.h0),  # Converts TrackedList to regular list
            # add h1 if you also need it
            # 'h1': list(self.h1),
        })
        return config
