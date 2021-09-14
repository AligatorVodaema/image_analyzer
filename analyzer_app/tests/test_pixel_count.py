import pytest
from analyzer_app.services import count_pixels_from_image, check_mode_of_image_and_convert
import os


@pytest.mark.pixel_counting
class TestPixelCounter:
    def test_should_be_rgba_mode(self):
        """Should not be converted to any mode. Cat image is
        in RGBA mode."""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_dir, 'cat.png')
        pil_instance = check_mode_of_image_and_convert(image_path)
        assert pil_instance.mode == 'RGBA', 'Result Pillow instance ' \
            'not in RGBA mode.'

    def test_should_be_rgba_mode_too(self):
        """Should be converted from P mode to RGBA."""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_dir, 'dogge_p.png')
        pil_instance = check_mode_of_image_and_convert(image_path)
        assert pil_instance.mode == 'RGBA', 'Result Pillow instance ' \
            'not in RGBA mode.'

    def test_should_be_success_with_jpg(self):
        """White pixels should be more then blacks in this image."""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_dir, 'grand_cheroki.jpg')
        assert 'The "White" pixels is dominated' in \
            count_pixels_from_image(image_path),\
                'pixels not counted in JPG.'

    def test_should_be_success_with_png(self):
        """Black pixels should be more then whites in this image."""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_dir, 'cat.png')
        assert 'The "Black" pixels is dominated' in \
            count_pixels_from_image(image_path),\
                'pixels not counted in PNG.'

    def test_should_be_success_with_p_mode(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_dir, 'dogge_p.png')
        assert 'The "White" pixels is dominated' in \
            count_pixels_from_image(image_path),\
                'pixels not counted in PNG image with palett mode.'

    