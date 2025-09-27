# TrakCoreLib
TrakCoreLib is a library with functionality that is often required for tracking
applications, such as reading images and modelling cameras.

## Installation
We recommend creating a virtual environment to install packages in. For example:
```bash
python -m venv .venv
. .venv/bin/activate
```

Alternatively, you can use tools like [`uv`](https://docs.astral.sh/uv/) to
automatically manage your Python project.

### Installing with `pip`
Install the `trakcorelib` package from PyPI with:
```bash
pip install trakcorelib
```

### Local editable installation
Navigate to your local TrakCoreLib directory and install the package:
```bash
pip install -e .
```
The `-e` flag makes the package "editable", ensuring that edits you make to
the TrakCoreLib directory will be reflected in your own package.

## Image examples

### Reading a single image as 8-bit grayscale
To read an image as a [Pillow](https://hugovk-pillow.readthedocs.io/en/stable/index.html)
`Image` object, use:

```python
image = read_image_as_8bit_grayscale("/path/to/image.tif")
```

For images with a bit depth higher than 8, different conversion modes to 8-bits
exist, for example, to use the lowest 8 bits:

```python
image = read_image_as_8bit_grayscale("/path/to/image.tif", convert_mode="low")
```

### Reading an image sequence from a directory
Use the `DirectoryImageSequence` class for reading an image sequence from a
directory; this represents a collection of images on disk. Images from this
sequence can be conveniently read, causing them to be cached such that the next
read does not need to touch the disk. Each image also has an identifier, which
can be any string.

To read an image sequence from a directory with a [glob](https://en.wikipedia.org/wiki/Glob_(programming)) pattern, use for example:
```python
sequence = DirectoryImageSequence.from_glob("/path/to/images", "cam001*.tif")
```
Here, a default image identifier is created for each image by finding the
substrings at the start and end of all filenames, and using the remainder as an
identifier. For example, the filenames "cam001_0005.tif", "cam001_0010.tif",
"cam001_0015.tif", all start with "cam001_00", and all end with ".tif", so the
remaining identifiers are: "05", "10", and "15".

Alternatively, an image sequence can be read from a directory with a [regular
expression](https://docs.python.org/3/library/re.html). This regular expression
should have a single group that contains the identifier. For example:
```python
sequence = DirectoryImageSequence.from_regex("/path/to/images", "cam001_(\d{4}).tif")
```
This will result in a sequence with the identifiers "0005", "0010", and "0015";
note that the leading "00" is preserved in this case, which may be useful in
some cases.

### Retrieving images from a sequence
Images can be easily retrieved from an image sequence, in the same way for all
types of images sequences.

Images can be retrieved by their index:
```python
image = sequence[10]
```

Or by their identifier:
```python
image = sequence.by_identifier("0010")
```

Furthermore, a sequence can be iterated over:
```python
for image in sequence:
    # Do something with the image.
    ...
```

### Saving an image to disk
An image sequence can be saved to disk, where each image is written to the same
directory.

For example, using a default filename pattern:
```python
sequence.save("/path/to/dest")
```
This will save the contents of the sequence as TIFF-images to
"image_<identifier>.tif", for example: "/path/to/dest/image_0005.tif",
"/path/to/dest/image_0010.tif", ...

The filename pattern and image format can also be specified. The filename
pattern should contain a single placeholder `{}`, which will be replaced by the
image identifier.
```python
sequence.save("/path/to/dest", filename_pattern="cam001_{}.jpg", image_format="JPEG")
```
Which will result in JPEG-images: "/path/to/dest/cam001_0005.jpg",
"/path/to/dest/cam001_0010.jpg", ...

### Creating and using an in-memory image sequence
Image sequences can also be created without any association with files on disk.
So-called "in-memory" sequences can be manipulated at will. Creating a
`MemoryImageSequence` can be done in several ways.

From an existing disk image sequence:
```python
disk_sequence = DirectoryImageSequence.from_glob("/path/to/images", "cam001*.tif")
memory_sequence = disk_sequence.to_memory_image_sequence()
```

Or a new sequence without any images:
```python
sequence = MemoryImageSequence.empty()
```

Or a new sequence with black (i.e. all pixels 0) images:
```python
sequence = MemoryImageSequence.new_8bit_grayscale(20, (1920, 1080))
```
This creates a sequence with 20 8-bit grayscale images, with a size of
1920 x 1080 pixels.

In-memory image sequences behave like lists, images can be set, inserted,
appended:
```python
sequence = MemoryImageSequence.new_8bit_grayscale(20, (1920, 1080))
sequence[10] = image
sequence.insert(3, image)
sequence.append(image)
```

Also, individual images in a `MemoryImageSequence` can be modified, unlike
disk image sequences: with a disk image sequence you always get a _copy_ of the
image, while a memory image sequence gives you a _reference_. For example:
```python
sequence = MemoryImageSequence.new_8bit_grayscale(20, (1920, 1080))

sequence[10].paste(image_to_be_pasted)
# The image at index 10 has now been modified.
```

### Applying image operations
Several common image operations have been defined in the module
`image.operations`.

They can be applied to a single image (i.e. a Pillow `Image` object), for
example:
```python
adjusted = adjust_brightness(image, 1.5)
```

Operations can also be applied to an image sequence, for example:
```python
adjusted = apply(sequence, adjust_brightness, 1.5)
```
This will produce a `MemoryImageSequence` with the operation (in this case
`adjust_brightness`) applied to all of the images in the original sequence.

## DLT calibration examples
TrakCoreLib has support for creating and handling Direct Linear Transformation
(DLT) calibrations. The mathematics behind the DLT are documented extensively
in the Python modules, so will not be addressed here.

### Estimating a DLT calibration from object/image point pairs
To create a DLT image calibration from object and image point pairs, there are
two methods available in TrakCoreLib: classic and optimisation.

The classic method uses a linear least-squares solution to compute the
DLT-matrix. This is historically used most often, but has the drawback that the
resulting camera orientation matrix may not be perfectly orthogonal (i.e. it is
not a valid rotation matrix).

An alternative approach is to optimise intrinsic and extrinsic camera properties
directly, guaranteeing that the camera orientation matrix is orthogonal. This
is computationally slightly more expensive, but still finishes nearly
instantaneously on modern hardware.

To estimate the DLT matrix, use for example:
```python
# Object points should be N x 3, with N the number of points.
object_points = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    ...
]
# Image points should be N x 2.
image_points = [
    [1.2, 3.4],
    [5.6, 7.8],
    ...
]

dlt_classic = estimate_dlt_classic(object_points, image_points)
dlt_optimised = estimate_dlt_optimisation(object_points, image_points)
```

### Estimating a DLT calibration with fixed intrinsic/extrinsic properties
The optimisation approach for estimating a DLT matrix has the advantage that
part of the camera properties can be prescribed, optimising only the remaining
properties. TrakCoreLib allows you to keep either the intrinsic
(principal point, focal lengths) or extrinsic (camera location and orientation)
fixed.

For example:
```
object_points = [...]
image_points = [...]
fixed_intrinsic = IntrinsicProperties(
    u_principal=512,
    v_principal=512,
    focal_length_u=100,
    focal_length_v=100
)
fixed_extrinsic = ExtrinsicProperties(
    coords=[0.1, 0.2, 0.3],
    rotation=pyquaternion.Quaternion(
        [1.0, 2.0, 3.0, 4.0]
    ).normalised
)

with_fixed_intrinsic = estimate_dlt_optimisation(
    object_points, image_points, fixed_intrinsic=fixed_intrinsic
)
with_fixed_extrinsic = estimate_dlt_optimisation(
    object_points, image_points, fixed_extrinsic=fixed_extrinsic
)
```

### Using a DLT calibration object
Estimating a DLT calibration results in a `DltCameraCalibration` object, which
has several useful operations defined on it.

The DLT can be expressed as a projection matrix:
```python
matrix = dlt.projection_matrix
```

Or it can be expressed as the 11 independent DLT coefficients. Refer to the
`dlt` module for the definition of these coefficients:
```python
coefs = dlt.coefficients
```

Object points can be projected to image points for the view represented by the
DLT:
```python
image_points = dlt.project(object_points)
```
This transforms the N x 3 object points array into an N x 2 image points array.

For assessing the accuracy of a DLT, you can compute the RMS of the reprojection
error:
```python
error = dlt.compute_reprojection_rms_error(object_points, image_points)
```

Finally, you can compute intrinsic and extrinsic camera properties from a DLT
calibration:
```python
properties = dlt.compute_camera_properties()
intrinsic = properties.intrinsic
extrinsic = properties.extrinsic
```

### Using a multi-view DLT calibration
When processing data from multiple views (for example, with a multi-camera
setup), the DLT calibrations can be grouped in a single `MultiViewCalibration`
object. Each view is given a name (by default `"view001"`, `"view002"`, ...) to
identify it.

Multi-view calibrations can be saved to a CSV file and loaded from it:
```python
calib = MultiViewCalibration([dlt1, dlt2, dlt3], ["cam1", "cam2", "cam3"])

calib.to_csv("/path/to/file.csv")
loaded_calib = MultiViewCalibration.from_csv("/path/to/file.csv")
```

Individual calibrations and names can be retrieved:
```python
dlt1 = calib[0]
name1 = calib.names[0]
```

Finally, an object point can be reconstructed if image points are provided for
it from each view. Image points are specified as an N x 2 array, where N is the
number of views in this calibration.
```python
image_points = [
    [10, 20],
    [30, 40],
    [50, 60]
]
object_point = calib.reconstruct_object_point(image_points)
```
The object point is a 3-tuple with the reconstructed x, y, z coordinates.

## Releasing to PyPI
To create a new release on PyPI follow these steps:

1. Update the version in `pyproject.toml`, keep the requirements of [Semantic
   Versioning](https://semver.org/) in mind.
2. Build the package with `python -m build`
