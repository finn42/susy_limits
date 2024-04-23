# SUSY_limits

I've recieved requests for my opinion on SUSY, or Surrogate Synchrony, as an analysis strategy for synchrony between music-concurrent physiology measurements. In the subsequent discussion with colleagues, I have learned that many folks in this research area are unfamiliar with the math defining SUSY's limitations. Rather than sketch the issues repeatedly over email, I've produced a demonstration notebook to show what kind of information is caught and what kind on information is missed by this method dependent on the average cross-correlation over lags of many seconds. What is demonstrated through these toy and real data examples may be obvious to researchers with any training in signal processing, however that background is a privilege in the interdisciplinary world of music psychology. 

Surrogate Synchrony (SUSY) is a strategy for identifying some shared information in parallel recordings of the same type of signal from people in some interactive context, originally in motion trajectories between people in dialogue (specifically therapy sessions), but it has been applied to many types of measurements taken for people in musical interaction conditions as well. Most recently in used in a Scientic Reports paper (Tschacher, et al., 2023) on physiological and motion measurements of an audience during a classical music concert, it has been applied in similar contexts a few times over without a reconning of how synchronised the shared information must be to be counted (Seibert, et al., 2019; Tschacher, et al., 2019). From my experience with similar measurements and other approaches to shared information in time series, I am very concern that this method is missing much of what readers (and maybe some authors) assume it is capturing in these musical contexts.

The current notebook is only on dyadic SUSY with average non-absolute-valued Fisher's Z transformed cross-correlations, though many of the consequences generalise to the multivariate derivative (M. What I am trying to show is not an opinion about where this technique could be useful, these are the mathematical facts of what kinds of "synchrony" it is capable of assessing. As it stands, there are surely some published false negatives from using this method without sensitivity to what it cannot see. 

If this analysis gives anyone some helpful context for the method, I'm glad the effort did some good. Please don't just take my python implementation of SUSY and ignore these caveats on its application. 

Finn Upham, 2024-01-23
			2024-04-23


References: 

Meier,D., Tschacher,W. Beyond Dyadic Coupling: The Method of Multivariate Surrogate Synchrony (mv-SUSY). Entropy 2021, 23,1385. https://doi.org/10.3390/e23111385

Seibert, C., Greb, F., & Tschacher, W. (2019). Nonverbale synchronie und Musik-Erleben im klassischen Konzert. Jahrbuch Musikpsychologie. Musikpsychologie–Musik und Bewegung, 28, 53-85.

Tschacher, W., Greenwood, S., Egermann, H., Wald-Fuhrmann, M., Czepiel, A., Tröndle, M., & Meier, D. (2021, September 23). Physiological Synchrony in Audiences of Live Concerts. Psychology of Aesthetics, Creativity, and the Arts. Advance online publication. http://dx.doi.org/10.1037/aca0000431

Tschacher, W., Greenwood, S., Ramakrishnan, S., Tröndle, M., Wald-Fuhrmann, M., Seibert, C., ... & Meier, D. (2023). Audience synchronies in live concerts illustrate the embodiment of music experience. Scientific Reports, 13(1), 14843.
https://doi.org/10.1038/s41598-023-41960-2 








