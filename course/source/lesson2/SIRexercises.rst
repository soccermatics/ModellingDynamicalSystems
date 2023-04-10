Modellering av epidemier
========================

I denna uppgift kommer vi att jobba med olika varianter av SIR-modellen.

| **Uppgift 4.1:**
| Simulera (med hjälp av och ) SIR-modellen:

  .. math::

     \begin{aligned}\frac{dS}{dt} & = - \beta S I \\
     \frac{dI}{dt} & = \beta S I -  \gamma I \\
     \frac{dR}{dt} & =  \gamma I 
     \end{aligned}

  Anta att :math:`\gamma=1/7`, :math:`S(0)=999/1000` och
  :math:`I(0)=1/1000`. Testa att simulera med olika smittsamhet
  :math:`\beta=1/3, 1/6, 1/10` och ange slutvärdet för :math:`R`. För
  vilket värde på :math:`\beta` bli det ingen epidemi (dvs för vilket
  värde på :math:`\beta` minskar alltid :math:`I`)? Varför?

| **Uppgift 4.2:**
| Skriv om koden i Matlab för att simulera SEIR modellen (som diskuteras
  i föreläsning 10):

  .. math::

     \begin{aligned}
     \frac{dS}{dt} & = - \beta S I \\
     \frac{dE}{dt} & = \beta S I - \delta E\\
     \frac{dI}{dt} & = \delta E -  \gamma I \\
     \frac{dR}{dt} & =  \gamma I 
     \end{aligned}

  Tillstånd :math:`E` kallas för *exponerad*: personen har fått viruset
  men smittar under en kort period ännu inte andra. Anta att
  :math:`\gamma=1/7` och :math:`\beta=1/5`. Anta att tidsenheten är
  dagar, dvs :math:`\gamma=1/7` betyder att det i snitt tar 7 dagar att
  tillfriskna. Skissa (eller klistra in från Matlab) en graf som plottar
  :math:`I(t)` som en funktion av tiden :math:`t` när man är exponerad
  (:math:`E`) i snitt under 1, 5 respektive 9 dagar innan man blir
  infekterad (:math:`I`). Anta att :math:`S(0)=999/1000`, :math:`E(0)=0`
  och :math:`I(0)=1/1000`. Har :math:`\delta` en stor eller liten effekt
  på slutvärdet för :math:`R`? Förklara ditt svar.

| Hälsomyndigheten bestämmer att införa restriktioner först när 1% av
  befolkning är infekterad. Med restriktioner är :math:`\beta=1/15` men
  utan restriktioner är :math:`\beta=1/5`. Undersök konsekvenser av
  detta beslut för olika värden på :math:`\delta`, dvs simulera
  spridning först under antagandet att :math:`\beta=1/5` och när
  :math:`I(0)=0.01` ändra smittsamheten till :math:`\beta=1/15`. Skissa
  :math:`R(t)` för olika :math:`\delta`-värden och beskriv hur
  :math:`\delta` påverkar utfallet.
| **Tips:** Använd

::

   ind = find(X(:,3)>=0.01);
   onepercent=ind(1);

för att hitta tidpunkten, :math:`t`, då :math:`I(t)=0.01`.

| **Uppgift 4.3 :**
| Undersök nu SIRS modellen:

  .. math::

     \begin{aligned}
     \frac{dS}{dt} & = - \beta S I + \alpha R\\
     \frac{dI}{dt} & = \beta S I  -  \gamma I \\
     \frac{dR}{dt} & =  \gamma I - \alpha R
     \end{aligned}

  Rita en fasporträtt för modellen för fallet :math:`\beta>\gamma`.
  Bestäm ’nullclines’ för modellen. Använd :math:`R=1-S-I` för att
  substituera bort :math:`R` i modellen ovan.

Hitta jämviktspunkten för systemet. Anta att :math:`\beta=1/5` och
:math:`\gamma =1/10`. Visa att (oavsett värdet för :math:`\alpha`)
jämviktspunkten är asymptotiskt stabil.

Skissa (eller klistra in från Matlab) en graf som plottar :math:`I(t)`
som en funktion av tiden :math:`t` för två olika fall - när
:math:`\alpha=1/100` respektive :math:`\alpha=1/4`. I vilket fall finns
det en ’andra våg’?

**Extra utmaning :** (bara om du tycker att det intressant) Ange villkor
för att jämviktspunkten är en stabil spiral.
