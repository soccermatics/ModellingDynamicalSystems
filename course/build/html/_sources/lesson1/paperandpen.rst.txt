Uppgifter (på svenska)
======================

#. Undersöker följande replicator ekvationen

   .. math::

      \begin{aligned}
      \dot{x}(t) & = &  x(t) (1-x(t)) (1/4 - 1/2 x(t)) 
     \label{repeqf}
     \end{aligned}

   Hitta alla jämviktspunkter och använder linjärisering för att bestäm stabilitet. Har modellen dynamik som
   mest likna prisoners dilemna, stag hunt eller hawk-dove?



#. SI modellen av en epidemi har följande tillståndsform

   .. math::

      \frac{dS}{dt}  =  - \beta S I +  \gamma I 

   Antar att :math:`\beta=1/3`, :math:`\gamma=1/6` och :math:`S+I=1`.

   * Visa att det finns en jämviktspunkt där :math:`S_*=I_* = 1/2`

   * Bestäm stabiliteten av jämviktspunkten.

   * Om :math:`\beta=1/3` för vilket värde av :math:`\gamma` är jämviktspunkten där :math:`S_* = 1` stabil?



#. Följande tillstånds model beskriver tillväxt av fisk bestånd i en sjö,
   där :math:`x(t)` är tusentals fisk i sjön.

   .. math::

      \begin{aligned}
        \frac{d}{dt}x(t) = r x(t)(1- x(t)) + c 
      \end{aligned}

   där :math:`c>0` är inflödet av nya fisk (från en närliggande sjö) och
   :math:`r>0` är tillväxthastighet. 

   * Hitta alla jämviktspunkter :math:`x_*` till ekvationen och beräkna stabiliteten. 

   * Hur många fisk finns i sjön när :math:`t \rightarrow \infty` om modellen stämmer?



#. När det finns minst :math:`F = 100` fisk i sjön utförs fisketillstånd
   så att turister får kommer dit och fiskar. Sjömyndigheten har kommit
   fram till att följande model gäller i detta fall.

   .. math::

      \begin{aligned}
        \frac{d}{dt}x(t) = f(x) = r x(t)(1- x(t)) + c - b \frac{x^3}{F^3 + x^3}
      \end{aligned}

   De skatar parameter :math:`r`, :math:`b`, :math:`c` och :math:`F` och
   skissa funktionen, :math:`f(x)`, nedan.

   .. image:: ../images/lesson1/fisk.png
      :width: 400

   Hur många jämviktspunkter har :math:`f(x)`? Hur många är stabila? Hur
   kan man tolka modellen när det gäller långsiktig fisk beståndet i
   sjön?

   **Obs:** Använd grafen att lösa problemet! Du behöver inte lösa
   ekvationen.


