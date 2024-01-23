# susy_limits

I keep getting asked my opinion on SUSY as an analysis strategy for synchrony between music-concurrent physiology measurements and in the subsequent discussion have learned that many folks in this research area are unfamiliar with the math defining its limitations. Rather than repeat myself over many emails, I've produced a demonstration notebook to show what kind of information is caught and what kind on information is missed by this methode dependent on the average cross-correlation over lags of many seconds. What is demonstrated through these toy and real data examples may be obvious to researchers with any training in signal processing, however that background is a privilege in the interdisciplinary world of music psychology. 

The current notebook is only on dyadic SUSY with average non-absolute-valued Fisher's Z transformed cross-correlations. What I am trying to show is not an opinion about where this technique could be useful but the mathematical facts of what kinds of "synchrony" it can reliably assess. As it stands, there are surely some published false negatives from using this method without sensitivity to what it cannot see. 

If this analysis gaves anyone some helpful context for the method, I'm glad the effort did some good. Please don't just take my python implementation of SUSY and ignore these caveats on it's application. 

Finn Upham, 2024-01-23