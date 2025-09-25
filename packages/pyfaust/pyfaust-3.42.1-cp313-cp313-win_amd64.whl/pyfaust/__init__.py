# -*- coding: utf-8 -*-
# ######################################################################################
# Copyright (c) 2015-2023, Inria and Authors:                                        #
#  (Researchers:) Rémi Gribonval, Luc Le Magoarou,                                   #
#  (Engineers:) Adrien Leman (2016), Nicolas Bellot(2015-2016),                      #
#  Thomas Gautrais (2015), Hakim Hadj-Djilani (2018-),                               #
#  Pascal Carrivain (2023-).                                                         #
#  All rights reserved.                                                              #
#                                                                                    #
#  BSD 3-clause License.                                                             #
#                                                                                    #
# Redistribution and use in source and binary forms, with or without                 #
# modification, are permitted provided that the following conditions are met:        #
#                                                                                    #
# 1. Redistributions of source code must retain the above copyright notice, this     #
# list of conditions and the following disclaimer.                                   #
#                                                                                    #
# 2. Redistributions in binary form must reproduce the above copyright notice,       #
#     this list of conditions and the following disclaimer in the documentation      #
#     and/or other materials provided with the distribution.                         #
#                                                                                    #
# 3. Neither the name of the copyright holder nor the names of its                   #
# contributors may be used to endorse or promote products derived from this          #
# software without specific prior written permission.                                #
#                                                                                    #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"        #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE          #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE         #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE          #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR                #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF               #
#         SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR            #
#         BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF                 #
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING               #
#         NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS         #
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                       #
######################################################################################

# 
# 
from sys import platform as _pf
from os.path import basename
from os import environ
libomp_loading_verbose = False
internal_libomp_loading = True


def load_lib_omp():
    """
        Loads libomp if it is embedded in the pyfaust package.
    """
    from os.path import join, exists
    import sys
    import ctypes
    import ctypes.util
    name = 'libomp'
    if _pf == 'darwin':
        ext = 'dylib'
    elif _pf == 'linux':
        ext = 'so'
    elif _pf == 'win32':
        name = 'vcomp140'
        ext = 'dll'
    for p in sys.path:
        lib_path = join(p, 'pyfaust', 'lib', name+'.'+ext)
        if exists(lib_path):
            ctypes.CDLL(lib_path)
            if libomp_loading_verbose:
                print(lib_path+" has been loaded successfully.")
            break
    else:
        print("failed to load libomp (didn't find any shared lib in"
              " sys.path:", sys.path)


def inform_user_how_to_install_libomp():
    """
    """
    from os.path import exists
    if _pf == 'darwin':
        if not exists('/opt/local/lib/libomp/libomp.dylib'):
            print("""ERROR: OpenMP for clang is not properly installed on your system.
                  You need to install it through MacPorts.
                  1) Install MacPorts: https://www.macports.org/install.php
                  2) Install libomp:
                      sudo port install libomp-devel libomp
                      sudo port -f activate libomp
                  """)
    elif _pf == 'linux':
        if not exists('/usr/lib64/libomp.so'):
            print("""ERROR: OpenMP for clang is not properly installed on your system.
                  You need to install the proper packages, for example:
                  - On Fedora the package is libomp-11*,
                  - On Debian the package is libomp-11*.
                  """)
    elif _pf == 'win32':
        print("""ERROR: OpenMP for Visual Studio is not properly installed on your system.
              You need to install \"Visual Studio C++ Redistribuable
              Binaries\". It works also by copying vcomp140.dll in the
              appropriate python site-packages path"""+basename(__file__)+""".
              """)

def try_modify_wrapper_lib_on_macos():
    from os.path import dirname, join
    from os import system
    from glob import glob
    from sys import platform
    if platform != 'darwin':
        return
    wrapper_path = glob(join(dirname(dirname(__file__)), '_Faust*so'))[0]
    libomp_path = join(dirname(__file__), 'lib/libomp.dylib')
    system('install_name_tool -change /opt/local/lib/libomp/libomp.dylib '+libomp_path+' '+wrapper_path)


# load libomp pyfaust embedded library if found in pyfaust location
if _pf in ['darwin', 'linux', 'win32']:
    try_modify_wrapper_lib_on_macos()
    if internal_libomp_loading and not 'DISABLE_PYFAUST_LIBOMP' in environ:
        load_lib_omp()
    else:
        inform_user_how_to_install_libomp()

# 

## @package pyfaust @brief @b The @b FAuST @b Python @b Wrapper

import numpy as np
import scipy
from scipy.io import loadmat
try:
    from scipy.sparse import (csr_array, csc_array, coo_array, bsr_array,
                              dia_array,
                              csr_matrix, csc_matrix, coo_matrix, bsr_matrix,
                              dia_matrix)
except:
    # older scipy versions, missing _array types
    from scipy.sparse import (csr_matrix, csc_matrix, coo_matrix, bsr_matrix,
                              dia_matrix)
    # add array aliases
    csr_array = csr_matrix
    csc_array = csc_matrix
    coo_array = coo_matrix
    bsr_array = bsr_matrix
    dia_array = dia_matrix

from scipy.sparse import (diags, eye as seye, kron, vstack as
                          svstack, hstack as shstack, issparse)
import _FaustCorePy
import pyfaust
import pyfaust.factparams
import warnings
import decimal
import numpy.lib.mixins
from os import environ
from pyfaust.tools import _sanitize_dtype

HANDLED_FUNCTIONS = {}
WARNING_ON_C_CONTIGUOUS_MATMUL = True


class Faust(numpy.lib.mixins.NDArrayOperatorsMixin):
    r"""<b>pyfaust main class</b> for using multi-layer sparse transforms.

    This class provides a NumPy-like interface for operations
    with FAuST data structures, which correspond ideally to matrices that can
    be written exactly as the product of sparse matrices.

    The Faust class is designed to allow fast matrix-vector multiplications
    together with reduced memory storage compared to what would be obtained by
    manipulating directly the corresponding dense matrix.

    A particular example is the matrix associated to the discrete Fourier
    transform, which can be represented exactly as a Faust,
    leading to a fast and compact implementation (see :py:func:`pyfaust.dft`)

    Although sparse matrices are more interesting for optimization it's not
    forbidden to define a Faust as a product of dense matrices or a mix of
    dense and sparse matrices.

    The matrices composing the Faust product, also called the factors, are
    defined on complex or real fields. Hence a Faust can be a complex Faust
    or a real Faust.

    Several Python built-ins have been overloaded to ensure that a Faust is
    almost handled as a native NumPy array.

    The main exception is that contrary to a NumPy array a Faust is immutable.
    It means that you cannot modify elements of a Faust using
    the assignment operator ``=`` as made with a NumPy array (e.g. ``M[i, j] =
    2``).
    That limitation is the reason why the Python built-in ``__setitem__()`` is
    not implemented in this class.
    Note however that you can optionally contravene the immuability in
    certain functions (e.g. with the `inplace` argument of the
    functions :py:func:`Faust.swap_rows`, :py:func:`Faust.swap_cols`,
    :py:func:`Faust.optimize_time`).

    Other noticeable limitations:

        - Elementwise multiplication, addition/subtraction are available, but
          performing elementwise operations between two Fausts is discouraged,
        - One cannot reshape a Faust.

    A last but not least caveat is that Faust doesn't support the NumPy
    universal functions (ufuncs) except if the contrary is specified in the
    API doc. for a particular function.

    Mainly for convenience and test purposes, a Faust can be converted into
    the corresponding full matrix using the function :py:func:`Faust.toarray`.

    Warning: using :func:`Faust.toarray` is discouraged except for test purposes, as it
        loses the main potential interests of the FAuST structure: compressed
        memory storage and faster matrix-vector multiplication compared to its
        equivalent full matrix representation.

    In this documentation, the expression 'full matrix' designates the array
    :func:`Faust.toarray()` obtained by the multiplication of the Faust factors.

    NOTE: it could be wiser to encapsulate a Faust in a
          <a href="https://faustgrp.gitlabpages.inria.fr/lazylinop/api_lazylinop.html">lazylinop.LazyLinOp</a>
          for a totally lazy paradigm on all available operations.

    List of functions that are memory costly:

        - element indexing (``F[i, j]`` / :py:func:`Faust.__getitem__`, but
          note that slicing is memory efficient through memory views),
        - function :py:func:`Faust.toarray()`,
        - function :py:func:`Faust.pinv()`.

    For more information about FAuST take a look at https://faust.inria.fr.

    \see :py:func:`pyfaust.Faust.__init__`
    """

    def __init__(F, factors=None, filepath=None, **kwargs):
        r""" Creates a Faust from a list of factors or alternatively from a file.
        Other easy ways to create a Faust is to call one of the following functions: pyfaust.rand, pyfaust.dft or pyfaust.wht.

        Args:
            factors: (list of numpy/scipy array/matrices or a single array/matrix.)
                     The factors must respect the dimensions needed for
                     the product to be defined <code>(for i in range(0, len(factors)-1): factors[i].shape[1] == factors[i+1].shape[0])</code>.<br/>
                     The factors can be sparse or dense matrices
                     (either scipy.sparse.csr_matrix/bsr_matrix or
                     numpy.ndarray with ndim == 2).
                     scipy.sparse.csc_matrix/coo_matrix are supported but
                     converted to csr_matrix on the fly.<br/>
                     The Faust will be in the same dtype as the factors
                     (only 'float32', 'float64'/'double' and 'complex128'/'complex' dtype are supported).
                     Passing only an array or a sparse matrix to the
                     constructor is equivalent to
                     passing a list of a single factor.
            filepath: (str)
                the file from which a Faust is created.<br/>
                The format is Matlab version 5 (.mat extension).<br/>
                The file must have been saved before with :func:`Faust.save().`
            dev: (str)
                'cpu' (by default) or 'gpu' to instantiate the Faust resp. on
                CPU or on NVIDIA GPU memory.
            kwargs: (dict)
                internal purpose arguments.

        NOTE: filepath and factors arguments are mutually exclusive. Either
            you specify one of them explicitly with the keyword or the first (positional) argument type
            will determine if it's a filepath (a str) or a factor list. If both of
            the keyword arguments are set then filepath will be prioritary.

        Examples:
                >>> # Example 1 -- Creating a Faust made of CSR matrices and numpy arrays:
                >>> from pyfaust import Faust
                >>> import numpy as np
                >>> from scipy import sparse
                >>> factors = []
                >>> factors += [sparse.random(100, 100, dtype=np.float64, format='csr', density=0.1)]
                >>> factors += [np.random.rand(100, 100).astype(np.float64) ]
                >>> factors += [sparse.random(100, 100, dtype=np.float64, format='csr', density=0.1)]
                >>> factors += [np.random.rand(100, 100).astype(np.float64) ]
                >>> factors += [sparse.random(100, 100, dtype=np.float64, format='csr', density=0.1)]
                >>> # define a Faust with those factors
                >>> F = Faust(factors)

                >>> F.save("F.mat")
                >>> # define a Faust from file
                >>> H = Faust(filepath="F.mat") # F = Faust("F.mat") does the same

                >>> # creating a Faust with only one
                >>> # factor
                >>> Faust(np.random.rand(10, 10))
                Faust size 10x10, density 1, nnz_sum 100, 1 factor(s):
                - FACTOR 0 (double) DENSE, size 10x10, density 1, nnz 100

                >>> # Example 2 -- Creating a Faust containing one BSR matrix:
                >>> from scipy.sparse import bsr_matrix
                >>> from pyfaust import Faust
                >>> from numpy import allclose
                >>> from numpy.random import rand
                >>> nzblocks = rand(3, 2, 3) # 3 blocks of size 2x3
                >>> # create a scipy BSR matrix
                >>> B = bsr_matrix((nzblocks, [0, 1, 2], [0, 1, 2, 3, 3, 3]), shape=(10, 9))
                >>> # create the single factor Faust
                >>> F = Faust(B)
                >>> F
                Faust size 10x9, density 0.2, nnz_sum 18, 1 factor(s):
                - FACTOR 0 (double) BSR, size 10x9 (blocksize = 2x3), density 0.2, nnz 18 (nnz blocks: 3)

                >>> allclose(F.toarray(), B.toarray())
                True
                >>> # of course it's ok to create a Faust with a BSR and another type of factors
                >>> Faust([B, rand(9, 18)])
                Faust size 10x18, density 1, nnz_sum 180, 2 factor(s):
                - FACTOR 0 (double) BSR, size 10x9 (blocksize = 2x3), density 0.2, nnz 18 (nnz blocks: 3)
                - FACTOR 1 (double) DENSE, size 9x18, density 1, nnz 162

        \see :py:func:`Faust.save`, :py:func:`pyfaust.rand`, :py:func:`pyfaust.dft`, :py:func:`pyfaust.wht`,
            <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html">csr_matrix, </a>
            <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.bsr_matrix.html">bsr_matrix</a>
            <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html">csc_matrix, </a>
            <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html">coo_matrix </a>

        """
        is_on_gpu = False
        if "scale" in kwargs.keys():
            # scale hidden argument
            scale = kwargs['scale']
            if not np.isscalar(scale):
                raise Exception("Scale must be a number.")
        else:
            scale = 1.0
        if "dev" in kwargs.keys():
            dev = kwargs['dev']
            if dev.startswith('gpu'):
                is_on_gpu = True
            check_dev(dev)
        if "core_obj" in kwargs.keys():
            core_obj = kwargs['core_obj']
            if core_obj:
                F.m_faust = core_obj
        else:
            if isinstance(factors, str) and not filepath:
                filepath = factors
            if filepath and isinstance(filepath, str):
                G = Faust.load(filepath)
                F.m_faust = G.m_faust
                F._is_real = G._is_real
                return
            if isinstance(factors,
                          (np.ndarray, csc_matrix, csr_matrix, coo_matrix, bsr_matrix)) and factors.ndim == 2:
                factors = [factors]
            if not isinstance(factors, list):
                raise Exception("factors must be a non-empty list of/or a numpy.ndarray, "
                                "scipy.sparse.csr_matrix/csc_matrix/bsr_matrix.")
            F._is_real = True
            # verify if all factors has the same dtype (mandatory)
            dtype = None
            if len(factors) == 0:
                raise ValueError("Empty list of matrices.")
            for f in factors:
                F._is_real = f.dtype != 'complex'
                if dtype is None:
                    dtype = f.dtype
                elif dtype != f.dtype:
                    raise TypeError('All Faust factors must have the same dtype.')
            dtype = _sanitize_dtype(dtype)
            if factors is not None and len(factors) > 0:
                if is_on_gpu:
                    if F._is_real:
                        if dtype == 'float64':
                            F.m_faust = _FaustCorePy.FaustCoreGenDblGPU(factors, scale)
                        else:  # if dtype == 'float32':
                            F.m_faust = _FaustCorePy.FaustCoreGenFltGPU(factors, scale)
                    else:
                        F.m_faust = _FaustCorePy.FaustCoreGenCplxDblGPU(factors, scale)
                elif F._is_real:
                    if dtype == 'float64':
                        F.m_faust = _FaustCorePy.FaustCoreGenDblCPU(factors, scale)
                    else:  # if dtype == 'float32':
                        F.m_faust = _FaustCorePy.FaustCoreGenFltCPU(factors, scale)
                else:
                    F.m_faust = _FaustCorePy.FaustCoreGenCplxDblCPU(factors, scale)
            else:
                raise Exception("Cannot create an empty Faust.")

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method == '__call__':
            if str(ufunc) == "<ufunc 'matmul'>" and len(inputs) >= 2 and \
               isFaust(inputs[1]):
                return inputs[1].__rmatmul__(inputs[0])
            elif str(ufunc) == "<ufunc 'multiply'>" and len(inputs) >= 2 and \
                    isFaust(inputs[1]):
                return inputs[1].__rmul__(inputs[0])
            elif str(ufunc) == "<ufunc 'add'>" and len(inputs) >= 2 and \
                    isFaust(inputs[1]):
                return inputs[1].__radd__(inputs[0])
            elif str(ufunc) == "<ufunc 'subtract'>" and len(inputs) >= 2 and \
                    isFaust(inputs[1]):
                return inputs[1].__rsub__(inputs[0])
        elif method == 'reduce':
            # # not necessary numpy calls Faust.sum
            # if ufunc == "<ufunc 'add'>":
            #     if len(inputs) == 1 and pyfaust.isFaust(inputs[0]):
            #         #return inputs[0].sum(*inputs[1:], **kwargs)
            #     else:
            return NotImplemented

    def __array__(self, *args, **kwargs):
        return self

    def __array_function__(self, func, types, args, kwargs):
        # Note: this allows subclasses that don't override
        # __array_function__ to handle Faust objects
        if not all(issubclass(t, Faust) for t in types):
            return NotImplemented
        if func.__name__ == 'ndim':
            return self.ndim
        return NotImplemented

    @property
    def nbytes(F):
        """
        Gives the memory size of the Faust in bytes.

        Example:
            >>> import pyfaust as pf
            >>> F = pf.rand(1024, 1024)
            >>> F
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> F.nbytes
            327700
            >>> F = pf.rand(1024, 1024, fac_type='dense')
            >>> F
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> F.nbytes
            41943040

        """
        return F.m_faust.nbytes()

    @property
    def shape(F):
        r"""Gives the shape of the Faust F.

        This function is intended to be used as a property (see the examples).

        The shape is a pair of numbers: the number of rows and the number of
        columns of F.todense().

        Args:
            F: the Faust object.

        Returns:
            the Faust shape tuple, with at first index the number of rows, and
            at second index the number of columns.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> nrows, ncols = F.shape
            >>> nrows = F.shape[0]
            >>> ncols = F.shape[1]

        \see :py:func:`Faust.nnz_sum`, :py:func:`Faust.size`,
        """
        return F.m_faust.shape()

    @property
    def ndim(F):
        """
            Number of Faust dimensions (always 2).
        """
        return 2

    @property
    def size(F):
        r"""Gives the size of the Faust F (that is F.shape[0]*F.shape[1]) .

        It's equivalent to numpy.prod(F.shape)).

        This function is intended to be used as a property (see the examples).

        Args:
            F: the Faust object.

        Returns:
            The number of elements in the Faust F.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> int(F.size)
            2500

        \see :py:func:`Faust.shape`

        """
        return np.prod(F.shape)

    @property
    def device(self):
        """
        Returns the device on which the Faust is located ('cpu' or 'gpu').

        Example:
            >>> import pyfaust as pf
            >>> cpuF = pf.rand(5, 5, dev='cpu')
            >>> cpuF.device
            'cpu'
            >>> if pf.is_gpu_mod_enabled(): gpuF = pf.rand(5, 5, dev='gpu')
            >>> gpuF.device if pf.is_gpu_mod_enabled() else None
            >>> # it should print 'gpu' if it is available

        """
        return self.m_faust.device()

    def transpose(F):
        r"""
        Returns the transpose of F.

        Args:
            F: the Faust object.

        Returns:
            a Faust object implementing the transpose of F.toarray(), such
            that:
            <code>F.transpose().toarray() == F.toarray().transpose()</code>

        Examples:
            >>> from pyfaust import rand, seed
            >>> F = rand(10, 18)
            >>> tF = F.transpose()
            >>> tF.shape
            (18, 10)

        \see :py:func:`Faust.conj`, :py:func:`Faust.getH`, :py:func:`Faust.H`, :py:func:`Faust.T`
        """
        F_trans = Faust(core_obj=F.m_faust.transpose())
        return F_trans

    @property
    def T(F):
        r"""
        Returns the transpose of F.

        This function is intended to be used as a property (see the examples).

        Args:
            F: the Faust object.

        Returns:
            a Faust object implementing the transpose of F.toarray(), such
            that:
            <code>F.T.toarray() == F.toarray().T</code>

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(10, 23)
            >>> tF = F.T
            >>> tF.shape
            (23, 10)

        \see :py:func:`Faust.conj`, :py:func:`Faust.getH`, :py:func:`Faust.H`, :py:func:`Faust.T`
        """
        return F.transpose()

    def conj(F):
        r"""
        Returns the complex conjugate of F.

        Args:
            F: the Faust object.

        Returns:
            a Faust object Fc implementing the conjugate of F.toarray() such
            that:
            <code>Fc.toarray() == F.toarray().conj()</code>


        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> Fc = F.conj()

        \see :py:func:`Faust.transpose`, :py:func:`Faust.getH`, :py:func:`Faust.H`,
        """
        F_conj = Faust(core_obj=F.m_faust.conj())
        return F_conj

    def conjugate(F):
        r"""
        Returns the complex conjugate of F.

        Args:
            F: the Faust object.

        Returns:
            a Faust object Fc implementing the conjugate of F.toarray() such
            that:
            <code>Fc.toarray() == F.toarray().conjugate()</code>


        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> Fc = F.conjugate()

        \see :py:func:`Faust.transpose`, :py:func:`Faust.getH`, :py:func:`Faust.H`,
        """
        return F.conj()

    def getH(F):
        r"""
        Returns the conjugate transpose of F.

        Args:
            F: the Faust object.

        Returns:
            a Faust object H implementing the conjugate transpose of
            F.toarray() such that:
            ``H.toarray() == F.toarray().getH()``

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> H1 = F.getH()
            >>> H2 = F.transpose()
            >>> H2 = H2.conj()
            >>> bool((H1.toarray() == H2.toarray()).all())
            True

        \see :py:func:`Faust.transpose`, :py:func:`Faust.conj`, :py:func:`Faust.H`
        """
        F_ctrans = Faust(core_obj=F.m_faust.getH())
        return F_ctrans

    @property
    def H(F):
        r"""Returns the conjugate transpose of F.

        This function is intended to be used as a property (see the examples).

        Returns:
            a Faust object H implementing the conjugate transpose of
            F.toarray() such that:
            ``H.toarray() == F.toarray().H``

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50, field='complex')
            >>> H1 = F.H
            >>> H2 = F.transpose()
            >>> H2 = H2.conj()
            >>> bool((H1.toarray() == H2.toarray()).all())
            True

        \see :py:func:`Faust.transpose`, :py:func:`Faust.conj`, :py:func:`Faust.getH`
        """
        return F.getH()

    def pruneout(F, thres=0, **kwargs):
        r"""Returns a Faust optimized by removing useless zero rows and columns as many times as needed.

        Args:
            F: (Faust)
                the Faust to optimize.
            thres: (int)
                the threshold in number of nonzeros under what the
                rows/columns are removed.

        Returns:
            The optimized Faust.

        Example:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(1024, 1024, dim_sizes=[1, 1024], num_factors=64, fac_type='mixed')
            >>> pF = F.pruneout()
            >>> F.nbytes
            49109760
            >>> pF.nbytes
            46535972

        \see :py:func:`Faust.optimize`
        """
        # hidden parameters (useless unless for debug)
        #            only_forward: True for applying only the forward passes of removal.
        #            npasses: the number of passes to run, by default it goes until the
        #            optimal Faust is obtained.
        npasses = 'auto'
        only_forward = False
        if 'npasses' in kwargs:
            npasses = kwargs['npasses']
        if 'only_forward' in kwargs:
            only_forward = kwargs['only_forward']
        if npasses == 'auto':
            npasses = -1
        elif not isinstance(npasses, int):
            raise TypeError('npasses must be a int'
                            ' or \'auto\'')
        if not isinstance(only_forward, bool):
            raise TypeError('only_forward '
                            'must be a bool.')
        if not isinstance(thres, int):
            raise TypeError('thres '
                            'must be a int.')
        # print("only_forward=", only_forward, "npasses=", npasses)
        F_prunedout = Faust(core_obj=F.m_faust.zpruneout(thres, npasses,
                                                         only_forward))
        return F_prunedout

    def __repr__(F):
        r"""Returns a str object representing the Faust object.
        This method overloads a Python function.

        NOTE: Ideally this function is intended to return a valid Python
            expression but here this is not the case. Only information is
            displayed.

        Args:
            F: the Faust object.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 50)
            >>> print(F.__repr__())
            Faust size 50x50, density 0.5, nnz_sum 1250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 1 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 2 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 3 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 4 (double) SPARSE, size 50x50, density 0.1, nnz 250

            >>> # the same function is called when typing F in a terminal:
            >>> F
            Faust size 50x50, density 0.5, nnz_sum 1250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 1 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 2 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 3 (double) SPARSE, size 50x50, density 0.1, nnz 250
            - FACTOR 4 (double) SPARSE, size 50x50, density 0.1, nnz 250

        \see :py:func:`Faust.nnz_sum`, :py:func:`Faust.rcg`, :py:func:`Faust.shape`, :py:func:`Faust.factors`, :py:func:`Faust.numfactors`, :py:func:`Faust.display`

        """
        _str = str(F.m_faust.to_string())
        return _str

    def __str__(F):
        """
        Converts F to its str representation.

        Returns:
            The str conversion of F.

        """
        return F.__repr__()

    def display(F):
        r"""
        Displays information about F.

        Args:
            F: the Faust object.

        Examples:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(50, 100, [1, 2], [50, 100], .5)
            >>> F.display()
            Faust size 50x100, density 1.3, nnz_sum 6500, 2 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.494253, nnz 2150
            - FACTOR 1 (double) SPARSE, size 87x100, density 0.5, nnz 4350

            >>> F
            Faust size 50x100, density 1.3, nnz_sum 6500, 2 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.494253, nnz 2150
            - FACTOR 1 (double) SPARSE, size 87x100, density 0.5, nnz 4350

            >>> print(F)
            Faust size 50x100, density 1.3, nnz_sum 6500, 2 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.494253, nnz 2150
            - FACTOR 1 (double) SPARSE, size 87x100, density 0.5, nnz 4350


        \see :py:func:`Faust.nnz_sum`, :py:func:`Faust.density`, :py:func:`Faust.shape`, :py:func:`Faust.factors`, :py:func:`Faust.numfactors`, :py:func:`Faust.__repr__`,

        """
        print(F.__repr__())
        # F.m_faust.display()

    def __pos__(F):
        r"""
        Returns + F (unary operator).

        NOTE: This method overloads the Python unary operator +.


        \see :py:func:`Faust.__add__`
        """
        return F

    def __neg__(F):
        r"""
        Returns - F (unary operator).


        NOTE: This method overloads the Python unary operator -.

        \see :py:func:`Faust.__sub__`, :py:func:`Faust.__mul__`
        """
        return -1 * F

    def __add__(F, *args, **kwargs):
        r"""
        Sums F to one or a sequence of variables (Faust objects, arrays or scalars).


        NOTE: This method overloads the Python function/operator +.

        Args:
            args: (list[Faust or np.ndarray or scipy.sparse.csr_matrix])
                the list of variables to sum all together with F.
                These can be Faust objects, numpy arrays (and
                scipy.sparse.csr_matrix) or scalars.
                Faust and arrays/matrices must be of compatible sizes.

        Returns:
            the sum as a Faust object.

        Example:
            >>> import pyfaust as pf
            >>> from numpy.linalg import norm
            >>> pf.seed(42) # just for reproducibility
            >>> F = pf.rand(10, 12)
            >>> F
            Faust size 10x12, density 2.04167, nnz_sum 245, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x12, density 0.333333, nnz 40
            - FACTOR 1 (double) SPARSE, size 12x10, density 0.5, nnz 60
            - FACTOR 2 (double) SPARSE, size 10x11, density 0.454545, nnz 50
            - FACTOR 3 (double) SPARSE, size 11x10, density 0.5, nnz 55
            - FACTOR 4 (double) SPARSE, size 10x12, density 0.333333, nnz 40

            >>> G = pf.rand(10, 12)
            >>> G
            Faust size 10x12, density 2.025, nnz_sum 243, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x11, density 0.454545, nnz 50
            - FACTOR 1 (double) SPARSE, size 11x10, density 0.5, nnz 55
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x12, density 0.333333, nnz 40
            - FACTOR 4 (double) SPARSE, size 12x12, density 0.333333, nnz 48

            >>> F+G
            Faust size 10x12, density 4.43333, nnz_sum 532, 7 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x23, density 0.195652, nnz 90
            - FACTOR 2 (double) SPARSE, size 23x20, density 0.25, nnz 115
            - FACTOR 3 (double) SPARSE, size 20x21, density 0.238095, nnz 100
            - FACTOR 4 (double) SPARSE, size 21x22, density 0.205628, nnz 95
            - FACTOR 5 (double) SPARSE, size 22x24, density 0.166667, nnz 88
            - FACTOR 6 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F+G).toarray() - F.toarray() - G.toarray()))
            5.975125014346798e-15
            >>> F+2
            Faust size 10x12, density 2.84167, nnz_sum 341, 7 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x22, density 0.113636, nnz 50
            - FACTOR 2 (double) SPARSE, size 22x20, density 0.159091, nnz 70
            - FACTOR 3 (double) SPARSE, size 20x21, density 0.142857, nnz 60
            - FACTOR 4 (double) SPARSE, size 21x11, density 0.281385, nnz 65
            - FACTOR 5 (double) SPARSE, size 11x24, density 0.19697, nnz 52
            - FACTOR 6 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F+2).toarray() - F.toarray() - 2))
            1.85775845048325e-15
            >>> F+G+2
            Faust size 10x12, density 5.4, nnz_sum 648, 9 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x30, density 0.05, nnz 30
            - FACTOR 2 (double) SPARSE, size 30x33, density 0.10101, nnz 100
            - FACTOR 3 (double) SPARSE, size 33x30, density 0.126263, nnz 125
            - FACTOR 4 (double) SPARSE, size 30x31, density 0.11828, nnz 110
            - FACTOR 5 (double) SPARSE, size 31x32, density 0.105847, nnz 105
            - FACTOR 6 (double) SPARSE, size 32x25, density 0.1225, nnz 98
            - FACTOR 7 (double) SPARSE, size 25x24, density 0.06, nnz 36
            - FACTOR 8 (double) SPARSE, size 24x12, density 0.0833333, nnz 24


            >>> float(norm((F+G+2).toarray() - F.toarray() - G.toarray() - 2))
            7.115828086306871e-15
            >>> F+G+F+2+F
            Faust size 10x12, density 11.05, nnz_sum 1326, 13 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x30, density 0.05, nnz 30
            - FACTOR 2 (double) SPARSE, size 30x40, density 0.0333333, nnz 40
            - FACTOR 3 (double) SPARSE, size 40x50, density 0.025, nnz 50
            - FACTOR 4 (double) SPARSE, size 50x53, density 0.045283, nnz 120
            - FACTOR 5 (double) SPARSE, size 53x52, density 0.0634978, nnz 175
            - FACTOR 6 (double) SPARSE, size 52x51, density 0.0678733, nnz 180
            - FACTOR 7 (double) SPARSE, size 51x55, density 0.0695187, nnz 195
            - FACTOR 8 (double) SPARSE, size 55x54, density 0.0717172, nnz 213
            - FACTOR 9 (double) SPARSE, size 54x36, density 0.063786, nnz 124
            - FACTOR 10 (double) SPARSE, size 36x34, density 0.0743464, nnz 91
            - FACTOR 11 (double) SPARSE, size 34x24, density 0.0784314, nnz 64
            - FACTOR 12 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F+G+F+2+F).toarray() - 3*F.toarray() - G.toarray() - 2))
            2.7030225852818652e-14


        \see :py:func:`Faust.__sub__`
        """
        array_types = (np.ndarray,
                       scipy.sparse.csr_matrix,
                       scipy.sparse.csc_matrix)
        brd_err = ("operands could not be broadcast"
                   " together with shapes ")
        # handle possible broadcasting of F
        # if dimensions are inconsistent it'll fail later
        if F.shape[1] == 1:
            max_ncols = np.max(
                [a.shape[1] for a in args if (
                    isinstance(a, (Faust, *array_types)) and a.ndim == 2
                )])
            F = F @ Faust(np.ones((1, max_ncols), dtype=F.dtype), dev=F.device)
        if F.shape[0] == 1:
            max_nrows = np.max(
                [a.shape[0] for a in args if isinstance(a,
                                                        (Faust,
                                                         *array_types))])
            F = Faust(np.ones((max_nrows, 1), dtype=F.dtype), dev=F.device) @ F

        def scalar2Faust(G):
            if not np.isscalar(G):
                raise TypeError("scalar must be int, float or complex")
            if np.isreal(G):
                if F.dtype == 'complex':
                    Gdtype = 'complex'
                else:
                    Gdtype = F.dtype
            else:
                Gdtype = 'complex'
            return Faust([np.full((F.shape[0], 1), G, dtype=Gdtype),
                          np.ones((1, F.shape[1]), dtype=Gdtype)],
                         dev=F.device)

        def broadcast_to_F(G):
            if G.shape[0] == 1:
                if G.shape[1] != F.shape[1]:
                    raise ve
                G = Faust(np.ones((F.shape[0], 1), dtype=F.dtype), dev=F.device) @ G
            # the next (commented) case never serves because we follow numpy broadcasting
            # i.e. only a scalar, a vector of size F.shape[1] or a 2d-array of size
            # (1, F.shape[1]) can be broadcast to F
            # according to numpy, there is no broadcasting of
            # G of shape (F.shape[0], 1) to F
#            elif G.shape[1] == 1:
#                if G.shape[0] != F.shape[0]:
#                    raise ve
#                G = G @ Faust(np.ones((1, F.shape[1]), dtype=F.dtype), dev=F.device)
            return G
        # prepare the list of Fausts
        largs = []
        for i in range(0, len(args)):
            G = args[i]
            if isinstance(G, Faust):
                ve = ValueError(brd_err +
                                str(F.shape) + " " +
                                str(G.shape) +
                                ", argument i=" + str(i))
                G = broadcast_to_F(G)
                if F.shape != G.shape:
                    raise Exception('Dimensions must agree, argument i='+str(i))
            elif isinstance(G,
                            array_types):
                if G.ndim == 1:
                    G = Faust([np.ones((F.shape[0], 1), dtype=F.dtype), G.reshape(1, G.size)], dev=F.device)
                elif G.size == 1:
                    G = scalar2Faust(G[0, 0])
                else:
                    G = broadcast_to_F(Faust(G, dev=F.device))
            elif np.isscalar(G):
                G = scalar2Faust(G)
            largs.append(G)

        C = F.concatenate(*largs, axis=1)
        id = seye(F.shape[1], dtype=C.dtype)
        id_vstack = svstack([id for i in range(0,
                                               len(largs)+1)])
        F = C@Faust(id_vstack, dev=F.device)
        return F

    def __radd__(F, lhs_op):
        r"""Returns lhs_op+F.

        \see :py:func:`Faust.__add__`,
        """
        return F.__add__(lhs_op)

    def __sub__(F, *args):
        r"""
        Subtracts from F one or a sequence of variables. Faust objects, arrays or scalars.

        NOTE: This method overloads the Python function/operator -.

        Args:
            args: (list[Faust or np.ndarray or scipy.sparse.csr_matrix])
                the list of variables to compute the difference with F. These can
                be Faust objects, arrays (and scipy.sparse.csr_matrix) or scalars.
                Faust and arrays/matrices must be of compatible sizes.

        Returns:
            the difference as a Faust object.

        Example:
            >>> import pyfaust as pf
            >>> from numpy.linalg import norm
            >>> pf.seed(42) # just for reproducibility
            >>> F = pf.rand(10, 12)
            >>> F
            Faust size 10x12, density 2.04167, nnz_sum 245, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x12, density 0.333333, nnz 40
            - FACTOR 1 (double) SPARSE, size 12x10, density 0.5, nnz 60
            - FACTOR 2 (double) SPARSE, size 10x11, density 0.454545, nnz 50
            - FACTOR 3 (double) SPARSE, size 11x10, density 0.5, nnz 55
            - FACTOR 4 (double) SPARSE, size 10x12, density 0.333333, nnz 40

            >>> G = pf.rand(10, 12)
            >>> G
            Faust size 10x12, density 2.025, nnz_sum 243, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x11, density 0.454545, nnz 50
            - FACTOR 1 (double) SPARSE, size 11x10, density 0.5, nnz 55
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x12, density 0.333333, nnz 40
            - FACTOR 4 (double) SPARSE, size 12x12, density 0.333333, nnz 48

            >>> F-G
            Faust size 10x12, density 4.43333, nnz_sum 532, 7 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x23, density 0.195652, nnz 90
            - FACTOR 2 (double) SPARSE, size 23x20, density 0.25, nnz 115
            - FACTOR 3 (double) SPARSE, size 20x21, density 0.238095, nnz 100
            - FACTOR 4 (double) SPARSE, size 21x22, density 0.205628, nnz 95
            - FACTOR 5 (double) SPARSE, size 22x24, density 0.166667, nnz 88
            - FACTOR 6 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F-G).toarray() - F.toarray() + G.toarray()))
            3.608651813623577e-15
            >>> F-2
            Faust size 10x12, density 2.84167, nnz_sum 341, 7 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x22, density 0.113636, nnz 50
            - FACTOR 2 (double) SPARSE, size 22x20, density 0.159091, nnz 70
            - FACTOR 3 (double) SPARSE, size 20x21, density 0.142857, nnz 60
            - FACTOR 4 (double) SPARSE, size 21x11, density 0.281385, nnz 65
            - FACTOR 5 (double) SPARSE, size 11x24, density 0.19697, nnz 52
            - FACTOR 6 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F-2).toarray() - F.toarray() + 2))
            0.0
            >>> F-G-2
            Faust size 10x12, density 5.4, nnz_sum 648, 9 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x30, density 0.05, nnz 30
            - FACTOR 2 (double) SPARSE, size 30x33, density 0.10101, nnz 100
            - FACTOR 3 (double) SPARSE, size 33x30, density 0.126263, nnz 125
            - FACTOR 4 (double) SPARSE, size 30x31, density 0.11828, nnz 110
            - FACTOR 5 (double) SPARSE, size 31x32, density 0.105847, nnz 105
            - FACTOR 6 (double) SPARSE, size 32x25, density 0.1225, nnz 98
            - FACTOR 7 (double) SPARSE, size 25x24, density 0.06, nnz 36
            - FACTOR 8 (double) SPARSE, size 24x12, density 0.0833333, nnz 24

            >>> float(norm((F-G-2).toarray() - F.toarray() + G.toarray() + 2))
            4.834253232627814e-15
            >>> F-G-F-2-F
            Faust size 10x12, density 11.05, nnz_sum 1326, 13 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x20, density 0.1, nnz 20
            - FACTOR 1 (double) SPARSE, size 20x30, density 0.05, nnz 30
            - FACTOR 2 (double) SPARSE, size 30x40, density 0.0333333, nnz 40
            - FACTOR 3 (double) SPARSE, size 40x50, density 0.025, nnz 50
            - FACTOR 4 (double) SPARSE, size 50x53, density 0.045283, nnz 120
            - FACTOR 5 (double) SPARSE, size 53x52, density 0.0634978, nnz 175
            - FACTOR 6 (double) SPARSE, size 52x51, density 0.0678733, nnz 180
            - FACTOR 7 (double) SPARSE, size 51x55, density 0.0695187, nnz 195
            - FACTOR 8 (double) SPARSE, size 55x54, density 0.0717172, nnz 213
            - FACTOR 9 (double) SPARSE, size 54x36, density 0.063786, nnz 124
            - FACTOR 10 (double) SPARSE, size 36x34, density 0.0743464, nnz 91
            - FACTOR 11 (double) SPARSE, size 34x24, density 0.0784314, nnz 64
            - FACTOR 12 (double) SPARSE, size 24x12, density 0.0833333, nnz 24


            >>> float(norm((F-G-F-2-F).toarray() - F.toarray() + 2*F.toarray() + G.toarray() + 2))
            1.4546887564889487e-14

        \see :py:func:`Faust.__add__`
        """

        nargs = []
        for arg in args:
            nargs += [arg*-1]
        return F.__add__(*nargs)

    def __rsub__(F, lhs_op):
        r"""Returns lhs_op-F.

        \see :py:func:`Faust.__sub__`
        """
        return F.__mul__(-1).__radd__(lhs_op)

    def __truediv__(F, s):
        r"""Divides F by the scalar s.
        This method overloads the Python function/operator `/' (whether s is a float or an integer).

        Args:
            F: (Faust)
                the Faust object.
            s: (scalar)
                the scalar to divide the Faust object with.

        Returns:
            the division result as a Faust object.

        \see :py:func:`Faust.__mul__`, :py:func:`Faust.__itruediv__`
        """
        if np.isscalar(s) or isinstance(s, np.ndarray):
            return F*(1./s)
        else:
            raise Exception("unsupported operand type(s) for /: a Faust can only be "
                  "divided by a scalar.")

    def __itruediv__(F, s):
        r"""Divides F by the scalar s inplace.
        This method overloads the Python function/operator `/=' (whether s is a
        float or an integer).

        Args:
            F: (Faust)
                the Faust object.
            s: (scalar)
                the scalar to divide the Faust object with.

        Returns:
            the division result as a Faust object.

        \see :py:func:`Faust.__mul__`, :py:func:`Faust.__truediv__`

        """
        F = F/s
        return F

    def __floordiv__(F, s):
        """
        F // s.

        Warning: this operation is not supported, it raises an exception.
        """
        raise Exception("Not supported operation")

    def __imatmul__(F, A):
        """
        Inplace operation: F = F @ A
        """
        if F.isFaust(A):
            F = F @ A
        elif isinstance(A, (csr_matrix, csc_matrix, coo_matrix, bsr_matrix,
                            np.ndarray)) and A.ndim == 2:
            F = F @ Faust(A)
        else:
            raise TypeError('Type of A is not supported')
        return F

    def __imul__(F, A):
        """
        Inplace operation: F = F * A
        """
        if isinstance(A, np.ndarray) and A.ndim == 2:
            F = F * Faust(A)
        elif np.isscalar(A):
            F = F * A
        else:
            raise TypeError('Type of A is not supported')
        return F

    def __iadd__(F, A):
        """
        Inplace operation: F = F + A
        """
        if F.isFaust(A):
            F = F+A
        elif isinstance(A, (csr_matrix, csc_matrix, coo_matrix, bsr_matrix,
                            np.ndarray)) and A.ndim == 2:
            F = F+Faust(A)
        elif np.isscalar(A):
            F = F + A
        else:
            raise TypeError('Type of A is not supported')
        return F

    def __isub__(F, A):
        """
        Inplace operation: F = F - A
        """
        if F.isFaust(A):
            F = F-A
        elif isinstance(A, (csr_matrix, csc_matrix, coo_matrix, bsr_matrix,
                            np.ndarray)) and A.ndim == 2:
            F = F-Faust(A)
        elif np.isscalar(A):
            F = F - A
        else:
            raise TypeError('Type of A is not supported')
        return F

    def __matmul__(F, A):
        r"""Multiplies F by A which is a dense numpy.matrix/numpy.ndarray or a Faust object.
        This method overloads a Python function/operator (@).

        <b>The primary goal</b> of this function is to implement “fast” multiplication by a
        Faust, which is the operation performed when A is a dense matrix.<br/>
        In the best case, F @ A is F.rcg() times faster than equivalent
        F.toarray() @ A.

        <b>Other use case</b> is available for this function:
        - If A is a Faust, no actual multiplication is performed, instead a
        new Faust is built to implement the multiplication.<br/>
        This Faust verifies that: ``(F @ A).toarray() == F.toarray() @ A.toarray()``
        (an elementwise non-significant absolute difference between the two
        members is possible).


        Args:
            F: (Faust)
                the Faust object.
            A: a Faust object, a sparse matrix (scipy.sparse.csr_matrix or dia_matrix) or a 2D full matrix (numpy.ndarray, numpy.matrix).
                In the latter case, A must be Fortran contiguous (i.e. Column-major order;
                `order' argument passed to np.ndararray() must be equal to str
                'F').
                Warning: if A is a numpy array then A.flags['F_CONTIGUOUS']
                    must be True (that is, in column-major order) or a on-the-fly
                    conversion will take place (with a little overhead).

            Note that performing a Faust-csr_matrix product is often
            slower than converting first the csr_matrix to a dense
            representation (toarray()) and then proceed to the
            Faust-dense_matrix multiplication. In some cases though,
            it stays quicker: moreover when the Faust is composed of a small number of factors.

        Returns:
            The result of the multiplication

                * as a numpy.ndarray if A is a ndarray,<br/>

                * as a Faust object if A is a Faust.

                * When either F or A is complex, G=F @ A is also complex.

        <br/>
        Raises:
            ValueError

        <br/>
        Examples:
            >>> from pyfaust import rand, seed
            >>> import numpy as np
            >>> F = rand(50, 100)
            >>> A = np.random.rand(F.shape[1], 50)
            >>> B = F@A # == F*A or F.dot(A)
            >>> # is equivalent to B = F.__matmul__(A)
            >>> G = rand(F.shape[1], 5)
            >>> H = F@G
            >>> # H is a Faust because F and G are

            The multiplying operand A can't be a scalar:
                >>> from pyfaust import rand
                >>> F = rand(5, 50)
                >>> F@2
                Traceback (most recent call last):
                ...
                ValueError: Scalar operands are not allowed, use '*' instead


        <br/>

        \see :py:func:`Faust.__init__`, :py:func:`Faust.rcg`, :py:func:`Faust.__mul__`, :py:func:`Faust.__rmatmul__`, :py:func:`Faust.dot`
        """
        if isinstance(A, Faust):
            if F.shape[1] != A.shape[0]:
                raise ValueError("The dimensions of "
                                 "the two Fausts must "
                                 "agree.")
            if F.dtype == 'complex' and A.dtype != 'complex':
                A = A.astype('complex')
            elif F.dtype != 'complex' and A.dtype == 'complex':
                F = F.astype('complex')
            return Faust(core_obj=F.m_faust.multiply_faust(A.m_faust))
        elif np.isscalar(A):
            raise ValueError("Scalar operands are not allowed, use '*'"
                             " instead")
        elif isinstance(A, np.ndarray):
            global WARNING_ON_C_CONTIGUOUS_MATMUL

            def w():
                warnings.warn("The numpy array to multiply is not "
                              "F_CONTIGUOUS, costly conversion on the "
                              "fly. Please use np.asfortranarray by "
                              "yourself.")
            if A.dtype == 'complex' and F.dtype != 'complex':
                A_r = A.real
                A_i = A.imag
                # whatever are the A.flags, real and imag will be F_CONTIGUOUS
                # == False because they don't own data (conversion needed)
                A_i = np.asfortranarray(A_i)
                A_r = np.asfortranarray(A_r)
                G = F.m_faust.multiply(A_r) + 1j*F.m_faust.multiply(A_i)
                return G
            else:
                if not A.flags['F_CONTIGUOUS']:
                    if WARNING_ON_C_CONTIGUOUS_MATMUL:
                        WARNING_ON_C_CONTIGUOUS_MATMUL = False
                        # a warning filter should be the same
                        w()
                    A = np.asfortranarray(A)
                if F.dtype == 'complex' and A.dtype != 'complex':
                    A = A.astype('complex')
                return F.m_faust.multiply(A)
        elif isinstance(A, scipy.sparse.csr_matrix):
            if A.dtype == 'complex' and F.dtype != 'complex':
                j = 1j
                return (F.__matmul__(A.real))*(1+0j) + \
                       (F.__matmul__(A.imag))*j
            else:
                return F.m_faust.multiply_csr_mat(A.astype(F.dtype))
        elif isinstance(A, (dia_matrix, csc_matrix, bsr_matrix, coo_matrix)):
            return F.__matmul__(A.tocsr())
        else:
            raise TypeError("can't multiply a Faust by something that is not a"
                            " Faust, a np.ndarray, a csr_matrix, a csc_matrix,"
                            " a coo_matrix or a dia_matrix.")

    def dot(F, A, *args, **kwargs):
        r"""Performs equivalent operation of numpy.dot() between the Faust F and A.
        More specifically:
            - Scalar multiplication if A is a scalar but F*A is preferred.
            - Matrix multiplication if A is a Faust or numpy.ndarray/numpy.matrix but F @ A is preferred.

        \see :py:func:`Faust.__init__`, :py:func:`Faust.rcg`, :py:func:`Faust.__mul__`, :py:func:`Faust.__matmul__`, :py:func:`Faust.dot`
        """
        if np.isscalar(A):
            return F*A
        return F.__matmul__(A)

    def matvec(F, x):
        r"""
        This function implements the scipy.sparse.linalg.LinearOperator.matvec function such that scipy.sparse.linalg.aslinearoperator function works on a Faust object.

        Example:
            >>> import numpy as np
            >>> import pyfaust as pf
            >>> pf.seed(42) # just for reproducibility
            >>> np.random.seed(42)
            >>> F = pf.rand(10, 10)
            >>> x = np.random.rand(F.shape[1])
            >>> F@x
            array([30.43795399, 55.16565252, 48.67306554, 34.64963666, 39.76690761,
                   47.94326492, 24.18156012, 26.61375659, 43.28975657, 60.90302137])
            >>> F.matvec(x)
            array([30.43795399, 55.16565252, 48.67306554, 34.64963666, 39.76690761,
                   47.94326492, 24.18156012, 26.61375659, 43.28975657, 60.90302137])


        \see :py:func:`Faust.dot`, :py:func:`Faust.__matmul__`
        """
        return F.dot(x)

    def __mul__(F, A):
        r"""Multiplies the Faust F by A.
        This method overloads a Python function/operator (*).

        More specifically:
        - It's a scalar multiplication if A is a scalar number.
        - if A is a vector of appropriate size, the function performs a Faust-vector broadcasting.

        Args:
            F: the Faust object.
            A: a scalar number or a (vector) numpy.ndarray or a Faust
                elementwise multiplication.

        NOTE: to compute the elementwise multiplication F * A
            column-by-column (hence avoiding calling toarray(), which consumes more
            memory) enable the environment variable PYFAUST_ELT_WISE_MUL_BY_COL.

        Returns: The result of the multiplication as a Faust (either A is a
        vector or a scalar).

        Raises: TypeError

        Examples:
            >>> from pyfaust import rand
            >>> import numpy as np
            >>> F = rand(50, 100)
            >>> v = np.random.rand(F.shape[1])
            >>> B = F*v # Faust vector broadcasting
            >>> # is equivalent to B = F.__mul__(v)
            >>> F_times_two = F*2

            Compute elementwise F * F, gives an array:
            >>> FFarray = F * F

            If the type of A is not supported:
            >>> import numpy
            >>> F*'a'
            Traceback (most recent call last):
            ...
            TypeError: must be real number, not str


        \see :py:func:`Faust.__rmul__`
        """
        if np.isscalar(A):
            if isinstance(A, int):
                A = float(A)
            elif isinstance(A, complex):
                if F.dtype != 'complex':
                    F = F.astype('complex')
            else:
                # A is a float
                if F.dtype == 'complex':
                    A = complex(A)
            return Faust(core_obj=F.m_faust.multiply_scal(A))
        elif isinstance(A, np.ndarray) and A.shape != F.shape:
            if A.size == 1:
                if A.dtype == 'complex':
                    return F*(A.squeeze().astype('complex'))
                else:
                    return F*(float(A.squeeze()))
            if A.ndim == 1 and A.size == F.shape[1] \
               or A.ndim == 2 and A.shape[0] == 1:
                return F@Faust(np.diag(A.squeeze()), dev=F.device)
        # A is a Faust or anything
        elif isinstance(A, (Faust, np.ndarray)) or issparse(A):
            return F._eltwise_mul(A)
        raise TypeError("* use is forbidden in this case. It is allowed only"
                        " for Faust-scalar multiplication or Faust vector"
                        " broadcasting.")

    def _eltwise_mul(F, A):
        if A.shape != F.shape:
            raise ValueError("Dimensions must be the same for an"
                             " elementwise multiplication of two Fausts.")
        if not isinstance(A, Faust):
            A = Faust(A) # handy but should be handled directly as an array/matrix
        k = "PYFAUST_ELT_WISE_MUL_BY_COL"
        if k in environ:
            out = np.empty(F.shape, dtype='complex' if F.dtype == 'complex'
                           or A.dtype == 'complex' else 'double')
            parallel = environ[k].startswith('parallel')
            use_thread = environ[k].endswith('thread')

            def out_col(j, ncols=1):
                for i in range(ncols):
                    F_col = F[:, j+i].toarray()
                    A_col = A[:, j+i].toarray()
                    out[:, j+i] = (F_col * A_col).reshape(F.shape[0])

            def out_col_proc(F, A, pipe):
                out = np.empty((F.shape[0], F.shape[1]), dtype='complex' if F.dtype == 'complex'
                               or A.dtype == 'complex' else 'double')
                for i in range(F.shape[1]):
                    F_col = F[:, i]
                    A_col = A[:, i]
                    out[:, i] = (F_col * A_col).reshape(F.shape[0])
                pipe[0].send(out)
            if parallel:
                from threading import Thread
                from multiprocessing import Process, Pipe
                nthreads = 4
                cols_per_thread = F.shape[1] // nthreads
                rem_cols = F.shape[1] - cols_per_thread * nthreads
                t = []
                p = []
                os = []
                col_offset = 0
                while len(t) < nthreads:
                    n = cols_per_thread + (1 if len(t) < rem_cols
                                           else 0)
                    if use_thread:
                        t.append(Thread(target=out_col, args=(col_offset, n)))
                    else:
                        p += [Pipe()]
                        o = col_offset
                        t.append(Process(target=out_col_proc,
                                         args=(F[:, o:o+n].toarray(),
                                               A[:, o:o+n].toarray(),
                                               p[-1])))
                        os += [o]
                    t[-1].start()
                    col_offset += n

                for j in range(nthreads):
                    if not use_thread:
                        if j < nthreads - 1:
                            out[:, os[j]:os[j+1]] = p[j][1].recv()
                        else:
                            out[:, os[j]:] = p[j][1].recv()
                    t[j].join()
            else:
                for j in range(F.shape[1]):
                    out_col(j)
            return out
        else:
            return F.toarray() * A.toarray()

    def __rmul__(F, lhs_op):
        r""" lhs_op*F

        \see :py:func:`Faust.__mul__`
        """
        if np.isscalar(lhs_op):
            return F.__mul__(lhs_op)
        elif isinstance(lhs_op, np.ndarray):
            #TODO: refactor with __mul__
            if lhs_op.size == 1:
                if lhs_op.dtype == 'complex':
                    return F*(lhs_op.squeeze().astype('complex'))
                else:
                    return F*(float(lhs_op.squeeze()))
            if lhs_op.ndim == 1 and lhs_op.size == F.shape[1] \
               or lhs_op.ndim == 2 and lhs_op.shape[0] == 1:
                return F@Faust(np.diag(lhs_op.squeeze()), dev=F.device)
        # A is a Faust, a numpy.ndarray (eg. numpy.matrix) or anything
        raise TypeError("* use is forbidden in this case. It is allowed only"
                        " for Faust-scalar multiplication or Faust vector"
                        " broadcasting.")

    def __rmatmul__(F, lhs_op):
        r"""Returns lhs_op.__matmul__(F).

        \see :py:func:`Faust.__matmul__`

        Examples:
            >>> from pyfaust import rand
            >>> import numpy as np
            >>> F = rand(50, 100)
            >>> A = np.random.rand(50, F.shape[0])
            >>> B = A@F # == A*F or pyfaust.dot(A, F)


        """
        if isinstance(lhs_op, (np.ndarray, csr_matrix, dia_matrix)):
            if F.dtype == 'complex' or lhs_op.dtype == 'complex':
                #return (F.H.__matmul__(lhs_op.T.conj())).T.conj()
                return (Faust([F.H.factors(i) for i in range(len(F))]).__matmul__(lhs_op.T.conj())).T.conj()
            else: # real Faust and real lhs_op
                return (F.T.__matmul__(lhs_op.T)).T
        else:
            raise TypeError("invalid type operand for Faust.__matmul__.")

    def concatenate(F, *args, **kwargs):
        """Concatenates F with len(args) Faust objects, numpy arrays or scipy sparse matrices.
        The resulting Faust:
                C = F.concatenate(G, H, ... , axis)
        verifies that:
                C.toarray() == numpy.concatenate((F.toarray(), G.toarray(),
                H.toarray(), ...), axis)

        <br/>N.B.: you could have an elementwise non-significant absolute
        difference between the two members.

        NOTE: it could be wiser to encapsulate a Faust in a
            <a href="https://faustgrp.gitlabpages.inria.fr/lazylinop/api_lazylinop.html#lazylinop.aslazylinearoperator">lazylinop.LazyLinearOp</a>
            for a lazy concatenation.


           Args:
               F: (Faust)
                   the Faust to concatenate to.
               args: the Fausts or matrices (numpy array or scipy.sparse.csr/csc_matrix)
                   The objects to be concatenated to F. If args[i] is a
                   matrix it will be Faust-converted on the fly.
               axis: (int)
                   the dimension index (0 or 1) along to concatenate the
                   Faust objects. By default, the axis is 0 (for vertical
                   concatenation).

            Returns:
                The concatenation result as a Faust.

            Raises:
                ValueError


            Examples:
                >>> from pyfaust import rand, seed
                >>> F = rand(50, 50)
                >>> G = rand(50, 50)
                >>> F.concatenate(G) # equivalent to F.concatenate(G, 0)
                Faust size 100x50, density 0.52, nnz_sum 2600, 6 factor(s):
                - FACTOR 0 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 1 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 2 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 3 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 4 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 5 (double) SPARSE, size 100x50, density 0.02, nnz 100

                >>> F.concatenate(G, axis=1)
                Faust size 50x100, density 0.52, nnz_sum 2600, 6 factor(s):
                - FACTOR 0 (double) SPARSE, size 50x100, density 0.02, nnz 100
                - FACTOR 1 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 2 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 3 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 4 (double) SPARSE, size 100x100, density 0.05, nnz 500
                - FACTOR 5 (double) SPARSE, size 100x100, density 0.05, nnz 500

                >>> from numpy.random import rand
                >>> F.concatenate(rand(34, 50), axis=0) # The random array is auto-converted to a Faust before the vertical concatenation
                Faust size 84x50, density 0.773809, nnz_sum 3250, 6 factor(s):
                - FACTOR 0 (double) SPARSE, size 84x100, density 0.232143, nnz 1950
                - FACTOR 1 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 2 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 3 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 4 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 5 (double) SPARSE, size 100x50, density 0.02, nnz 100

                >>> from scipy.sparse import rand as sprand
                >>> F.concatenate(sprand(50, 24, format='csr'), axis=1) # The sparse random matrix is auto-converted to a Faust before the horizontal concatenation
                Faust size 50x74, density 0.422162, nnz_sum 1562, 6 factor(s):
                - FACTOR 0 (double) SPARSE, size 50x100, density 0.02, nnz 100
                - FACTOR 1 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 2 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 3 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 4 (double) SPARSE, size 100x100, density 0.03, nnz 300
                - FACTOR 5 (double) SPARSE, size 100x74, density 0.0354054, nnz 262

                >>> F.concatenate(F, G, F, G, rand(34, 50), F, G) # it's allowed to concatenate an arbitrary number of Fausts
                Faust size 384x50, density 0.575521, nnz_sum 11050, 6 factor(s):
                - FACTOR 0 (double) SPARSE, size 384x400, density 0.0224609, nnz 3450
                - FACTOR 1 (double) SPARSE, size 400x400, density 0.01125, nnz 1800
                - FACTOR 2 (double) SPARSE, size 400x400, density 0.01125, nnz 1800
                - FACTOR 3 (double) SPARSE, size 400x400, density 0.01125, nnz 1800
                - FACTOR 4 (double) SPARSE, size 400x400, density 0.01125, nnz 1800
                - FACTOR 5 (double) SPARSE, size 400x50, density 0.02, nnz 400

                >>> from pyfaust import rand
                >>> F = rand(2, 51)
                >>> G = rand(2, 25)
                >>> F.concatenate(G, 0)
                Traceback (most recent call last):
                ...
                ValueError: The dimensions of the two Fausts must agree.
                >>> from pyfaust import rand
                >>> F = rand(2, 50);
                >>> G = rand(2, 50);
                >>> F.concatenate(G, axis=5)
                Traceback (most recent call last):
                ...
                ValueError: Axis must be 0 or 1.
                >>> from pyfaust import rand
                >>> F = rand(2, 5);
                >>> G = rand(2, 5);
                >>> F.concatenate(G, 'a')
                Traceback (most recent call last):
                ...
                ValueError: You can't concatenate a Faust with something that is not a Faust, a numpy array or scipy sparse matrix.


        """
        if "axis" in kwargs.keys():
            axis = kwargs['axis']
        else:
            axis = 0
        if axis not in [0, 1]:
            raise ValueError("Axis must be 0 or 1.")

        largs = []
        largest_dtype = F.dtype
        for i, G in enumerate(args):
            if isinstance(G, (np.ndarray, csr_matrix, csc_matrix)):
                G = Faust(G, dev=F.device)
            elif not isinstance(G, Faust):
                raise ValueError("You can't concatenate a "
                                 "Faust with something "
                                 "that is not a Faust, "
                                 "a numpy array or scipy "
                                 "sparse matrix.")
            largest_dtype = G.dtype if np.dtype(G.dtype).itemsize > np.dtype(largest_dtype).itemsize else largest_dtype
            largs.append(G)

            if (axis == 0 and F.shape[1] != G.shape[1] or axis == 1 and F.shape[0]
                    != G.shape[0]):
                raise ValueError("The dimensions of "
                                 "the two Fausts must "
                                 "agree.")

            for i in range(len(largs)):
                if largs[i].dtype != largest_dtype:
                    largs[i] = largs[i].astype(largest_dtype)
            if F.dtype != largest_dtype:
                F = F.astype(largest_dtype)

        if all([isFaust(G) for G in largs]) and "iterative" not in kwargs.keys() or kwargs['iterative']:
            # use iterative meth.
            if axis == 0:
                C = Faust(core_obj=F.m_faust.vertcatn([G.m_faust for G in largs]))
            else: # axis == 1
                C = Faust(core_obj=F.m_faust.horzcatn([G.m_faust for G in largs]))
            return C

        # use recursive meth.
        C = F
        for G in args:
            if not isFaust(G):
                G = Faust(G)
            if C.dtype != G.dtype:
                G = G.astype(C.dtype)
            if axis == 0:
                C = Faust(core_obj=C.m_faust.vertcat(G.m_faust))
            elif axis == 1:
                C = Faust(core_obj=C.m_faust.horzcat(G.m_faust))

        return C

    def toarray(F):
        r"""Returns a numpy array for the full matrix implemented by F.

        WARNING: Using this function is discouraged except for test purposes,
            as it loses the main potential interests of the Faust structure:
            compressed memory storage and faster matrix-vector multiplication
            compared to its equivalent full matrix representation.

        Returns:
            A numpy ndarray.

        Raises:
            MemoryError

        WARNING: running the example below is likely to raise a memory
            error or freeze your computer for a certain amount of time.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(10**5, 10**5, 2, 10**5, density=10**-4, fac_type='sparse')
            >>> F
            Faust size 100000x100000, density 0.00018, nnz_sum 1800000, 2 factor(s):
            - FACTOR 0 (double) SPARSE, size 100000x100000, density 9e-05, nnz 900000
            - FACTOR 1 (double) SPARSE, size 100000x100000, density 9e-05, nnz 900000
            >>> # an attempt to convert F to a dense matrix is most likely to raise a memory error
            >>> # the sparse format is the only way to handle such a large Faust
            >>> F.toarray()
            Traceback (most recent call last):
            ...
            numpy._core._exceptions._ArrayMemoryError: Unable to allocate 74.5 GiB for an array with shape (100000, 100000) and data type float64

        \see :py:func:`Faust.todense`
        """
        return F.m_faust.get_product()

    def todense(F):
        r"""Returns a numpy matrix for the full matrix implemented by F.

        WARNING: Using this function is discouraged except for test purposes,
            as it loses the main potential interests of the Faust structure:
            compressed memory storage and faster matrix-vector multiplication
            compared to its equivalent full matrix representation.

        WARNING: this function is deprecated in favor to toarray function and
            will be removed in a future version. The cause behind is that this
            function returns a numpy.matrix which is deprecated too.

        Returns:
            A numpy matrix M such that M*x == F*x for any vector x.

        Raises:
            MemoryError

        WARNING: running the example below is likely to raise a memory
            error or freeze your computer for a certain amount of time.

        WARNING: this function is deprecated and might be deleted in future
            versions of pyfaust. Please use :func:`Faust.toarray` instead.

        \see :py:func:`Faust.toarray`
        """
        warnings.warn("Faust.todense() is deprecated and will be deleted in the "
                      "future.")
        return np.matrix(F.toarray())

    def __getitem__(F, indices):
        """Indexes or slices a Faust.
        Returns a Faust representing a submatrix of F.toarray() or a scalar element if that Faust can be reduced to a single element.
        This function overloads a Python built-in.

        WARNING:
                - This function doesn't implement F[l1, l2] where l1 and l2 are
                  integer lists, rather use F[l1][:, l2].
                - It is not advised to use this function as an element accessor
                  (e.g. F[0, 0]) because such a use induces to convert the Faust to its
                  dense matrix representation and that is a very expensive computation if used
                  repetitively.
                - Subindexing a Faust which would create an empty Faust will raise
                  an error.
                - 'Fancy indexing' must be done with a list not a numpy array.

        Args:
            F: (Faust)
                the Faust object.
            indices: (list)
                array of length 1 or 2 which elements must be slice, integer or
                Ellipsis (...) (see examples below). Note that using Ellipsis for
                more than two indices is forbidden.

        Returns:
            the Faust object requested or just the corresponding scalar if that Faust has
            a shape equal to (1, 1).

        Raises:
            IndexError


        Examples:
            >>> from pyfaust import rand, seed
            >>> import numpy as np
            >>> from numpy.random import randint, seed as rseed
            >>> seed(42) # just for reproducibility
            >>> rseed(42)
            >>> F = rand(50, 100)
            >>> i1 = randint(1, min(F.shape)-1)
            >>> i2 = randint(1, min(F.shape)-1)

            >>> # the scalar element located at
            >>> # at row i1, column i2 of the F dense matrix
            >>> F[i1, i2]
            0.0

            >>> F[:, i2] # full column i2
            Faust size 50x1, density 24.64, nnz_sum 1232, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.045977, nnz 200
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x1, density 0, nnz 0

            >>> # from row 2 to 3, each row containing
            >>> # only elements from column 1 to 3
            >>> F[2:4, 1:4]
            Faust size 2x3, density 174.833, nnz_sum 1049, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 2x87, density 0.045977, nnz 8
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x3, density 0.05, nnz 9

            >>> # from row 0 to end row, each row
            >>> # containing only elements from column 4 to
            >>> # column before the last one.
            >>> F[::, 4:-1]
            Faust size 50x95, density 0.318947, nnz_sum 1515, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.045977, nnz 200
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x95, density 0.0496491, nnz 283

            >>> F[0:i1, ...] # equivalent to F[0:i1, ::]
            Faust size 39x100, density 0.381538, nnz_sum 1488, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 39x87, density 0.045977, nnz 156
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x100, density 0.05, nnz 300

            >>> F[2::, :3:] # equivalent to F[2:F.shape[0], 0:3]
            Faust size 48x3, density 8.56944, nnz_sum 1234, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 48x87, density 0.045977, nnz 192
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x3, density 0.0555556, nnz 10

            >>> F[0:i2:2, :] # takes every row of even index until the row i2 (excluded)
            Faust size 15x100, density 0.928, nnz_sum 1392, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 15x87, density 0.045977, nnz 60
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x100, density 0.05, nnz 300

            >>> F[-1:-3:-1, :] # takes the two last rows in reverse order
            Faust size 2x100, density 6.7, nnz_sum 1340, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 2x87, density 0.045977, nnz 8
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x100, density 0.05, nnz 300

            >>> F[i2:0:-2, :] # starts from row i2 and goes backward to take one in two rows until the first one (reversing order of F)
            Faust size 15x100, density 0.928, nnz_sum 1392, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 15x87, density 0.045977, nnz 60
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x100, density 0.05, nnz 300

            >>> F[[1, 18, 2], :] # takes in this order the rows 1, 18 and 2
            Faust size 3x100, density 4.48, nnz_sum 1344, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 3x87, density 0.045977, nnz 12
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x100, density 0.05, nnz 300

            >>> F[:, [1, 18, 2]] # takes in this order the columns 1, 18 and 2
            Faust size 50x3, density 8.27333, nnz_sum 1241, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 50x87, density 0.045977, nnz 200
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x3, density 0.05, nnz 9

            >>> F[[1, 18, 2]][:, [1, 2]] # takes the rows 1, 18 and 2 but keeps only columns 1 and 2 in these rows
            Faust size 3x2, density 175, nnz_sum 1050, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 3x87, density 0.045977, nnz 12
            - FACTOR 1 (double) SPARSE, size 87x63, density 0.0793651, nnz 435
            - FACTOR 2 (double) SPARSE, size 63x69, density 0.057971, nnz 252
            - FACTOR 3 (double) SPARSE, size 69x60, density 0.0833333, nnz 345
            - FACTOR 4 (double) SPARSE, size 60x2, density 0.05, nnz 6


        """
        #TODO: refactor (by index when indices == tuple(2), error message,
        #      out_indices checking on the end)
        empty_faust_except = Exception("Cannot create empty Faust.")
        idx_error_exception = IndexError("only integers, slices (`:`), ellipsis"
                                         " (`...`), and integer are valid indices")
        if isinstance(indices, np.ndarray):
            indices = list(indices)
        if indices == Ellipsis: # F[...]
            out_indices = [slice(0, F.shape[0]), slice(0, F.shape[1])]
        elif isinstance(indices, int): # F[i] # a row
            out_indices = [slice(indices, indices+1), slice(0, F.shape[1])]
        elif isinstance(indices, slice):
            #F[i:j] a group of contiguous lines
            out_indices = [indices, slice(0, F.shape[1])]
        elif isinstance(indices, list):
            out_indices = [indices, slice(0, F.shape[1])]
            #TODO: check indices are all integers lying into F shape
        elif isinstance(indices, tuple):
            if len(indices) == 1:
                return F.__getitem__(indices[0])
            if len(indices) == 2:
                out_indices = [0, 0]
                if isinstance(indices[0], int) and isinstance(indices[1], int):
                    if 'OPT_GET_ITEM' in environ and environ['OPT_GET_ITEM'] == '0':
                        return F.toarray()[indices[0], indices[1]]
                    else:
                        return F.m_faust.get_item(indices[0], indices[1])
                if isinstance(indices[0], np.ndarray):
                    indices = (list(indices[0]), indices[1])
                if isinstance(indices[1], np.ndarray):
                    indices = (indices[0], list(indices[1]))
                if indices[0] == Ellipsis:
                    if indices[1] == Ellipsis:
                        raise IndexError('an index can only have a single ellipsis '
                                         '(\'...\')')
                    else:
                        # all rows
                        out_indices[0] = slice(0, F.shape[0])
                elif isinstance(indices[0], int):
                    # row F[i]
                    out_indices[0] = slice(indices[0], indices[0]+1)
                elif isinstance(indices[0], slice):
                    out_indices[0] = indices[0]
                elif isinstance(indices[0], list):
                    if len(indices[0]) == 0:
                        raise empty_faust_except
                    out_indices[0] = indices[0]
                else:
                    raise idx_error_exception
                if indices[1] == Ellipsis:
                    # all columns
                    out_indices[1] = slice(0, F.shape[1])
                elif isinstance(indices[1], int):
                    # col F[i]
                    out_indices[1] = slice(indices[1], indices[1]+1)
                elif isinstance(indices[1], slice):
                    out_indices[1] = indices[1]
                elif isinstance(indices[1], list):
                    if isinstance(indices[0], list):
                        raise Exception("F[list1, list2] error: fancy indexing "
                                        "on both dimensions is not implemented "
                                        "rather use F[list1][:, list2].")
                    if len(indices[1]) == 0:
                        raise empty_faust_except
                    out_indices[1] = indices[1]
                else:
                    raise idx_error_exception
            else:
                raise IndexError('Too many indices.')
        else:
            raise idx_error_exception

        for i in range(0, 2):
            if isinstance(out_indices[i], slice):
                if out_indices[i].start is None and out_indices[i].stop is None:
                    #F[::] or F[::, any] or F[any, ::]
                    out_indices[i] = slice(0, F.shape[i], out_indices[i].step)
                elif out_indices[i].start is None: # out_indices[i].stop != None
                    out_indices[i] = slice(0, out_indices[i].stop,
                                           out_indices[i].step)
                elif out_indices[i].stop is None: # out_indices[i].start != None
                    out_indices[i] = slice(out_indices[i].start,
                                           F.shape[i], out_indices[i].step)
                if out_indices[i].stop < 0:
                    out_indices[i] = slice(out_indices[i].start,
                                           F.shape[i]+out_indices[i].stop,
                                           out_indices[i].step)

                if out_indices[i].step is None:
                    out_indices[i] = slice(out_indices[i].start,
                                           out_indices[i].stop,
                                           1)
                if out_indices[i].start < 0:
                    out_indices[i] = \
                            slice(F.shape[i]+out_indices[i].start, out_indices[i].stop,
                                  out_indices[i].step)

                if out_indices[i].start >= F.shape[i] or out_indices[i].stop > F.shape[i]:
                    raise IndexError("index " +
                                     str(max(out_indices[i].start, out_indices[i].stop-1)) +
                                     " is out of bounds for axis "+str(i)+" with size " +
                                     str(F.shape[i]))

                # transform slice with neg. step to a list for using fancy
                # indexing
                # likewise for step > 1
                if out_indices[i].step < 0 or out_indices[i].step > 1:
                    out_indices[i] = \
                            list(range(out_indices[i].start, out_indices[i].stop, out_indices[i].step))
                    if len(out_indices[i]) == 0:
                        raise empty_faust_except
                elif out_indices[i].start >= out_indices[i].stop:
                    raise empty_faust_except
                elif out_indices[i].step == 0:
                    raise ValueError("slice step cannot be zero")

        if isinstance(out_indices[0], list) or \
           isinstance(out_indices[1], list):
            sub_F = Faust(core_obj=F.m_faust.fancy_idx(out_indices))
        else:
            sub_F = Faust(core_obj=F.m_faust.slice(out_indices))

        return sub_F

    def nnz_sum(F):
        r"""Gives the total number of non-zero elements in the factors of F.

        The function sums together the number of non-zero elements of
        each factor and returns the result. Note that for efficiency the sum is
        computed at Faust creation time and kept in cache.

        Returns:
            the number of non-zeros.

        Example:
            >>> import pyfaust as pf
            >>> F = pf.rand(1024, 1024)
            >>> F
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> F.nnz_sum()
            25600

        \see :py:func:`Faust.rcg`, :py:func:`Faust.density.`
        """
        return F.m_faust.nnz()

    def density(F):
        r""" Calculates the density of F such that ``F.nnz_sum() == F.density() * F.size``.

        NOTE: A value of density below one indicates potential memory savings
        compared to storing the corresponding dense matrix F.toarray(), as well
        as potentially faster matrix-vector multiplication when applying F @ x
        instead of F.toarray() @ x.

        NOTE: A density above one is possible but prevents any saving.

        Args:
            F: the Faust object.

        Returns:
            the density value (float).

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(5, 50, density=.5)
            >>> dens = F.density()

        \see :py:func:`Faust.nnz_sum`, :py:func:`Faust.rcg`, :py:func:`Faust.size`, :py:func:`Faust.toarray`
        """
        return float(F.nnz_sum())/F.size

    def rcg(F):
        r"""Computes the Relative Complexity Gain.

        The RCG is the theoretical gain brought by the Faust representation relatively to its dense
        matrix equivalent. <br/>The higher is the RCG, the more computational
        savings are made.
        This gain applies both for storage space and computation time.

        NOTE: F.rcg() == 1/F.density()

        Args:
            F: the Faust object.

        Returns:
            the RCG value (float).

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(1024, 1024)
            >>> float(F.rcg())
            40.96
            >>> F
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> float(F.size / F.nnz_sum())
            40.96

        \see :py:func:`Faust.density`, :py:func:`Faust.nnz_sum`, :py:func:`Faust.shape.`
        """
        d = F.density()
        if d > 0:
            return 1/d
        elif d == 0:
            return float("inf")
        else:
            return float(-1)

    def norm(F, ord='fro', **kwargs): #**kwargs):
        r"""Computes the norm of F.
        Several types of norm are available: 1-norm, 2-norm, inf-norm and Frobenius norm.
        The norm of F is equal to the numpy.linalg.norm of F.toarray().

        WARNING:
            The norm computation time can be expected to be of order
            n*min(F.shape) with n the time for multipliying F by a vector.
            Nevertheless, the implementation allows that memory usage remains
            controlled by avoiding to explicitly compute F.toarray(). Please pay
            attention to the full_array (and batch_size) arguments for a better
            understanding.

        Args:
            F: (Faust)
                the Faust object.
            ord: (int or str)
                the norm order (1, 2, numpy.inf) or "fro" for
                Frobenius norm (by default the Frobenius norm is computed).
            threshold: (float)
                power iteration algorithm threshold (default
                to .001). Used only for norm(2).
            max_num_its: (int)
                maximum number of iterations for
                power iteration algorithm (default to 100). Used only for norm(2).
            full_array: (bool)
                this argument applies only for 1-norm,
                inf-norm and Frobenius norm. If True the Faust full array
                is computed before computing the norm otherwise it is not. By
                default it is set to False. Many configurations exist in which
                full_array == False can be more efficient but it needs to
                finetune the batch_size argument.
            batch_size: (int)
                this argument applies only when the
                full_array argument is set to False (for the 1-norm, inf-norm and
                Frobenius norm). It determines the number of Faust columns (resp. rows)
                that are built in memory in order to compute the Frobenius norm and
                the 1-norm (resp. the inf-norm). This parameter is primary in the
                efficiency of the computation and memory consumption. By  default,
                it is set to 1 (which is certainly not the optimal configuration in
                many cases in matter of computation time but always the best in
                term of memory cost).

        Returns:
            the norm (float).

                * If ord == 1,
                    the norm is `norm(F.toarray(), 1) == max(sum(abs(F.toarray())))`.

                * If ord == 2,
                    the norm is the maximum singular value of F or approximately
                    `norm(F.toarray(), 2) == max(scipy.linalg.svd(F.toarray())[1])`.
                    This is the default norm calculated when calling to norm(F).

                * If ord == numpy.inf,
                    the norm is `norm(F.toarray(), numpy.inf) == max(sum(abs(F.T.toarray())))`

                * If ord == 'fro',
                    the norm is `norm(F.toarray(), 'fro')`.

        Raises:
            ValueError.


        <br/>
        Examples:
            >>> from pyfaust import rand, seed
            >>> import numpy as np
            >>> seed(42) # just for reproducibility
            >>> F = rand(50, 100, [1, 2], density=.5)
            >>> F.norm()
            388.2689201639318
            >>> F.norm(2)
            382.3775910865066
            >>> F.norm('fro')
            388.2689201639318
            >>> F.norm(np.inf)
            624.0409076619496

        \see :py:func:`Faust.normalize`
        """
        if ord not in [1, 2, "fro", np.inf]:
            raise ValueError("ord must have the value 1, 2, 'fro' or numpy.inf.")
        return F.m_faust.norm(ord, **kwargs)

    def power_iteration(self, threshold=1e-3, maxiter=100):
        """Performs the power iteration algorithm to compute the greatest eigenvalue of the Faust.

        For the algorithm to succeed the Faust should be diagonalizable
        (similar to a digonalizable Faust), ideally, a symmetric positive-definite Faust.

        Args:
            threshold: the precision required on the eigenvalue.
            maxiter: the number of iterations above what the algorithm will stop anyway.

        Returns:
            The greatest eigenvalue approximate.

        Examples:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(50, 50)
            >>> F = F@F.H
            >>> float(F.power_iteration())
            12653.806783532553

        """
        return self.m_faust.power_iteration(threshold=threshold,
                                            max_num_its=maxiter)

    def normalize(F, ord='fro', axis=1):
        r"""Normalizes F along the axis dimension using the ord-norm.
        The function is able to normalize the columns (default axis=1):

            NF = F.normalize(ord) is such that for all i in range(0, F.shape[1]) NF.toarray()[:, i] == F.toarray()[:, i]/norm(F.toarray(), ord)

        Likewise for normalization of the rows (axis=0):

            NF = F.normalize(ord, axis=0) is such that for all i in range(0, F.shape[0]) NF.toarray()[i, :] == F.toarray()[i, :]/norm(F.toarray(), ord)

        The variable ord designates one of the :func:`Faust.norm()` compatible norms.

        Args:
            ord: the norm order to use (see :py:func:`Faust.norm`).
            axis: if 1 the columns are normalized, if 0 the rows.

        Returns:
            the normalized Faust

        Example:
            >>> from numpy.linalg import norm
            >>> import numpy as np
            >>> import pyfaust as pf
            >>> pf.seed(42) # just for reproducibility
            >>> F = pf.rand(10, 10)
            >>> F
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> # normalize columns according to default fro-norm/2-norm
            >>> # then test the second column is properly normalized
            >>> nF2 = F.normalize()
            >>> nF2
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> float(norm(nF2[:, 1].toarray() - F[:, 1].toarray()/F[:, 1].norm()))
            1.0385185452638061e-16
            >>>
            >>> # this time normalize rows using 1-norm and test the third row
            >>> nF1 = F.normalize(ord=1, axis=0)
            >>> nF1
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50


            >>> float(norm(nF1[2, :].toarray() - F[2, :].toarray()/F[2, :].norm(ord=1)))
            2.5438405243138006e-16
            >>>
            >>> # and the same with inf-norm
            >>> nFinf = F.normalize(ord=np.inf, axis=0)
            >>> float(norm(nFinf[2, :].toarray() - F[2, :].toarray()/F[2, :].norm(ord=np.inf)))
            5.238750013840908e-17


        \see :py:func:`Faust.norm`
        """
        if ord not in [1, 2, np.inf, "fro"]:
            raise ValueError("ord must have the value 1, 2, 'fro' or "
                             "numpy.inf.")
        if axis not in [0, 1]:
            raise ValueError("Invalid axis.")
        if ord == float('Inf') or ord == np.inf:
            ord = -1
        elif ord == "fro":
            ord = -2
        if axis == 0:
            tF = F.T
            if ord == -1:
                ord = 1
            elif ord == 1:
                ord = -1
            NF = Faust(core_obj=tF.m_faust.normalize(ord))
            NF = NF.T
        else:
            NF = Faust(core_obj=F.m_faust.normalize(ord))
        return NF

    def numfactors(F):
        r"""
        Returns the number of factors of F.

        NOTE: using len(F) is more shorter!

        Returns:
            the number of factors.

        Examples:
        >>> from pyfaust import rand
        >>> F = rand(100, 100, num_factors=2, density=.5)
        >>> nf = F.numfactors()
        >>> nf
        2
        >>> nf == len(F)
        True

        \see :py:func:`Faust.factors`, :py:func:`Faust.__len__`
        """
        return F.m_faust.get_nb_factors()

    def __len__(F):
        r"""
        Returns the number of factors of F.

        Returns:
            the number of factors.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(50, 100)
            >>> nf = F.numfactors()
            >>> nf
            5
            >>> nf == len(F)
            True

        \see :py:func:`Faust.factors`, :py:func:`Faust.numfactors`
        """
        return F.numfactors()

    def factors(F, indices, as_faust=False):
        r"""
        Returns the i-th factor of F or a new Faust composed of F factors whose indices are listed in indices.

        Note: Factors are copied in memory.

        Args:
            F: (Faust)
                the Faust object.
            indices: (list[int])
                the indices of wanted factors.
            as_faust: (bool)
                True to return a Faust even if a single factor is asked,
                otherwise (as_faust == False) and a numpy array or a scipy
                sparse matrix is returned.

        Returns:
            if indices is a single index and as_faust == False: a copy of the i-th factor.
            Otherwise a new Faust composed of the factors of F pointed by
            indices (no copy is made).
            For a single factor (with as_faust == False), the matrix type is:

                * numpy.ndarray if it is a full storage matrix or,

                * scipy.sparse.csc.matrix_csc if it's a sparse matrix of a
                transposed Faust,

                * scipy.sparse.csr.csr_matrix if it's a sparse matrix of a
                non-transposed Faust.

                * a scipy.sparse.bsr matrix if the factor is a BSR matrix.


        <br/>
        Raises:
            ValueError.


        <br/>
        Example:
            >>> from pyfaust import rand
            >>> F = rand(5, 10)
            >>> f0 = F.factors(0)
            >>> G = F.factors(range(3, 5)) # a new Faust composed of the two last factors of F

        <br/>

        \see :py:func:`Faust.numfactors`, :py:func:`Faust.transpose`, :py:func:`Faust.left`, :py:func:`Faust.right`
        """
        if hasattr(indices, '__iter__'):
            indices = list(indices)
        else:
            indices = list([indices])
        for i in indices:
            if not isinstance(i, int):
                raise TypeError("Index must be an integer.")
        if len(indices) == 1 and not as_faust:
            return F.m_faust.get_fact_opt(indices[0])
        else:
            return Faust(core_obj=F.m_faust.factors(indices))

    def right(F, i, as_faust=False):
        r"""Returns the right hand side factors of F from index i to F.numfactors()-1.

        Args:
            F: (Faust)
                the Faust from which to extract right factors.
            i: (int)
                the far left index of right factors to extract.
            as_faust: (bool)
                True to return a Faust even if a single factor is asked
                (i.e.: F.right(len(F)-1, as_faust=True) is a Faust, F.left(len(F)-1) is not).

        Returns:
            a Faust if the number of factors to be returned is greater than 1
            or if as_faust == True,
            a numpy array or a sparse matrix otherwise.

        Examples:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(5, 10, 5)
            >>> RF = F.right(2)
            >>> print(F)
            Faust size 5x10, density 2.98, nnz_sum 149, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 5x9, density 0.555556, nnz 25
            - FACTOR 1 (double) SPARSE, size 9x6, density 0.666667, nnz 36
            - FACTOR 2 (double) SPARSE, size 6x7, density 0.714286, nnz 30
            - FACTOR 3 (double) SPARSE, size 7x6, density 0.666667, nnz 28
            - FACTOR 4 (double) SPARSE, size 6x10, density 0.5, nnz 30

            >>> print(RF)
            Faust size 6x10, density 1.46667, nnz_sum 88, 3 factor(s):
            - FACTOR 0 (double) SPARSE, size 6x7, density 0.714286, nnz 30
            - FACTOR 1 (double) SPARSE, size 7x6, density 0.666667, nnz 28
            - FACTOR 2 (double) SPARSE, size 6x10, density 0.5, nnz 30



        \see :py:func:`Faust.factors`, :py:func:`Faust.left`, :py:func:`Faust.numfactors`,
        """
        i = F._check_factor_idx(i)
        rF = Faust(core_obj=F.m_faust.right(i))
        if len(rF) == 1 and not as_faust:
            return rF.factors(0)
        return rF

    def left(F, i, as_faust=False):
        r"""
        Returns the left hand side factors of F from index 0 to i included.

        Args:
            F: (Faust)
                the Faust from which to extract left factors.
            i: (int)
                the far right index of left factors to extract.
            as_faust: (bool)
                True to return a Faust even if a single factor is asked
                (i.e.: F.left(0, as_faust=True) is a Faust, F.left(0) is not).

        Returns:
            a Faust if the number of factors to be returned is greater than 1
            or if as_faust == True,
            a numpy array or a sparse matrix otherwise.

        Examples:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(5, 10, 5)
            >>> LF = F.left(3)
            >>> print(F)
            Faust size 5x10, density 2.98, nnz_sum 149, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 5x9, density 0.555556, nnz 25
            - FACTOR 1 (double) SPARSE, size 9x6, density 0.666667, nnz 36
            - FACTOR 2 (double) SPARSE, size 6x7, density 0.714286, nnz 30
            - FACTOR 3 (double) SPARSE, size 7x6, density 0.666667, nnz 28
            - FACTOR 4 (double) SPARSE, size 6x10, density 0.5, nnz 30

            >>> print(LF)
            Faust size 5x6, density 3.96667, nnz_sum 119, 4 factor(s):
            - FACTOR 0 (double) SPARSE, size 5x9, density 0.555556, nnz 25
            - FACTOR 1 (double) SPARSE, size 9x6, density 0.666667, nnz 36
            - FACTOR 2 (double) SPARSE, size 6x7, density 0.714286, nnz 30
            - FACTOR 3 (double) SPARSE, size 7x6, density 0.666667, nnz 28


        \see :py:func:`Faust.factors`, :py:func:`Faust.right`
        """
        i = F._check_factor_idx(i)
        lF = Faust(core_obj=F.m_faust.left(i))
        if len(lF) == 1 and not as_faust:
            return lF.factors(0)
        return lF

    def replace(F, i, new_factor):
        r"""
        Replaces the factor of index i by new_factor in a new Faust copy of F.

        NOTE: this is not a true copy, only references to pre-existed factors
        are copied.

        Args:
            i: (int)
                The factor index to replace.
            new_factor: (a numpy array or a scipy matrix)
                The factor replacing the i-th factor of F.

        Returns:
            a copy of F with the i-th factor replaced by new_factor.

        Raises:
            ValueError: in case new_factor has invalid dimensions.

            ValueError: if i is out of range.

            TypeError: if i is not an integer.

        Example:
            >>> import numpy as np
            >>> import pyfaust as pf
            >>> from scipy.sparse import random
            >>> F = pf.rand(10, 10, num_factors=5)
            >>> S = random(10, 10, .2)
            >>> G = F.replace(2, S)
            >>> np.allclose((F.left(1) @ pf.Faust(S) @ F.right(3)).toarray(), G.toarray())
            True


        \see :py:func:`Faust.factors`, :py:func:`Faust.left`, :py:func:`Faust.right`, :py:func:`Faust.insert`
        """
        F._check_factor_idx(i)
        cur_fac_shape = F.m_faust.get_fact_shape(i)

        if cur_fac_shape != new_factor.shape:
            raise ValueError('Dimensions must agree')
        if i > 0:
            out_F = F.left(i - 1, as_faust=True) @ Faust(new_factor)
        else:
            out_F = Faust(new_factor)
        if i < len(F) - 1:
            out_F = out_F @ F.right(i + 1, as_faust=True)
        return out_F

    def insert(F, i, new_factor):
        r"""
        Inserts new_factor at index i in a new Faust copy of F.

        NOTE: this is not a true copy, only references to pre-existed factors
        are copied.

        Args:
            i: (int)
                The index of insertion.
            new_factor: (a numpy array or a scipy matrix)
                The factor to insert as the i-th factor of F.

        Returns:
            a copy of F with new_factor inserted at index i.

        Raises:
            ValueError: in case new_factor has invalid dimensions.

            ValueError: if i is out of range.

            TypeError: if i is not an integer.

        Example:
            >>> import numpy as np
            >>> import pyfaust as pf
            >>> from scipy.sparse import random
            >>> F = pf.rand(10, 10, num_factors=5)
            >>> S = random(10, 10, .2)
            >>> G = F.insert(2, S)
            >>> np.allclose((F.left(1) @ pf.Faust(S) @ F.right(2)).toarray(), G.toarray())
            True


        \see :py:func:`Faust.factors`, :py:func:`Faust.left`, :py:func:`Faust.right`, :py:func:`Faust.replace`
        """
        F._check_factor_idx(i)
        if i == 0:
            expected_shape = (new_factor.shape[0],
                              F.m_faust.get_fact_shape(0)[0])
        elif i == len(F) - 1:
            # i > 0, hence fact i-1 exists
            expected_shape = (F.m_faust.get_fact_shape(i-1)[1],
                              new_factor.shape[1])
        else:
            expected_shape = (F.m_faust.get_fact_shape(i-1)[1],
                              F.m_faust.get_fact_shape(i)[0])
        if expected_shape != new_factor.shape:
            raise ValueError('Dimensions must agree')
        out_F = None
        if i > 0:
            out_F = F.left(i-1, as_faust=True) @ Faust(new_factor)
        else:
            out_F = Faust(new_factor)
        out_F = out_F @  F.right(i, as_faust=True)
        return out_F

    def _check_factor_idx(F, i):
        if not np.isscalar(i) or not np.isreal(i):
            raise TypeError('i must be an integer.')
        i = int(np.floor(i))
        if i < 0 or i >= F.numfactors():
            raise ValueError('i is out of range.')
        return i

    def get_factor_nonopt(F, i):
        r"""
        DEPRECATED: use :func:`Faust.factors`
        Returns the i-th factor of F.

        Args:
            F: (Faust)
                the Faust object.
            i: (int)
                the factor index.

        Returns:
            a copy of the i-th factor as a dense matrix (of type numpy.ndarray).

        Raises:
            ValueError.


        Examples:
            >>> from pyfaust import rand
            >>> F = rand(5, 10)
            >>> f0 = F.factors(0)

        \see :py:func:`Faust.numfactors`
        """
        fact = F.m_faust.get_fact(i)
        return fact

    def save(F, filepath, format="Matlab"):
        r"""Saves the Faust F into a file.

        The file is saved in Matlab format version 5 (.mat extension).

        NOTE: storing F should typically use rcg(F) times less disk space than
        storing F.toarray(). See :py:func:`Faust.nbytes` for a precise size.

        Args:
            F: (Faust)
                the Faust object.
            filepath: (str)
                the path for saving the Faust (should end with .mat
                if Matlab format is used).
            format: (str)
                The format to use for
                writing. By default, it's "Matlab" to save the Faust in a .mat
                file (currently only that format is available).

        Raises:
            ValueError.


        Example:
            >>> from pyfaust import rand, Faust
            >>> F = rand(5, 10, field='complex')
            >>> F.save("F.mat")
            >>> G = Faust(filepath="F.mat")

        \see :py:func:`Faust.__init__`, :py:func:`Faust.rcg`, :py:func:`Faust.load`, :py:func:`Faust.load_native`
        """
        if format not in ["Matlab"]:
            raise ValueError("Only Matlab or Matlab_core format is supported.")
        if format == "Matlab":
            F.m_faust.save_mat_file(filepath)

    @staticmethod
    def load(filepath):
        r"""Loads a Faust from a MAT file.

        The format is Matlab format version 5 and the filepath should end with
        a .mat extension.

        The Faust must have been saved before with :func:`Faust.save.`

        Args:
            filepath: (str)
                the filepath of the .mat file.

        Example:
            >>> from pyfaust import rand, Faust
            >>> F = rand(5, 10, field='complex')
            >>> F.save("F.mat")
            >>> G = Faust.load(filepath="F.mat") # equiv. to Faust("F.mat")

        \see :py:func:`Faust.__init__`, :py:func:`Faust.save`,
        """
        contents = loadmat(filepath)
        factors = contents['faust_factors'][0].tolist()

        for i in range(len(factors)):
            # check if any BSR matrix exists here
            try:
                # using try statement because the indexing to check the bsr type
                # might fail for some types of arrays (e.g. coo_array)
                # for which we don't need this code block anyway
                # see issue #346
                if factors[i][0][0].dtype == '<U3' and factors[i][0][0][0] == 'bsr':
                    nrows, ncols, bnnz = factors[i][0][1][0]
                    bcolinds = factors[i][0][2][0]
                    browptr = factors[i][0][3][0]
                    bdata = factors[i][0][4][0]
                    bnrows = int(nrows/(browptr.shape[0]-1))
                    bncols = int(bdata.shape[0]/bnrows/bnnz)
                    bdata_ = np.empty((bnnz, bnrows, bncols))
                    for bi in range(bnnz): # .mat is in col-major order for blocks
                        bdata_[bi] = bdata.reshape(bnnz, bncols, bnrows)[bi].T
                    # override the factor with the corresponding scipy bsr matrix
                    factors[i] = bsr_matrix((bdata_, bcolinds, browptr), shape=(nrows,
                                                                                ncols))
            except:
                pass
        return Faust(factors)

    def load_native(filepath):
        r"""
        The format is Matlab format version 5 and the filepath should end with
        a .mat extension (native C++ version).

        The Faust must have been saved before with :func:`Faust.save.`

        Args:
            filepath: (str)
                the filepath of the .mat file.

        Example:
            >>> from pyfaust import rand, Faust
            >>> F = rand(5, 10, field='complex')
            >>> F.save("F.mat")
            >>> G = Faust.load_native(filepath="F.mat") # equiv. to Faust("F.mat")

        \see :py:func:`Faust.__init__`, :py:func:`Faust.save`
        """
        _type = _FaustCorePy.FaustCoreGenDblCPU.get_mat_file_type(filepath)
        if _type == -1:
            raise Exception("Invalid .mat file")
        elif _type == 0:
            F = Faust(core_obj=_FaustCorePy.FaustCoreGenFltCPU.read_from_mat_file(filepath))
        elif _type == 1:
            F = Faust(core_obj=_FaustCorePy.FaustCoreGenDblCPU.read_from_mat_file(filepath))
        elif _type == 2:
            F = Faust(core_obj=_FaustCorePy.FaustCoreGenCplxDblCPU.read_from_mat_file(filepath))
        return F

    def astype(F, dtype):
        """
        Converts F to the dtype passed as argument in a new Faust.

        Args:
            dtype: (str)
                'float32', 'float64' or 'complex'.

        Returns:
            A Faust copy of F converted to dtype.

        Example:
            >>> from pyfaust import rand
            >>> F = rand(10, 10, dtype='float64')
            >>> F.astype('float32')
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (float) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (float) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (float) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (float) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (float) SPARSE, size 10x10, density 0.5, nnz 50

            >>> F.astype('complex')
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (complex) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (complex) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (complex) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (complex) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (complex) SPARSE, size 10x10, density 0.5, nnz 50

        """
        #TODO: full list of numpy args or **kw_unknown
        dtype = _sanitize_dtype(dtype)
        if dtype == F.dtype:
            return F.clone(dev=F.device)
        if F.dtype == 'complex':
            if dtype == 'float32':
                return Faust(core_obj=F.real.m_faust.to_float())
            else:  # dtype in ['float64', 'double']:
                # (dtype sanitized and != complex)
                return Faust(core_obj=F.real.m_faust.to_double())
        else:
            return Faust([F.factors(i).astype(dtype) for i in
                          range(F.numfactors())], dev=F.device)

    @property
    def real(F):
        """
        Returns the real part of F as a Faust.
        """
        if F.dtype != 'complex':
            return F
        else:
            #  return 1/2 * (F + F.conj())
            r = _cplx2real_op(F)[:F.shape[0],
                                 :F.shape[1]]
            return r
        #return 1/2 * (F + F.conj())

    @property
    def imag(F):
        """Returns the imaginary part of F as a Faust.
        """
        if F.dtype != 'complex':
            # return Faust(csr_matrix(F.shape)) # TODO: debug pyx code
            return Faust(csr_matrix((np.array([0.]).astype(F.dtype),
                                     ([0], [0])), (F.shape)), dev=F.device)
        else:
            # return 1/2j * (F + F.conj())
            i = _cplx2real_op(F)[F.shape[0]:2*F.shape[0],
                                 :F.shape[1]]
            return i

    def asarray(F, *args, **kwargs):
        return F

    @property
    def dtype(F):
        """Returns the dtype of the Faust.

        This function is intended to be used as a property (see the examples).

        Args:
            F: the Faust object.

        Returns:
            the dtype of F, which can be float32, float64 or complex128.

        Examples:
            >>> from pyfaust import rand
            >>> F = rand(5, 10, field='complex')
            >>> F.dtype
            dtype('complex128')
            >>> F = rand(5, 10)
            >>> F.dtype
            dtype('float64')
            >>> G = rand(5, 5, dtype='float32')
            >>> G.dtype
            dtype('float32')


        """
        return F.m_faust.dtype()

    def imshow(F, name='F'):
        r"""
        Displays image of F's full matrix and its factors.

        Args:
            F: (Faust)
                the Faust object.
            name: (str)
                the displayed name on the plotted figure.


        Examples:
        >>> from pyfaust import rand
        >>> import matplotlib.pyplot as plt
        >>> F = rand(10, 20, density=.5, field='complex')
        >>> F.imshow()
        >>> plt.show()


        \see :py:func:`Faust.display`
        """
        import matplotlib.pyplot as plt
        if not isinstance(name, str):
            raise TypeError('name must be a str.')
        nf = F.numfactors()
        max_cols = 5
        ncols = min(nf, max_cols)
        nrows = int(nf/ncols)+1
        plt.subplot(nrows, ncols, nrows*ncols)
        plt.title(name+'.toarray()', fontweight='bold')
        if F.dtype == 'complex':
            plt.imshow(abs(F.toarray()), aspect='equal')
        else:
            plt.imshow(F.toarray(), aspect='equal')
        #plt.xticks([]); plt.yticks([])
        for i in range(0, nf):
            plt.subplot(nrows, ncols, (i % ncols) + int(i / ncols) * ncols + 1)
            plt.title(str(i))
            fac = F.factors(i)
            if not isinstance(fac, np.ndarray):
                fac = fac.toarray()
            plt.xticks([])
            plt.yticks([])
            plt.suptitle('Factors of the Faust ' + name, fontweight='bold')
            if fac.dtype == 'complex':
                plt.imshow(abs(fac), aspect='equal')
            else:
                plt.imshow(fac, aspect='equal')

    def pinv(F):
        """Computes the (Moore-Penrose) pseudo-inverse of F.toarray().

        Warning: this function makes a call to :func:`Faust.toarray().`

        Returns:
            The dense pseudo-inverse matrix.

        Example:
            >>> from pyfaust import rand
            >>> import numpy as np
            >>> from numpy.linalg import pinv
            >>> F = rand(128, 32)
            >>> M = F.toarray()
            >>> np.allclose(F.pinv(), pinv(M))
            True

        See also <a href="https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html">numpy.linalg.pinv</a>, :py:func:`pyfaust.fact.pinvtj`
        """
        from numpy.linalg.linalg import pinv
        return pinv(F.toarray())

    @staticmethod
    def isFaust(obj):
        """
        Returns True if obj is a Faust object, False otherwise.

        Examples:
            >>> from pyfaust import *
            >>> Faust.isFaust(2) # isFaust(2) works as well
            False
            >>> Faust.isFaust(rand(5, 10))
            True

        """
        return isinstance(obj, Faust)

    def issparse(F, csr=True, bsr=False):
        r"""
        Returns True if all F factors are sparse False otherwise.

        What a sparse factor is, depends on csr and bsr arguments.

        Args:
            csr: (bool)
                True to consider CSR matrices in F as sparse matrices, False otherwise.
            bsr: (bool)
                True to consider BSR matrices in F as sparse matrices, False otherwise.

        Example:
            >>> import pyfaust as pf
            >>> F = pf.rand(10, 10, fac_type='sparse')
            >>> F
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> F.issparse()
            True
            >>> F.issparse(csr=True)
            True
            >>> F.issparse(csr=False)
            Traceback (most recent call last):
            ...
            ValueError: It doesn't make sense to set csr=False and bsr=False as the function will always return False

            >>> F = pf.rand_bsr(10, 10, 2, 2, 2, .1)
            >>> F
            Faust size 10x10, density 0.24, nnz_sum 24, 2 factor(s):
            - FACTOR 0 (double) BSR, size 10x10 (blocksize = 2x2), density 0.12, nnz 12 (nnz blocks: 3)
            - FACTOR 1 (double) BSR, size 10x10 (blocksize = 2x2), density 0.12, nnz 12 (nnz blocks: 3)

            >>> # default config. recognizes only csr
            >>> F.issparse()
            False
            >>> F.issparse(bsr=True)
            True
            >>> F = pf.rand(10, 10, fac_type='dense')
            >>> F.issparse()
            False


        \see :py:func:`Faust.isdense`, :py:func:`pyfaust.rand`, :py:func:`pyfaust.rand_bsr`
        """
        if not csr and not bsr:
            raise ValueError('It doesn\'t make sense to set csr=False and'
                             ' bsr=False as the function will always return'
                             ' False')
        return F.m_faust.is_all_sparse(csr, bsr)

    def isdense(F):
        r"""
        Returns True if all factors are dense arrays (as np.ndarray-s) False otherwise.

        Example:
            >>> import pyfaust as pf
            >>> pf.seed(42) # just for reproducibility
            >>> F = pf.rand(10, 10, fac_type='sparse')
            >>> F
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> F.isdense()
            False
            >>> F = pf.rand(10, 10, fac_type='dense')
            >>> F
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) DENSE, size 10x10, density 0.5, nnz 50

            >>> F.isdense()
            True
            >>> F = pf.rand(10, 10, fac_type='mixed')
            >>> F
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) DENSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) DENSE, size 10x10, density 0.5, nnz 50

            >>> F.isdense()
            False

        \see :py:func:`Faust.issparse`, :py:func:`pyfaust.rand`, :py:func:`pyfaust.rand_bsr`
        """
        return F.m_faust.is_all_dense()

    def swap_cols(F, id1, id2, permutation=False, inplace=False):
        r"""
        Swaps F columns of indices id1 and id2.

        Args:
            id1: (int)
                index of the first column of the swap.
            id2: (int)
                index of the second column of the swap.
            permutation: (bool)
                if True then the swap is performed by inserting a permutation
                matrix to the output Faust. If False, the last matrix
                in the Faust F sequence is edited to swap the columns.
            inplace: (bool)
                if True then F is modified instead of returning a new Faust.
                Otherwise, by default, a new Faust is returned.

        Returns:
            The column swapped Faust.

        Example:
            >>> from pyfaust import rand as frand
            >>> F = frand(10, 10)
            >>> G = F.swap_cols(2, 4)
            >>> G
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            >>> G[:, 2].toarray() == F[:, 4].toarray()
            array([[ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True]])
            >>> G[:, 4].toarray() == F[:, 2].toarray()
            array([[ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True],
                   [ True]])
            >>> H  = F.swap_cols(2, 4, permutation=True)
            >>> H
            Faust size 10x10, density 2.6, nnz_sum 260, 6 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 5 (double) SPARSE, size 10x10, density 0.1, nnz 10

        \see :py:func:`Faust.swap_rows`
        """
        if inplace:
            F.m_faust.swap_cols(id1, id2, permutation,
                                inplace)
            return F
        F_swapped = Faust(core_obj=F.m_faust.swap_cols(id1, id2, permutation,
                                                       inplace))
        return F_swapped

    def swap_rows(F, id1, id2, permutation=True, inplace=False):
        r"""Swaps F rows of indices id1 and id2.

        Args:
            id1: (int)
                index of the first row of the swap.
            id2: (int)
                index of the second row of the swap.
            permutation: (bool)
                if True then the swap is performed by inserting a permutation
                matrix to the output Faust. If False, the last matrix
                in the Faust F sequence is edited to swap the rows.
            inplace: (bool)
                if True then F is modified instead of returning a new Faust.
                Otherwise, by default, a new Faust is returned.

        Returns:
            The rows swapped Faust.

        Example:
            >>> from pyfaust import rand as frand
            >>> F = frand(10, 10)
            >>> G = F.swap_rows(2, 4)
            >>> G
            Faust size 10x10, density 2.6, nnz_sum 260, 6 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.1, nnz 10
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 5 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> G[2, :].toarray() == F[4, :].toarray()
            array([[ True,  True,  True,  True,  True,  True,  True,  True,  True,
                     True]])

            >>> G[4, :].toarray() == F[2, :].toarray()
            array([[ True,  True,  True,  True,  True,  True,  True,  True,  True,
                     True]])

            >>> H  = F.swap_rows(2, 4, permutation=True)
            >>> H
            Faust size 10x10, density 2.6, nnz_sum 260, 6 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.1, nnz 10
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 5 (double) SPARSE, size 10x10, density 0.5, nnz 50

        \see :py:func:`Faust.swap_cols`
        """
        if inplace:
            F.m_faust.swap_rows(id1, id2, permutation,
                                inplace)
            return F
        F_swapped = Faust(core_obj=F.m_faust.swap_rows(id1, id2, permutation,
                                                       inplace))
        return F_swapped

    def optimize_memory(F):
        r"""Optimizes a Faust by changing the storage format of each factor in order to optimize the memory size.

        Returns:
            The optimized Faust.

        Example:
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(1024, 1024, fac_type='mixed')
            >>> F
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) DENSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> F.nbytes
            8650768
            >>> pF = F.optimize_memory()
            >>> pF
            Faust size 1024x1024, density 0.0244141, nnz_sum 25600, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120
            - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00488281, nnz 5120

            >>> pF.nbytes
            327700

        \see :py:func:`Faust.optimize`,
        """
        F_opt = Faust(core_obj=F.m_faust.optimize_storage(False))
        return F_opt

    def optimize(F, transp=False):
        r"""Returns a :py:func:`Faust`, optimized with :py:func:`Faust.pruneout`, :py:func:`Faust.optimize_memory`, and :py:func:`Faust.optimize_time`.

        Args:
            transp: (bool)
                True in order to optimize the Faust according to its transpose.

        Returns:
            The optimized Faust.

        Note: this function is still experimental, you might use manually
              :py:func:`Faust.optimize_time`, :py:func:`Faust.optimize_memory` or :py:func:`Faust.pruneout` to be
              more specific about the optimization to proceed.

        Example:
            This example shows how :func:`Faust.optimize` can diminish the memory size and
            speed up the :func:`Faust.toarray()` and Faust-vector multiplication.

            >>> import numpy as np
            >>> from pyfaust import rand, seed
            >>> seed(42) # just for reproducibility
            >>> F = rand(1024, 1024, dim_sizes=[1, 1024], num_factors=32, fac_type='mixed')
            >>> F.nbytes
            13991076
            >>> pF = F.optimize()
            >>> pF.nbytes
            910368
            >>> from time import time
            >>> t1 = time(); M = F.toarray(); print("F.toarray() time:", time()-t1) # doctest:+ELLIPSIS
            F.toarray() time: ...
            >>> # e.g: F.toarray() time: 0.2779221534729004
            >>> t1 = time(); M_ = pF.toarray(); print("pF.toarray() time:", time()-t1) # doctest:+ELLIPSIS
            pF.toarray() time: ...
            >>> # e.g:pF.toarray() time: 0.2017652988433838
            >>> np.allclose(M_, M)
            True
            >>> v = np.random.rand(F.shape[1])
            >>> t1 = time(); Fv = F@v;print("F@v time:", time()-t1) # doctest:+ELLIPSIS
            F@v time: ...
            >>> # e.g: F@v time: 0.0016832351684570312
            >>> t1 = time(); Fv_ = pF@v; print("pF@v time:", time()-t1) # doctest:+ELLIPSIS
            pF@v time: ...
            >>> # e.g: pF@v time: 0.0002257823944091797
            >>> np.allclose(Fv_, Fv)
            True


        \see :py:func:`Faust.optimize_time`, :py:func:`Faust.optimize_memory`, :py:func:`Faust.pruneout`, :py:func:`Faust.nbytes`, <a href="https://faust.inria.fr/tutorials/pyfaust-jupyter-notebooks/faust-optimizations-with-pyfaust/">Jupyter notebook about :py:func:`Faust`, optimizations</a>
        """
        F_opt = Faust(core_obj=F.m_faust.optimize(transp))
        return F_opt

    def optimize_time(F, transp=False, inplace=False, nsamples=1, mat=None):
        r"""Returns a Faust configured with the quickest Faust-matrix multiplication mode (benchmark ran on the fly).

        NOTE: this function launches a small benchmark on the fly. Basically, the methods
            available differ by the order used to compute the matrix chain.

        The evaluated methods in the benchmark are listed in pyfaust.FaustMulMode.
        Although depending on the package you installed and the capability of your
        hardware the methods based on Torch library can be used.

        Args:
            transp: (bool)
                True in order to optimize the Faust according to its transpose.
            inplace: (bool)
                to optimize the current Faust directly instead of returning a new
                Faust with the optimization enabled. If True, F is returned
                otherwise a new Faust object is returned.
            nsamples: (int)
                the number of Faust-Dense matrix products
                calculated in order to measure time taken by each method (it could matter
                to discriminate methods when the performance is similar). By default,
                only one product is computed to evaluate the method.
            mat: (NoneType, np.ndarray, or scipy.sparse.csr_matrix)
                Use this argument to run the benchmark on
                the Faust multiplication by the matrix mat instead of :func:`Faust.toarray()` (if mat
                is None). Note that mat must be of the same dtype as F.

        Returns:
            The optimized Faust.

        Example:
            >>> from pyfaust import rand, seed
            >>> from time import time
            >>> import numpy as np
            >>> seed(42) # just for reproducibility
            >>> F = rand(1024, 1024, dim_sizes=[1, 1024], num_factors=32, fac_type='dense', density=.5)
            >>> oF = F.optimize_time()
            >>> # possible outout: best method measured in time on operation Faust-toarray is: DYNPROG
            >>> t1 = time(); M = F.toarray(); print("F.toarray() time:", time()-t1) # doctest:+ELLIPSIS
            F.toarray() time:...
            >>> # F.toarray() time: 0.2891380786895752
            >>> t1 = time(); M_ = oF.toarray(); print("oF.toarray() time:", time()-t1) # doctest:+ELLIPSIS
            oF.toarray() time:...
            >>> # example: oF.toarray() 0.0172119140625
            >>> np.allclose(M, M_)
            True

        \see :py:func:`Faust.optimize`, :py:class:`pyfaust.FaustMulMode`

        """
        if inplace:
            F.m_faust.optimize_time(transp, inplace, nsamples, M=mat)
            return F
        else:
            F_opt = Faust(core_obj=F.m_faust.optimize_time(transp, inplace,
                                                           nsamples, M=mat))
            return F_opt

    def copy(F, dev='cpu'):
        r"""Clone alias function (here just to mimic numpy API).

        \see :py:func:`Faust.clone`,
        """
        check_dev(dev)
        return F.clone(dev)

    def clone(F, dev=None):
        """Clones the Faust (in a new memory space).

        Args:
            dev: (str)
                'cpu' to clone on CPU RAM, 'gpu' to clone on
                the GPU device. By default (None), the device is
                the F.device.

        Returns:
            The Faust clone.

        Example:
            >>> from pyfaust import rand, is_gpu_mod_enabled
            >>> F = rand(10, 10)
            >>> F.clone()
            Faust size 10x10, density 2.5, nnz_sum 250, 5 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50

            >>> if is_gpu_mod_enabled(): F.clone(dev='gpu') # only if a NVIDIA compatible GPU is available
            >>> #- GPU FACTOR 0 (double) SPARSE size 10 x 10, addr: 0x2c85390, density 0.500000, nnz 50
            >>> #- GPU FACTOR 1 (double) SPARSE size 10 x 10, addr: 0x7ff00c0, density 0.500000, nnz 50
            >>> #- GPU FACTOR 2 (double) SPARSE size 10 x 10, addr: 0x977f280, density 0.500000, nnz 50
            >>> #- GPU FACTOR 3 (double) SPARSE size 10 x 10, addr: 0x9780120, density 0.500000, nnz 50
            >>> #- GPU FACTOR 4 (double) SPARSE size 10 x 10, addr: 0x9780fc0, density 0.500000, nnz 50

        """
        if dev is None:
            dev = F.device
        check_dev(dev)
        # dev is 'gpu[:id]' or 'cpu'
        if F.device.startswith('gpu'):
            if F.dtype == 'float64':
                clone_F = \
                        Faust(core_obj=_FaustCorePy.FaustCoreGenNonMemberFuncsDblGPU.clone(F.m_faust,
                                                                                           dev))
            else: # F.dtype == 'complex'
                clone_F = \
                        Faust(core_obj=_FaustCorePy.FaustCoreGenNonMemberFuncsCplxDblGPU.clone(F.m_faust,
                                                                                               dev))
#            clone_F = Faust(core_obj=F.m_faust.clone(dev))
        elif F.device == 'cpu':
            if dev == 'cpu':
                clone_F = Faust(core_obj=F.m_faust.clone(-1))
            else:
                if F.dtype == 'float64':
                    clone_F = \
                            Faust(core_obj=_FaustCorePy.FaustCoreGenNonMemberFuncsDblCPU.clone(F.m_faust, dev))
                else:
                    clone_F = \
                            Faust(core_obj=_FaustCorePy.FaustCoreGenNonMemberFuncsCplxDblCPU.clone(F.m_faust,
                                                                                                   dev))
        else:
            raise ValueError("F.device is not valid")
        return clone_F

    def sum(F, axis=None, **kwargs):
        """
        Sums Faust elements over a given axis.

        Args:
            axis: (None or int or tuple of ints)
                Axis or axes along which the the sum is performed

        Returns:
            The Faust sum.

        Example:
            >>> from pyfaust import rand as frand, seed
            >>> seed(42) # just for reproducibility
            >>> F = frand(10, 10)
            >>> F.sum()
            Faust size 1x1, density 270, nnz_sum 270, 7 factor(s):
            - FACTOR 0 (double) DENSE, size 1x10, density 1, nnz 10
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 5 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 6 (double) DENSE, size 10x1, density 1, nnz 10

            >>> F.sum(axis=0).toarray()
            array([[ 80.49374154,  45.09382766,  78.8607646 , 136.65920307,
                    115.25872767,  62.70720879,  90.48774161,  62.26010951,
                      0.        , 158.34355964]])
            >>> F.sum(axis=1)
            Faust size 10x1, density 26, nnz_sum 260, 6 factor(s):
            - FACTOR 0 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 1 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 2 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 3 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 4 (double) SPARSE, size 10x10, density 0.5, nnz 50
            - FACTOR 5 (double) DENSE, size 10x1, density 1, nnz 10

            >>> F.sum(axis=1).toarray()
            array([[ 60.96835408],
                   [112.00753373],
                   [ 97.28363377],
                   [ 69.45346776],
                   [ 80.20182354],
                   [ 96.1022012 ],
                   [ 48.61063623],
                   [ 54.15081295],
                   [ 88.20644303],
                   [123.1799778 ]])


        """
        if axis is None:
            axis = (0, 1)
        is_tuple = isinstance(axis, tuple)
        is_int = isinstance(axis, int)
        is_tuple_or_int = is_tuple or is_int
        if not is_tuple_or_int or is_tuple and \
           (not isinstance(axis[0], int) or not isinstance(axis[1], int)):
            raise TypeError("axis must be int or tuple of ints")
        if axis is None or axis == 0 or is_tuple and 0 in axis:
            F = Faust(np.ones((1, F.shape[0]), dtype=F.dtype), dev=F.device)@F
        if axis == 1 or is_tuple and 1 in axis:
            F = F@Faust(np.ones((F.shape[1], 1), dtype=F.dtype), dev=F.device)
        if is_tuple and len([i for i in axis if i < 0
                             or i > 1]) or is_int and (axis < 0 or axis > 1):
            raise ValueError("axis "+str(axis)+" is out of bounds for a Faust "
                             " (only two dimensions)")
        return F

    def sliceMultiply(F, start_col_id, end_col_id, vec):
        return F.m_faust.colSliceMultiply(start_col_id, end_col_id, vec)

    def indexMultiply(F, x, d0_ids=None, d1_ids=None):
        if d0_ids is not None:
            d0_ids = d0_ids if isinstance(d0_ids, np.ndarray) else np.array(d0_ids)
        if d1_ids is not None:
            d1_ids = d1_ids if isinstance(d1_ids, np.ndarray) else np.array(d1_ids)
        return F.m_faust.indexMultiply(d0_ids, d1_ids, x)

    def average(F, axis=None, weights=None, sw_returned=False):
        """
        Computes the weighted average of F along the specified axis.

        Args:
            axis: (None or int or tuple of ints)
                Axis or axes along which to average the Faust F.
                The default, axis=None, will average over all of the elements of the input array.
                If axis is a tuple of ints, averaging is performed on all of the axes specified in the tuple

            weights: (np.ndarray)
                an array of weights associated with the values in F.
                Each value in F contributes to the average according to its associated weight.
                The weights array can either be 1-D (in which case its length must be the size
                of a along the given axis) or of the same shape as a.
                If weights=None, then all data in F are assumed to have a weight equal to one.
                The 1-D calculation is:

                    avg = sum(F @ weights) / sum(weights)

                    The only constraint on weights is that sum(weights) must not be 0.
            returned: (bool)
                True to return the sum of weights in addition to average (as a pair
                (avg, sum(weights))), False otherwise (default).

        Returns:
            The Faust average.

        Example:
            >>> from pyfaust import Faust
            >>> import numpy as np
            >>> data = np.arange(1, 5).astype('double')
            >>> data
            array([1., 2., 3., 4.])
            >>> F = Faust(data.reshape(1, data.shape[0]))
            >>> FA = F.average()
            >>> FA
            Faust size 1x1, density 9, nnz_sum 9, 3 factor(s):
            - FACTOR 0 (double) DENSE, size 1x1, density 1, nnz 1
            - FACTOR 1 (double) DENSE, size 1x4, density 1, nnz 4
            - FACTOR 2 (double) DENSE, size 4x1, density 1, nnz 4

            >>> FA.toarray()
            array([[2.5]])
            >>> data2 = np.arange(6).reshape((3, 2)).astype('double')
            >>> F2 = Faust(data2)
            >>> F2.average(axis=1, weights=[1./4, 3./4]).toarray()
            array([[0.75],
                   [2.75],
                   [4.75]])


        """
        if axis is None:
            axis = (0, 1)
        is_tuple = isinstance(axis, tuple)
        is_int = isinstance(axis, int)
        is_tuple_or_int = is_tuple or is_int
        if not is_tuple_or_int or is_tuple and \
           (not isinstance(axis[0], int) or not isinstance(axis[1], int)):
            raise TypeError("axis must be int or tuple of ints")
        if not isinstance(weights, np.ndarray) and weights is None:
            def_rweights = np.ones(F.shape[0])
            def_cweights = np.ones(F.shape[1])
            if isinstance(axis, int):
                if axis == 0:
                    weights = def_rweights
                elif axis == 1:
                    weights = def_cweights
            elif isinstance(axis, tuple):
                if 0 in axis:
                    F = F.average(axis=0,
                                  weights=def_rweights,
                                  sw_returned=sw_returned)
                if 1 in axis:
                    F = F.average(axis=1,
                                  weights=def_cweights,
                                  sw_returned=sw_returned)
                return F

        if not isinstance(weights, np.ndarray):
            weights = np.array(weights)
        if weights.shape != F.shape and weights.ndim != 1:
            raise TypeError("1D weights expected when shapes of F and weights"
                            " differ.")

        weights = weights.astype(F.dtype)
        zw_err = decimal.DivisionByZero("Weights sum to zero, can't be normalized")
        if weights.ndim == 2 and weights.shape == F.shape:
            # form the vector:
            # aF.toarray() = [
            #     sum(F[:, i] * weights[:, i]) for i in range(F.shape[1])
            # ]
            aF = pyfaust.hstack(tuple([pyfaust.Faust(weights[:, i].T.reshape(1, F.shape[0])) @
                                       F[:, i] for i in range(F.shape[1])]))
            # multiply each vector element by 1/sum(weights)
            sum_weights = np.sum(weights, axis=(0, 1))
            print("sum_weights ============================", sum_weights)
            if sum_weights == 0:
                raise zw_err
            sum_weights = 1 / sum_weights
            swF = Faust(np.array([sum_weights for i in
                                  range(aF.shape[1])]).reshape(aF.shape[1], 1),
                        dev=F.device)
            aFw = aF @ swF

            if sw_returned:
                return (aFw, 1 / sum_weights)
            return aFw

        if axis == 1 or isinstance(axis, tuple) and 1 in axis:
            if weights.shape[0] == F.shape[1]:
                aF = F@Faust(weights.reshape(weights.size, 1), dev=F.device)
            else:
                raise ValueError("Length of weights not compatible"
                                 " with specified axis 1.")
            sum_weights = np.sum(weights.reshape(weights.size, 1), axis=0)[0]

        if axis == 0 or isinstance(axis, tuple) and 0 in axis:
            weightsM = weights
            if weights.ndim == 1:
                weightsM = weights.reshape(1, weights.size)
            if weightsM.shape[1] == F.shape[0]:
                aF = Faust(weightsM, dev=F.device)@F
            else:
                raise ValueError("Length of weights not compatible"
                                 " with axis 0.")
            sum_weights = np.sum(weightsM.reshape(1, weights.size),
                                 axis=1)[0]

        if sum_weights != 0:
            aF = aF * (1/sum_weights)
        else:
            raise zw_err
        if sw_returned:
            return (aF, sum_weights)
        return aF


pyfaust.Faust.__div__ = pyfaust.Faust.__truediv__


def implements(numpy_function):
    """Register an __array_function__ implementation for MyArray
    objects."""
    def decorator(func):
        HANDLED_FUNCTIONS[numpy_function] = func
        return func
    return decorator


def version():
    """Returns the FAuST package version.
    """
    return __version__


__version__ = "3.42.1"


def faust_fact(*args, **kwargs):
    r"""
    This function is a shorthand for :py:func:`pyfaust.fact.hierarchical`.

    \see :py:func:`pyfaust.fact.hierarchical`
    """
    import pyfaust.fact
    return pyfaust.fact.hierarchical(*args, **kwargs)


def license():
    """ Prints the FAuST license.
    """
    print("""######################################################################################
# Copyright (c) 2015-2023, Inria and Authors:                                        #
#  (Researchers:) Rémi Gribonval, Luc Le Magoarou,                                   #
#  (Engineers:) Adrien Leman (2016), Nicolas Bellot(2015-2016),                      #
#  Thomas Gautrais (2015), Hakim Hadj-Djilani (2018-),                               #
#  Pascal Carrivain (2023-).                                                         #
#  All rights reserved.                                                              #
#                                                                                    #
#  BSD 3-clause License.                                                             #
#                                                                                    #
# Redistribution and use in source and binary forms, with or without                 #
# modification, are permitted provided that the following conditions are met:        #
#                                                                                    #
# 1. Redistributions of source code must retain the above copyright notice, this     #
# list of conditions and the following disclaimer.                                   #
#                                                                                    #
# 2. Redistributions in binary form must reproduce the above copyright notice,       #
#     this list of conditions and the following disclaimer in the documentation      #
#     and/or other materials provided with the distribution.                         #
#                                                                                    #
# 3. Neither the name of the copyright holder nor the names of its                   #
# contributors may be used to endorse or promote products derived from this          #
# software without specific prior written permission.                                #
#                                                                                    #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"        #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE          #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE         #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE          #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR                #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF               #
#         SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR            #
#         BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF                 #
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING               #
#         NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS         #
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                       #
######################################################################################
""")


def norm(F, ord='fro', **kwargs):
    r"""
    Returns ``Faust.norm(F, ord)` or ``numpy.linalg.norm(F, ord)`` depending of F type.

    \see :py:func:`Faust.norm`
    """
    if Faust.isFaust(F):
        return F.norm(ord, **kwargs)
    else: # if F is not a Faust, try to rely on numpy (not breaking possible
        # past import)
        axis = None
        keepdims = False
        if 'axis' in kwargs.keys():
            axis = kwargs['axis']
        if 'keepdims' in kwargs.keys():
            keepdims = kwargs['keepdims']
        return np.linalg.norm(F, ord, axis=axis,
                              keepdims=keepdims)


@implements(np.dot)
def dot(A, B, **kwargs):
    r"""Returns ``Faust.dot(A, B)`` if A or B is a Faust object, returns numpy.dot(A, B) ortherwise.

    \see :py:func:`Faust.norm`, :func:`Faust.dot`
    """
    if Faust.isFaust(A):
        return A.dot(B)
    elif Faust.isFaust(B):
        return B.T.dot(A.T).T
    else: # if F is not a Faust, try to rely on numpy (not breaking possible
        # past import)
        return np.dot(A, B)


def pinv(F):
    """A package function alias for the member function :func:`Faust.pinv().`
    """
    if Faust.isFaust(F):
        return F.pinv()
    else:
        return np.linalg.pinv(F)


@implements(np.concatenate)
def concatenate(_tuple, *args, axis=0, **kwargs):
    r"""
    A package function alias for the member function :func:`Faust.concatenate.`

    Example:
        >>> from pyfaust import *
        >>> seed(42) # just for reproducibility
        >>> F1 = rand(5, 50)
        >>> F2 = rand(5, 50)
        >>> concatenate((F1, F2), axis=0)
        Faust size 10x50, density 2.17, nnz_sum 1085, 6 factor(s):
        - FACTOR 0 (double) SPARSE, size 10x67, density 0.0746269, nnz 50
        - FACTOR 1 (double) SPARSE, size 67x33, density 0.151515, nnz 335
        - FACTOR 2 (double) SPARSE, size 33x31, density 0.16129, nnz 165
        - FACTOR 3 (double) SPARSE, size 31x56, density 0.0892857, nnz 155
        - FACTOR 4 (double) SPARSE, size 56x100, density 0.05, nnz 280
        - FACTOR 5 (double) SPARSE, size 100x50, density 0.02, nnz 100

    \see numpy.concatenate, :py:func:`Faust.concatenate`,
    """
    if not isinstance(_tuple, tuple):
        raise TypeError("first arg must be a tuple")
    if isFaust(_tuple[0]):
        return _tuple[0].concatenate(*_tuple[1:], axis=axis, **kwargs)
    elif np.array([isFaust(_tuple[i]) for i in range(len(_tuple))]).any():
        return Faust(_tuple[0]).concatenate(*_tuple[1:], axis=axis, **kwargs)
    elif np.array([issparse(_tuple[i]) for i in range(len(_tuple))]).all():
        if axis == 0:
            return svstack(_tuple)
        elif axis == 1:
            return hstack(_tuple)
        else:
            raise ValueError("Invalid axis")
    else:
        # convert any _tuple element to np.ndarray if possible (it has a
        # toarray func)
        _tuple = tuple(t if isinstance(t, np.ndarray) else t.toarray() for t in
                       _tuple)
        return np.concatenate(_tuple, axis=axis)


def hstack(_tuple):
    r"""
    Concatenates horizontally Faust-s and/or numpy.ndarray objects using :func:`Faust.concatenate().`

    \see numpy.hstack


    NOTE: it could be wiser to encapsulate a Faust in a
    <a href="https://faustgrp.gitlabpages.inria.fr/lazylinop/api_lazylinop.html#lazylinop.aslazylinearoperator">lazylinop.LazyLinearOp</a>
    for a lazy concatenation.

    Example:
        >>> from pyfaust import *
        >>> seed(42) # just for reproducibility
        >>> F1 = rand(5, 50)
        >>> F2 = rand(5, 50)
        >>> hstack((F1, F2))
        Faust size 5x100, density 1.99, nnz_sum 995, 6 factor(s):
        - FACTOR 0 (double) SPARSE, size 5x10, density 0.2, nnz 10
        - FACTOR 1 (double) SPARSE, size 10x67, density 0.0746269, nnz 50
        - FACTOR 2 (double) SPARSE, size 67x33, density 0.151515, nnz 335
        - FACTOR 3 (double) SPARSE, size 33x31, density 0.16129, nnz 165
        - FACTOR 4 (double) SPARSE, size 31x56, density 0.0892857, nnz 155
        - FACTOR 5 (double) SPARSE, size 56x100, density 0.05, nnz 280
    """
    return pyfaust.concatenate(_tuple, axis=1)


def vstack(_tuple):
    r"""
    Concatenates vertically Faust-s and/or numpy.ndarray arrays using :func:`Faust.concatenate().`

    \see numpy.vstack


    NOTE: it could be wiser to encapsulate a Faust in a
    <a href="https://faustgrp.gitlabpages.inria.fr/lazylinop/api_lazylinop.html#lazylinop.aslazylinearoperator">lazylinop.LazyLinearOp</a>
    for a lazy concatenation.

    Example:
        >>> from pyfaust import *
        >>> seed(42) # just for reproducibility
        >>> F1 = rand(5, 50)
        >>> F2 = rand(5, 50)
        >>> vstack((F1, F2))
        Faust size 10x50, density 2.17, nnz_sum 1085, 6 factor(s):
        - FACTOR 0 (double) SPARSE, size 10x67, density 0.0746269, nnz 50
        - FACTOR 1 (double) SPARSE, size 67x33, density 0.151515, nnz 335
        - FACTOR 2 (double) SPARSE, size 33x31, density 0.16129, nnz 165
        - FACTOR 3 (double) SPARSE, size 31x56, density 0.0892857, nnz 155
        - FACTOR 4 (double) SPARSE, size 56x100, density 0.05, nnz 280
        - FACTOR 5 (double) SPARSE, size 100x50, density 0.02, nnz 100
    """
    return pyfaust.concatenate(_tuple, axis=0)


def isFaust(obj):
    r"""
    Package alias function of :func:`Faust.isFaust.`

    \see :py:func:`Faust.__init__`, :py:func:`Faust.isFaust.`,
    """
    return Faust.isFaust(obj)


def wht(n, normed=True, dev="cpu", dtype='float64'):
    r"""
    Constructs a Faust implementing the Walsh-Hadamard Transform (WHT) of order n.

    The resulting Faust has log2(n) sparse factors of order n, each one having
    2 nonzeros per row and per column.

    Args:
       n: (int)
           order of the WHT (must be a power of two).
       normed: (bool)
           default to True to normalize the Hadamard Faust as if you called
           :func:`Faust.normalize()` and False otherwise.
       dev: (str)
           device on which to create the Faust ('cpu' or 'gpu').
       dtype: (str)
           the Faust dtype, it must be 'float32', 'float64' or 'complex'.


    Returns:
       The Faust implementing the Hadamard transform of dimension n.

    Examples:
      >>> from pyfaust import wht
      >>> wht(1024)
      Faust size 1024x1024, density 0.0195312, nnz_sum 20480, 10 factor(s):
      - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 5 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 6 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 7 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 8 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 9 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048

      >>> wht(1024, normed=True) # is equiv. to next call
      Faust size 1024x1024, density 0.0195312, nnz_sum 20480, 10 factor(s):
      - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 5 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 6 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 7 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 8 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 9 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048

      >>> wht(1024, normed=False).normalize() # which is less optimized though
      Faust size 1024x1024, density 0.0195312, nnz_sum 20480, 10 factor(s):
      - FACTOR 0 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 1 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 2 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 3 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 4 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 5 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 6 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 7 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 8 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
      - FACTOR 9 (double) SPARSE, size 1024x1024, density 0.00195312, nnz 2048

   \see scipy.linalg.hadamard, :py:func:`pyfaust.dft`, :py:func:`pyfaust.fact.butterfly`,
    """
    dtype = _sanitize_dtype(dtype)
    check_dev(dev)
    log2n = np.floor(np.log2(n))
    if n > 2**log2n:
        raise ValueError("n must be a power of 2.")
    if not isinstance(normed, bool):
        raise TypeError("normed must be True of False.")
    if dev == "cpu":
        if dtype == 'float64':
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUDbl.hadamardFaust(log2n, normed))
        elif dtype == 'float32':
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUFlt.hadamardFaust(log2n, normed))
        else: # dtype == 'complex'
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUCplxDbl.hadamardFaust(log2n, normed))
    elif dev.startswith("gpu"):
        if dtype == 'float64':
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUDbl.hadamardFaust(log2n, normed))
        elif dtype == 'float32':
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUFlt.hadamardFaust(log2n, normed))
        else: # dtype == 'complex'
            H = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUCplxDbl.hadamardFaust(log2n, normed))
    return H


def bitrev_perm(n):
    r"""
    Bitreversal permutation.

    Args:
        n: (int)
            the size of the permutation, it must be a power of two. P dimensions will be n x n

    Returns:
        P: a scipy csr_matrix defining the bit-reversal permutation.

    \see :py:func:`pyfaust.dft`
    """
    if np.log2(n) > np.log2(np.floor(n)):
        raise ValueError('n must be a power of two')
    row_inds = np.arange(0, n, dtype='int')
    col_inds = bitrev(row_inds)
    ones = np.ones((n), dtype='float')
    return csr_matrix((ones, (row_inds, col_inds)), shape=(n, n))


def bitrev(inds):
    r"""
    Bitreversal permutation.

    Args:
        inds: (list[int])
            the list of indices to bit-reverse.

    Returns:
        The bit-reversal permutation of inds.

    Example:
        >>> import numpy as np
        >>> from pyfaust import bitrev
        >>> bitrev(np.arange(4))
        array([0, 2, 1, 3])

    See also: https://en.wikipedia.org/wiki/Bit-reversal_permutation.
    """
    n = len(inds)
    if n == 1:
        return inds
    else:
        even = bitrev(inds[np.arange(0, n, 2, dtype='int')])
        odd = bitrev(inds[np.arange(1, n, 2, dtype='int')])
        return np.hstack((even, odd))


def dft(n, normed=True, dev='cpu', diag_opt=False):
    r"""
    Constructs a Faust F implementing the Discrete Fourier Transform (DFT) of order n.

    The factorization corresponds to the butterfly structure of the
    Cooley-Tukey FFT algorithm.
    The resulting Faust is complex and has (log2(n)+1) sparse factors.
    The log2(n) first has 2 nonzeros per row and per column.
    The last factor is a bit-reversal permutation matrix.

    Args:
        n: (int)
            order of the Discrete Fourier Transform (must be a power of two).
        normed: (bool)
            default to True to normalize the DFT Faust as if you called
            :func:`Faust.normalize()` and False otherwise.
        dev: (str)
            device to create the Faust on ('cpu' or 'gpu').
        diag_opt: (bool)
            if True then the returned Faust is optimized using pyfaust.opt_butterfly_faust.

    Returns:
        The Faust implementing the DFT of dimension n.

    Examples:
        >>> from pyfaust import dft
        >>> dft(1024)
        Faust size 1024x1024, density 0.0205078, nnz_sum 21504, 11 factor(s):
        - FACTOR 0 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 1 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 2 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 3 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 4 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 5 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 6 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 7 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 8 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 9 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 10 (complex) SPARSE, size 1024x1024, density 0.000976562, nnz 1024

        >>> dft(1024, normed=True) # is equiv. to next call
        Faust size 1024x1024, density 0.0205078, nnz_sum 21504, 11 factor(s):
        - FACTOR 0 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 1 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 2 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 3 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 4 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 5 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 6 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 7 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 8 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 9 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 10 (complex) SPARSE, size 1024x1024, density 0.000976562, nnz 1024

        >>> dft(1024, normed=False).normalize()
        Faust size 1024x1024, density 0.0205078, nnz_sum 21504, 11 factor(s):
        - FACTOR 0 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 1 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 2 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 3 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 4 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 5 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 6 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 7 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 8 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 9 (complex) SPARSE, size 1024x1024, density 0.00195312, nnz 2048
        - FACTOR 10 (complex) SPARSE, size 1024x1024, density 0.000976562, nnz 1024

   \see :py:func:`pyfaust.bitrev`, :py:func:`pyfaust.wht`, :py:func:`pyfaust.dct`, :py:func:`pyfaust.dst`, scipy.fft.fft, :py:func:`pyfaust.fact.butterfly`, :py:func:`pyfaust.rand_butterfly.`
    """
    log2n = np.floor(np.log2(n))
    if n > 2**log2n:
        raise ValueError("n must be a power of 2.")
    if not isinstance(normed, bool):
        raise TypeError("normed must be True of False.")
    if dev == "cpu":
        F = \
                Faust(core_obj=_FaustCorePy.FaustAlgoCplxDblGenCPU.fourierFaust(log2n,
                                                                                normed,
                                                                                diag_opt))
    elif dev.startswith("gpu"):
        F = \
                Faust(core_obj=_FaustCorePy.FaustAlgoCplxDblGenGPU.fourierFaust(log2n,
                                                                                normed,
                                                                                diag_opt))
    return F


def dct(n, normed=True, dev='cpu', dtype='float64'):
    r"""Constructs a Faust implementing the Direct Cosine Transform (Type II) Faust of order n.

    The analytical formula of DCT II used here is:
        \f$2 \sum_{i=0}^{n-1} x_i cos \left( {\pi k (2i + 1)} \over {2n} \right)\f$


    Args:
        n: (int)
            the order of the DCT (must be a power of two).
        normed: (bool)
            default to True to normalize the DFT Faust as if you called
            :func:`Faust.normalize()` and False otherwise.
        dev: (str)
            the device on which the Faust is created.
        dtype: (str)
            'float64' (default) or 'float32'.

    Returns:
        The DCT Faust.

    Example:
        >>> from pyfaust import dct
        >>> from scipy.fft import dct as scipy_dct
        >>> import numpy as np
        >>> DCT8 = dct(8, normed=False)
        >>> x = np.arange(8).astype('double')
        >>> np.real(DCT8@x)
        array([ 56.        , -25.76929209,   0.        ,  -2.6938192 ,
                 0.        ,  -0.80361161,   0.        ,  -0.20280929])
        >>> scipy_dct(x)
        array([ 56.        , -25.76929209,   0.        ,  -2.6938192 ,
                 0.        ,  -0.80361161,   0.        ,  -0.20280929])
        >>> np.allclose(DCT8@x, scipy_dct(x))
        True
        >>> # check the density with a larger DCT Faust of size 1024
        >>> float(dct(1024).density())
        0.076171875
        >>> # it is smaller than 1

    \see :py:func:`pyfaust.dft`, :py:func:`pyfaust.dst`, <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dct.html">scipy.fft.dct</a>, :py:func:`pyfaust.fact.butterfly`, :py:func:`pyfaust.rand_butterfly`, :py:func:`pyfaust.Faust.density`
    """
    dtype = _sanitize_dtype(dtype)
    DFT = pyfaust.dft(n, dev='cpu', normed=False)
#    P_ = np.zeros((n, n))
#    P_[np.arange(0, n//2), np.arange(0, n, 2)] = 1
#    P_[np.arange(n//2, n), np.arange(1, n, 2)[::-1]] = 1
    # P_ as sparse matrix
    P_row_inds = np.arange(0, n)
    P_col_inds = np.hstack((np.arange(0, n, 2), np.arange(1, n, 2)[::-1]))
    P_ = csr_matrix((np.ones(n), (P_row_inds, P_col_inds)), shape=(n, n))
    E = diags([2*np.exp(-1j*np.pi*k/2/n) for k in range(0, n)])
    f0 = csr_matrix(E @ DFT.factors(0))
    f_end = csr_matrix(DFT.factors(len(DFT)-1) @ P_)
    mid_factors = DFT.factors(range(1, len(DFT)-1))
    if pyfaust.isFaust(mid_factors):
        mid_F = mid_factors
    else:
        mid_F = Faust(mid_factors)
    DCT = (Faust(f0) @ mid_F @ Faust(f_end)).real
    if normed:
        DCT = DCT.normalize()
    if dev.startswith('gpu'):
        DCT = DCT.clone(dev='gpu')
    if dtype != 'float64':
        DCT = DCT.astype(dtype)
    return DCT




def dst(n, normed=True, dev='cpu', dtype='float64'):
    r"""
    Constructs a Faust implementing the Direct Sine Transform (Type II) Faust of order n.

    The analytical formula of DST II used here is:
        \f$2 \sum_{i=0}^{n-1} x_i sin \left( {\pi (k+1) (2i + 1)} \over {2n} \right)\f$

    Args:
        n: (int)
            the order of the DST (must be a power of two).
        normed: (bool)
            default to True to normalize the Hadamard Faust as if you called
            :func:`Faust.normalize()` and False otherwise.
        dev: (str)
            the device on which the Faust is created.
        dtype: (str)
            'float64' (default) or 'float32'.

    Returns:
        The DST Faust.

    Example:
        >>> from pyfaust import dst
        >>> from scipy.fft import dst as scipy_dst
        >>> import numpy as np
        >>> DST8 = dst(8, normed=False)
        >>> x = np.ones(8)
        >>> np.real(DST8@x)
        array([1.02516618e+01, 4.93038066e-32, 3.59990489e+00, 3.94430453e-31,
               2.40537955e+00, 9.86076132e-32, 2.03918232e+00, 0.00000000e+00])
        >>> scipy_dst(x)
        array([10.25166179,  0.        ,  3.59990489,  0.        ,  2.40537955,
                0.        ,  2.03918232,  0.        ])
        >>> np.allclose(DST8@x, scipy_dst(x))
        True
        >>> # check the density with a larger DST Faust of size 1024
        >>> float(dst(1024).density())
        0.201171875
        >>> # it is smaller than 1

    \see :py:func:`pyfaust.dft`, :py:func:`pyfaust.dct`, <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dst.html">scipy.fft.dst</a>, :py:func:`pyfaust.fact.butterfly`, :py:func:`pyfaust.rand_butterfly`, :py:func:`pyfaust.Faust.density`
    """
    def omega(N):
        """
        Returns the list of n-th root of unity raised to the power of -(k+1) (instead of
        k as in the FFT, the purpose here is to write the DST).
        """
        omega = np.exp(np.pi*1j/N) # exp(-i*2*pi/2N)
        return diags([omega**-(k+1) for k in range(0, N)]).tocsr()

    def B(N):
        """
        Butterfly factor of order N.
        """
        I_N2 = seye(N//2, format='csr')
        O_N2 = omega(N//2)
        return svstack((shstack((I_N2, O_N2)), shstack((I_N2, - O_N2))))

    def mod_fft(N, dev='cpu'):
        """
        Modified FFT for DST computation (it would have been the standard FFT
        if omega was raised to the power of -k instead of -(k+1)).
        """
        N_ = N
        Bs = []
        while N_ != 1:
            B_ = B(N_)
            diag_B = kron(seye(N//N_, format='csr'), B_).tocsr() # to avoid BSR
            # matrices because FAµST doesn't support BSR matrices concatenation
            # TODO: let BSR format after concatenation is supported
            Bs += [diag_B]
            N_ //= 2
        return Faust(Bs+[bitrev_perm(N).astype(Bs[-1].dtype)], dev=dev)

    log2n = np.floor(np.log2(n))
    if n > 2**log2n:
        raise ValueError("n must be a power of 2.")

    dtype = _sanitize_dtype(dtype)
    # compute the DST (look at issue #265 for doc, S permutation was replaced by mod_fft to fix missing last frequency)
    MDFT = mod_fft(n, dev=dev)
    D1 = csr_matrix(-2*diags([- 1j * np.exp(-1j * np.pi / 2 / n * (k+1)) for k in range(0,
                                                                                        n)]))
    D2 = csr_matrix(diags([np.exp(-1j * np.pi / n * (k+1)) for k in range(0, n)]))
    #    P_ = np.zeros((n*2, n))
    #    P_[np.arange(0, n//2), np.arange(0, n, 2)] = 1
    #    P_[np.arange(n, n + n // 2), np.arange(1, n, 2)] = 1
    # P_ as as sparse matrix
    P_row_inds = np.hstack((np.arange(0, n//2), np.arange(n, n + n // 2)))
    P_col_inds = np.hstack((np.arange(0, n, 2), np.arange(1, n, 2)))
    P_ = csr_matrix((np.ones(n), (P_row_inds, P_col_inds)), shape=(n*2, n))
    F_even = Faust(D1, dev=dev) @ MDFT
    F_odd = Faust(D1, dev=dev) @ Faust(D2) @ MDFT
    F = pyfaust.hstack((F_even, F_odd))
    F = F @ Faust(P_, dev=dev)
    F = F.real
    if normed:
        F = F.normalize()
    if dev.startswith('gpu'):
        F = F.clone(dev='gpu')
    if dtype != 'float64':
        F = F.astype(dtype)
    return F


def circ(c, dev='cpu', diag_opt=False):
    r"""Returns a circulant Faust C defined by the vector c (which is the first
    column of C.toarray()).

    Args:
        c: (np.ndarray)
            the vector to define the circulant Faust.
        dev: (str)
            the device on which the Faust is created, 'cpu' (default) or 'gpu'.
        diag_opt: (bool)
            if True then the returned Faust is optimized using
            pyfaust.opt_butterfly_faust (because the DFT is used to implement circ).

    Example:
        >>> from pyfaust import circ
        >>> import numpy as np
        >>> c = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> C = circ(c)
        >>> C
        Faust size 8x8, density 1.5, nnz_sum 96, 6 factor(s):
        - FACTOR 0 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 1 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 2 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 3 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 4 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 5 (complex) SPARSE, size 8x8, density 0.25, nnz 16

        >>> np.allclose(C.toarray()[:, 0], c)
        True
        >>> np.real(C.toarray())
        array([[1., 8., 7., 6., 5., 4., 3., 2.],
               [2., 1., 8., 7., 6., 5., 4., 3.],
               [3., 2., 1., 8., 7., 6., 5., 4.],
               [4., 3., 2., 1., 8., 7., 6., 5.],
               [5., 4., 3., 2., 1., 8., 7., 6.],
               [6., 5., 4., 3., 2., 1., 8., 7.],
               [7., 6., 5., 4., 3., 2., 1., 8.],
               [8., 7., 6., 5., 4., 3., 2., 1.]])
        >>> # Look at the density of a larger circulant Faust
        >>> # it indicates a speedup of the Faust-matrix/vector product
        >>> float(circ(np.random.rand(1024)).density())
        0.0390625

    \see <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.circulant.html">scipy.linalg.circulant</a>, :py:func:`pyfaust.anticirc`, :py:func:`pyfaust.toeplitz`
    """
    #TODO: handle cases len(c) == 1, 2
    if isinstance(c, list):
        c = np.array(c)
    if not isinstance(c, np.ndarray) or c.ndim != 1:
        raise TypeError('c must be a vector of numpy array type')
    diag_factor = 'multiplied'
    if diag_factor not in ['multiplied', 'csr']:
        raise ValueError('option diag_factor must be \'csr\' or'
                         ' \'multiplied\'')
    log2c = np.log2(len(c))
    if log2c != np.floor(log2c):
        C = toeplitz(c, np.hstack((c[0:1], c[-1:0:-1])), dev=dev)
        return C
    n = len(c)
    F = dft(n, normed=False, diag_opt=False)
    nf = len(F)
    P = F.factors(nf-1) # bitrev perm
    D = diags(F.T.conj()@(c/n))
    S = csr_matrix(P @ D @ P.T.conj())
    FwP = F.left(nf - 2) # F without permutation
    if not isFaust(FwP):
        # F is two factors, so FwP is one factor (i.e. a csr_matrix, not a
        # Faust)
        FwP = Faust(FwP)
    if diag_opt:
        right = opt_butterfly_faust(FwP).H
    else:
        right = FwP.H
    nfwp = len(FwP)
    left = FwP.left(nfwp-2, as_faust=True) # ignoring last butterfly factor
    # reintegrate last butterfly factor multiplied by S
    left = left @ Faust(FwP.factors(nfwp-1) @ S)
    if diag_opt:
        left = opt_butterfly_faust(left)
    C = left @ right
    if dev.startswith('gpu'):
        C = C.clone('gpu')
    return C


def anticirc(c, dev='cpu', diag_opt=False):
    r"""Returns an anti-circulant Faust A defined by the vector c (which is the last column of A.toarray()).

    Args:
        c: (np.ndarray)
            the vector to define the anti-circulant Faust.
        dev: (str)
            the device on which the Faust is created, 'cpu' (default) or 'gpu'.
        diag_opt: (bool)
            cf. pyfaust.circ.

    Example:
        >>> from pyfaust import anticirc
        >>> import numpy as np
        >>> c = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> A = anticirc(c)
        >>> A
        Faust size 8x8, density 1.5, nnz_sum 96, 6 factor(s):
        - FACTOR 0 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 1 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 2 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 3 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 4 (complex) SPARSE, size 8x8, density 0.25, nnz 16
        - FACTOR 5 (complex) SPARSE, size 8x8, density 0.25, nnz 16

        >>> np.allclose(A.toarray()[:, -1], c)
        True
        >>> np.real(A.toarray())
        array([[2., 3., 4., 5., 6., 7., 8., 1.],
               [3., 4., 5., 6., 7., 8., 1., 2.],
               [4., 5., 6., 7., 8., 1., 2., 3.],
               [5., 6., 7., 8., 1., 2., 3., 4.],
               [6., 7., 8., 1., 2., 3., 4., 5.],
               [7., 8., 1., 2., 3., 4., 5., 6.],
               [8., 1., 2., 3., 4., 5., 6., 7.],
               [1., 2., 3., 4., 5., 6., 7., 8.]])
        >>> # Look at the density of a larger anticirculant Faust
        >>> # it indicates a speedup of the Faust-matrix/vector product
        >>> float(anticirc(np.random.rand(1024)).density())
        0.0390625

    \see :py:func:`pyfaust.circ`, :py:func:`pyfaust.toeplitz`
    """
    #TODO: handle cases len(c) == 1, 2
    G = circ(c, diag_opt=diag_opt)
    nG = len(G)
    i = np.arange(len(c)-1, -1, -1)
    j = np.arange(0, len(c))
    P = csr_matrix((np.ones(j.size), (i, j)))
    if diag_opt:
        A = G @ Faust(P)
    else:
        # nG > 2
        A = G.left(nG-2) @ Faust(G.factors(nG-1) @ P)
    if dev.startswith('gpu'):
        return A.clone('gpu')
    return A


def toeplitz(c, r=None, dev='cpu', diag_opt=False):
    r"""Constructs a toeplitz Faust whose first column is c and first row r.

    Args:
        c: (np.ndarray)
            the first column of the toeplitz Faust.
        r: (np.ndarray)
            the first row of the toeplitz Faust. If none then r =
            np.conjugate(c). r[0] is ignored, the first row is always [c[0],
            r[1:]].
        dev: (str)
            the device on which the Faust is created, 'cpu' (default) or 'gpu'.
        diag_opt: (bool)
            cf. pyfaust.circ.

    Returns:
        The toeplitz Faust.

    Example:
        >>> from pyfaust import toeplitz
        >>> import numpy as np
        >>> c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> T = toeplitz(c)
        >>> T
        Faust size 10x10, density 5.52, nnz_sum 552, 10 factor(s):
        - FACTOR 0 (complex) SPARSE, size 10x32, density 0.0625, nnz 20
        - FACTOR 1 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 2 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 3 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 4 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 5 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 6 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 7 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 8 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 9 (complex) SPARSE, size 32x10, density 0.0625, nnz 20

        >>> np.allclose(T.toarray()[:, 0], c)
        True
        >>> np.allclose(T.toarray()[0, :], c)
        True
        >>> np.real(T.toarray())
        array([[ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.],
               [ 2.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.],
               [ 3.,  2.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.],
               [ 4.,  3.,  2.,  1.,  2.,  3.,  4.,  5.,  6.,  7.],
               [ 5.,  4.,  3.,  2.,  1.,  2.,  3.,  4.,  5.,  6.],
               [ 6.,  5.,  4.,  3.,  2.,  1.,  2.,  3.,  4.,  5.],
               [ 7.,  6.,  5.,  4.,  3.,  2.,  1.,  2.,  3.,  4.],
               [ 8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.,  2.,  3.],
               [ 9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.,  2.],
               [10.,  9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.]])
        >>> r = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        >>> T2 = toeplitz(c, r)
        >>> T2
        Faust size 10x10, density 5.52, nnz_sum 552, 10 factor(s):
        - FACTOR 0 (complex) SPARSE, size 10x32, density 0.0625, nnz 20
        - FACTOR 1 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 2 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 3 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 4 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 5 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 6 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 7 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 8 (complex) SPARSE, size 32x32, density 0.0625, nnz 64
        - FACTOR 9 (complex) SPARSE, size 32x10, density 0.0625, nnz 20

        >>> np.allclose(T2.toarray()[0, :], np.hstack((c[0:1], r[1:])))
        True
        >>> np.allclose(T2.toarray()[:, 0], c)
        True
        >>> np.real(T2.toarray())
        array([[ 1., 12., 13., 14., 15., 16., 17., 18., 19., 20.],
               [ 2.,  1., 12., 13., 14., 15., 16., 17., 18., 19.],
               [ 3.,  2.,  1., 12., 13., 14., 15., 16., 17., 18.],
               [ 4.,  3.,  2.,  1., 12., 13., 14., 15., 16., 17.],
               [ 5.,  4.,  3.,  2.,  1., 12., 13., 14., 15., 16.],
               [ 6.,  5.,  4.,  3.,  2.,  1., 12., 13., 14., 15.],
               [ 7.,  6.,  5.,  4.,  3.,  2.,  1., 12., 13., 14.],
               [ 8.,  7.,  6.,  5.,  4.,  3.,  2.,  1., 12., 13.],
               [ 9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1., 12.],
               [10.,  9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.]])
        >>> # Look at the density of a larger Toeplitz Faust
        >>> # it indicates a speedup of the Faust-matrix/vector product
        >>> float(toeplitz(np.random.rand(1024), np.random.rand(1024)).density())
        0.08203125

    \see <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.toeplitz.htm">scipy.linalg.toeplitz</a>, :py:func:`pyfaust.circ`, :py:func:`pyfaust.anticirc`
    """
    if r is None:
        r = np.conjugate(c)
    m = len(c)
    n = len(r)
    N = int(2**np.ceil(np.log2(max(m, n))))
    c_ = np.hstack((c, np.zeros(N-m+1+N-n), r[:0:-1]))
    #TODO: handle cases len(c) == 1, 2
    C = circ(c_, diag_opt=diag_opt)
    if diag_opt:
        # see issue #335
        T = Faust(seye(m, C.shape[0], format='csr')) @ C @ Faust(seye(C.shape[1], n, format='csr'))
    else:
        T = C[:m, :n]
    if dev.startswith('gpu'):
        return T.clone('gpu')
    return T


def eye(m, n=None, dtype='float64',  dev="cpu"):
    """
        Faust identity.

        Args:
          m: (int)
              number of rows,
          n: (int)
              number of columns, set to m by default.
          dtype: (str)
              the dtype of the identity ('float32', the default 'float64'/'double',
              or 'complex'/'complex128').

        Examples:
            >>> from pyfaust import eye
            >>> eye(5)
            Faust size 5x5, density 0.2, nnz_sum 5, 1 factor(s):
            - FACTOR 0 (double) SPARSE, size 5x5, density 0.2, nnz 5
             identity matrix flag

            >>> eye(5, 4)
            Faust size 5x4, density 0.2, nnz_sum 4, 1 factor(s):
            - FACTOR 0 (double) SPARSE, size 5x4, density 0.2, nnz 4
             identity matrix flag

            >>> eye(5, dtype='complex')
            Faust size 5x5, density 0.2, nnz_sum 5, 1 factor(s):
            - FACTOR 0 (complex) SPARSE, size 5x5, density 0.2, nnz 5
             identity matrix flag
    """
    check_dev(dev)
    if n is None:
        n = m
    unknown_dtype_err = ValueError('Unknown dtype has been used')
    dtype = _sanitize_dtype(dtype)
    if dev == "cpu":
        if dtype == 'float64':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUDbl.eyeFaust(m, n))
        elif dtype == 'float32':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUFlt.eyeFaust(m, n))
        elif dtype == 'complex':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUCplxDbl.eyeFaust(m, n))
        else:
            raise unknown_dtype_err
    elif dev.startswith("gpu"):
        if dtype == 'float64':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUDbl.eyeFaust(m, n))
        elif dtype == 'float32':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUFlt.eyeFaust(m, n))
        elif dtype == 'complex':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUCplxDbl.eyeFaust(m, n))
        else:
            raise unknown_dtype_err
    return rF
#    from scipy.sparse import eye
#    if not n:
#        n = m
#    e = eye(m, n).tocsr()
#    if t == 'complex':
#        e = e.astype('complex')
#    elif t != 'real':
#        raise ValueError("t must be 'real' or 'complex'")
#    return Faust(e)


def rand_bsr(num_rows, num_cols, bnrows, bncols, num_factors=None, density=.1,
             dev='cpu', dtype='float64'):
    r"""
    Generates a random Faust composed only of BSR matrices.

    Args:
        num_rows: (int)
            the Faust number of rows.
        num_cols: (int)
            the Faust number of columns.
        bnrows: (int)
            the nonzero block number of rows (must divide num_rows).
        bncols: (int)
            the nonzero block number of columns (must divide num_cols).
        num_factors: (int or tuple(int, int) or NoneType)
                If it's an integer it will be the number of random factors to set in the Faust.
                If num_factors is a tuple of 2 integers then the
                number of factors will be set randomly between
                num_factors[0] and num_factors[1] (inclusively).
                If num_factors is None then 5 factors are generated.
        density: (float)
            the Faust factor density (it determines the number of nonzero blocks). It must be between 0 and 1.
        dev: (str)
            the device on which the Faust is created, 'cpu' (default) or 'gpu'.
        dtype: (str)
            the numpy dtype of the Faust.

    Example:
        >>> from pyfaust import rand_bsr
        >>> rand_bsr(100, 100, 20, 10, num_factors=6)
        Faust size 100x100, density 0.6, nnz_sum 6000, 6 factor(s):
        - FACTOR 0 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)
        - FACTOR 1 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)
        - FACTOR 2 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)
        - FACTOR 3 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)
        - FACTOR 4 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)
        - FACTOR 5 (double) BSR, size 100x100 (blocksize = 20x10), density 0.1, nnz 1000 (nnz blocks: 5)

    \see <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.bsr_matrix.html">bsr_matrix</a>, :py:func:`Faust.__init__`, :py:func:`pyfaust.rand`
    """
    dtype = _sanitize_dtype(dtype)
    if num_factors is None:
        min_num_factors = max_num_factors = 5
    elif isinstance(num_factors, int):
        min_num_factors = max_num_factors = num_factors
    elif isinstance(num_factors, tuple) and len(num_factors) == 2 and isinstance(num_factors[0], int) and isinstance(num_factors[1], int):
        min_num_factors = num_factors[0]
        max_num_factors = num_factors[1]
    else:
        raise ValueError('num_factors must be None, a int or a tuple of int')
    # sanity checks
    if num_rows != num_cols:
        raise ValueError('currently only random square BSR Fausts can be'
                         ' generated.')
    if num_rows % bnrows != 0 or num_cols % bncols != 0:
        raise ValueError('the size of blocks must evenly divide the size of Faust matrices')
    if dev.startswith('gpu') and bnrows != bncols:
        raise ValueError('currently only square blocks are supported on GPU.')
    if dev == "cpu":
        if dtype == 'float64':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUDbl.randBSRFaust(num_rows,
                                                                             num_cols,
                                                                             min_num_factors,
                                                                             max_num_factors,
                                                                             bnrows,
                                                                             bncols,
                                                                             density))
        elif dtype == 'float32': # type == 'float'
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUFlt.randBSRFaust(num_rows,
                                                                             num_cols,
                                                                             min_num_factors,
                                                                             max_num_factors,
                                                                             bnrows,
                                                                             bncols,
                                                                             density))
        elif dtype == 'complex':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUCplxDbl.randBSRFaust(num_rows,
                                                                                 num_cols,
                                                                                 min_num_factors,
                                                                                 max_num_factors,
                                                                                 bnrows,
                                                                                 bncols,
                                                                                 density))
    elif dev.startswith("gpu"):
        if dtype == 'float64':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUDbl.randBSRFaust(num_rows,
                                                                             num_cols,
                                                                             min_num_factors,
                                                                             max_num_factors,
                                                                             bnrows,
                                                                             bncols,
                                                                             density))
        elif dtype == 'float32': # type == 'float'
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUFlt.randBSRFaust(num_rows,
                                                                             num_cols,
                                                                             min_num_factors,
                                                                             max_num_factors,
                                                                             bnrows,
                                                                             bncols,
                                                                             density))
        elif dtype == 'complex':
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUCplxDbl.randBSRFaust(num_rows,
                                                                                 num_cols,
                                                                                 min_num_factors,
                                                                                 max_num_factors,
                                                                                 bnrows,
                                                                                 bncols,
                                                                                 density))
    else:
        raise ValueError('Invalid device')
    return rF


def rand(num_rows, num_cols, num_factors=None, dim_sizes=None,
         density=None, fac_type='sparse',
         per_row=True, dev='cpu', dtype='float64', field=None, seed=0):
    r"""
    Generates a random Faust.

        Args:
            num_rows: the Faust number of rows.
            num_cols: the Faust number of columns.
            num_factors: if it's an integer it is the number of random factors to set in the Faust.
                        If num_factors is a list or tuple of 2 integers then the
                        number of factors is set randomly between
                        num_factors[0] and num_factors[1] (inclusively).
                        Defaultly, num_factors is None, it means a 5 factors
                        long Faust is generated.
                        dim_sizes: if it's an integer all Faust factors
                        are square matrices (except maybe the first and last
                        ones, depending on num_rows and num_cols). The size of
                        the intermediary square factors is size_dims**2.
                        If it's a list or tuple of 2 integers then the
                        number of rows and columns are both
                        a random number between size_dims[0] and
                        size_dims[1] (inclusively).
                        Note that the first factor number of rows and the last
                        factor number of columns are always fixed (they are the
                        dimension sizes of the Faust: num_rows, num_cols arguments).
                        if dim_sizes is None then dim_sizes is defaultly [num_rows,
                        num_cols].
            density: the approximate density of factors. The
                    default value is such that each factor gets 5 non-zero
                    elements per row, if per_row is True, or per column otherwise.
                    It should be a floating point number greater than 0 and
                    lower or equal to 1.
                    A density of zero is equivalent to the default case.
            fac_type: the storage representation of factors. It must be
                    'sparse', 'dense' or 'mixed'. The latter designates a mix of dense and
                    sparse matrices in the generated Faust (the choice is made according
                    to a uniform distribution).
            dtype: the dtype of the Faust ('float32', 'float64' or 'complex').
            per_row: if True the factor matrix is constructed per row
                    applying the density to each row. If False the construction is
                    made with the density applied on each column.
            dev: the device on which to create the Faust ('cpu' or 'gpu').
            field: (DEPRECATED, use dtype) a str to set the Faust field: 'real' or 'complex'.
            seed: set PRNG initialization, useful for reproducibility of this function calls,
            otherwise seed argument shouldn't be used (the PRNG is automatically initialized).


    Returns:
        the random Faust.

    Examples:
        >>> from pyfaust import rand, seed
        >>> seed(42)
        >>> F = rand(2, 10, density=.5, dtype='complex')
        >>> G = rand(10, 20, num_factors=[2, 5], density=.5, fac_type="dense")
        >>> F
        Faust size 2x10, density 2.6, nnz_sum 52, 5 factor(s):
        - FACTOR 0 (complex) SPARSE, size 2x8, density 0.5, nnz 8
        - FACTOR 1 (complex) SPARSE, size 8x4, density 0.5, nnz 16
        - FACTOR 2 (complex) SPARSE, size 4x5, density 0.4, nnz 8
        - FACTOR 3 (complex) SPARSE, size 5x3, density 0.333333, nnz 5
        - FACTOR 4 (complex) SPARSE, size 3x10, density 0.5, nnz 15

        >>> G
        Faust size 10x20, density 1.65, nnz_sum 330, 4 factor(s):
        - FACTOR 0 (double) DENSE, size 10x15, density 0.466667, nnz 70
        - FACTOR 1 (double) DENSE, size 15x12, density 0.5, nnz 90
        - FACTOR 2 (double) DENSE, size 12x11, density 0.454545, nnz 60
        - FACTOR 3 (double) DENSE, size 11x20, density 0.5, nnz 110

    \see :func:`Faust.__init__, ` :py:func:`pyfaust.rand_bsr`
    """
    check_dev(dev)
    dtype = _sanitize_dtype(dtype)
    if field is not None:
        field = field.lower()
        warnings.warn("pyfaust.rand field argument is deprecated, please use"
                      " dtype to remove this warning.")
        if field == 'complex' and dtype != 'complex'\
           or field != 'complex' and dtype == 'complex':
            warnings.warn('one of field or dtype argument is complex, the'
                          ' other is not: enforcing complex for both.')
            # necessary conversion for backward compatibility with field
            field = dtype = 'complex'
        elif field == 'real' and dtype not in ['float32', 'float64']:
            raise ValueError('field and dtype arguments aren\'t consistent, one'
                             'is real the other not.')
    else:
        field = 'real' if dtype in ['float32', 'float64'] else 'complex'
    if field not in ['real', 'complex']:
        raise ValueError('field argument must be either \'real\' or \'complex\'.')
    if field == 'real':
        is_real = True
        if dtype == 'float64':
            type = 'double'
        elif dtype == 'float32':
            type = 'float'
    elif field == 'complex' or dtype == 'complex':
        type = 'complex'
        is_real = False
    DENSE = 0
    SPARSE = 1
    MIXED = 2
    REAL = 3
    COMPLEX = 4
    # set repr. type of factors
    if not isinstance(fac_type, str) or fac_type not in ['sparse',
                                                         'dense',
                                                         'mixed']:
        raise ValueError('rand(): argument fac_type must be a'
                         ' str equal to \'sparse\','
                         ' \'dense\' or \'mixed\'.')

    fac_type_map = {"sparse": SPARSE, "dense": DENSE, "mixed": MIXED}
    # set field of matrices/factors
    if not isinstance(is_real, bool):
        raise ValueError('rand(): argument is_real must be a'
                         'boolean.')
    if is_real:
        field = REAL
    else:
        field = COMPLEX
    if num_factors is None:
        num_factors = 5
    if (isinstance(num_factors, (list, tuple))) and len(num_factors) == 2:
        min_num_factors = num_factors[0]
        max_num_factors = num_factors[1]
    elif isinstance(num_factors, int):
        min_num_factors = max_num_factors = num_factors
    else:
        raise ValueError("rand(): num_factors argument must be an "
                         "integer or a list/tuple of 2 integers.")
    if dim_sizes is None:
        dim_sizes = [num_rows, num_cols]
    if isinstance(dim_sizes, (list, tuple)) and len(dim_sizes) == 2:
        min_dim_size = dim_sizes[0]
        max_dim_size = dim_sizes[1]
    elif isinstance(dim_sizes, (int, np.int64)):
        min_dim_size = max_dim_size = dim_sizes
    else:
        raise ValueError("rand(): dim_sizes argument must be an "
                         "integer or a list/tuple of 2 integers.")
    if not isinstance(per_row, bool):
        raise ValueError("FaustFact.rand(): per_row argument must be a "
                         "bool.")
    if not density:
        density = -1
    elif not np.isscalar(density) or not np.isreal(density):
        raise ValueError("rand(): density must be a float")
    density = float(density)
    if dev == "cpu":
        if field == REAL:
            if type == 'double':
                rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUDbl.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
            else: # type == 'float'
                rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUFlt.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
        elif field == COMPLEX:
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenCPUCplxDbl.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
        # no else possible (see above)
    elif dev.startswith("gpu"):
        if field == REAL:
            if type == 'double':
                rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUDbl.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
            else: # type == float:
                rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUFlt.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
        elif field == COMPLEX:
            rF = Faust(core_obj=_FaustCorePy.FaustAlgoGenGPUCplxDbl.randFaust(num_rows,
                                                                              num_cols,
                                                                              fac_type_map[fac_type], min_num_factors, max_num_factors,
                                                                              min_dim_size,
                                                                              max_dim_size,
                                                                              density,
                                                                              per_row,
                                                                              seed))
    return rF


def rand_butterfly(n, dtype='float64', dev='cpu', diag_opt=False):
    r"""
    Constructs a Faust corresponding to the product of log2(n) square factors of size n with butterfly supports and random nonzero coefficients.

    The random coefficients are drawn i.i.d. according to a standard Gaussian
    (real or complex circular according to the type).

    Args:
        n: order of the butterfly (must be a power of two).
        diag_opt: if True then the returned Faust is optimized using
        pyfaust.opt_butterfly_faust.
        dtype: 'float32', 'float64' or 'complex', the dtype of the random Faust.
        dev: 'cpu' or 'gpu', the device where the Faust is created.


    Returns:
        F, a random butterfly support Faust.

    \see :py:func:`pyfaust.fact.butterfly`, :py:func:`pyfaust.dft`, :py:func:`pyfaust.opt_butterfly_faust`
    """
    from numpy.random import randn
    dtype = _sanitize_dtype(dtype)
    DFT = dft(n)
    # ignore the bitreversal permutation
    B = DFT.factors(range(0, DFT.numfactors()-1))
    if n == 2:
        # B is a csr mat
        B = Faust(B)
    RB_factors = []
    for i in range(len(B)):
        rb = B.factors(i).astype(dtype)
        if dtype != 'complex':
            rb[rb != 0] = randn(rb.size).astype(dtype)
        else:
            rb[rb != 0] = randn(rb.size) + 1j * randn(rb.size)
        RB_factors.append(rb)
    F = Faust(RB_factors)
    if diag_opt:
        F = opt_butterfly_faust(F)
    return F


def opt_butterfly_faust(F):
    r"""
    Optimizes any Faust composed of butterfly factors.

    The returned Faust will be more efficient if multiplied by a vector or a
    matrix.
    This optimization is based on the diagonals of each butterfly factor.
    Multiplying a butterfly factor B by a vector x (y = B@x) is equivalent to forming
    two diagonal matrices D1 and D2 from B and compute y' = D1@x + D2 @ x[I] where I is
    set in the proper order to obtain y' = y.

    Args:
        F: The Faust to optimize. If the factors of F are not set according to
        a butterfly structure, the result is not defined.

    Returns:
        The optimized Faust.

    \see :py:func:`pyfaust.fact.butterfly`, :py:func:`pyfaust.dft`, :py:func:`pyfaust.rand_butterfly`
    """
    oF = Faust(core_obj=F.m_faust.optimizeButterfly())
    return oF


def enable_gpu_mod(libpaths=None, backend='cuda', silent=False, fatal=False):
    """
    This function loads explicitly the gpu_mod library in memory.

    Normally it's not required to load the library manually, but it could be
    useful to set a non-default path or to diagnose a loading issue.

    Args:
        libpaths: (list[str])
            the absolute or relative paths where to search the dynamic
            library (gm) to load. By default, it's none to auto-find the library
            (if possible).
        backend: (str)
            the GPU backend to use, only 'cuda' is available for now.
        silent: (bool)
            if True nothing or almost will be displayed on loading,
            otherwise all messages are visible.
    """
    return _FaustCorePy.enable_gpu_mod(libpaths, backend, silent, fatal)


def is_gpu_mod_enabled():
    r"""
    Returns True if the gpu_mod plug-in has been loaded correctly, False otherwise.

    \see :py:func:`pyfaust.is_gpu_mod_working`
    """
    return _FaustCorePy._is_gpu_mod_enabled()


def is_gpu_mod_working():
    """
    This function returns True if gpu_mod is working properly False otherwise.

    is_gpu_mod_working comes as a complement of :py:func:`pyfaust.is_gpu_mod_enabled`
    The latter ensures that gpu_mod shared library/plugin is properly loaded in
    memory but doesn't ensure that the GPU is available (for example, the
    NVIDIA driver might not be installed). The former ensures both that the
    gpu_mod is loaded and the GPU (device 0) is properly available for
    computing.

    """
    # TODO: test another device (dev argument)
    if is_gpu_mod_enabled():
        try:
            gpuF = rand(1, 1, dev='gpu')
        except Exception:
            # knowing that the Faust size can't be smaller than one
            # it is not likely a full GPU memory comsumption error
            # then it is a CUDA device availability error
            # (e.g. CUDA installed but the driver is not or GPU not plugged in)
            # anyway the gpu_mod can't work
            return False
        return 'gpuF' in locals()
    else:
        return False


def check_dev(dev):
    if dev.startswith('gpu'):
        if not is_gpu_mod_enabled():
            raise Exception('GPU device is not available on your environment.')
    elif dev != 'cpu':
        raise ValueError("dev must be 'cpu' or 'gpu[:id]'")


def _cplx2real_op(op):
    if pyfaust.isFaust(op):
        return Faust([_cplx2real_op(op.factors(i)) for i in
                      range(op.numfactors())], dev=op.device)
    else:
        rop = np.real(op) # doesn't change type for scipy matrix if it is one
        iop = np.imag(op)
        if isinstance(op, (csr_matrix, csc_matrix, coo_matrix, bsr_matrix)):
            vertcat = svstack
            horzcat = shstack
        elif isinstance(op, np.ndarray):
            vertcat = vstack
            horzcat = hstack
        else:
            raise TypeError('op must be a scipy sparse matrix or a np.ndarray')
        real_part = horzcat((rop, - iop))
        imag_part = horzcat((iop, rop))
        return vertcat((real_part, imag_part))


def seed(s):
    """(Re)Initializes the pyfaust pseudo-random generator.

    It is useful to reproduce some code based for example on pyfaust.rand or
    pyfaust.rand_bsr.

    Example:
        >>> from pyfaust import rand, seed
        >>> seed(42) # just for reproducibility
        >>> F = rand(1024, 1024, dim_sizes=[1, 1024], num_factors=5, fac_type='mixed')
        >>> # F will always be the same
        >>> F
        Faust size 1024x1024, density 0.017313, nnz_sum 18154, 5 factor(s):
        - FACTOR 0 (double) SPARSE, size 1024x754, density 0.0066313, nnz 5120
        - FACTOR 1 (double) SPARSE, size 754x386, density 0.0129534, nnz 3770
        - FACTOR 2 (double) DENSE, size 386x1000, density 0.004, nnz 1544
        - FACTOR 3 (double) SPARSE, size 1000x544, density 0.00919118, nnz 5000
        - FACTOR 4 (double) SPARSE, size 544x1024, density 0.00488281, nnz 2720



    """
    _FaustCorePy.FaustCoreGenDblCPU.set_seed(s)


def faust_logo():
    """
    Generates the FAµST logo and returns it as a Faust.

    Example:
        >>> import pyfaust as pf
        >>> pf.seed(42)
        >>> logo = pf.faust_logo()
        >>> logo
        Faust size 50x50, density 1.3412, nnz_sum 3353, 5 factor(s):
        - FACTOR 0 (double) DENSE, size 50x50, density 0.2372, nnz 593
        - FACTOR 1 (double) DENSE, size 50x50, density 0.3228, nnz 807
        - FACTOR 2 (double) DENSE, size 50x50, density 0.2432, nnz 608
        - FACTOR 3 (double) DENSE, size 50x50, density 0.3564, nnz 891
        - FACTOR 4 (double) DENSE, size 50x50, density 0.1816, nnz 454

        >>> # logo.imshow()
        >>> # import matplotlib.pyplot as plt
        >>> # plot.show()
    """
    from pyfaust.logo import gen_faust_logo
    return gen_faust_logo()



class FaustMulMode:
    """
    <b/> Enumeration class of all matrix chain multiplication methods available to multiply a Faust to a matrix or to compute :func:`Faust.toarray().`

    These methods are used by :func:`Faust.optimize_time().`

    NOTE: it's not advisable to use these methods directly. The user should use
    :func:`Faust.optimize_time()` but the access is left open for experimental purpose.

    Examples:
        >>> from pyfaust import rand as frand, seed as fseed, FaustMulMode
        >>> from numpy.random import rand, seed
        >>> fseed(42) # just for reproducibility
        >>> seed(42)
        >>> F = frand(100, 100, 5, [100, 1024])
        >>> F.m_faust.set_FM_mul_mode(FaustMulMode.DYNPROG) # method used to compute Faust-matrix product or Faust.toarray()
        >>> F @ rand(F.shape[1], 512) # Faust-matrix mul. using method DYNPROG
        array([[34.29346113, 33.5135258 , 31.83862847, ..., 32.89901332,
                36.90417709, 32.20140406],
               [45.40983901, 42.52512058, 42.14810308, ..., 44.2648802 ,
                48.4027215 , 40.55809844],
               [27.12859996, 28.26596387, 25.898984  , ..., 27.47460378,
                29.35053152, 25.24167465],
               ...,
               [48.42899773, 47.4001851 , 43.96370573, ..., 47.25218683,
                53.03379773, 46.12690926],
               [39.9583232 , 40.778263  , 36.65671168, ..., 40.69390161,
                43.55280684, 40.37781963],
               [26.92859133, 28.40176389, 24.73304576, ..., 27.72648267,
                28.78612539, 25.82727371]])
        >>> F.toarray() # using the same method
        array([[1.13340453, 0.94853857, 0.60713635, ..., 1.29155048, 0.98107444,
                0.30254208],
               [1.92753189, 0.45268035, 0.72474175, ..., 0.43439703, 1.21532731,
                0.50115957],
               [1.35028724, 0.30557493, 0.15632569, ..., 0.80602032, 0.56741856,
                0.58193385],
               ...,
               [0.63172715, 1.0883051 , 1.2760964 , ..., 0.45745425, 0.85951258,
                0.25173183],
               [0.85748924, 0.68716077, 0.96293286, ..., 1.09480206, 0.8219215 ,
                0.83602967],
               [0.5461995 , 0.36918089, 0.4556373 , ..., 0.57842966, 0.52784458,
                0.30465166]])

    """
    ## \brief The default method, it computes the product from the right to the left.
    DEFAULT_L2R = 0
    ## \brief This method implements the classic dynamic programming solution to the chain matrix problem.
    ##
    ## See https://en.wikipedia.org/wiki/Matrix_chain_multiplication#A_dynamic_programming_algorithm.
    ## Note that the standard method is extended in order to take into account the complexity of multiplications including a sparse matrix (because that's not the same cost than multiplying dense matrices).
    DYNPROG = 5
    ## \brief This method computes the product of the matrix chain from the left to the right using the Torch C++ library (CPU backend).
    ##
    ## This method is only available for the specific packages pyfaust_torch.
    TORCH_CPU_L2R = 8
    ## \brief This method is implemented using the Torch library and follows a greedy principle: it chooses to multiply the less costly product of two matrices at each step of the whole product computation.
    ##
    ## The computational cost depends on the matrix dimensions and the number of nonzeros (when a matrix is in sparse format).
    ## This method is only available for the specific packages pyfaust_torch.
    TORCH_CPU_GREEDY = 9
    ## \brief The same as TORCH_CPU_L2R except that torch::chain_matmul is used to
    ## compute in one call the intermediary product of dense contiguous
    ## factors, then the result is multiplied by sparse factors if any remains.
    ##
    ## torch::chain_matmul follows the dynamic programming principle as DYNPROG method does (but the former handles only dense matrices).
    ##
    ## References:
    ## https://pytorch.org/cppdocs/api/function_namespaceat_1aee491a9ff453b6033b4106516bc61a9d.html?highlight=chain_matmul
    ## https://pytorch.org/docs/stable/generated/torch.chain_matmul.html?highlight=chain_matmul#torch.chain_matmul
    ## This method is only available for the specific packages pyfaust_torch.
    TORCH_CPU_DENSE_DYNPROG_SPARSE_L2R = 10
