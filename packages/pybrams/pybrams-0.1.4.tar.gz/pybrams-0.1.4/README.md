# PyBRAMS

**PyBRAMS** is a Python package that allows you to access information and data from the BRAMS (Belgian RAdio Meteor Stations) project.

BRAMS is a network of radar receiving stations that use forward scattering techniques to study the meteoroid population.

This project, coordinated by the Belgian Institute for Space Aeronomy (BIRA-IASB), provides a valuable source of data for space operators, research scientists and amateur astronomers.

# Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-line tool](#command-line-tool)
    - [Available commands](#available-commands)
      - [get](#get)
      - [cache](#cache)
      - [config](#config)
      - [spectrogram](#spectrogram)
      - [wavinfo](#wavinfo)
      - [trajectory](#trajectory)
      - [cams](#cams)
      - [availability](#availability)
      - [psd](#psd)
- [Notebooks](#notebooks)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetch detailed information about BRAMS stations, including their location, name, number of antennas, and more.
- Retrieve raw data files in WAV format, which can be used for in-depth analysis of meteoroid activity.
- Access PNG images representing spectrograms, making it easy to visualize meteoroid detections.
- Compute trajectories, speeds and their associated uncertainties.
- Allow validation of results with optical data.

## Installation

We recommend installing **PyBRAMS** using [uv](https://docs.astral.sh/uv/),
which makes the installation in an isolated virtual environment to prevent conflicts with system-wide packages:

```bash
uv venv
uv pip install pybrams
```

To use **PyBRAMS**, you then need to activate the virtual environment.

On Unix-like systems :

```bash
source .venv/bin/activate
```

On Windows (Powershell)

```Powershell
.venv\Scripts\Activate.ps1
```

On Windows (CMD)

```bat
.venv\Scripts\Activate.bat
```

## Usage

This library can be used in two ways:

- As a command-line tool  for quick execution.
- As a Python module for integration into custom scripts.

### Command-line tool

The library provides an executable script called `pybrams`, which can be run from the terminal :

```bash
pybrams [options] [command]
```

#### Available options

##### --verbose

Some commands may take a significant amount of time to execute. The --verbose option provides detailed output and displays real-time progress.

#### Available commands

##### location

The `location list` command displays a table of all available BRAMS locations.

```bash
$ pybrams location list
            BRAMS locations             
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Location code ┃     Display name     ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│    BEBILZ     │        Bilzen        │
│    BEBOEC     │       Boechout       │
│    BEBROE     │       Broechem       │
│    BEDINA     │        Dinant        │
│    BEECON     │       Ecotron        │
│    BEFRAM     │      Frameries       │
│    BEGAVE     │        Gavere        │
│    BEGEMB     │        Gembes        │
│    BEGENK     │         Genk         │
│    BEGENT     │         Gent         │
│    BEGRIM     │      Grimbergen      │
│    [ ...]     │        [ ...]        │
└───────────────┴──────────────────────┘
```

##### system

The `system list` command displays a table of all available BRAMS systems.

```bash
$ pybrams system list
            BRAMS systems
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃  System code  ┃     Display name     ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ BEBILZ_SYS001 │        Bilzen        │
│ BEBOEC_SYS001 │       Boechout       │
│ BEBROE_SYS001 │       Broechem       │
│ BEDINA_SYS001 │        Dinant        │
│ BEECON_SYS001 │      Ecotron 1       │
│ BEECON_SYS002 │      Ecotron 2       │
│ BEECON_SYS003 │      Ecotron 3       │
│ BEECON_SYS004 │      Ecotron 4       │
│ BEECON_SYS005 │      Ecotron 5       │
│ BEFRAM_SYS001 │      Frameries       │
│ BEGAVE_SYS001 │        Gavere        │
│    [ ...]     │        [ ...]        │
└───────────────┴──────────────────────┘
```

##### get

The `get` command fetches BRAMS files in WAV format and saves them in the current working directory.

```bash
pybrams get INTERVAL [SYSTEMS...]
```

The  INTERVAL argument  must be in one of the following format :

- a single datetime  in ISO 8601 format :

```bash
pybrams get 2025-01-01T03:05
```

- a datetime interval using ISO 8601 format, separated by / :

 ```bash
pybrams get 2025-02-12T03:03/2025-02-12T03:17
```

You can also provide one or multiple system codes to only fetch files from specific BRAMS system(s) :

```bash
pybrams get 2025-03-15T12:00 BESAFF_SYS001 BEHUMA_SYS001
```

##### cache

PyBRAMS uses a caching system to store metadata, WAV files and result files in a local directory.
This improve performance by avoiding redundant calls to the BRAMS API and computations.

The `cache` commands allow the user to manage this cache by :

- checking the current status of the cache

```bash
$ pybrams cache status
Cache is enabled
```

- enabling or disabling the cache

```bash
$ pybrams cache disable
Cache is disabled
$ pybrams cache enable
Cache is enabled
```

- clearing the cache

```bash
$ pybrams cache clear
Cache was cleared
```

- get information about the cache

```bash
$ pybrams cache info
Number of files : 385
Total size : 1811688538 B
Total size : 1769227.09 KB
Total size : 1727.76 MB
```

##### config

PyBRAMS uses a global configuration file to manage settings.
The config command allows users to view the current configuration or copy it to the current working directory for customization.

To display the global configuration used by PyBRAMS, run :

```bash
$ pybrams config show
PyBRAMS Configuration
└── pybrams
    ├── brams
    │   ├── adsb
    │   │   └── api_endpoint
    │   │       └── 'adsb.php'
    │   ├── fetch
    │   │   ├── api
    │   │   │   └── base_url
    │   │   │       └── 'https://brams.aeronomie.be/v1/'
    │   │   └── archive
    │   │       └── base_path
    │   │           └── '/bira-iasb/data/GROUNDBASED/BRAMS/wav'
    │   ├── file
    │   │   └── api_endpoint
    │   │       └── 'file.php'
    │   ├── location
    │   │   └── api_endpoint
    │   │       └── 'location.php'
    │   └── system
    │       └── api_endpoint
    │           └── 'system.php'
    ├── event
    │   └── meteor
    │       ├── identification_half_range_frequency
    │       │   └── 100
    │       ├── filtering_half_range_frequency
    │       │   └── 300
    │       ├── filtering_length_kernel
    │       │   └── 2501
    [...]
```

If you want to modify the settings, you can copy the global configuration file to the current working directory by running :

```bash
pybrams config copy
```

This creates a pybrams.json file in the current working directory, which you can edit to override the default settings.
When present, this file takes precedence over the global configuration.

You can also get or set a single entry from the global configuration by using these subcommands :

```bash
$ pybrams config get pybrams.processing.signal calibrator_subtraction
False
$ pybrams config set pybrams.processing.signal airplane_subtraction True
```

If you need to restore the default global configuration, you can use this command :

```bash
pybrams config restore
```

##### spectrogram

The `spectrogram` command generates spectrograms from WAV files found in the current working directory or in the path specified by the user.

```bash
$ ls -1 *.wav
RAD_BEDOUR_20240729_2305_BESAFF_SYS001.wav
RAD_BEDOUR_20240729_2310_BESAFF_SYS001.wav
RAD_BEDOUR_20240729_2315_BESAFF_SYS001.wav
RAD_BEDOUR_20240729_2320_BESAFF_SYS001.wav
RAD_BEDOUR_20240729_2325_BESAFF_SYS001.wav
$ pybrams spectrogram
RAD_BEDOUR_20240729_2310_BESAFF_SYS001.png
RAD_BEDOUR_20240729_2305_BESAFF_SYS001.png
RAD_BEDOUR_20240729_2315_BESAFF_SYS001.png
RAD_BEDOUR_20240729_2320_BESAFF_SYS001.png
RAD_BEDOUR_20240729_2325_BESAFF_SYS001.png
```

##### wavinfo

The `wavinfo` command displays information about the WAV file provided by the user.

By default, the command displays information found in the header of the file :

```bash
$ pybrams wavinfo RAD_BEDOUR_20240729_2310_BESAFF_SYS001.wav
Header
Version : 4
Samplerate : 6048.0 Hz
LO frequency : 49969000.0 Hz
Start (us) : 1722294600326662
PPS count : 1800
Beacon latitude : 50.097526
Beacon longitude : 4.588525
Beacon altitude : 273.3 m
Beacon frequency : 49970000.0 Hz
Beacon power : 84.9
Beacon polarization : 3
Antenna ID : 1
Antenna latitude : 50.784132
Antenna longitude : 5.233545
Antenna altitude : 1
Antenna azimuth : 1
Antenna elevation : 1
Beacon code : BEDOUR
Observer code : 
Station code : BESAFF
Description : Calclock
```

##### trajectory

The `trajectory` command retrieves meteoroid trajectories using times of flight and phase information. It can be called with the brams subcommand and a corresponding datetime interval:

```bash
pybrams trajectory brams 2020-07-29T23:36:27/2020-07-29T23:36:32
```

You can also provide a CAMS-BeNeLux date and trajectory number.
You can list all available CAMS trajectories using the `cams` command.

```bash
pybrams trajectory cams 2020-07-29 79
```

Both these subcommands can be complemented with options:

- `--recompute_meteors` to reprocess meteor data even if it is already cached.
- `--recompute_trajectory` to redetermine the best trajectory even if it is already cached.
- `--uncertainty` to perform a MCMC uncertainty quantification on the solution, based on [Kastinen and Kero (2022)](https://academic.oup.com/mnras/article/517/3/3974/6726639).

An example call to the `trajectory` command is then finally:

```bash
pybrams --verbose trajectory cams 2020-07-30 188 --uncertainty
```

##### cams

The `cams list` command dispalys all available CAMS trajectories.

```bash
$ pybrams cams list
               CAMS trajectories               
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Trajectory ┃ Observed Date ┃ Reference Time ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│     79     │  2020-07-29   │  23:14:00.43   │
│    105     │  2020-07-29   │  23:36:27.99   │
│    188     │  2020-07-30   │  00:51:27.48   │
│    477     │  2020-07-30   │  22:07:59.00   │
│    532     │  2020-07-30   │  23:03:22.61   │
│     92     │  2022-03-23   │  00:44:00.38   │
│     39     │  2022-04-27   │  22:28:04.86   │
│     49     │  2022-04-27   │  23:07:25.39   │
│     57     │  2025-01-31   │  20:33:55.47   │
│    166     │  2025-01-31   │  23:36:28.45   │
└────────────┴───────────────┴────────────────┘
```

##### availability

The `availability` command retrieves information about the availability of BRAMS or ADS-B data. It can be called with the brams or adsb subcommand and a corresponding datetime interval:

```bash
$ pybrams availability adsb 2025-06-01/2025-06-09
  Availability from 2025-06-01  
  00:00:00+00:00 to 2025-06-09  
         00:00:00+00:00         
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ ADSB Receiver ┃ Availability ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ BEUCCL        │ ████████     │
└───────────────┴──────────────┘
$ pybrams availability brams 2025-06-01/2025-06-03
     Availability from 2025-06-01 00:00:00+00:00 to 2025-06-03      
                           00:00:00+00:00                           
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ System        ┃ Availability                                     ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BEBILZ_SYS001 │ ████████████████████████████████████████████████ │
├───────────────┼──────────────────────────────────────────────────┤
│ LUKIRC_SYS001 │ ████████████████████████████████████████████████ │
├───────────────┼──────────────────────────────────────────────────┤
│ NLMAAS_SYS001 │ ████████████████████████████████████████████████ │
└───────────────┴──────────────────────────────────────────────────┘
[ ... ]

```

##### psd

The `psd` command computes the calibrator or noise power spectral density for
files in a datetime interval and for the specified system(s) :

 ```bash
$ pybrams psd calibrator 2025-08-01/2025-08-10 BEMAAM_SYS001
                            Calibrator PSD                             
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                    File                    ┃          PSD           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ RAD_BEDOUR_20250731_2355_BEMAAM_SYS001.wav │ 2.304543733506049e-08  │
│ RAD_BEDOUR_20250801_0000_BEMAAM_SYS001.wav │ 2.3073969355195496e-08 │
│ RAD_BEDOUR_20250801_0005_BEMAAM_SYS001.wav │ 2.3108002900549175e-08 │
│ RAD_BEDOUR_20250801_0010_BEMAAM_SYS001.wav │ 2.3149156546909356e-08 │
└────────────────────────────────────────────┴────────────────────────┘
```

&nbsp;
***

For more information about a specific command and available arguments, run :

```bash
pybrams COMMAND --help
```

## Notebooks

This repository includes two Jupyter notebooks that showcase the usage of **PyBRAMS**:

1. **Get Brams Data Notebook** ([get_brams_data.ipynb](./notebooks/get_brams_data.ipynb)):
   - Retrieves BRAMS data corresponding to a user-defined time interval or to a CAMS-BeNeLux event.
   - Outputs spectrograms, time series and amplitude curves.

2. **Reconstruct Trajectory Notebook** ([reconstruct_trajectory.ipynb](./notebooks/reconstruct_trajectory.ipynb)):
   - Focuses on reconstructing meteor trajectories from observational radar data, similar to the `trajectory` command.
   - Compares the results with optical data from CAMS-BeNeLux.

These notebooks serve as practical examples and are a good starting point for new implementations.

**Note**: Both notebooks require `ipykernel` and `ipympl` packages.

## Contributing

Contributions and feedback are welcome !

## License

This package is licensed under the MIT License. Feel free to use and modify it as needed.
