# ver 3.0.0
# 高速サンプリング

import platform
import numpy as np
os = platform.system()
import ctypes
if os == 'Windows':
    import ctypes.wintypes
from enum import IntEnum, auto
from threading import Thread
import time

class DIO_ch(IntEnum):
    O_0 = 0
    O_1 = auto()
    O_2 = auto()
    O_3 = auto()
    O_4 = auto()
    O_5 = auto()
    O_6 = auto()
    O_7 = auto()
    O_10 = auto()
    O_11 = auto()
    O_12 = auto()
    O_13 = auto()
    O_14 = auto()
    O_15 = auto()
    O_16 = auto()
    O_17 = auto()


class _AIOfunc:
    class status:
        class AioSetAiSamplingClock:
            ok = 0  # 正常終了
            out_func_range = 11140  # AiSamplingClockの値が関数の指定範囲外です
            out_dev_range = 21140  # AiSamplingClockの値が使用しているデバイスの指定範囲外です
        class AioSetAiChannels:
            ok = 0  # 正常終了
            out_func_range = 11020  # AiSamplingClockの値が関数の指定範囲外です
            out_dev_range = 21020  # AiSamplingClockの値が使用しているデバイスの指定範囲外です
        class AioGetAiStatus:
            AIS_BUSY = 0x00000001  # デバイス動作中
            AIS_START_TRG = 0x00000002  # 開始トリガ待ち
            AIS_DATA_NUM = 0x00000010  # 指定サンプリング回数格納
            AIS_OFERR = 0x00010000  # オーバーフロー
            AIS_SCERR = 0x00020000  # サンプリングクロック周期エラー
            AIS_AIERR = 0x00040000  # AD変換エラー
            AIS_DRVERR = 0x00080000  # ドライバスペックエラー

    def __init__(self):
        if os == 'Windows':
            caio_dll = ctypes.windll.LoadLibrary('caio.dll')
        elif os == 'Linux':
            caio_dll = ctypes.cdll.LoadLibrary('libcaio.so')

        # Define function
        self.AioInit = caio_dll.AioInit
        self.AioInit.restype = ctypes.c_long
        self.AioInit.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short)]

        self.AioGetAoMaxChannels = caio_dll.AioGetAoMaxChannels
        self.AioGetAoMaxChannels.restype = ctypes.c_long
        self.AioGetAoMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

        self.AioGetAiMaxChannels = caio_dll.AioGetAiMaxChannels
        self.AioGetAiMaxChannels.restype = ctypes.c_long
        self.AioGetAiMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

        self.AioSingleAiEx = caio_dll.AioSingleAiEx
        self.AioSingleAiEx.restype = ctypes.c_long
        self.AioSingleAiEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

        self.AioSingleAoEx = caio_dll.AioSingleAoEx
        self.AioSingleAoEx.restype = ctypes.c_long
        self.AioSingleAoEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]

        self.AioOutputDoBit = caio_dll.AioOutputDoBit
        self.AioOutputDoBit.restype = ctypes.c_long
        self.AioOutputDoBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

        self.AioExit = caio_dll.AioExit
        self.AioExit.restype = ctypes.c_long
        self.AioExit.argtypes = [ctypes.c_short]

        self.AioInputDiBit = caio_dll.AioInputDiBit
        # self.AioInputDiBit.restype = ctypes.c_long
        # self.AioInputDiBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_ubyte)]

        self.AioStartAi = caio_dll.AioStartAi
        self.AioStopAi = caio_dll.AioStopAi
        self.AioSetAiSamplingClock = caio_dll.AioSetAiSamplingClock
        self.AioGetAiSamplingClock = caio_dll.AioGetAiSamplingClock
        self.AioSetAiStopTrigger = caio_dll.AioSetAiStopTrigger
        self.AioSetAiEventSamplingTimes = caio_dll.AioSetAiEventSamplingTimes
        self.AioGetAiSamplingCount = caio_dll.AioGetAiSamplingCount
        self.AioGetAiStatus = caio_dll.AioGetAiStatus
        self.AioGetAiSamplingDataEx = caio_dll.AioGetAiSamplingDataEx
        self.AioSetAiChannels = caio_dll.AioSetAiChannels
        self.AioGetAiChannels = caio_dll.AioGetAiChannels

        self.sample_clock = 100.0
        self.channel_num = 8
        self.buff_size = 30
        self._ai_ch_num = ctypes.c_short()  # チャネル数
        self._lret = ctypes.c_long()
        self._aio_id = ctypes.c_short()
        self._AiData = ctypes.c_float()
        self._DiData = ctypes.c_short()
        self.MaxAoChannels = ctypes.c_short()
        self.MaxAiChannels = ctypes.c_short()
        self._now_data = np.empty([0,])
        self._th = Thread(target=self._tick, daemon=True)

    def init(self, devicename):
        self._lret.value = self.AioInit(devicename.encode(), ctypes.byref(self._aio_id))
        if self._lret.value == 0:
            print('Success to initialize')
            self.AioGetAoMaxChannels(self._aio_id, ctypes.byref(self.MaxAoChannels))
            self.AioGetAiMaxChannels(self._aio_id, ctypes.byref(self.MaxAiChannels))
            ret = ctypes.c_long()
            ret.value = self.AioSetAiSamplingClock(self._aio_id, ctypes.c_float(self.sample_clock))  # 内部クロックをusec単位
            if ret.value == self.status.AioSetAiSamplingClock.ok:
                AiSamplingClock = ctypes.c_float()
                self.AioGetAiSamplingClock(self._aio_id, ctypes.byref(AiSamplingClock))
            else:
                raise ValueError('設定したクロック値が不正です')
            ret.value = self.AioSetAiChannels(self._aio_id, self.channel_num)
            if ret.value == self.status.AioSetAiChannels.ok:
                self.AioGetAiChannels(self._aio_id, ctypes.byref(self._ai_ch_num))
            else:
                raise ValueError('設定したチャンネル数が不正です')

            self.sample_clock = AiSamplingClock.value
            ret.value = self.AioSetAiStopTrigger(self._aio_id, 4)  # 停止トリガー設定
            ret.value = self.AioSetAiEventSamplingTimes(self._aio_id, 1)  # 格納バッファサイズ
            self._now_data = np.empty([0, self._ai_ch_num.value])
            self._th.start()
            return 1
        else:
            print('Failure to initialize')
            return 0

    def read(self, channel, AI_DI='AI'):
        # return -100
        if AI_DI == 'AI':
            if channel < 0 or channel > self.MaxAiChannels.value - 1:
                print('Set channel is failure')
                return -100
            while self._now_data.shape[0] == 0:
                pass
            now_data = self._now_data[0]
            self._now_data = self._now_data[1:]
            return now_data[channel]
        else:
            ret = self.AioInputDiBit(self._aio_id, channel, ctypes.byref(self._DiData))
            if ret != 0:
                print("CHECK")
            return self._DiData.value

    def _tick(self):
        ret = ctypes.c_long()
        ret.value = self.AioStartAi(self._aio_id)
        time.sleep(0.1)
        ai_status = ctypes.c_long()  # ステータス
        ai_sampling_count = ctypes.c_long()  # サンプリング回数

        while True:
            ret.value = self.AioGetAiSamplingCount(self._aio_id, ctypes.byref(ai_sampling_count))
            ret.value = self.AioGetAiStatus(self._aio_id, ctypes.byref(ai_status))
            self._status_checker(ai_status.value)
            if ai_sampling_count.value == 0:
                time.sleep(0.0001)
                continue
            AiDataType = ctypes.c_float * (ai_sampling_count.value * self._ai_ch_num.value)
            AiData = AiDataType()
            ret.value = self.AioGetAiSamplingDataEx(self._aio_id, ctypes.byref(ai_sampling_count), AiData)
            sampling_data_count = ai_sampling_count.value * self._ai_ch_num.value
            now_data = (ctypes.c_float * sampling_data_count).from_buffer_copy(AiData)
            now_data = np.array(now_data).astype('float')
            self._now_data = now_data.reshape([int(sampling_data_count/self._ai_ch_num.value), self._ai_ch_num.value])
            self._now_data = self._now_data[-self.buff_size:]

    def _status_checker(self, status):
        if status == self.status.AioGetAiStatus.AIS_BUSY:
            return 1
        now_status = '{:08x}'.format(status)
        # print(now_status)
        if now_status[-1] == 2:
            self.AioStartAi(self._aio_id)
            time.sleep(0.3)
            return 1
        if now_status[-2] == 1:
            # self.AioStartAi(self._aio_id)
            # time.sleep(0.3)
            return 1
        if (fifth_status:=now_status[-5]) != '0':
            fifth_status = int('0x' + fifth_status, 0)
            fifth_status = '{:04b}'.format(fifth_status)
            if int(fifth_status[-1]):  # オーバーフロー
                self.AioStartAi(self._aio_id)
                time.sleep(0.3)
            elif int(fifth_status[-2]):  # サンプリングクロック周期エラー
                raise ValueError('サンプリングクロック周期が速すぎます')
            elif int(fifth_status[-3]) or int(fifth_status[-4]):
                raise ValueError('デバイス故障の可能性')


    def write(self, channel, value, AO_DO='AO'):
        if AO_DO == 'AO':
            if channel < 0 or channel > self.MaxAoChannels.value - 1:
                print('Set channel is failure')
                return 0
            self._lret.value = self.AioSingleAoEx(self._aio_id, channel, value)
        else:
            self._lret.value = self.AioOutputDoBit(self._aio_id, channel, bool(value))
        if self._lret.value != 0:
            print('Action failure')
            return 0
        return 1

    def exit(self):
        for i in range(self.MaxAoChannels.value):
            self.write(i, 0, AO_DO='AO')
        i = 0
        while self.write(i, 0, AO_DO='DO'):
            i = i + 1
        self.AioExit(self._aio_id)


class _DIOfunc:
    def __init__(self):
        if os == 'Windows':
            cdio_dll = ctypes.windll.LoadLibrary('cdio.dll')
        elif os == 'Linux':
            cdio_dll = ctypes.cdll.LoadLibrary('libcdio.so')

        # Define function
        self.DioInit = cdio_dll.DioInit
        self.DioInit.restype = ctypes.c_long
        self.DioInit.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short)]

        self.DioGetMaxPorts = cdio_dll.DioGetMaxPorts
        self.DioGetMaxPorts.restype = ctypes.c_long
        self.DioGetMaxPorts.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

        self.DioOutBit = cdio_dll.DioOutBit
        self.DioOutBit.restype = ctypes.c_long
        self.DioOutBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_ubyte]

        self.DioInpBit = cdio_dll.DioInpBit
        self.DioInpBit.restype = ctypes.c_long
        self.DioInpBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_ubyte)]

        self.DioExit = cdio_dll.DioExit
        self.DioExit.restype = ctypes.c_long
        self.DioExit.argtypes = [ctypes.c_short]

        self._lret = ctypes.c_long()
        self._dio_id = ctypes.c_short()
        self._DiData = ctypes.c_ubyte()
        self.MaxDoChannels = ctypes.c_short()
        self.MaxDiChannels = ctypes.c_short()

    def init(self, devicename):
        self._lret.value = self.DioInit(devicename.encode(), ctypes.byref(self._dio_id))
        if self._lret.value == 0:
            print('Success to initialize')
            self.DioGetMaxPorts(self._dio_id, self.MaxDiChannels, self.MaxDoChannels)
            self.MaxDiChannels = self.MaxDiChannels.value * 8
            self.MaxDoChannels = self.MaxDoChannels.value * 8
            return 1
        else:
            print('Failure to initialize')
            return 0

    def write(self, channel, value):
        if type(channel) == DIO_ch:
            channel = channel.value
        self._lret.value = self.DioOutBit(self._dio_id, channel, bool(value))
        if self._lret.value != 0:
            print('Action failure')
            return 0
        return 1

    def read(self, channel):
        self._lret.value = self.DioInpBit(self._dio_id, channel, ctypes.byref(self._DiData))
        if self._lret.value != 0:
            print('Action failure')
            return 0
        return self._DiData.value

    def exit(self):
        for i in range(self.MaxDoChannels):
            self.write(i, False)
        self.DioExit(self._dio_id)

class ADfunc:
    def __init__(self, DeviceType):
        self.devicetype = DeviceType
        if DeviceType == 'AIO':
            self.now_func = _AIOfunc()
        elif DeviceType == 'DIO':
            self.now_func = _DIOfunc()

    def init(self, devicename):
        return self.now_func.init(devicename)

    def write(self, channel, value, AO_DO):
        if self.devicetype == 'AIO':
            self.now_func.write(channel, value, AO_DO)
        elif self.devicetype == 'DIO':
            self.now_func.write(channel, value)

    def read(self, channel, AI_DI):
        if self.devicetype == 'AIO':
            return self.now_func.read(channel, AI_DI)
        elif self.devicetype == 'DIO':
            return self.now_func.read(channel)

    def exit(self):
        self.now_func.exit()




