# ig-live
Download videos from instagram live

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

Things you need to install the software and how to install them.

```
pip install git+https://git@github.com/ping/instagram_private_api.git@1.5.7
pip install git+https://git@github.com/ping/instagram_private_api_extensions.git@0.3.8
```

```
pip install git+https://github.com/wright15/ig-live.git
```

### Important steps

Make sure to run the savesettings file first with arguments detailed below.
Run savesettings_logincallback.
```
python examples/savesettings_logincallback.py -u "yyy" -p "zzz" -settings "test_credentials.json"
```

After that you can run your ig-live program only after pointing your definitions
in the ig-live file to your arg.parse arguments defined in the first step as well
as populating commented collections with appropriate data.


## Acknowledgments

* Ping