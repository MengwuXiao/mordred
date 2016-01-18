import conf
from mordred import all_descriptors, get_descriptors_from_module

prelude = '''
Descriptor List
===============
preset descriptors

.. code:: python

    calc = Calculator(all_descriptors())

.. csv-table:: Descriptor list
    :header: "#", "module", "name", "constructor"
    :widths: 10, 25, 25, 40

'''[1:]


def main(out):
    out.write(prelude)
    
    i = 0

    for mdl in all_descriptors():
        for Desc in get_descriptors_from_module(mdl):
            for desc in Desc.preset():
                i += 1

                if mdl:
                    mdl_name = '.'.join(mdl.__name__.split('.')[1:])
                    mdl = None
                else:
                    mdl_name = ''

                out.write('    {}, {}, {}, "{!r}"\n'.format(i, mdl_name, desc, desc))


if __name__ == '__main__':
    import sys
    main(sys.stdout)
