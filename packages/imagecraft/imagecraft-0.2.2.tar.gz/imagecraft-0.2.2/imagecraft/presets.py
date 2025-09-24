from PIL import Image, ImageEnhance
from .utils import ImageUtils

class ImagePresets:
    @staticmethod
    def make_profile_image(path, size=256, verbose=False):
        """
        Preset: Generate a square, sharp profile image for avatars. 
        Resizes, sharpens slightly, and optimizes for web.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_square(img, size)
        img = utils.adjust_sharpness(img, 1.2)
        return utils.optimize_for_web(img)
    
    # --- SQUARE LOGO ---
    @staticmethod
    def logo_square(path, size=256, sharpness=2.0, format="JPEG", verbose=False):
        """
        Square logo: logo-only or logo below text.
        Crops from center instead of padding, keeps aspect ratio.
        """

        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None

        # Resize and crop center to square
        img = utils.resize_to_square(img, size)
        img = utils.adjust_sharpness(img, sharpness)

        return utils.optimize_for_web(img, format=format, quality=95, bg_color=(255,255,255))


    # --- HORIZONTAL LOGO ---
    @staticmethod
    def logo_horizontal(path, width=512, sharpness=2.0, format="JPEG", height_ratio=0.5, verbose=False):
        """
        Horizontal logo: logo + text (text below optional).
        Height auto-scaled by height_ratio, cropped if necessary.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None

        # Compute target height
        target_height = int(width * height_ratio)

        # Resize by width keeping aspect ratio
        img = utils.resize_to_width(img, width)
        img = utils.adjust_sharpness(img, sharpness)

        # Crop center to target_height if taller
        w, h = img.size
        if h > target_height:
            img = utils.crop_center(img, (w, target_height))

        return utils.optimize_for_web(img, format=format, quality=95, bg_color=(255,255,255))


    # --- VERTICAL LOGO ---
    @staticmethod
    def logo_vertical(path, height=512, sharpness=2.0, format="JPEG", width_ratio=0.6, verbose=False):
        """
        Vertical logo: logo + text below.
        Width auto-scaled by width_ratio, cropped from center if needed.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None

        # Compute target width
        target_width = int(height * width_ratio)

        # Resize by height keeping aspect ratio
        img = utils.resize_to_height(img, height)
        img = utils.adjust_sharpness(img, sharpness)

        # Crop center if wider
        w, h = img.size
        if w > target_width:
            img = utils.crop_center(img, (target_width, h))

        return utils.optimize_for_web(img, format=format, quality=95, bg_color=(255,255,255))
    
    @staticmethod
    def make_icon(path, size=64, sharpness=5.0, verbose=False):
        """
        Preset: Generate a small square icon (e.g., favicon). 
        Resizes and optimizes for web.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_square(img, size)
        img = utils.adjust_sharpness(img, sharpness)
        return utils.optimize_for_web(img)

    @staticmethod
    def make_thumbnail(path, width=400, verbose=False):
        """
        Preset: Generate a small thumbnail for previews. 
        Resizes to given width, keeps aspect ratio, optimizes for web.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_width(img, width)
        return utils.optimize_for_web(img)

    @staticmethod
    def make_poster(path, size=(1080, 1920), verbose=False):
        """
        Preset: Generate a vertical poster (e.g., story format). 
        Resizes by height, then center-crops to target aspect ratio.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_height(img, size[1])
        img = utils.crop_center(img, size)
        return utils.optimize_for_web(img)

    @staticmethod
    def make_banner(path, size=(1920, 600), verbose=False):
        """
        Preset: Generate a wide banner (landscape style). 
        Resizes by width, then crops center to final size.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_width(img, size[0])
        img = utils.crop_center(img, size)
        return utils.optimize_for_web(img)

    @staticmethod
    def make_cover(path, size=(1200, 628), verbose=False):
        """
        Preset: Generate a social media cover (Facebook, Twitter, etc.). 
        Resizes by width, then crops center to exact size.
        """
        utils = ImageUtils(verbose=verbose)

        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_width(img, size[0])
        img = utils.crop_center(img, size)
        return utils.optimize_for_web(img)

    @staticmethod
    def make_gallery_image(path, size=800, verbose=False):
        """
        Preset: Generate a square gallery image. 
        Resizes, crops square, and optimizes for web.
        """
        utils = ImageUtils(verbose=verbose)
        
        img = utils.load_image(path)
        if not img:
            return None
        img = utils.resize_to_square(img, size)
        return utils.optimize_for_web(img)