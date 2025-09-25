This package fits several different **Network Scale-Up Models (NSUM)** to **Aggregated Relational Data (ARD)**. ARD represents survey responses to questions of the form: *"How many X’s do you know?"*, where respondents report how many people they know in different subpopulations.

Specifically, if Nᵢ respondents are asked about Nₖ subpopulations, then the ARD is an Nᵢ times Nₖ matrix, where the *(i, j)* element represents how many people respondent *i* reports knowing in subpopulation *j*.

NSUM leverages these responses to estimate the unknown size of **hard-to-reach populations**.

In this package, we provide functions to estimate the size and accompanying parameters (e.g. degrees) from 2 papers:  


Killworth, P. D., Johnsen, E. C., McCarty, C., Shelley, G. A., and Bernard, H. R. (1998) plug-in MLE  


Killworth, P. D., McCarty, C., Bernard, H. R., Shelley, G. A., and Johnsen, E. C. (1998) MLE  



## Requirements

This package requires the following Python libraries:
- `numpy` 
- `pandas`

## PIMLE

The plug-in MLE (PIMLE) estimator from Killworth, P. D., Johnsen, E. C., McCarty, C., Shelley, G. A., and Bernard, H. R. (1998) 
is a two-stage estimator that first estimates the degrees for each respondent dᵢ by maximizing the following likelihood for each respondent:
<div align="center">
 <i><strong>L(dᵢ; y, {Nₖ}) = ∏ₖ₌₁ᴸ [ (⁽ᵈⁱ⁾⁄₍ʸⁱₖ₎) × (Nₖ / N)<sup>yᵢₖ</sup> × (1 − Nₖ / N)<sup>dᵢ − yᵢₖ</sup> ],</strong></i>
</div>

Where: *L* is the number of 
subpopulations with known sizes *Nₖ*. *yᵢₖ* is the number of people respondent *i* reports knowing in subpopulation *k*. *(⁽ᵈⁱ⁾⁄₍ʸⁱₖ₎)* is the binomial coefficient. 
In the second stage, the model plugs in the estimated *dᵢ* into the equation: 
<div align="center">
<i><strong>yᵢₖ / dᵢ = Nₖ / N </strong></i>
</div>
and solves for the unknown *Nₖ* for each respondent.  
These estimates are then averaged to obtain a single estimate of *Nₖ*.   

To summarize, Stage 1 estimates *dᵢ* using: 

<div align="center"><i><strong>dᵢ = N × (∑ₖ₌₁ᴸ yᵢₖ) / (∑ₖ₌₁ᴸ Nₖ)</strong></i>
</div>

 Stage 2 estimates 
the unknown subpopulation size *Nₖ* with:

<div align="center"><i><strong> N̂ₖᴾᴵᴹᴸᴱ = (N / n) × ∑ᵢ₌₁ⁿ (yᵢₖ / dᵢ)</strong></i>
</div>

Here is an example of this package creating an estimate using the PIMLE function:

<p><code>pimle.est = killworth(ard,
  known_sizes = sizes[c(1, 2, 4)],
  known_ind = c(1, 2, 4),
  N = N, model = "PIMLE")</code></p>

Note that the function will provide a warning saying that at least *dᵢ*
 was 0. This occurs when a respondent does not resport knowing anyone in the known subpopulations. This is an issue for the PIMLE since a 0 value is in the denominator for N̂ᵤᴾᴵᴹᴸᴱ
. Thus, we ignore the responses from respondents that correspond to *dᵢ* =0
.

## MLE

Next, we analyze the data from the Killworth, P. D., McCarty, C., Bernard, H. R., Shelley, G. A., and Johnsen, E. C. (1998) MLE estimator. This is also a two-stage model, which an identical first stage, i.e.

<div align="center"><i><strong>d̂ⁱ = N̂ ⋅ (∑ₖ₌₁ᴸ yᵢₖ) / (∑ₖ₌₁ᴸ Nₖ)</strong></i>
</div>

However, the second stage estimates Nₖ
 by maximizing the Binomial likelihood with respect to Nₖ
, fixing *dᵢ*
 at the estimated *d̂ᵢ*
. Thus, the estimate for the unknown subpopulation size is given by

<div align="center"><i><strong>N̂⁽ᴹᴸᴱ⁾ₖ = N ⋅ (∑ᵢ₌₁ⁿ yᵢₖ) / (∑ᵢ₌₁ⁿ d̂ᵢ)</strong></i>
</div>

For example, the estimate can be obtained using:

<p><code>mle.est = killworth(ard,
  known_sizes = sizes[c(1, 2, 4)],
  known_ind = c(1, 2, 4),
  N = N, model = "MLE")</code></p>

Note that this function will not create a warning for a *dᵢ* =0 value since the denominator depends on the summation of d̂ᵢ.
