import copy
from typing import Dict, Any
import autograd.numpy as np
from numpy.typing import NDArray
from .constants import SHORT_TO_FLOAT_FACTOR
import logging
from scipy.signal import windows
from scipy.fft import rfft, rfftfreq

logger = logging.getLogger(__name__)


class FFTData:
    def __init__(self, fft: NDArray[np.float64], freq: NDArray[np.float64]):
        self.fft = fft
        self.freq = freq


class Series:
    """
    Represents a time-series signal with optional FFT capabilities.

    Supports conversion from integer data to float, slicing,
    FFT computation, and series concatenation.

    Attributes
    ----------
    data : NDArray[np.float64]
        The time-domain data of the series in float64 format.
    fft : Optional[NDArray[np.float64]]
        Full FFT result (complex values).
    real_fft_freq : Optional[NDArray[np.float64]]
        Frequencies corresponding to the real FFT.
    real_fft : Optional[NDArray[np.float64]]
        One-sided FFT (real-valued spectrum).
    """

    def __init__(self, data: NDArray[np.float64 | np.int16], samplerate: float):
        self.data: NDArray[np.float64] = (
            data
            if data.dtype == np.float64
            else (data / SHORT_TO_FLOAT_FACTOR).astype(np.float64)
        )
        self.samplerate = samplerate
        self._fft_freq: NDArray[np.float64] | None = None
        self._fft: NDArray[np.float64] | None = None
        self._windowed_fft_freq: NDArray[np.float64] | None = None
        self._windowed_fft: NDArray[np.float64] | None = None
        self.properties: dict[str, Any] = {}

    def json(self) -> Dict[str, Any]:
        return {}

    @property
    def fft(self):
        if self._fft is None:
            logger.info("Computing FFT")
            self._fft = rfft(self.data) / self.data.size
            self._fft_freq = rfftfreq(self.data.size, d=1 / self.samplerate)
            logger.debug("FFT successfully computed")
        return FFTData(self._fft, self._fft_freq)

    @property
    def windowed_fft(self):
        if self._windowed_fft is None:
            logger.info("Computing windowed FFT")
            window = windows.hann(self.data.size)
            window_scale = 1 / window.mean()
            windowed_data = self.data * window * window_scale
            self._windowed_fft = np.fft.rfft(windowed_data) / self.data.size
            self._windowed_fft[1:-1] *= 2
            self._windowed_fft_freq = rfftfreq(
                windowed_data.size, d=1 / self.samplerate
            )
            logger.debug("Windowed FFT successfully computed")
        return FFTData(self._windowed_fft, self._windowed_fft_freq)

    def psd(self, flow, fhigh):
        fft = self.windowed_fft.fft
        freq = self.windowed_fft.freq
        idx = (freq >= flow) & (freq < fhigh)
        p = (fft[idx] * fft[idx].conj()).real / 2
        bin_width = self.samplerate / self.data.size
        psd = p.mean() / bin_width
        return psd

    def __getitem__(self, index):
        series = copy.deepcopy(self)
        if isinstance(index, slice):
            series.data = series.data[index.start : index.stop : index.step]
            self._fft_freq = None
            self._windowed_fft_freq = None
            self._fft = None
            self._windowed_fft = None
        else:
            series.data = series.data[index]
        return series

    def __deepcopy__(self, memo):
        return Series(np.copy(self.data), self.samplerate)

    def __str__(self):
        fft_status = "Computed" if self._fft is not None else "Not computed"
        windowed_fft_status = (
            "Computed" if self._windowed_fft is not None else "Not computed"
        )
        return (
            f"Series(data={self.data[:2]} ... {self.data[int(self.data.size / 2)]} ... {self.data[-2:]} (size={self.data.size}), "
            f"FFT: {fft_status}, "
            f"Windowed FFT : {windowed_fft_status})"
        )

    def __add__(self, other: object) -> "Series":
        if not isinstance(other, Series):
            raise TypeError(
                f"Unsupported operand type(s) for +: Series and {type(other).__name__}"
            )
        if self.data.dtype != other.data.dtype:
            raise TypeError(
                f"Adding Series objects from different dtype is not supported : {type(self.data.dtype).__name__} and {type(other.data.dtype).__name__}"
            )

        series = Series(np.concatenate((self.data, other.data)))
        return series
