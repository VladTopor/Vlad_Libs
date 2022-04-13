import cona
def test(module_name):
    try:
        exec(f"import {module_name}")
    except ImportError:
        cona.cprint(cona.CROSS+" "+module_name,cona.RED)
    except:
        cona.cprint(cona.CROSS + " " + module_name+", python error", cona.RED)
    else:
        cona.cprint(cona.TICK+" "+module_name,cona.GREEN)
def tests():
    for i in ["algoritms","config","custom_types","databaser","ejson","log"]:
        test(i)
tests()