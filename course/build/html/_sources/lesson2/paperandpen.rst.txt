Uppgifter (på svenska)
======================

#. Givet differentialekvationen

   .. math:: \ddot{x} - (0.1 - \frac{10}{3} \dot{x}^2 ) \dot{x} + x + x^2 = 0

   Inför tillståndsvariablerna :math:`x_1 = x` och :math:`x_2 = \dot{x}`,
   och skriv systemet på tillståndsform. Bestäm de stationära punkterna,
   linjärisera tillståndsmodellen kring dessa och undersök de stationära
   punkternas karaktär. 

#. En variant av Lotka-Voltera modellen är

   .. math::

      \begin{aligned}
         \frac{dx}{dt} & = f(x,y) = bx-xy - ax^2  \\
         \frac{dy}{dt} & = g(x,y) =xy-dy
      \end{aligned}

   Skriv fasportraiter för modellerna (det finns minst två olika ’typ’ av 
   fasportrait), hitta jämviktspunkter och bestäm stabilitet.
   
   #. Undersök SIRS modellen:

  .. math::

     \begin{aligned}
     \frac{dS}{dt} & = & - \beta S I + \alpha R\\
     \frac{dI}{dt} & = & \beta S I  -  \gamma I \\
     \frac{dR}{dt} & = & \gamma I - \alpha R
     \end{aligned}

   Rita en fasporträtt för modellen för fallet :math:`\beta>\gamma`.
   Bestäm ’nullclines’ för modellen. Använd :math:`R=1-S-I` för att
   substituera bort :math:`R` i modellen ovan.
   Hitta jämviktspunkten för systemet. Anta att :math:`\beta=1/5` och
   :math:`\gamma =1/10`. Visa att (oavsett värdet för :math:`\alpha`)
   jämviktspunkten är asymptotiskt stabil.
   
   **Extra utmaning :** Ange villkor för att jämviktspunkten är en stabil spiral.
  
  #. Betrakta systemet

   .. math::

     \dot{x} = \left(
      \begin{array}{c}
      -x_1^3 + u \\ x_1
      \end{array} \right)
   
   Skissa fasplanet för :math:`u = 0`.

#. I processlabben stötte vi på dubbeltankprocessen. I princip kan ett 
   system av olinjära differentialekvationer som beskriver vätskehöjderna i
   tankarna skrivas som

   .. math::

      \begin{aligned}
      \dot{h_1}(t)&=-\frac{a}{A}\sqrt{2 g h_1(t)}+\frac{K_P}{A}u(t)\\
      \dot{h_2}(t)&=\frac{a}{A}\sqrt{2 g h_1(t)}-\frac{a}{A}\sqrt{2 g h_2(t)}
      \end{aligned}

   där :math:`h_1` är vätskehöjden i övre tanken, :math:`h_2` är
   vätskehöjden i undre tanken, :math:`u(t)` är spänningen på den lilla
   motor som pumpar vatten till övre tanken. Övriga variabler är
   konstanter, :math:`a/A` är kvoten mellan bottenhålets area och tankens
   tvärsnittsarea (som vi antar vara samma för båda tankarna),
   :math:`K_P/A` [cm/s/V] är förhållandet mellan en motorkonstant och
   tankarean, och :math:`g` är tyngdaccelerationen :math:`981`
   [cm/s\ :math:`^2`]. I ett lab-experiment har vi erhållit
   :math:`a/A`\ =0.015 och :math:`K_P/A`\ =0.125. Sätter man in dessa
   värden i modellen ovan får man:

   .. math::

      \begin{aligned}
      \dot{h_1}(t)&=-0.06644\sqrt{h_1(t)}+0.125u(t)\\
      \dot{h_2}(t)&=0.0664\sqrt{h_1(t)}-0.0664\sqrt{h_2(t)}
      \end{aligned}

   *  Antag nu att de tillstånd vi väljer är vätskehöjderna i respektive
    tank. Tag fram en linjär modell som beskriver systemet (eg avvikelsen
    från jmv.punkten :math:`x-x_0`) i ett område runt den stationära
    punkt som fås då insignalen u(t) är konstant 2 V, dvs
    :math:`u=u_0=2`.

   * Antag nu att den utsignal vi vill studera är vätskenivåns avvikelse
    från jämviktsläget i den undre tanken (:math:`y-y_0`). Tag fram
    överföringsfunktionen från insignalens avvikelse från jämviktspunkten
    (:math:`u-u_0`) till :math:`y-y_0`. Är systemet stabilt?
