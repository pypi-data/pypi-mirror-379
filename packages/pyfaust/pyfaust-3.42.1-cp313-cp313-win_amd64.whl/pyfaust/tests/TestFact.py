import numpy as np
import os
from pyfaust import fact
import warnings
try:
    import torch

    found_pytorch = True
except ImportError:
    found_pytorch = False
    warnings.warn("Did not find PyTorch, therefore use NumPy/SciPy.")
import scipy as sp
import unittest


class TestFact(unittest.TestCase):
    """Test case for the 'fact' module."""

    def __init__(self, methodName='runTest', dev='cpu', dtype='double'):
        super(TestFact, self).__init__(methodName)
        self.dev = dev
        if dtype == 'real':  # backward compat
            dtype = 'double'
        self.dtype = dtype
        # TODO: use different types later

    def test_fdb(self):
        """Test of the function 'fdb'."""

        n_repeats = 10

        M = 2 ** np.random.randint(1, high=11)
        N = 2 ** np.random.randint(1, high=11)
        matrix = np.random.randn(M, N)
        self.assertRaises(Exception, fact.fdb, matrix, 2, max(M, N) + 1)
        self.assertRaises(NotImplementedError,
                          fact.fdb, matrix, 2, 1, True, 'nothing')

        for i in range(n_repeats):
            # Ones matrix
            rank = 1
            n_factors = np.random.randint(2, high=9)
            M = np.random.randint(2, high=257)  #2 ** np.random.randint(1, high=11) + 1
            N = np.random.randint(2, high=257)  #2 ** np.random.randint(1, high=11) + 1
            matrix = np.ones((M, N))
            print("ones {0:d}: shape=({1:d}, {2:d}),".format(i, M, N) +
                  " number of factors={0:d}".format(n_factors))
            for h in ['left-to-right', 'balanced']:
                for b in [False, True]:
                    F = fact.fdb(matrix, n_factors=n_factors,
                                 rank=rank, hierarchical_order=h,
                                 orthonormalize=b)
                    print(F)
                    ncols = F.factors(F.numfactors() - 1).shape[1]
                    approx = np.eye(ncols, M=N, k=0)
                    for f in range(F.numfactors()):
                        approx = F.factors(F.numfactors() - 1 - f) @ approx
                    error = np.linalg.norm(matrix - approx) / np.linalg.norm(matrix)
                    print(h, b, 'error={0:e}'.format(error))
                    self.assertTrue(error < 1e-12)

        for i in range(n_repeats):
            # Hadamard matrix
            N = 2 ** np.random.randint(1, high=8)
            n_factors = np.random.randint(2, high=9)
            H = sp.linalg.hadamard(N)
            print("hadamard {0:d}: shape=({1:d}, {2:d}),".format(i, N, N) +
                  " number of factors={0:d}".format(n_factors))
            for h in ['left-to-right', 'balanced']:
                for b in [False, True]:
                    F = fact.fdb(H, n_factors=n_factors,
                                 rank=rank, hierarchical_order=h,
                                 orthonormalize=b)
                    print(F)
                    ncols = F.factors(F.numfactors() - 1).shape[1]
                    approx = np.eye(ncols, M=N, k=0)
                    for f in range(F.numfactors()):
                        approx = F.factors(F.numfactors() - 1 - f) @ approx
                    error = np.linalg.norm(H - approx) / np.linalg.norm(H)
                    print(h, b, 'error={0:e}'.format(error))
                    self.assertTrue(error < 1e-12)

        for i in range(n_repeats):
            # DFT matrix
            N = 2 ** np.random.randint(1, high=8)
            M = N
            # M = N + 1
            # while M > N:
            #     M = 2 ** np.random.randint(1, high=8)
            n_factors = np.random.randint(2, high=9)
            rank = 2 ** (int(np.log2(min(M, N))) // 2)
            x = np.exp(-2.0j * np.pi * np.arange(N) / N)
            V = np.vander(x, N=None, increasing=True)[:M, :]
            print("vandermonde {0:d}: shape=({1:d}, {2:d}),".format(i, M, N) +
                  " rank={0:d},".format(rank) +
                  " number of factors={0:d}".format(n_factors))
            for h in ['left-to-right', 'balanced']:
                for b in [False, True]:
                    # No bit-reversal permutation.
                    F = fact.fdb(V, n_factors=n_factors,
                                 rank=rank, hierarchical_order=h,
                                 orthonormalize=b)
                    print(F)
                    nf = F.numfactors()
                    ncols = F.factors(nf - 1).shape[1]
                    approx = np.eye(ncols, M=N, k=0)
                    for f in range(nf):
                        approx = F.factors(nf - 1 - f) @ approx
                    # Because of bit-reversal permutation we do not need
                    # to tune the rank as a function of matrix size.
                    F_bitrev = fact.fdb(V, n_factors=n_factors,
                                        bit_rev_perm=True, rank=1,
                                        hierarchical_order=h,
                                        orthonormalize=b)
                    print(F_bitrev)
                    nf = F_bitrev.numfactors()
                    ncols = F_bitrev.factors(nf - 1).shape[1]
                    approx_bitrev = np.eye(ncols, M=N, k=0)
                    for f in range(nf):
                        approx_bitrev = F_bitrev.factors(nf - 1 - f) @ approx_bitrev
                    # np.set_printoptions(linewidth=200)
                    # print(V)
                    # import pyfaust as pyf
                    # print(pyf.dft(M, normed=False).toarray())
                    # print(pyf.dft(M, normed=True).toarray())
                    # print(approx)
                    error = np.linalg.norm(V - approx) / np.linalg.norm(V)
                    print(h, b, 'error(no bitrev)={0:e}'.format(error))
                    self.assertTrue(error < 1e-12)
                    error = np.linalg.norm(V - approx_bitrev) / np.linalg.norm(V)
                    print(h, b, 'error(bitrev)={0:e}'.format(error))
                    self.assertTrue(error < 1e-12)

        # Cross-validation no PyTorch version versus PyTorch version.
        for i in range(n_repeats):
            continue
            if not found_pytorch:
                continue
            rank = 1
            n_factors = np.random.randint(2, high=9)
            M = np.random.randint(2, high=257)  #2 ** np.random.randint(1, high=9)
            N = np.random.randint(2, high=257)  #2 ** np.random.randint(1, high=9)
            print("random {0:d}: shape=({1:d}, {2:d}),".format(i, M, N) +
                  " number of factors={0:d}".format(n_factors))
            # Use PyTorch
            matrix0 = torch.randn(M, N)
            F0 = fact.fdb(matrix0, n_factors=n_factors,
                          rank=rank, backend='pytorch')
            print(F0)
            nf = F0.numfactors()
            ncols = F0.factors(nf - 1).shape[1]
            approx0 = np.eye(ncols, M=N, k=0)
            for f in range(nf):
                approx0 = F0.factors(nf - 1 - f) @ approx0
            # Use NumPy
            matrix1 = matrix0.numpy()
            F1 = fact.fdb(matrix1, n_factors=n_factors,
                          rank=rank, backend='numpy')
            print(F1)
            nf = F1.numfactors()
            ncols = F1.factors(nf - 1).shape[1]
            approx1 = np.eye(ncols, M=N, k=0)
            for f in range(nf):
                approx1 = F1.factors(nf - 1 - f) @ approx1
            error = np.linalg.norm(approx0 - approx1) / np.linalg.norm(approx0)
            # print(approx0[:3, 1])
            # print(approx1[:3, 1])
            print('error={0:e}'.format(error))
            self.assertTrue(error < 1e-4)


if __name__ == "__main__":
    unittest.main()
