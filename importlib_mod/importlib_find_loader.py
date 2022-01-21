import importlib

spec = importlib.util.find_spec('example')
print('Loader:', spec.loader)

m = spec.loader.load_module()
print('Module:', m)
