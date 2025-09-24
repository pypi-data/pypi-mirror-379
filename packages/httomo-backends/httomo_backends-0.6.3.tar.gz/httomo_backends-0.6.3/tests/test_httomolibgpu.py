from typing import Literal
import pytest
import numpy as np
from numpy import uint16, float32

from pytest_mock import MockerFixture
import os

cupy = pytest.importorskip("cupy")
httomolibgpu = pytest.importorskip("httomolibgpu")
import cupy as cp

from httomo_backends.methods_database.query import MethodsDatabaseQuery


from httomolibgpu.misc.morph import data_resampler, sino_360_to_180
from httomolibgpu.prep.normalize import normalize
from httomolibgpu.prep.phase import paganin_filter_tomopy
from httomolibgpu.prep.alignment import distortion_correction_proj_discorpy
from httomolibgpu.prep.stripe import (
    remove_stripe_based_sorting,
    remove_stripe_ti,
    remove_all_stripe,
    raven_filter,
)
from httomolibgpu.misc.corr import remove_outlier
from httomolibgpu.misc.denoise import total_variation_ROF, total_variation_PD
from httomolibgpu.recon.algorithm import (
    FBP3d_tomobar,
    SIRT3d_tomobar,
    LPRec3d_tomobar,
    CGLS3d_tomobar,
)
from httomolibgpu.misc.rescale import rescale_to_int

from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.misc.morph import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.prep.phase import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.prep.stripe import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.recon.algorithm import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.recon.peak_memory_line_profile_hook import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.misc.rescale import *
from httomo_backends.methods_database.packages.backends.httomolibgpu.supporting_funcs.prep.normalize import *


module_mem_path = "httomo.methods_database.packages.external."


class MaxMemoryHook(cp.cuda.MemoryHook):
    def __init__(self, initial=0):
        self.max_mem = initial
        self.current = initial

    def malloc_postprocess(
        self, device_id: int, size: int, mem_size: int, mem_ptr: int, pmem_id: int
    ):
        self.current += mem_size
        self.max_mem = max(self.max_mem, self.current)

    def free_postprocess(
        self, device_id: int, mem_size: int, mem_ptr: int, pmem_id: int
    ):
        self.current -= mem_size

    def alloc_preprocess(self, **kwargs):
        pass

    def alloc_postprocess(self, device_id: int, mem_size: int, mem_ptr: int):
        pass

    def free_preprocess(self, **kwargs):
        pass

    def malloc_preprocess(self, **kwargs):
        pass


@pytest.mark.parametrize("dtype", ["uint16", "float32"])
@pytest.mark.parametrize("slices", [50, 121])
@pytest.mark.cupy
def test_normalize_memoryhook(flats, darks, ensure_clean_memory, dtype, slices):
    hook = MaxMemoryHook()
    data = cp.random.random_sample(
        (slices, flats.shape[1], flats.shape[2]), dtype=np.float32
    )
    if dtype == "uint16":
        darks = (darks * 1233).astype(np.uint16)
        flats = flats.astype(np.uint16)
        data = data.astype(np.uint16)
    with hook:
        normalize(cp.copy(data), flats, darks, minus_log=True).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_normalize(
        data.shape[1:], dtype=data.dtype
    )

    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.parametrize("dtype", ["uint16"])
@pytest.mark.parametrize("slices", [10, 20])
@pytest.mark.cupy
def test_remove_outlier_memoryhook(flats, ensure_clean_memory, dtype, slices):
    hook = MaxMemoryHook()
    data = cp.random.random_sample((slices, 2560, 2560), dtype=np.float32)
    if dtype == "uint16":
        data = data.astype(np.uint16)
    with hook:
        remove_outlier(cp.copy(data))

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    method_query = MethodsDatabaseQuery("httomolibgpu.misc.corr", "remove_outlier")
    memory_requirements = method_query.get_memory_gpu_params()
    assert memory_requirements is not None
    assert memory_requirements.multiplier is not None
    estimated_memory_bytes = (
        memory_requirements.multiplier * np.prod(cp.shape(data)) * uint16().nbytes
    )

    estimated_memory_mb = round(estimated_memory_bytes / (1024**2), 2)

    max_mem_mb = round(max_mem / (1024**2), 2)
    # now compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 25


@pytest.mark.parametrize("slices", [3, 10, 20])
@pytest.mark.cupy
def test_denoiser_ROF_TV_memoryhook(ensure_clean_memory, slices):
    hook = MaxMemoryHook()
    data = cp.random.random_sample((slices, 2560, 2560), dtype=np.float32)

    with hook:
        total_variation_ROF(cp.copy(data), regularisation_parameter=1.0, iterations=5)

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    method_query = MethodsDatabaseQuery(
        "httomolibgpu.misc.denoise", "total_variation_ROF"
    )
    memory_requirements = method_query.get_memory_gpu_params()
    assert memory_requirements is not None
    assert memory_requirements.multiplier is not None
    estimated_memory_bytes = (
        memory_requirements.multiplier * np.prod(cp.shape(data)) * float32().nbytes
    )

    estimated_memory_mb = round(estimated_memory_bytes / (1024**2), 2)

    max_mem_mb = round(max_mem / (1024**2), 2)
    # now compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.parametrize("slices", [3, 10, 20])
@pytest.mark.cupy
def test_denoiser_PD_TV_memoryhook(ensure_clean_memory, slices):
    hook = MaxMemoryHook()
    data = cp.random.random_sample((slices, 2560, 2560), dtype=np.float32)

    with hook:
        total_variation_PD(cp.copy(data), regularisation_parameter=1.0, iterations=5)

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    method_query = MethodsDatabaseQuery(
        "httomolibgpu.misc.denoise", "total_variation_PD"
    )
    memory_requirements = method_query.get_memory_gpu_params()
    assert memory_requirements is not None
    assert memory_requirements.multiplier is not None
    estimated_memory_bytes = (
        memory_requirements.multiplier * np.prod(cp.shape(data)) * float32().nbytes
    )

    estimated_memory_mb = round(estimated_memory_bytes / (1024**2), 2)

    max_mem_mb = round(max_mem / (1024**2), 2)
    # now compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [64, 128])
@pytest.mark.parametrize("dim_x", [81, 260, 320])
@pytest.mark.parametrize("dim_y", [340, 135, 96])
def test_paganin_filter_tomopy_memoryhook(slices, dim_x, dim_y, ensure_clean_memory):
    data = cp.random.random_sample((slices, dim_x, dim_y), dtype=np.float32)
    hook = MaxMemoryHook()
    with hook:
        data_filtered = paganin_filter_tomopy(cp.copy(data)).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_paganin_filter_tomopy(
        (dim_x, dim_y), dtype=np.float32()
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [128, 190, 256])
def test_distortion_correction_memoryhook(
    slices, distortion_correction_path, ensure_clean_memory
):
    data_size_dim = 320
    data = cp.random.random_sample(
        (slices, data_size_dim, data_size_dim), dtype=np.float32
    )

    distortion_coeffs_path = os.path.join(
        distortion_correction_path, "distortion-coeffs.txt"
    )
    shift_xy = [0, 0]
    step_xy = [1, 1]

    hook = MaxMemoryHook()
    with hook:
        data_corrected = distortion_correction_proj_discorpy(
            cp.copy(data), distortion_coeffs_path, shift_xy, step_xy
        ).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook
    max_mem_mb = round(max_mem / (1024**2), 2)  # now in mbs

    # now we estimate how much of the total memory required for this data
    method_query = MethodsDatabaseQuery(
        "httomolibgpu.prep.alignment", "distortion_correction_proj_discorpy"
    )
    memory_requirements = method_query.get_memory_gpu_params()
    assert memory_requirements is not None
    assert memory_requirements.multiplier is not None
    estimated_memory_bytes = (
        memory_requirements.multiplier * np.prod(cp.shape(data)) * float32().nbytes
    )
    estimated_memory_mb = round(estimated_memory_bytes / (1024**2), 2)
    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [128, 256, 320])
def test_remove_stripe_based_sorting_memoryhook(
    slices, distortion_correction_path, ensure_clean_memory
):
    data_size_dim = 300
    data = cp.random.random_sample(
        (data_size_dim, slices, data_size_dim), dtype=np.float32
    )

    hook = MaxMemoryHook()
    with hook:
        data_filtered = remove_stripe_based_sorting(cp.copy(data)).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook
    max_mem_mb = round(max_mem / (1024**2), 2)  # now in mbs

    # now we estimate how much of the total memory required for this data
    method_query = MethodsDatabaseQuery(
        "httomolibgpu.prep.stripe", "remove_stripe_based_sorting"
    )
    memory_requirements = method_query.get_memory_gpu_params()
    assert memory_requirements is not None
    assert memory_requirements.multiplier is not None
    estimated_memory_bytes = (
        memory_requirements.multiplier * np.prod(cp.shape(data)) * float32().nbytes
    )
    estimated_memory_mb = round(estimated_memory_bytes / (1024**2), 2)
    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [64, 129])
def test_remove_stripe_ti_memoryhook(slices, ensure_clean_memory):
    dim_x = 156
    dim_y = 216
    data = cp.random.random_sample((slices, dim_x, dim_y), dtype=np.float32)
    hook = MaxMemoryHook()
    with hook:
        data_filtered = remove_stripe_ti(cp.copy(data)).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_remove_stripe_ti(
        (dim_x, dim_y), dtype=np.float32()
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("projections", [180, 360, 720, 1080, 1440])
def test_raven_filter_memoryhook(projections, ensure_clean_memory):
    vert_det = 10
    horiz_det = 2560
    data = cp.random.random_sample((projections, vert_det, horiz_det), dtype=np.float32)
    kwargs = {}
    kwargs["pad_x"] = 20
    kwargs["pad_y"] = 20
    hook = MaxMemoryHook()
    with hook:
        data_filtered = raven_filter(cp.copy(data), **kwargs).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_raven_filter(
        (projections, horiz_det), dtype=np.float32(), **kwargs
    )
    estimated_memory_mb = round(vert_det * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 27


@pytest.mark.cupy
@pytest.mark.parametrize("angles", [900, 1800])
@pytest.mark.parametrize("dim_x_slices", [1, 3, 5])
@pytest.mark.parametrize("dim_y", [1280, 2560])
def test_remove_all_stripe_memoryhook(angles, dim_x_slices, dim_y, ensure_clean_memory):
    data = cp.random.random_sample((angles, dim_x_slices, dim_y), dtype=np.float32)
    hook = MaxMemoryHook()
    with hook:
        data_filtered = remove_all_stripe(cp.copy(data)).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook
    max_mem_mb = round(max_mem / (1024**2), 2)  # now in mbs

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_remove_all_stripe(
        (angles, dim_y), dtype=np.float32()
    )
    estimated_memory_mb = round(dim_x_slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    assert estimated_memory_mb >= max_mem_mb
    # this function is too complex to estimate the memory needed exactly,
    # but it works in slice-by-slice fashion.
    # We overestimate and ensure that we're always above the memoryhook limit.


@pytest.mark.cupy
@pytest.mark.parametrize("interpolation", ["nearest", "linear"])
@pytest.mark.parametrize("slices", [1, 3, 10])
@pytest.mark.parametrize("newshape", [[256, 256], [500, 500], [1000, 1000]])
def test_data_sampler_memoryhook(slices, newshape, interpolation, ensure_clean_memory):
    recon_size = 2560
    data = cp.random.random_sample((recon_size, slices, recon_size), dtype=cp.float32)
    kwargs = {}
    kwargs["newshape"] = newshape
    kwargs["interpolation"] = interpolation
    kwargs["axis"] = 1

    hook = MaxMemoryHook()
    with hook:
        scaled_data = data_resampler(cp.copy(data), **kwargs)

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_data_resampler(
        (recon_size, recon_size), dtype=np.float32(), **kwargs
    )
    # as this is slice-by-slice implementation we should be adding slices number
    estimated_memory_mb = slices * round(estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    assert estimated_memory_mb >= max_mem_mb
    # for this function it is difficult to estimate the memory requirements as it works
    # slice by slice. Also the memory usage inside interpn/RegularGridInterpolator is
    # unknown. We should generally overestitmate the memory here.


@pytest.mark.cupy
@pytest.mark.parametrize("padding_detx", [0, 10, 100, 200])
@pytest.mark.parametrize("projections", [1801, 3601])
@pytest.mark.parametrize("slices", [7, 11, 15])
@pytest.mark.parametrize("detectorX", [1200, 2560])
def test_recon_FBP3d_tomobar_memoryhook(
    slices,
    detectorX,
    projections,
    padding_detx,
    ensure_clean_memory,
    mocker: MockerFixture,
):
    data = cp.random.random_sample((projections, slices, detectorX), dtype=np.float32)
    kwargs = {}
    kwargs["angles"] = np.linspace(
        0.0 * np.pi / 180.0, 180.0 * np.pi / 180.0, data.shape[0]
    )
    kwargs["detector_pad"] = padding_detx
    kwargs["center"] = 500
    kwargs["recon_size"] = detectorX
    kwargs["recon_mask_radius"] = 0.8

    hook = MaxMemoryHook()
    p1 = mocker.patch(
        "tomobar.astra_wrappers.astra_base.astra.data3d.delete",
        side_effect=lambda id: hook.free_postprocess(0, data.nbytes, 0, 0),
    )

    with hook:
        recon_data = FBP3d_tomobar(cp.copy(data), **kwargs)

    p1.assert_called_once()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_FBP3d_tomobar(
        (projections, detectorX), dtype=np.float32(), **kwargs
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert (
        percents_relative_maxmem <= 100
    )  # overestimation happens here because of the ASTRA's part


@pytest.mark.cupy
@pytest.mark.parametrize("padding_detx", [0, 10, 50, 100])
@pytest.mark.parametrize("projections", [1500, 1801, 2560])
@pytest.mark.parametrize("detX_size", [2560])
@pytest.mark.parametrize("slices", [3, 4, 5, 10, 15, 20])
@pytest.mark.parametrize("projection_angle_range", [(0, np.pi)])
def test_recon_LPRec3d_tomobar_0_pi_memoryhook(
    slices,
    detX_size,
    projections,
    projection_angle_range,
    padding_detx,
    ensure_clean_memory,
):
    __test_recon_LPRec3d_tomobar_memoryhook_common(
        slices,
        detX_size,
        projections,
        projection_angle_range,
        padding_detx,
        ensure_clean_memory,
    )


@pytest.mark.full
@pytest.mark.cupy
@pytest.mark.parametrize("padding_detx", [0, 10, 50, 100])
@pytest.mark.parametrize("projections", [1500, 1801, 2560, 3601])
@pytest.mark.parametrize("detX_size", [2560])
@pytest.mark.parametrize("slices", [3, 4, 5, 10, 15, 20])
@pytest.mark.parametrize("projection_angle_range", [(0, np.pi)])
def test_recon_LPRec3d_tomobar_0_pi_memoryhook_full(
    slices,
    detX_size,
    projections,
    projection_angle_range,
    padding_detx,
    ensure_clean_memory,
):
    __test_recon_LPRec3d_tomobar_memoryhook_common(
        slices,
        detX_size,
        projections,
        projection_angle_range,
        padding_detx,
        ensure_clean_memory,
    )


@pytest.mark.full
@pytest.mark.cupy
@pytest.mark.parametrize("padding_detx", [0, 10, 50, 100])
@pytest.mark.parametrize("projections", [1500, 1801, 2560, 3601])
@pytest.mark.parametrize("detX_size", [2560])
@pytest.mark.parametrize("slices", [3, 4, 5, 10, 15, 20])
@pytest.mark.parametrize(
    "projection_angle_range", [(0, np.pi), (0, 2 * np.pi), (-np.pi / 2, np.pi / 2)]
)
def test_recon_LPRec3d_tomobar_memoryhook_full(
    slices,
    detX_size,
    projections,
    projection_angle_range,
    padding_detx,
    ensure_clean_memory,
):
    __test_recon_LPRec3d_tomobar_memoryhook_common(
        slices,
        detX_size,
        projections,
        projection_angle_range,
        padding_detx,
        ensure_clean_memory,
    )


def __test_recon_LPRec3d_tomobar_memoryhook_common(
    slices,
    detX_size,
    projections,
    projection_angle_range,
    padding_detx,
    ensure_clean_memory,
):
    angles_number = projections
    data = cp.random.random_sample((angles_number, slices, detX_size), dtype=np.float32)
    kwargs = {}
    kwargs["angles"] = np.linspace(
        projection_angle_range[0], projection_angle_range[1], data.shape[0]
    )
    kwargs["center"] = 1280
    kwargs["detector_pad"] = padding_detx
    kwargs["recon_size"] = detX_size
    kwargs["recon_mask_radius"] = 0.8

    hook = MaxMemoryHook()
    hook2 = PeakMemoryLineProfileHook(["methodsDIR_CuPy.py"])
    with hook, hook2:
        # with hook:
        recon_data = LPRec3d_tomobar(cp.copy(data), **kwargs)
    # hook2.print_report()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    non_slice_dims_shape = (angles_number, detX_size)
    input_data_type = np.float32()

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_LPRec3d_tomobar(
        non_slice_dims_shape, dtype=input_data_type, **kwargs
    )

    odd_horiz = bool(detX_size % 2)
    odd_vert = bool(slices % 2)

    padded_slices = slices + odd_vert

    if not odd_horiz and not odd_vert:
        input_slice_size = np.prod(non_slice_dims_shape) * input_data_type.itemsize
        estimated_memory_bytes -= input_slice_size

    estimated_memory_mb = round(padded_slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 80


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [3, 5])
@pytest.mark.parametrize("recon_size_it", [1200, 2000])
def test_recon_SIRT3d_tomobar_memoryhook(slices, recon_size_it, ensure_clean_memory):
    data = cp.random.random_sample((1801, slices, 2560), dtype=np.float32)
    kwargs = {}
    kwargs["recon_size"] = recon_size_it

    hook = MaxMemoryHook()
    with hook:
        recon_data = SIRT3d_tomobar(
            cp.copy(data),
            np.linspace(0.0 * np.pi / 180.0, 180.0 * np.pi / 180.0, data.shape[0]),
            1200,
            recon_size=recon_size_it,
            iterations=2,
            nonnegativity=True,
        )

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_SIRT3d_tomobar(
        (1801, 2560), dtype=np.float32(), **kwargs
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 25


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [3, 5])
@pytest.mark.parametrize("recon_size_it", [1200, 2000])
def test_recon_CGLS3d_tomobar_memoryhook(slices, recon_size_it, ensure_clean_memory):
    data = cp.random.random_sample((1801, slices, 2560), dtype=np.float32)
    kwargs = {}
    kwargs["recon_size"] = recon_size_it

    hook = MaxMemoryHook()
    with hook:
        recon_data = CGLS3d_tomobar(
            cp.copy(data),
            np.linspace(0.0 * np.pi / 180.0, 180.0 * np.pi / 180.0, data.shape[0]),
            1200,
            recon_size=recon_size_it,
            iterations=2,
            nonnegativity=True,
        )

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_CGLS3d_tomobar(
        (1801, 2560), dtype=np.float32(), **kwargs
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 20


@pytest.mark.cupy
@pytest.mark.parametrize("bits", [8, 16, 32])
@pytest.mark.parametrize("slices", [3, 5, 8])
@pytest.mark.parametrize("glob_stats", [False, True])
def test_rescale_to_int_memoryhook(
    data, ensure_clean_memory, slices: int, bits: Literal[8, 16, 32], glob_stats: bool
):
    data = cp.random.random_sample((1801, slices, 600), dtype=np.float32)
    kwargs: dict = {}
    kwargs["bits"] = bits
    if glob_stats:
        kwargs["glob_stats"] = (0.0, 10.0, 120.0, data.size)
    hook = MaxMemoryHook()
    with hook:
        rescale_to_int(cp.copy(data), **kwargs).get()

    # make sure estimator function is within range (80% min, 100% max)
    max_mem = (
        hook.max_mem
    )  # the amount of memory in bytes needed for the method according to memoryhook
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we estimate how much of the total memory required for this data
    (estimated_memory_bytes, subtract_bytes) = _calc_memory_bytes_rescale_to_int(
        (data.shape[0], data.shape[2]), dtype=np.float32(), **kwargs
    )
    estimated_memory_mb = round(slices * estimated_memory_bytes / (1024**2), 2)
    max_mem -= subtract_bytes
    max_mem_mb = round(max_mem / (1024**2), 2)

    # now we compare both memory estimations
    difference_mb = abs(estimated_memory_mb - max_mem_mb)
    percents_relative_maxmem = round((difference_mb / max_mem_mb) * 100)
    # the estimated_memory_mb should be LARGER or EQUAL to max_mem_mb
    # the resulting percent value should not deviate from max_mem on more than 20%
    assert estimated_memory_mb >= max_mem_mb
    assert percents_relative_maxmem <= 35


@pytest.mark.cupy
@pytest.mark.parametrize("slices", [3, 8, 30, 50])
@pytest.mark.parametrize("det_x", [600, 2160])
def test_sino_360_to_180_memoryhook(
    ensure_clean_memory,
    det_x: int,
    slices: int,
):
    # Use a different overlap value for stitching based on the width of the 360 sinogram
    overlap = 350 if det_x == 600 else 1950
    shape = (1801, slices, det_x)
    data = cp.random.random_sample(shape, dtype=np.float32)

    # Run method to see actual memory usage
    hook = MaxMemoryHook()
    with hook:
        sino_360_to_180(cp.copy(data), overlap)

    # Call memory estimator to estimate memory usage
    (estimated_bytes, subtract_bytes) = _calc_memory_bytes_sino_360_to_180(
        non_slice_dims_shape=(shape[0], shape[2]),
        dtype=np.float32(),
        overlap=overlap,
    )
    estimated_bytes *= slices

    max_mem = hook.max_mem - subtract_bytes

    # For the difference between the actual memory usage and estimated memory usage, calculate
    # that as a percentage of the actual memory used
    difference = abs(estimated_bytes - max_mem)
    percentage_difference = round((difference / max_mem) * 100)

    assert estimated_bytes >= max_mem
    assert percentage_difference <= 35


def test_FBP2d_astra_output_dim():
    # Call memory estimator to estimate memory usage
    recon_size = 300
    output_dims = _calc_output_dim_FBP2d_astra(
        non_slice_dims_shape=(10, 10),
        recon_size=recon_size,
    )
    assert output_dims == (recon_size, recon_size)
