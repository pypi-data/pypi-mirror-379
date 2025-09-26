# Changelog

## v1.0.1

### Fixes
- Add data trace and fresnel calculation now correctly updates the reflectivity figure

## v1.0.0

### Features
- Result summary tab with barplot for fresnel data and data export as .csv now available 
- Included .csv data saving option for all figures and changed to filedialog window for choosing filenames
- Included bulk correction to sensorgram in quantification tab

### Fixes
- Included pywin32 as dependency for Windows platforms (required for command "SPRpy-desktop-shortcut")
- Limited dependency for dash to v2.18.2 as graph changes in dash >= 3.0.0 cause CSS problems with indefinitely growing plots
- Limited dependency for dash-bootstrap-components to v1.7.2 as last compatible release to dash v2.18.2
- Fixed sensor remove logic similarly to removal of fresnel objects
- Added compatibility fix for loading older session versions. NOTE: Will still cause erroneous results in result summary tab if multiple layers were fitted for one sensor object
- Clarified text for batch fresnel modelling options

## v0.2.3

### Fixes
- Fixed build problem with python 3.12

## v0.2.2

### Fixes
- Added support for python 3.12 (still problem with python 3.13.0 due to tkinter issue until patch 3.13.1)
- Added support for latest kaleido version (v0.4.1)

## v0.2.1

### Features
- Added support for using fewer than the maximum number of available logical cores in parallel computing steps. Change "max_logical_cores" in config.toml

### Fixes

- Fixed X-calibration not accounting for scanspeed
- Fixed Y-calibration error for calibration scans with reflectivity above 1.0 
- Moved default X-cal filename to config.toml
- Generalised TIR_determination() to work for any scanspeed (different filtering and fitting for scanspeeds below or above 5)

## v0.2.0

### Features

- Generalised `SPRpy_X_cal.py` and `SPRpy_spr2_to_csv.py` to work with Bionavis instruments with any wavelength setup.
- Added support for 850 nm lasers
- Added batch analysis processing for fresnel modelling
- Added offset and prism extinction fit settings to fresnel modelling and exclusion height determination
- Added automatic angle range detection based on SPR minimum to fresnel modelling (can be tuned in `config.toml`)

### Fixes

- Updated README with accurate documentation
- Updated algorithm in `SPRpy_spr2_to_csv.py` producing more accurate absolute angles (5 mdeg variation between measurements)
- `SPRpy` is now compatible with `numpy 2.0`
- New refractive index values for Cr, Pt
- Changed fresnel algorithm from iterating reflectivity offsets to fitting a reflectivity offset for the whole range

## v0.1.3

### Features

-

### Fixes

- Fixed bug with angle range slider max values
- Fixed bug with renaming sessions

## v0.1.1 

- First working release of `SPRpy`