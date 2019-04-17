- Install the Natural Language Toolkit: `conda install nltk`
- Install textblob. Try this command first:

`conda install -c conda-forge textblob`

**Explanation:** The `conda` command-line tool comes with the Anaconda Python distribution. It helps manage dependencies for data science packages. `conda-forge` is a package repository. `textblob` is a package for natural language processing. The command above uses `conda` to download `textblob` from `conda-forge` and install it locally.

If that command does not work, try this one instead:

`pip install textblob`

**Explanation:** `pip` is a general tool for installing Python packages and managing dependencies. It is generally not as good as `conda` for managing data science dependencies, but it covers more packages. Usually when installing a new data science package I  first try `conda` without `-c conda-forge`. If that doesn't, then I try `conda` with that flag. Finally, I fall back to `pip`. If the package is not particularly related to data science, then I go straight to `pip`.

- Install some data for use with `textblob`:

`python -m textblob.download_corpora lite`
