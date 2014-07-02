import os
import sys

requirements = [
    ('numpy', '1.8.1'),
    ('pandas', '0.14.0'),
    ('sklearn', '0.14'),
    ('scipy', '0.14.0'),
    ('matplotlib', '1.3.1'),
    ('IPython', '2.1.0'),
]

# Check that module requirements are met

if sys.version_info[:2] not in [(2, 7), (3, 4)]:
    print("\nWarning: Materials tested with python2.7 and python3.4")

number_errors = [0]
number_warnings = [0]

def try_import(package_name, suggested_version):
    try:
        module = __import__(package_name)
    except ImportError:
        print("\nError: Couldn't import %s" % package_name)
        number_errors[0] += 1
    else:
        if module.__version__ < suggested_version:
            print("\nWarning: Tutorial tested with %s=%s" %(package_name, suggested_version))
            print("You have %s=%s" %(package_name, module.__version__))
            number_warnings[0] += 1

[try_import(package_name, suggested_version) for package_name, suggested_version in requirements]

print("\nCompleted requirements check with %d errors and %d warnings"
      % (number_errors[0], number_warnings[0]))

# Make sure an IPython notebook is available

try:
    import IPython.html.notebookapp
except ImportError:
    print("\nERROR: You can't seem to start up an IPython notebook")
else:
    print("\nExcellent, you have notebook capabilities")

# Try loading data

try:
    import bird_data
except ImportError:
    print("\nError: Couldn't load data module for tutorial. Are you in the birds_scipy2014 folder?")
except:
    print("\nSomething went wrong with data loading. Please email the traceback to mattwescott@gmail.com")
    raise

# Print a row of data

try:
    print("")
    print(bird_data.call_df.iloc[27])
    print("\nSuccessfully loaded the data")
except:
    print("\nSomething went wrong with the loaded data. Please email the traceback to mattwescott@gmail.com")
    raise

