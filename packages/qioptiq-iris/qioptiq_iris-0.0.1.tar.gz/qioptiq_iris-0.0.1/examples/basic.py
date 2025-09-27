# %%
import logging
logging.basicConfig(level=logging.DEBUG)

import qioptiq_iris as qi
# %%
iris = qi.Iris("COM6", timeout=3, write_timeout=3)
print(iris.power)
iris.on()
# %%
