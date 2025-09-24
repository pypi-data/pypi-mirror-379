from typing import Optional

import numpy
import skimage
from packaging.version import Version
from skimage.registration import phase_cross_correlation as _phase_cross_correlation
from skimage.transform import SimilarityTransform
from skimage.transform import warp_polar

from ..math.fft import fft2
from ..math.fft import fftshift
from ..transformation.scikitimage_backend import SciKitImageHomography
from ..transformation.types import TransformationType
from .base import IntensityMapping


class SkimageCorrelationIntensityMapping(
    IntensityMapping,
    registry_id=IntensityMapping.RegistryId("CrossCorrelation", "SciKitImage"),
):
    SUPPORTED_TRANSFORMATIONS = ["translation"]

    def __init__(
        self,
        transfo_type: TransformationType,
        upsample_factor: int = 5,
        normalization: bool = True,
        mask: Optional[numpy.ndarray] = None,
        **kw,
    ) -> None:
        self._factor = upsample_factor
        if normalization:
            self._normalization = "phase"
        else:
            self._normalization = None
        self._mask = mask
        super().__init__(transfo_type, **kw)

    def identity(self, dimension: int = 2) -> SciKitImageHomography:
        return SciKitImageHomography(
            numpy.identity(dimension + 1), TransformationType.identity
        )

    def calculate(
        self,
        from_image: numpy.ndarray,
        to_image: numpy.ndarray,
    ) -> SciKitImageHomography:
        if self.transformation_type == self.transformation_type.translation:
            if self._mask is not None:
                self._mask = self._mask.astype(bool)
                shift = phase_cross_correlation(
                    from_image,
                    to_image,
                    moving_mask=self._mask,
                    reference_mask=self._mask,
                )
            else:
                shift = phase_cross_correlation(
                    from_image,
                    to_image,
                    normalization=self._normalization,
                    upsample_factor=self._factor,
                )

            passive_matrix = numpy.identity(from_image.ndim + 1)
            passive_matrix[0:-1, -1] = shift
            return SciKitImageHomography(passive_matrix, transfo_type="translation")
        elif self.transformation_type == self.transformation_type.similarity:
            # magnitude of FFT
            from_ft = numpy.abs(fftshift(fft2(from_image)))
            to_ft = numpy.abs(fftshift(fft2(to_image)))

            # transform magnitudes into log-polar
            radius = min(from_image.shape) // 4
            warped_from_ft = warp_polar(from_ft, radius=radius, scaling="log", order=1)
            warped_to_ft = warp_polar(to_ft, radius=radius, scaling="log", order=1)

            # half the log-polar fourier magnitudes and calculate their relative shift
            warped_from_ft = warped_from_ft[: warped_from_ft.shape[0] // 2, :]
            warped_to_ft = warped_to_ft[: warped_to_ft.shape[0] // 2, :]
            shifts = phase_cross_correlation(
                warped_from_ft,
                warped_to_ft,
                normalization=self._normalization,
                upsample_factor=self._factor,
            )

            # recover scale and angle from the shift
            recovered_angle = shifts[0] / 180 * numpy.pi
            scale = numpy.exp(-shifts[1] * numpy.log(radius) / radius)

            # apply scale and angle as a centered transform
            similarity = SimilarityTransform(scale=scale, rotation=-recovered_angle)
            translation = SimilarityTransform(
                translation=(from_image.shape[0] / 2, from_image.shape[1] / 2)
            )
            mtranslation = SimilarityTransform(
                translation=(-from_image.shape[0] / 2, -from_image.shape[1] / 2)
            )
            full = mtranslation + similarity + translation
            return SciKitImageHomography(full.params, transfo_type="similarity")

        else:
            raise ValueError(
                "Only translation possible with SciKitImage Phase Correlation"
            )


def phase_cross_correlation(img1, img2, **kw) -> numpy.ndarray:
    version = Version(skimage.__version__)
    if version >= Version("0.22.0"):
        shift, _, _ = _phase_cross_correlation(img1, img2, **kw)
        return shift
    if version >= Version("0.20.0"):
        shift, _, _ = _phase_cross_correlation(img1, img2, return_error="always", **kw)
        return shift
    return _phase_cross_correlation(img1, img2, return_error=False, **kw)
