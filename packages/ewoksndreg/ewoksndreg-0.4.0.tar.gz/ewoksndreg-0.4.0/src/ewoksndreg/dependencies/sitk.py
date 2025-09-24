import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # When warnings are treated as errors (e.g. -W error)
    # importing SimpleITK segfaults.
    import SimpleITK as sitk  # noqa F401
