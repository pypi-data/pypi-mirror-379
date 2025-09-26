Changelog (nionswift-eels-analysis)
===================================

0.6.13 (2025-09-25):
--------------------
- Fix issue with measure temperature.

0.6.12 (2025-06-21):
--------------------
- Handle case where user drags interval right-over-left resulting in temporary max/min interval.

0.6.10 (2025-05-29):
--------------------
- Maintenance release.

0.6.9 (2025-04-23):
-------------------
- Package dependencies updated.
- Modify computations to use auto-titling.

0.6.8 (2025-01-07):
-------------------
- Package dependencies updated.

0.6.7 (2024-10-24):
-------------------
- Include AREELS High Contrast color table.
- Require Numpy 2. Add Python 3.13 support. Drop Python 3.9, 3.10 support.

0.6.6 (2024-06-18):
-------------------
- Swift 16.11 compatibility (no changes).

0.6.5 (2023-09-28):
-------------------
- Fix a bug in temperature calculation.

0.6.4 (2023-08-17):
-------------------
- Add Python 3.11 support. Drop 3.8.
- Update titles for new auto-title system in nionswift.
- Fix thermometry issues.

0.6.3 (2022-09-14):
-------------------
- Fix regression in elemental mapping radio buttons for picked edge.

0.6.2 (2022-07-26):
-------------------
- Introduce power law (uniform) background model, uses uniform background shape.

0.6.1 (2022-05-28):
-------------------
- Minor changes for improved nionui compatibility.

0.6.0 (2021-11-12):
-------------------
- Nion Swift 0.16 compatibility.
- Add measure temperature computation.

0.5.4 (2021-05-26):
-------------------
- Maintenance to reduce dependency on new/unstable niondata features.
- Improve colors for better visibility in align ZLP, live ZLP, live thickness.
- Vectorize thickness mapping for significant speed-up.
- Add calibrate spectrum tool.

0.5.3 (2021-03-12):
-------------------
- Fix issue with Align ZLP (COM) when using it on empty data.
- Fix issue with Align ZLP (COM) that caused a bias towards half-integer shifts.
- Allow Align ZLP to be used on single spectra. Useful for bringing the ZLP to calibrated zero.

0.5.2 (2020-11-13):
-------------------
- Fix issue with single channel zero loss peaks in thickness calculation.
- Ensure default background is power law.
- Improve wording in background menu.

0.5.1 (2020-10-06):
-------------------
- Add exponential functions for two-area method.
- Add two-area background fitting class.
- Improve speed of polynomial background and fix power law.

0.5.0 (2020-08-31):
-------------------
- Rework background models to allow for plug-in models.
- Made Align ZLP output the measured shifts in addition to the aligned spectra.
- Allow graphics to select the ROI for aligning spectra in Align ZLP.
- Allow 2D images in Align ZLP and interpret y-axis as sequence axis.
- Reworked Align ZLP to eliminate duplicate code.

0.4.4 (2019-10-24)
------------------
- Changed shift method in ZLP subpixel align to scipy.ndimage.shift with linear interpolation to get rid of artifacts.

0.4.3 (2019-04-29)
------------------
- Added checks to avoid applying live ZLP and thickness to 2D data items.
- Moved ZLP analysis functions to nion.eels_analysis module for better reuse.

0.4.2 (2019-03-27)
------------------
- Make Align ZLP support sequences AND 1D collections.
- Added menu items for center-of-mass and gaussian fit for ZLP alignment (both do sub-pixel alignment but much faster than cross-correlation)

0.4.1 (2019-01-07)
------------------
- Improve data type handling (do not auto-promote to float64).
- Improve menu item layout.

0.4.0 (2018-12-21)
------------------
- Add menu items for live thickness, thickness mapping, align zlp.

0.3.0 (2018-12-12)
------------------
- Nion Swift 0.14 compatibility.
- Use composite line plot display for display again.

0.2.1 (2018-10-14)
------------------
- Update original background subtraction to not use deprecated composite library item.

0.2.0 (2018-09-28)
------------------
- Add simplified background subtraction.
- Add live ZLP tracking.

0.1.1 (2018-05-12)
------------------
- Initial version online.
