"""Data to test registration"""

from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import numpy
import numpy.linalg
import numpy.random

try:
    from skimage import data as skdata
    from skimage.color import rgb2gray
    from skimage.filters import gaussian
    from skimage.transform import AffineTransform
    from skimage.transform import ProjectiveTransform
    from skimage.transform import SimilarityTransform
    from skimage.transform import warp
    from skimage.util import img_as_float
    from skimage.util import random_noise
except ImportError:
    skdata = None

try:
    from ..dependencies.sitk import sitk
except ImportError:
    sitk = None

from ..transformation.types import TransformationType


def generate_image(name: Optional[str] = None) -> numpy.ndarray:
    """Generate image from a name."""
    if skdata is None:
        raise ModuleNotFoundError("No module named 'skimage'")
    if not name:
        name = "astronaut"
    load_image = getattr(skdata, name)
    image0 = load_image()
    if image0.ndim > 2:
        image0 = rgb2gray(image0)
    image0 = img_as_float(image0)
    image0 = image0[::-1, :]
    return image0


def generate_image_stack(
    image: numpy.ndarray,
    transfo_type: TransformationType,
    shape: Optional[Tuple[int, int]] = None,
    nimages: Optional[int] = None,
    plot: float = 0,
) -> Tuple[List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray]]:
    """Generate a stack of transformed images based on one image.

    :param image: 2D
    :param transfo_type: type of transformation
    :param shape: image shape of the stack
    :param nimages: number of images in the stack
    :param plot: show images
    :returns: images (3D), active transformations (3D), passive transformations (3D)
    """
    if skdata is None:
        raise ModuleNotFoundError("No module named 'skimage'")
    if shape is None:
        shape = (200, 220)
    if not nimages:
        nimages = 4
    if nimages < 1:
        raise ValueError("At least 1 image is required.")

    # Sub-image centered around the center of the full image
    full_shape = numpy.array(image.shape)
    if all(shape):
        sub_shape = numpy.minimum(numpy.array(shape), full_shape)
    else:
        sub_shape = full_shape
    center = (full_shape / 2).astype(int)
    d = (sub_shape / 2).astype(int)
    idx0 = center - d
    idx1 = center + d
    idx = tuple(slice(i0, i1) for i0, i1 in zip(idx0, idx1))

    # Return stack with complex deformations
    if transfo_type == TransformationType.bspline:
        return _generate_bspline_deformed_image_stack(image, nimages, idx)
    elif transfo_type == TransformationType.displacement_field:
        return _generate_displacement_field_image_stack(image, nimages, idx)

    # Transformation between two successive images in the stack
    if transfo_type == TransformationType.identity:
        tform = SimilarityTransform()
    elif transfo_type == TransformationType.translation:
        tform = SimilarityTransform(translation=[2, 3])
    elif transfo_type == TransformationType.rigid:
        tform = SimilarityTransform(rotation=numpy.radians(4))
    elif transfo_type == TransformationType.similarity:
        tform = SimilarityTransform(scale=1.05)
    elif transfo_type == TransformationType.affine:
        tform = AffineTransform(shear=numpy.radians(4))
    elif transfo_type == TransformationType.projective:
        matrix = numpy.array([[1, 0, 0], [0, 1, 0], [0.001, 0.001, 1]])
        tform = ProjectiveTransform(matrix=matrix)
    else:
        raise NotImplementedError(transfo_type)

    tbefore = SimilarityTransform(translation=-center[::-1])
    tafter = SimilarityTransform(translation=center[::-1])

    change_orig1 = SimilarityTransform(translation=idx0[::-1])
    change_orig2 = SimilarityTransform(translation=-idx0[::-1])
    tform0 = tbefore + tform + tafter

    # Apply transformation successively and record the accumulated transformation
    # (activate and passive) for each image with respect to the original image.
    transformed_image = image.copy()
    tform1 = tform0
    images = [transformed_image[idx]]
    passive_matrices = [numpy.identity(3)]
    active_matrices = [numpy.identity(3)]
    if plot:
        import matplotlib.pyplot as plt

        fig = plt.figure()
        plt.imshow(images[-1], origin="lower")
        plt.pause(plot)
    for _ in range(1, nimages):
        transformed_image = warp(image, tform1, order=3)
        images.append(transformed_image[idx])
        active_matrices.append(
            _indexing_order((change_orig1 + tform1 + change_orig2).params)
        )
        passive_matrices.append(
            _indexing_order(
                numpy.linalg.inv((change_orig1 + tform1 + change_orig2).params)
            )
        )
        if plot:
            fig.clear()
            plt.imshow(images[-1], origin="lower")
            plt.pause(plot)
        tform1 = tform1 + tform0

    return images, active_matrices, passive_matrices


def generate_image_stacks(
    image_stacks: List[numpy.ndarray],
    nstacks: Optional[int] = None,
    noise: Optional[str] = None,
) -> Dict[str, numpy.ndarray]:
    """Generate several images stacks from one image stack using different noise levels."""
    if not noise:
        noise = "s&p"
    if noise == "s&p" and skdata is None:
        noise = "uniform"
    if not nstacks:
        nstacks = 3
    if nstacks < 1:
        raise ValueError("At least 1 stack is required.")
    image_stacks = numpy.asarray(image_stacks)

    num_digits = len(str(nstacks - 1))
    if noise == "s&p":
        return {
            f"stack_{i:0{num_digits}d}": random_noise(
                image_stacks, mode="s&p", amount=i * 0.08
            )
            for i in numpy.random.permutation(nstacks)
        }
    elif noise == "uniform":
        noise_inc = numpy.random.uniform(
            0, numpy.nanmax(image_stacks) * 0.05, image_stacks.shape
        )
        return {
            f"stack_{i:0{num_digits}d}": image_stacks + i * noise_inc
            for i in numpy.random.permutation(nstacks)
        }
    else:
        return {
            f"stack_{i:0{num_digits}d}": image_stacks
            for i in numpy.random.permutation(nstacks)
        }


def _generate_displacement_field_image_stack(
    image: numpy.ndarray, nimages: int, idx: Tuple[slice]
) -> Tuple[List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray]]:
    """Generate a list of displacement-field deformed images based on one image.

    :returns: images, active transformations, passive transformations
    """
    images = [image[idx]]
    if sitk is None:
        raise ModuleNotFoundError("No module named 'SimpleITK'")
    simage = sitk.GetImageFromArray(image)
    shape = image.shape
    deformation = (numpy.random.rand(*shape, 2) - 0.5) * 10
    passive_matrices = [numpy.zeros_like(deformation)]
    active_matrices = [numpy.zeros_like(deformation)]
    for i in range(nimages):
        active_matrices.append(gaussian(deformation * (1.5 * i + 1), i / 4 + 1))
        field = sitk.GetImageFromArray(active_matrices[-1], True)
        passive_matrices.append(
            sitk.GetArrayFromImage(sitk.InvertDisplacementField(field))
        )

        displ = sitk.DisplacementFieldTransform(field)
        result = sitk.Resample(
            simage, simage, displ, sitk.sitkBSpline1, 0.0, simage.GetPixelID()
        )
        images.append(sitk.GetArrayFromImage(result)[idx])
    for i in range(len(passive_matrices)):
        passive_matrices[i] = passive_matrices[i][idx]
        active_matrices[i] = active_matrices[i][idx]
    return images, active_matrices, passive_matrices


def _generate_bspline_deformed_image_stack(
    image: numpy.ndarray, nimages: int, idx: Tuple[slice]
) -> Tuple[List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray]]:
    """Generate a list of spline deformed images based on one image.

    :returns: images, active transformations, passive transformations
    """
    if sitk is None:
        raise ModuleNotFoundError("No module named 'SimpleITK'")
    images = [image[idx]]

    simage = sitk.GetImageFromArray(images[0])
    shape = image.shape
    spline_order = 3
    mesh_size = [int(i / 20) for i in shape]
    npoints = [m + spline_order for m in mesh_size]

    displacements = numpy.random.rand(numpy.prod(npoints) * 2) - 0.5
    transform = sitk.BSplineTransformInitializer(simage, mesh_size, 3)
    passive = [numpy.zeros((*shape, 2))]
    active = [[*transform.GetCoefficientImages(), 3]]
    for i in range(nimages):
        scaled = displacements * (i + 1)
        transform.SetParameters(scaled)
        active.append([*transform.GetCoefficientImages(), 3])
        field = sitk.TransformToDisplacementField(
            transform,
            outputPixelType=sitk.sitkVectorFloat64,
            size=simage.GetSize(),
            outputOrigin=simage.GetOrigin(),
            outputSpacing=simage.GetSpacing(),
            outputDirection=simage.GetDirection(),
        )

        passive.append(sitk.GetArrayFromImage(sitk.InvertDisplacementField(field)))
        result = sitk.Resample(
            simage, simage, transform, sitk.sitkBSpline1, 0.0, simage.GetPixelID()
        )
        images.append(sitk.GetArrayFromImage(result))

    return images, active, passive


def _indexing_order(matrix: numpy.ndarray) -> numpy.ndarray:
    matrix = matrix.copy()
    matrix[:2, :2] = matrix[:2, :2].T
    matrix[:2, 2] = matrix[:2, 2][::-1]
    return matrix
