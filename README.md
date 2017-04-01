# proxy_checker
A python multithread proxy checker script

# Usage

## activate online proxy finder

scrape www.freeproxylists.com for free proxy lists by just running this (this will scrap FR proxies only)

```python
python app.py
```

## read proxies from local file

you have to change the following in the app.py file

```python
    #proxyfinder = ProxyFinder()
    #hosts = proxyfinder.find()

    """
    read proxies from file
    """
    hosts = [host.strip() for host in open(input_file).readlines()]
```
here we have commented the ProxyFinder class and its method find. then we commentend the in file reader. and finally, run :

```python
python app.py
```


Enjoy !
