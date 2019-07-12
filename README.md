# aldohonen
This is a simple tool to visualize a Kohonen Network with color training.

Colors represent neurons weight. So, when training with an constant input color set, network learn from this pattern, then self organize to represent this pattern. The more iterations executed, the more the network will look like the input.

# Authors
Luiz Eduardo Pizzinatto

&

Bruno Martins Crocomo

# Execution
```
python Main.py
```

# Examples
Below are shown 4 screenshots from a simple training process.

Starting with a random image, every training step (`activate` and `backward`) turn the network more organized, culminating in organized colors (i.e. organized neurons).

![step 1](/img/a1.png)
![step 2](/img/a2.png)
![step 3](/img/a3.png)
![step 4](/img/a4.png)

# Infos
* `pybrain` works only with `numpy 1.11.0`.
* This is a single thread approach.
