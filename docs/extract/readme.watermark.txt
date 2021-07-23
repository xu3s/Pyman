Watermark Remover for the Browser

Usage:

  The basic usage is to just click through the top bar from left to right.
  The following explains what each button does.
  
  "Load Image":
    Loads the image to unwatermark. If you select multiple files, the tool
    will go through them all one after another.
  
  "Default watermark position":
    Specifies where the watermark will be put after it has been loaded, so
    you don't have to drag it all over the page to the opposite corner.
    Using it after the watermark has been loaded will have no effect.

  "Load Watermark":
    Load the watermark file to be used. They are the same as the ones from
    FIRE's extractor.

  Positioning the Watermark:
    You can drag and drop the watermark once it has been loaded. For fine
    tuning the positioning, use the arrow keys on your keyboard to move it
    by 1px. However, since that might still not be fine enough of an adjust-
    ment for some watermarks, you may hold the CTRL-key while using the arrow
    keys to move in 0.05px steps to *really* get it in the right spot.
    
  "Preview blending mode":
    To help with the positioning, you can switch between "normal" blending
    (the watermark is simply overlayed on top of the image) and "difference"
    blending mode (which works differently and emphasizes misalignment).
    Note that the preview you can see *doesn't* represent the actual un-
    watermarking result.

  "Unwatermark":
    When the watermark is in the right spot, click this button to start the
    unwatermarking process. Once done, the unwatermarked image will download
    and if you don't have any other images loaded/queued, it will also be
    shown in the image area.
    File name will be the original file name with "_uwm" appended, as PNG.
    (uwm = UnWaterMarked)

Options:

  If you click on the "Options" in the top bar, additional options will be
  shown below the top bar. Clicking this again, will hide them again. These
  options are evaluated during the unwatermarking process, so you can change
  them even in the middle of going through multiple files.
  
  "Transparency threshold":
    Pixels with an alpha value less than this value (= more transparent) will
    not be processed. The reason being, you can't really tell that small
    changes apart, so they don't need to be processed, speeding up the
    unwatermarking a little bit. Plus, most of them stem from JPEG compression
    anyway, meaning they're not really part of the watermark in the first place.

  "Opaque smoothing":
    For some very opaque watermarks (especially JPEG-heavy), there can be ugly
    artefacts in the resulting image. This option tries to hide the worst of
    them by averaging especially opaque pixels with their preceeding pixel.
    The strength/mix of the averaging is determined by how much the alpha is
    over the limit. The default value is high enough to not interfere with
    bilibili's watermark, one of the more common, yet very opaque watermarks.
    As such, the default value will not smooth that strongly, so play around
    with it if you really need it. 255 will disable it.
    Example: https://cdn.discordapp.com/attachments/743513778150178877/779279135796494337/unknown.png

  "Confirm results":
    As it states in the tool, with this it will not discard source images once
    they've been unwatermarked, but will ask you for confirmation (the buttons
    will pop up just below the top bar). "Yes" will confirm the changes,
    download the result and move on to the next image (if applicable). "No"
    will revert to the original image, discarding any changes. Useful if the
    watermark is hard to position.
