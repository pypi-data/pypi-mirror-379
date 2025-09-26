from __future__ import print_function, division, absolute_import
import unittest
import pygsl
import pygsl.fft as fft
import sys
sys.stdout = sys.stderr
pygsl.set_debug_level(0)
pygsl.init.add_c_traceback_frames(True)
import pygsl._numobj as numx
#import pygsl._mlab as MLab
import string
from pygsl.math import fcmp



from array_check import array_check
get_typecode = pygsl.get_typecode
_eps = 1e-5

_fcmp = fcmp

try:
    _float32 = numx.Float32
except AttributeError:
    # For numpy
    _float32 = numx.float32


try:
    _complex32 = numx.Complex64
except AttributeError:
    # For numpy
    _complex32 = numx.complex64
    
def fcmp(a, b, eps):
    return _fcmp(float(a), float(b), eps)


def printvec(array, value, eps):
    for i in range(len(array)):
        if fcmp(array[i]+1, value+1, eps) != 0:
            print ("v[%d]=%e   " % (i, array[i]),)
    print()        
   
class _ffttest(unittest.TestCase):
    # Type of the array
    typecode = None

    def _GetN2(self):
        n2 = int(self.n/2)
        #print("n2", n2)
        return n2

    def _CalculateAbsMax(self, an_array):
        tmp = an_array.ravel()
        result = tmp.max()
        result = numx.absolute(result)
        
        l_shape = len(result.shape)
        self.assertEqual(l_shape, 0, "max array shape too long")
        return result
    
    def _CheckSinResult(self, f, l):
        a = numx.absolute(f)
        test = 0
        tmp1 = None
        tmp2 = None
        try:
            tmp1 = f[l].imag
            tmp2 = self.sin_n
            self.assertAlmostEqual(tmp1, tmp2, places=4)
            a[l] = 0

            n2 = self._GetN2()
            if(len(f) > n2 + 1):
                # Only for the complex transform
                tmp1 = f[self.n-l].imag
                tmp2 = self.sin_n_l
                self.assertAlmostEqual(tmp1, tmp2, places=4)
                a[self.n-l] = 0
            test = 1
        finally:
            if test == 0:
                print()
                print ("Check Sin Result len(f) = %s, self.n/2 = %s", len(f), self.n/2)
                print (f[l])
                print ("tmp1 = %s, tmp2 = %s" % (tmp1, tmp2))
                #print f[self.n-l]
                
        # Take the maximum
        test_val = self._CalculateAbsMax(a)
        self.assertAlmostEqual(1+test_val, 1, places=4)

    def _CheckCosResult(self, f, l):
        # Take all data
        a = numx.absolute(f)
        
        self.assertAlmostEqual(f[l].real, self.n/2, places=4)
        stmp = ["%s" % a[l]]
        a[l] = 0
        stmp.append("should be zero %s" % (a[l],))
        n2 = self._GetN2()
        if(len(f) > n2 + 1):
            # Only for the complex transform
            self.assertAlmostEqual(f[self.n-l].real, self.n/2, places=4)
            a[self.n-l] = 0
        # Take the maximum
        test = 0
        test_val = self._CalculateAbsMax(a)
        self.assertAlmostEqual(1+test_val, 1, places=4)
                
    def SinOne(self, x, l, args=()):
        y = numx.sin(x * l)
        tmp = self.convert(y)
        f = self.transform(*((tmp,) + args))
        self._CheckSinResult(f, l)

    def CosOne(self, x, l, args=()):
        y = numx.cos(x * l)
        tmp = self.convert(y)
        f = self.transform(*((tmp,) + args))
        self._CheckCosResult(f, l)
        
    def testSin(self):        
        x = numx.arange(self.n) * (2 * numx.pi / self.n)
        for i in range(1, self._GetN2()):
           self.SinOne(x,i)

    def testCos(self):        
        x = numx.arange(self.n) * (2 * numx.pi / self.n)
        for i in range(1, self._GetN2()):
            if self.__class__.__name__ == "testrealforwardfloat":
                pygsl.set_debug_level(0)
            try:                
                self.CosOne(x,i)
            finally:
                pygsl.set_debug_level(0)
                
class _radix2(_ffttest):
    pass

class _mixedradix(_ffttest):
    def testSinSpace(self):        
        x = numx.arange(self.n) * (2 * numx.pi / self.n)
        space = self.workspace(self.n)
        self.assertEqual(space.get_n(), self.n)
        table = self.wavetable(self.n)
        self.assertEqual(table.get_n(), self.n)
        for i in range(1, self._GetN2()):
           self.SinOne(x,i, (space,table))

    def testCosSpace(self):        
        x = numx.arange(self.n) * (2 * numx.pi / self.n)
        space = self.workspace(self.n)
        self.assertEqual(space.get_n(), self.n)
        table = self.wavetable(self.n)
        self.assertEqual(table.get_n(), self.n)
        for i in range(1, self._GetN2()):
           self.CosOne(x,i, (space,table))

class _mixedradixcomplex(_mixedradix):
    def testSinReturnSaveSpaces(self):
        space = self.workspace(self.n)
        table = self.wavetable(self.n)
        x = numx.arange(self.n) * ((2+0j) * numx.pi / self.n)
        for i in range(1, self._GetN2()):
            y = numx.sin(x * i)
            tmp = self.convert(y)
            f = self.transform(tmp, space, table, tmp)
            self._CheckSinResult(f, i)

class DoubleType:
    _eps = 1e-8
    def convert(self, y):
        return y

class FloatType:
    _eps = 1e-4
    def convert(self, y):
        code = get_typecode(y)

        # adaption for numpy
        try:
            code = code.char
        except AttributeError:
            pass
        
        if  code in  numx.typecodes['Float']:
            return y.astype(_float32)
        elif code in  numx.typecodes['Complex']:
            return y.astype(_complex32)
        else:
            raise TypeError("Not implemented for an array of type %s" % (code,))
        
class number:
    n = 64
    sin_n = - n / 2
    sin_n_l = n / 2

class numberbackward:
    n = 64
    sin_n =  n / 2
    sin_n_l = - n / 2

class numbermixedradix:
    n = 2 * 3 * 5  #*7 * 11
    sin_n = - n / 2
    sin_n_l = n / 2

class numberinverse(numberbackward):
    pass

class complexspace:
    wavetable = fft.complex_wavetable
    workspace = fft.complex_workspace

class realspace:
    wavetable = fft.real_wavetable
    workspace = fft.real_workspace

class complexspacefloat:
    wavetable = fft.complex_wavetable_float
    workspace = fft.complex_workspace_float

class realspacefloat:
    wavetable = fft.real_wavetable_float
    workspace = fft.real_workspace_float

class testcomplexbackwardradix2(_radix2, numberbackward, DoubleType):
    transform = fft.complex_radix2_backward

class testcomplexbackwardradix2dif(_radix2, numberbackward, DoubleType):
    transform = fft.complex_radix2_dif_backward

class testcomplexinverseradix2(_radix2, numberinverse, DoubleType):
    transform = fft.complex_radix2_backward

class testcomplexinverseradix2dif(_radix2, numberinverse, DoubleType):
    transform = fft.complex_radix2_dif_backward

class testcomplexforwardradix2(_radix2, number, DoubleType):
    transform = fft.complex_radix2_forward

class testcomplexforwardradix2dif(_radix2, number, DoubleType):
    transform = fft.complex_radix2_dif_forward

class testcomplexbackward64(_mixedradixcomplex, complexspace, numberbackward, DoubleType):
    "fft.complex_backward"
    transform = fft.complex_backward

class testcomplexinverse64(_mixedradixcomplex, complexspace, numberinverse, DoubleType):
    transform = fft.complex_backward



class testcomplexforward64(_mixedradixcomplex, complexspace, number, DoubleType):
    transform = fft.complex_forward


class testcomplexforward(_mixedradixcomplex, complexspace, numbermixedradix, DoubleType):
    transform = fft.complex_forward


class testrealforward(_mixedradix, realspace, numbermixedradix, DoubleType):
    transform = fft.real_transform

class testrealforwardradix2(_radix2, realspace, number, DoubleType):    
    def transform(self, x):
        return fft.halfcomplex_radix2_unpack(fft.real_radix2_transform(x))

class testcomplexbackwardradix2float(_radix2, numberbackward, FloatType):
    transform = fft.complex_radix2_backward_float

class testcomplexbackwardradix2diffloat(_radix2, numberbackward, FloatType):
    transform = fft.complex_radix2_dif_backward_float

class testcomplexinverseradix2float(_radix2, numberinverse, FloatType):
    transform = fft.complex_radix2_backward_float

class testcomplexinverseradix2diffloat(_radix2, numberinverse, FloatType):
    transform = fft.complex_radix2_dif_backward_float

class testcomplexforwardradix2float(_radix2, number, FloatType):
    transform = fft.complex_radix2_forward_float

class testcomplexforwardradix2diffloat(_radix2, number, FloatType):
    transform = fft.complex_radix2_dif_forward_float

class testcomplexbackward64float(_mixedradixcomplex, complexspacefloat, numberbackward, FloatType):
    transform = fft.complex_backward_float

class testcomplexinverse64float(_mixedradixcomplex, complexspacefloat, numberinverse, FloatType):
    transform = fft.complex_backward_float



class testcomplexforward64float(_mixedradixcomplex, complexspacefloat, number, FloatType):
    transform = fft.complex_forward_float


class testcomplexforwardfloat(_mixedradixcomplex, complexspacefloat, numbermixedradix, FloatType):
    transform = fft.complex_forward_float


class testrealforwardfloat(_mixedradix, realspacefloat, numbermixedradix, FloatType):
    transform = fft.real_transform_float

class testrealforwardradix2float(_radix2, realspacefloat, number, FloatType):    
    def transform(self, x):
        tmp = self.convert(x)
        return fft.halfcomplex_radix2_unpack_float(fft.real_radix2_transform_float(tmp))

del _ffttest
del _radix2
del _mixedradix
del _mixedradixcomplex

if __name__ == '__main__':
    unittest.main()
