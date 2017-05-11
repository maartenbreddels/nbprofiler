# nbprofiler
Profiler extension for Jupyter notebook to profile the notebook server itself

# Installation
```
$ git clone https://github.com/maartenbreddels/nbprofiler
$ cd nbprofiler
$ pip install -v -e .
```

# Usage
Start jupyter with the extension
```
$ jupyter-notebook  --NotebookApp.server_extensions="['nbprofiler.ext']" 
```

Start the profiler
```
$ curl localhost:8888/profiler/start
```

Stop the profiler
```
$ curl localhost:8888/profiler/stop
```

Report
```
$ curl localhost:8888/profiler/report
$ curl localhost:8888/profiler/report/cumtime
$ curl localhost:8888/profiler/report/tottime
```

# Documentation
[Use the source Luke!](https://github.com/maartenbreddels/nbprofiler/nbprofiler/ext.py) and google cProfile.



