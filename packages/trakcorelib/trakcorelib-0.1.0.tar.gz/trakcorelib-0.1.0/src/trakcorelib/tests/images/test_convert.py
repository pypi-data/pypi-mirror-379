import numpy as np

from trakcorelib.images.convert import convert_to_8bit_grayscale
from trakcorelib.tests.images.utils import (
    create_example_constant_image,
    create_example_random_image,
)


def test_convert_to_8bit_grayscale_from_8bit_grayscale() -> None:
    source = create_example_constant_image(8, 255)
    converted = convert_to_8bit_grayscale(source)
    assert converted.mode == "L"
    # This should just be a no-op.
    assert np.all(np.asarray(converted) == 255)


def test_convert_to_8bit_grayscale_from_12bit_grayscale_mode_high() -> None:
    #                  we should get these bits:     vvvvvvvv
    source = create_example_constant_image(12, 0b0000101100110110)
    converted = convert_to_8bit_grayscale(source, mode="high")

    assert converted.mode == "L"
    assert np.all(np.asarray(converted) == 0b10110011)


def test_convert_to_8bit_grayscale_from_12bit_grayscale_mode_low() -> None:
    #                  we should get these bits:         vvvvvvvv
    source = create_example_constant_image(12, 0b0000101100110110)
    converted = convert_to_8bit_grayscale(source, mode="low")

    assert converted.mode == "L"
    assert np.all(np.asarray(converted) == 0b00110110)


def test_convert_to_8bit_grayscale_from_12bit_grayscale_mode_minmax() -> None:
    source = create_example_random_image(12, random_value_range=(300, 1500))
    converted = convert_to_8bit_grayscale(source, mode="minmax")

    assert converted.mode == "L"
    # Pixels with a value 300 should now be 0, pixels with a value 1500 should
    # now be 255.
    source_array = np.asarray(source)
    converted_array = np.asarray(converted)
    assert np.all(converted_array[np.where(source_array == 300)] == 0)
    assert np.all(converted_array[np.where(source_array == 1500)] == 255)


def test_convert_to_8bit_grayscale_from_12bit_grayscale_mode_custom() -> None:
    source = create_example_random_image(12, random_value_range=(300, 1500))
    converted = convert_to_8bit_grayscale(
        source, mode="custom", custom_range=(456, 1234)
    )

    assert converted.mode == "L"
    # Pixels with a value 300 should now be 0, pixels with a value 1500 should
    # now be 255.
    source_array = np.asarray(source)
    converted_array = np.asarray(converted)
    assert np.all(converted_array[np.where(source_array <= 456)] == 0)
    assert np.all(converted_array[np.where(source_array >= 1234)] == 255)


def test_convert_to_8bit_grayscale_from_16bit_grayscale_mode_high() -> None:
    #                  we should get these bits: vvvvvvvv
    source = create_example_constant_image(16, 0b1010101100110110)
    converted = convert_to_8bit_grayscale(source, mode="high")

    assert converted.mode == "L"
    assert np.all(np.asarray(converted) == 0b10101011)


def test_convert_to_8bit_grayscale_from_16bit_grayscale_mode_low() -> None:
    #                  we should get these bits:         vvvvvvvv
    source = create_example_constant_image(16, 0b1010101100110110)
    converted = convert_to_8bit_grayscale(source, mode="low")

    assert converted.mode == "L"
    assert np.all(np.asarray(converted) == 0b00110110)


def test_convert_to_8bit_grayscale_from_16bit_grayscale_mode_minmax() -> None:
    source = create_example_random_image(16, random_value_range=(300, 56789))
    converted = convert_to_8bit_grayscale(source, mode="minmax")

    assert converted.mode == "L"
    # Pixels with a value 300 should now be 0, pixels with a value 1500 should
    # now be 255.
    source_array = np.asarray(source)
    converted_array = np.asarray(converted)
    assert np.all(converted_array[np.where(source_array == 300)] == 0)
    assert np.all(converted_array[np.where(source_array == 56789)] == 255)


def test_convert_to_8bit_grayscale_from_16bit_grayscale_mode_custom() -> None:
    source = create_example_random_image(12, random_value_range=(300, 56789))
    converted = convert_to_8bit_grayscale(
        source, mode="custom", custom_range=(456, 34567)
    )

    assert converted.mode == "L"
    # Pixels with a value 300 should now be 0, pixels with a value 1500 should
    # now be 255.
    source_array = np.asarray(source)
    converted_array = np.asarray(converted)
    assert np.all(converted_array[np.where(source_array <= 456)] == 0)
    assert np.all(converted_array[np.where(source_array >= 34567)] == 255)
