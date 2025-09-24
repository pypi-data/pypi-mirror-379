from .utils import ImageUtils


class ImageDynamic:
    @staticmethod
    def process(path, verbose=False, *args, **kwargs):
        """
        Dynamic image processor.  
        - If one size given: square resize with crop.  
        - If two sizes: resize to width then crop to target (w, h).  
        - Supports adjustments: sharpness, brightness, quality, max_size_kb.  
        Returns final optimized image.
        """
        utils = ImageUtils()

        img = utils.load_image(path)
        if not img:
            return None

        if len(args) == 1:  # square
            img = utils.resize_to_square(img, args[0])
        elif len(args) == 2:  # rectangular
            target = (args[0], args[1])
            img = utils.resize_to_width(img, target[0])
            img = utils.crop_center(img, target)
        else:
            utils._log("No size specified, returning original image")
            return img

        if kwargs.get("sharpness", 1.0) != 1.0:
            img = utils.adjust_sharpness(img, kwargs["sharpness"])

        if kwargs.get("brightness", 1.0) != 1.0:
            img = utils.adjust_brightness(img, kwargs["brightness"])

        quality = kwargs.get("quality", 85)
        max_size_kb = kwargs.get("max_size_kb", None)
        img = utils.optimize_for_web(img, quality=quality, max_size_kb=max_size_kb)

        return img