.. _hawkdove:

The hawk-dove game
==================

Game theory is used both in biology and in economics to understand how
individuals act when faced with tradeoffs between certain costs and benefits.
Here we look at a competition between two behavioural strategies, one
we call ’co-operate’ the other ’defect’. In general co-operators try
to share resources and defectors try to take resources for
themselves. To illustrate the problem, we construct a payoff table based on the
interactions of co-operators (C) and defectors (D). We assume that when

-  C meets C they both get payoff :math:`1` (reward).

-  D meets D they both get payoff :math:`0` (punishment).

-  C meets D then D gets payoff :math:`T` (temptation), and C gets
   payoff :math:`S` (sucker).

In table form this can be written 

=================== ========= =========
individual/opponent C         D
=================== ========= =========
C                   1         :math:`S`
D                   :math:`T` 0
=================== ========= =========

giving the payoffs for the individual playing the game. 

In this section, we will look at the following example known as the hawk-dove game,

=================== ============= =============
individual/opponent Dove          Hawk
=================== ============= =============
Dove                1             :math:`S=1/4`
Hawk                :math:`T=5/4` 0
=================== ============= =============

In a world full of doves (and no hawks) everyone gets a payoff of 1, while in a world of 
hawks everyone gets zero. But... the best payoff is for hawks who live in a world full of doves, they 
will get payoff 5/4 every time they meet a dove.


Evolutionary game theory considers how a population of individuals following these rules will 
evolve over time. We make the following assumptions:

-  Pairwise contests occur between two individuals.

-  Population is infinite. So every time an individual plays the game against a different person.

-  Those with higher payoffs (fitness) increase in the population. (Darwin’ law of natural selection)


Let :math:`x` be the proportion of the population who co-operate. Let
the **fitness** of an individual be its expected payoff given that
there are :math:`x` co-operators in the population. We assume that the rate of 
increase of co-operators is proportional to their fitness minus average
fitness of both co-operators and defectors.

  .. math:: \frac{dx}{dt} = x (\mbox{fitness of C - average fitness}) \label{repeq}

This is known as the **replicator equation**. 

The fitness of C is

.. math:: 

  x.1+(1-x)\frac{1}{4} = \frac{1}{4} + \frac{3x}{4}

That is, if a co-operator chooses a person to play the game with at random
then they will interact with another co-operator with probability :math:`x` and get payoff 1
and they will interact with a defector with probability :math:`1-x` and get payoff :math:`1/4`.

Likewise, the fitness of  D is

.. math:: 
    
  x.\frac{5}{4} +(1-x).0 = \frac{5}{4} x

The average fitness is then

  .. math:: 
  
    x(\frac{1}{4} + \frac{3x}{4}) + (1-x) \frac{5}{4} x 

i.e. the 

Thus

.. math::
  :label: repeqf

  \frac{dx}{dt} = f(x) = x (1-x) (\frac{1}{4} + \frac{3x}{4} - \frac{5}{4} x ) = \frac{1}{4} x(1-x)(1-2x)

is the replicator equation.


The steady states of equation :eq:`repeqf` are :math:`x_*=0`, :math:`x_*=1` 
or :math:`x_*  = 1/2`.

We can determine the stability of these three steady states by
differentiating equation `[repeqf] <#repeqf>`__ with respect to
:math:`x` to get:

.. math:: 
  f'(x) = \frac{1}{4} \left((1-2x)^2 - 2x(1-x) \right)

Evaluating at the steady states we get

.. math:: 
  
  f'(0) =  f'(1) = 1/4

so the 0 steady state (all defect) and the 1 steady state (all co-operate) are unstable. 
The steady state where there is a balance between co-operation and defect
has

.. math:: 

  f'(1/2) = \frac{1}{4} \left(0 - 2\frac{1}{4}  \right) = - \frac{1}{8} 

so is stable.

The analysis thus reveals that the hawks and doves coexist at a proportion
:math:`1/2`. Note that this is not optimal for the population as a
whole. The mean fitness in this situation is 

.. math::

  1/2(1/2+1/2 \times 1/4)+5/4 \times 1/2\times1/2=5/16+5/16=10/16

If all played Dove the mean fitness would be :math:`1`. In situations like this 
natural selection acts to maximise individual fitness and not group fitness.
