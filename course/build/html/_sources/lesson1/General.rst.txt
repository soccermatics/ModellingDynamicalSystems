
.. _general1D:

The general case
================

In this section we analyse the general form of 2-player games.

=================== ========= =========
individual/opponent C         D
=================== ========= =========
C                   1         :math:`S`
D                   :math:`T` 0
=================== ========= =========

gives the payoffs for the individuals playing the game. The replicator
equations


  .. math:: \frac{dx}{dt} = x (\mbox{fitness of C - average fitness}) \label{repeq}

can be found by first noting that the fitness of C is

.. math:: 

  x.1+(1-x)S

That is, if a co-operator chooses a person to play the game with at random
then they will choose another co-operator with probability :math:`x` and get payoff 1
and they will choose a defector with probability :math:`1-x` and get payoff :math:`S`.

Likewise, the fitness of D is

.. math:: 
    
  xT+(1-x).0 = xT

The average fitness is then

  .. math:: 
  
    x(x+(1-x)S) + (1-x)xT 

Thus

.. math::
  :label: repeqg

  \begin{aligned}
  \frac{dx}{dt} = f(x) & = & x (x+(1-x)S - x(x+(1-x)(S+T))) \nonumber \\
  & = & x (1-x) (x+(1-x)S - Tx)
  \end{aligned}

is the replicator equation for the general case.

The steady states of equation :eq:`repeqg` are :math:`x_*=0`, :math:`x_*=1` 
and the solution to

.. math:: 
  
  x_*+(1-x_*)S = Tx_*

or

  .. math:: x_* = \frac{S}{S+T-1}

In order for this steady state to lie between 0 and 1 we need either

-  | :math:`T>1` and :math:`S>0`

-  | or :math:`T<1` and :math:`S<0`

We can determine the stability of the three steady states by
differentiating equation :eq:`repeqg` with respect to
:math:`x` we get:

.. math:: 
  f'(x) = x(1-x)(1-S-T) + (1-2x)(x+(1-x)S-Tx)

Evaluating at the steady states we get

.. math:: 
  
  f'(0) = S

so the 0 steady state is stable if :math:`S<0`.

.. math:: 

  f'(1) = T - 1

So the 1 steady state is stable if :math:`T<1`.

.. math::

  \begin{aligned}
  f'\left(\frac{S}{S+T-1}\right) & = & -S (1 - \frac{S}{S+T-1}) \\ 
  & = & \frac{S(T-1)}{1-S-T} 
  \end{aligned}

Thus the co-existence steady state is stable if both :math:`T>1` and
:math:`S>0`, but unstable if :math:`T<1` and :math:`S<0`.

Below we illustrate how the stability is determined in the :math:`ST`
plane.

FIGURE HERE

We now consider some further examples. The prisoners dilemma is

=================== ============= ==============
individual/opponent Keep quiet    Blame other
=================== ============= ==============
Keep quiet          1             :math:`S=-1/4`
Blame other         :math:`T=5/4` 0
=================== ============= ==============

Here :math:`S<0` and :math:`T>1` and the stable strategy is to keep
quiet. Here the situation is very bad for the population as a whole.
The group could do best by all co-operating but by acting rationally
or following natural selection all will defect.

The stag hunt is

=================== ============= ==============
individual/opponent Group         Self
=================== ============= ==============
Group               1             :math:`S=-1/4`
Self                :math:`T=1/2` 0
=================== ============= ==============

thus :math:`S<0` and :math:`T<1`, so all defect and all co-operate are
both stable. The steady state

.. math:: 

  \frac{S}{S+T-1} = \frac{1}{3}

thus if :math:`x(0)>1/3` then all defect, if :math:`x(0)<2/3` then all
co-operate. Stag hunts are hard to establish but when established are
stable to defection.
