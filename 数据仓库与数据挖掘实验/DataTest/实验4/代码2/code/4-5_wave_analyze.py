#-*- coding: utf-8 -*-
#利用小波分析进行特征分析

#参数初始化
inputfile= '../data/leleccum.mat' #提取自Matlab的信号文件

from scipy.io import loadmat #mat是MATLAB专用格式，需要用loadmat读取它
mat = loadmat(inputfile)
signal = mat['leleccum'][0]

import pywt #导入PyWavelets
coeffs = pywt.wavedec(signal, 'bior3.7', level = 5)
#返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组

#绘制小波系数图
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 3))
plt.plot(coeffs[0], 'r', label='Approximation')
for i in range(1, len(coeffs)):
    plt.plot(coeffs[i], 'g', alpha=0.5, label='Detail {}'.format(i))
plt.legend(loc='upper right')
plt.show()

#绘制小波系数的频谱图
import numpy as np
from scipy.fftpack import fft, fftshift

def plot_wavelet_spectrum(coeffs, wavelet_name):
    fig, axes = plt.subplots(nrows=len(coeffs), ncols=1, figsize=(12, 3))
    for i, coeff in enumerate(coeffs):
        ax = axes[i]
        ax.plot(np.abs(fftshift(fft(coeff))))
        ax.set_title('Wavelet Spectrum {} {}'.format(wavelet_name, i))
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
plot_wavelet_spectrum(coeffs, 'bior3.7')
