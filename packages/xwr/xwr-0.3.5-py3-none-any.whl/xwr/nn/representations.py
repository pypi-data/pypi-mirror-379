"""Spectrum representations."""

import cmath
from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any, Literal, cast

import numpy as np
from jaxtyping import Complex64, Float32, Shaped

from . import backend
from .backend import TArray
from .utils import resize


class Representation(ABC):
    """Generic representation which maps complex spectrum to real channels.

    Args:
        scale: scale factor to apply to the magnitude.
        transform: transformation to apply to the magnitude.
        eps: small value to avoid log(0) in log transform.
    """

    def __init__(
        self, scale: float = 1e-6,
        transform: Literal["log", "sqrt", "linear"] = "sqrt",
        eps: float = 1e-6
    ) -> None:
        self.scale = scale
        self.eps = eps
        self._magnitude_transform = transform

    def _flip(
        self, spectrum: Shaped[TArray, "batch doppler el az rng"],
        aug: Mapping[str, Any] = {}
    ) -> Shaped[TArray, "batch doppler el az rng"]:
        if aug.get("azimuth_flip", False):
            spectrum = backend.flip(spectrum, axis=-2)
        if aug.get("doppler_flip", False):
            spectrum = backend.flip(spectrum, axis=-3)
        return spectrum

    def _scale(
        self, data: Float32[TArray, "..."]
    ) -> Float32[TArray, "..."]:
        data = cast(TArray, data * self.scale)
        if self._magnitude_transform == "log":
            return backend.log(cast(TArray, data + self.eps))
        elif self._magnitude_transform == "sqrt":
            return backend.sqrt(data)
        else:
            return data

    @abstractmethod
    def __call__(
        self, spectrum: Complex64[TArray, "batch doppler el az rng"],
        aug: Mapping[str, Any] = {}
    ) -> Float32[TArray, "batch doppler el az rng c"]:
        """Get spectrum representation.

        Type Parameters:
            - `TArray`: array type; `np.ndarray` or `torch.Tensor`.

        Args:
            spectrum: complex spectrum as output by one of the
                [`xwr.rsp.numpy`][xwr.rsp.numpy] classes.
            aug: dictionary of augmentations to apply.

        Returns:
            Real 4D spectrum with a leading batch axis and trailing channel
                axis.
        """
        ...

    def __repr__(self) -> str:  # noqa: D105
        return (
            f"{self.__class__.__name__}({self._magnitude_transform} * "
            f"{self.scale})")


class Magnitude(Representation):
    """Real spectrum magnitude with phase discarded.

    Args:
        scale: scale factor to apply to the magnitude.
        transform: transformation to apply to the magnitude.
        eps: small value to avoid log(0) in log transform.
    """

    def __call__(
        self, spectrum: Complex64[TArray, "batch doppler el az rng"],
        aug: Mapping[str, Any] = {}
    ) -> Float32[TArray, "batch doppler el az rng 1"]:
        """Get spectrum amplitude.

        Type Parameters:
            - `TArray`: array type; `np.ndarray` or `torch.Tensor`.

        Args:
            spectrum: complex spectrum as output by one of the
                [`xwr.rsp.numpy`][xwr.rsp.numpy] classes.
            aug: augmentations to apply.

        Returns:
            Real 4D spectrum with a leading batch axis and trailing
                `[magnitude]` channel axis.
        """
        spectrum = self._flip(spectrum, aug)

        magnitude = backend.abs(spectrum)
        if aug.get("radar_scale", 1.0) != 1.0:
            magnitude *= aug["radar_scale"]
        magnitude = self._scale(magnitude)

        # Phase is unused; explicitly fetch it here to "touch" it
        _ = aug.get("radar_phase", 0.0)

        resized = resize(
            magnitude, range_scale=aug.get("range_scale", 1.0),
            speed_scale=aug.get("speed_scale", 1.0))

        return cast(TArray, resized[..., None])


class PhaseAngle(Representation):
    """Complex spectrum with magnitude and phase angle.

    Args:
        scale: scale factor to apply to the magnitude.
        transform: transformation to apply to the magnitude.
        eps: small value to avoid log(0) in log transform.
    """

    def __call__(
        self, spectrum: Complex64[TArray, "batch doppler el az rng"],
        aug: Mapping[str, Any] = {}
    ) -> Float32[TArray, "batch doppler el az rng 2"]:
        """Get complex spectrum representation.

        Type Parameters:
            - `TArray`: array type; `np.ndarray` or `torch.Tensor`.

        Args:
            spectrum: complex spectrum as output by one of the
                [`xwr.rsp.numpy`][xwr.rsp.numpy] classes.
            aug: augmentations to apply.

        Returns:
            Complex 4D spectrum with a leading batch axis and trailing
                `[magnitude, phase]` channel axis.
        """
        spectrum = self._flip(spectrum, aug)

        magnitude = backend.abs(spectrum)
        phase = backend.angle(spectrum)

        if aug.get("radar_scale", 1.0) != 1.0:
            magnitude *= aug["radar_scale"]
        if aug.get("radar_phase", 0.0) != 0.0:
            phase += aug["radar_phase"]
        magnitude = self._scale(magnitude)

        range_scale = aug.get("range_scale", 1.0)
        speed_scale = aug.get("speed_scale", 1.0)
        return cast(TArray, backend.stack([
            resize(magnitude, range_scale=range_scale, speed_scale=speed_scale),
            resize(phase, range_scale, speed_scale) % (2 * np.pi)
        ], axis=-1))


class PhaseVec(Representation):
    """Complex spectrum with magnitude and re/im phase vector.

    Args:
        scale: scale factor to apply to the magnitude.
        transform: transformation to apply to the magnitude.
        eps: small value to avoid log(0) in log transform.
    """

    def __call__(
        self, spectrum: Complex64[TArray, "batch doppler el az rng"],
        aug: Mapping[str, Any] = {}
    ) -> Float32[TArray, "batch doppler el az rng 3"]:
        """Get amplitude spectrum.

        Type Parameters:
            - `TArray`: array type; `np.ndarray` or `torch.Tensor`.

        Args:
            spectrum: complex spectrum as output by one of the
                [`xwr.rsp.numpy`][xwr.rsp.numpy] classes.
            aug: augmentations to apply.

        Returns:
            Real 4D spectrum with a leading batch axis and trailing
                `[magnitude, re, im]` channel axis.
        """
        spectrum = self._flip(spectrum, aug)

        magnitude = backend.abs(spectrum)
        normed = spectrum / backend.maximum(magnitude, self.eps)
        if aug.get("radar_phase", 0.0) != 0.0:
            # aug["radar_phase"] is a python scalar, so we always use cmath
            normed *= cmath.exp(-1j * aug["radar_phase"])
        re = backend.real(normed)
        im = backend.imag(normed)

        if aug.get("radar_scale", 1.0) != 1.0:
            magnitude *= aug["radar_scale"]
        magnitude = self._scale(magnitude)

        range_scale = aug.get("range_scale", 1.0)
        speed_scale = aug.get("speed_scale", 1.0)
        return cast(TArray, backend.stack([
            resize(magnitude, range_scale=range_scale, speed_scale=speed_scale),
            resize(re, range_scale=range_scale, speed_scale=speed_scale),
            resize(im, range_scale=range_scale, speed_scale=speed_scale)
        ], axis=-1))
