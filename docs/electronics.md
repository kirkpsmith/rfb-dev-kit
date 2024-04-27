# Preparing the power electronics


{{BOM}}

one [potentiostat](pstat.md){cat:tool, qty:1}

one [L298N motor driver](drivers.md){cat:part, qty:1, Note:or equivalent}

one [Arduino UNO R3]{qty:1, Note:or equivalent microcontroller that can output two independent 5V PWM signals and connect to PC over USB serial}

one [PC]{cat:tool, qty:1, Note:Must be able to flash firmware to microcontroller and connect over USB serial to microcontroller and potentiostat}

some [jumper wires]{qty: some}

## Flash firmware to microcontroller {pagestep}

```{.python}
import numpy as np
print('Hello World!')
print('It works with other common languages')
```

## Wire up pump controller {pagestep}

TODO

## Connect microcontroller to PC



