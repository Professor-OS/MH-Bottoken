import glob
from pathlib import Path
from Professor.utils import load_plugins
import logging
from . import PROFESSOR, PROFESSOR2, PROFESSOR3, PROFESSOR5 , PROFESSOR6, PROFESSOR7, PROFESSOR8, PROFESSOR9, PROFESSOR10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "Professor/Agora/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Ab ki baar AGORA Sir k sarkar")
print("Congratulations")

if __name__ == "__main__":
    PROFESSOR.run_until_disconnected()
    
if __name__ == "__main__":
    PROFESSOR2.run_until_disconnected()

if __name__ == "__main__":
    PROFESSOR3.run_until_disconnected()
    
if __name__ == "__main__":
    PROFESSOR4.run_until_disconnected()

if __name__ == "__main__":
    PROFESSOR5.run_until_disconnected()
    
if __name__ == "__main__":
    PROFESSOR6.run_until_disconnected()

if __name__ == "__main__":
    PROFESSOR7.run_until_disconnected()
    
if __name__ == "__main__":
    PROFESSOR8.run_until_disconnected()

if __name__ == "__main__":
    PROFESSOR9.run_until_disconnected()
    
if __name__ == "__main__":
    PROFESSOR10.run_until_disconnected()
