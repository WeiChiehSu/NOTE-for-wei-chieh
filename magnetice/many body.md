$$
\widehat{H}_{electron}= -\sum_{i=1}^{n} \frac{\nabla^{2} _{r_{i}  }  } {2} +\sum_{i=1 }^{n} \sum_{j>i }^{n} \frac{1 }{r_{ij}}+ \sum_{i=1 }^{n} \sum_{a=1 }^{k} \frac{Z_{a} }{r_{ia}}
$$

$$
\widehat{H}\Psi_{i}  (r_{1}\sigma _{1},r_{2}\sigma _{2}...r_{N}\sigma _{N})=\varepsilon_{i} \Psi_{i}(r_{1}\sigma _{1},r_{2}\sigma _{2}...r_{N}\sigma _{N})
$$

$$
Difficult:\sum_{i=1 }^{n} \sum_{j>i }^{n} \frac{1 }{r_{ij}}\Longrightarrow \Psi_{i}  (r_{1}\sigma _{1},r_{2}\sigma _{2}...r_{N}\sigma _{N})\ne \phi_{1} (r_{1}\sigma _{1})\phi_{2} (r_{2}\sigma _{2})...\phi_{N} (r_{N}\sigma _{N})(many-body \to single-electron)
$$

# no electron-electron interaction

$$
\widehat{H}=h_{1}(1)+ h_{2}(2):h_{1}\to electron_{1} ;h_{2}\to electron_{2}
$$

$$
h_{1}(1)\phi _{1}(1)=\varepsilon_{1}\phi _{1}(1),h_{2}(2)\phi _{2}(2)=\varepsilon_{2}\phi _{2}(2)
$$

$$
\psi=\phi _{1}(1)\phi _{2}(2)\Longrightarrow \widehat{H}\psi=[h_{1}(1)+h_{2}(2)][\phi _{1}(1)\phi _{2}(2)]
$$

$$
\widehat{H}\psi=h_{1}(1)\phi _{1}(1)\phi _{2}(2)+h_{2}(2)\phi _{1}(1)\phi _{2}(2)\Longrightarrow \widehat{H}\psi=\varepsilon _{1}\phi _{1}(1)\phi _{2}(2)+\varepsilon _{2}\phi _{1}(1)\phi _{2}(2)
$$

$$
\widehat{H}\psi =(\varepsilon _{1}+ \varepsilon _{2})\phi _{1}(1)\phi _{2}(2)\Longrightarrow wave{}fuction{}can{}separate
$$

# have electron-electron interaction

$$
\widehat{H}=h_{1}(1)+ h_{2}(2)+\frac{1}{\left | r_{1}-r_{2}\right | } 
$$

$$
\widehat{H}\psi=[h_{1}(1)+h_{2}(2)+\frac{1}{\left | r_{1}-r_{2}\right | }][\phi _{1}(1)\phi _{2}(2)]
$$

$$
\widehat{H}\psi=\varepsilon _{1}\phi _{1}(1)\phi _{2}(2)+\varepsilon _{2}\phi _{1}(1)\phi _{2}(2)+\frac{1}{\left | r_{1}-r_{2}\right | }\phi _{1}(1)\phi _{2}(2) \Longrightarrow can't{}separate
$$

# mean field theory

$$
\frac{1}{\left | r_{1}-r_{2}\right | }\Longrightarrow V_{ee}(r_{i})(potential-effect-single-electron)
$$

$$
\frac{1}{\left | r-r'\right | }\Longrightarrow V_{H}=\int \frac{n(r')}{\left | r-r' \right | }dr'(Hatree-term)+Exchange-correlation-term
$$

$$
electron-electron{}interaction\Longrightarrow electron{}in{}potential{}from{}other{}electrons\longrightarrow mean-field
$$

$$
many-body \to single-electron
$$

$$
\begin{aligned}
\text{Obtain-grand-state-charge-density:} \, n(r) \\
\Downarrow \\
\text{Guess-perturbate-charge-density:} \, \Delta n(r) \\
\Downarrow \\
\text{Total-perturbation-potebtial:} \,\Delta V_{\text{SCF}}(r) = \Delta V_{\text{per}}^{q} (r) + e^2 \int \frac{\Delta n(r')}{|r - r'|} dr' \\
\Downarrow \\
\text{Fourier-Transformation:} \, \Delta V_{K-S}(r) = -\frac{1}{\sqrt{N_{p}}} \sum_{k} e^{-i(q+G)\cdot r} \Delta V_{K-S}(q+G) \\
\Downarrow \\
\text{perturbate-charge-density-by-perturbation:} \, \Delta n_{\text{new}}(q+G) = \frac{4}{N \Omega} \sum_{k} \sum_{c,v} \frac{\langle \psi_{v,k} | e^{-i(q+G)\cdot r} | \psi_{c,k+q} \rangle \langle \psi_{c,k+q} | \Delta V_{\text{SCF}}(q+G) | \psi_{v,k} \rangle}{\varepsilon_{v,k} - \varepsilon_{c,k+q}} \\
\Downarrow \\
\text{Fourier-Transformation:} \, \Delta n_{\text{new}}(q+G) \Longrightarrow \Delta n_{\text{new}}(r) \\
\Downarrow \\
\Delta n(r) = \Delta n_{\text{new}}(r) \vee \Delta n(r) \neq \Delta n_{\text{new}}(r)
\end{aligned}
$$
