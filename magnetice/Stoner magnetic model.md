# Stoner magnetic model

$$
Magnetic{}moment{}M=\int_{}^{E_{F} }[N_{\uparrow}(E)-N_{\downarrow}(E)]dE
$$

$$
Magnetic{}moment\Longrightarrow spin-up/down{}potential{}different{}by{}xc
$$

$$
g(M)\equiv v_{xc}^{\uparrow }-v_{xc}^{\downarrow}  \overset{taylor}{\rightarrow}g(M)=\frac{\partial v_{xc}^{\uparrow }-v_{xc}^{\downarrow}}{\partial M}| _{M=0}  
$$

$$
spin-up/down{}potential{}different\Longrightarrow band{}split:\Delta \varepsilon _{i}=\varepsilon_{i}^{\uparrow }-\varepsilon_{i}^{\downarrow  }\approx M\left \langle \psi_{i}  \right |\frac{\partial v_{xc}^{\uparrow }-v_{xc}^{\downarrow}}{\partial M}\left | \psi_{i}   \right \rangle  
$$

$$
all{}state{}have{}same{}split
\begin{cases}
  & \varepsilon _{i}^{\uparrow }=\varepsilon _{i}-\frac{1}{2}IM \\
  & \varepsilon _{i}^{\downarrow }=\varepsilon _{i}+\frac{1}{2}IM 
\end{cases}
\Longrightarrow \Delta \varepsilon_{i}=IM(I:stoner-coefficient)
$$

$$
split\Longrightarrow occupied{}spin-up/down{}dos{}different{}n_{\uparrow }\ne n_{\downarrow}\Longrightarrow  new{}magnetic{}moment:F(M)=M_{new}(M)
$$

$$
DOS:N(E)=\sum_{i}\delta (E-\varepsilon _{i})[\varepsilon _{i}^{\uparrow \downarrow }=\varepsilon _{i}\pm \frac{IM}{2}]\longrightarrow N_{\uparrow \downarrow} (E)= \delta (E-\varepsilon _{i}^{\uparrow \downarrow }+\frac{IM}{2})\to N_{\uparrow \downarrow} (E)= \delta (E\pm \frac{IM}{2})
$$

$$
M_{new}=n_{\uparrow }-n_{\downarrow},n_{\uparrow \downarrow }=\int_{-\infty }^{E_{F} } N_{\uparrow \downarrow }(E)dE\to\int_{-\infty }^{E_{F} } N_{\uparrow \downarrow }(E\pm \frac{IM}{2} )dE \longrightarrow N_{\uparrow \downarrow} (E)= \delta (E-\varepsilon _{i}^{\uparrow \downarrow }+\frac{IM}{2})\Longrightarrow  M_{new}=\int_{}^{E_{F} } [N(E+\frac{1}{2}IM)-N(E-\frac{1}{2}IM) ]dE 
$$

$$
self-consistent:M[old]=F(M)[new]
$$

$$
M
\begin{cases}
  & M=0\to no-Magnetic-moment \\
  & M\ne 0 \to tend-to-form-Magnetic-moment
\end{cases}
$$

$$
M\approx 0\overset{Taylor}{\rightarrow} F(M)\approx F(0)+\frac{dF}{dM}|_{M=0}M+O(M^{2} )+.....\to M\approx 0,F(M){}How{}to{}change{}?
$$

$$
F(0)=0\to F(M\approx 0)=F(M)\approx \frac{dF}{dM}|_{M=0}M\longrightarrow M_{new} =\frac{dF}{dM}|_{M=0}M
$$

$$
M\ne 0\to \frac{\mathrm{d} F(M)}{\mathrm{d} M}|_{M\approx 0}>1\Longrightarrow F(M)>M
$$

$$
\frac{\mathrm{d} F(M)}{\mathrm{d} M}\Longrightarrow F(M)=\int_{}^{E_{F} } [N(E+\frac{1}{2}IM)-N(E-\frac{1}{2}IM) ]dE\overset{Taylor}{\rightarrow}  IM\frac{\mathrm{d} N(E)}{\mathrm{d} E} 
$$

$$
F(M)=\int_{}^{E_{F} } IM\frac{\mathrm{d} N(E)}{\mathrm{d} E}dE\Longrightarrow F(M)\approx IMN(E_{F})\Longrightarrow \frac{\mathrm{d} F(M)}{\mathrm{d} M}\approx IN(E_{F})>1 
$$

$$
IN(E_{F})>1 \begin{cases}
  & I:xc-split-strength \\
  & N(E_{F}):How-much-state-at-E_{F}
\end{cases}
$$
