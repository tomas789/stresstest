# stresstest

## Usage

```
$ python -m stresstest
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Test name                                                          ┃ Duration ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ interpreter / dict_class / CreateLargeDictionaryFromListStresstest │ 0.113092 │
│ interpreter / dict_class / DictionaryRandomAccessStresstest        │ 0.198488 │
│ interpreter / dict_class / DictionarySequentialAccessStresstest    │ 0.086654 │
│ interpreter / random_module / RandomIntegerGeneratorStresstest     │ 0.017334 │
│ interpreter / random_module / RandomNumberGeneratorStresstest      │ 0.001902 │
│ interpreter / random_module / SortIntegersStresstest               │ 0.068338 │
│ compute / pi_digits / CalculatePiDigitsStresstest                  │ 0.905477 │
│ compute / pi_digits / PiDigitsMonteCarloStresstest                 │ 1.317290 │
│ compute / hashlib / Sha1Stresstest                                 │ 0.158356 │
│ compute / hashlib / Sha224Stresstest                               │ 0.157216 │
│ compute / hashlib / Sha256Stresstest                               │ 0.154774 │
│ compute / hashlib / Sha384Stresstest                               │ 0.164426 │
│ compute / hashlib / Sha512Stresstest                               │ 0.158992 │
│ compute / hashlib / Sha3Stresstest                                 │ 0.162025 │
│ compute / factorization / FactorizeNNumbersStresstest              │ 0.368712 │
│ compute / n_body / NBodySimulationPurePythonStresstest             │ 2.067632 │
└────────────────────────────────────────────────────────────────────┴──────────┘
Collected data will be sent to server in 3 seconds (use --dont-send to avoid this) ...
Collected data successfully sent to server with collection ID:
dcad44f4c74531ed752655ab8e305317a897defb3ce9538cfb8a4c396d49c2f1
```

## Requirements

Python 3.7 or newer. All other dependencies will be installed during the installation process by PIP itself.

## Installation

You can install this package as you'd do with any other Python package. The easiest way is to use PIP.

```
pip install stresstest
```

If Python 2.x is your default Python version (check with `python --version`) you can use Python 3 specifically.

```
python3 -m pip install stresstest
```

Or you can install the package directly from source code

```
git clone https://github.com/tomas789/stresstest.git
cd stresstest
python setup.py install
```

Or let PIP do the clone for you

```
pip install git+https://github.com/tomas789/stresstest.git
```
