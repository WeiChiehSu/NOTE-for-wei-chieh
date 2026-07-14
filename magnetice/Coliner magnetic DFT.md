
# Coliner magnetic DFT

$$
Magnetic{}K-S{}equation:
\begin{pmatrix}
\left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)+B_{xc}^{z}(r)    \right]   & v_{xc}(r)+B_{xc}^{x}(r)-iB_{xc}^{y}(r) \\
v_{xc}(r)+B_{xc}^{x}(r)+iB_{xc}^{y}(r)   & \left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)-B_{xc}^{z}(r)    \right] 
\end{pmatrix}
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)   & \\
\varphi _{i}^{\downarrow }(r)  &
\end{pmatrix}=\varepsilon _{i}
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)   & \\
\varphi _{i}^{\downarrow }(r)  &
\end{pmatrix} 
$$

$$
\Longrightarrow 
\begin{pmatrix}
\left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)+B_{xc}^{z}(r)    \right]   & 0 \\
0   & \left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)-B_{xc}^{z}(r)    \right] 
\end{pmatrix}
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)   & \\
\varphi _{i}^{\downarrow }(r)  &
\end{pmatrix}=\varepsilon _{i}
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)   & \\
\varphi _{i}^{\downarrow }(r)  &
\end{pmatrix} 
$$

$$
\begin{cases}
  & \left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)+B_{xc}^{z}(r)    \right] \varphi _{i}^{\uparrow }(r)= \varepsilon_{i}^{\uparrow } \varphi _{i}^{\uparrow }(r)\\
  & \left[ -\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r) + V_{\text{SCF}}(r) +v_{xc}(r)-B_{xc}^{z}(r)    \right] \varphi _{i}^{\downarrow }(r)= \varepsilon_{i}^{\downarrow }   \varphi _{i}^{\downarrow }(r)
\end{cases}
$$

$$
charge{}density\begin{cases}
  & n^{\uparrow }(r)=\sum_{i}^{}\omega_{i}^{\uparrow }  \left | \psi _{i}^{\uparrow }  \right |^{2}    \\
  & n^{\downarrow}(r)=\sum_{i}^{}\omega_{i}^{\downarrow }  \left | \psi _{i}^{\downarrow }  \right |^{2}
\end{cases}
$$

$$
\omega_{i}\begin{cases}
  &   & E>E_{F} \Longrightarrow no-occupy \Longrightarrow \omega _{i}=0  \\
  &   & E=E_{F} \Longrightarrow part-occupy \Longrightarrow 0 \le \omega _{i} \le 1 \\
  &   & E\le E_{F} \Longrightarrow full-occupy \Longrightarrow \omega _{i}=1
\end{cases}
$$

$$
total{}charge{}densityn{}(r)=n^{\uparrow }(r)+n^{\downarrow}(r)
$$

$$
\nabla V_{Hatree}(r) =-4 \pi n{}(r) \to  n{}(r)=n^{\uparrow }(r)+n^{\downarrow}(r)\Leftrightarrow V_{Hatree}(r)
$$

$$
Approximation:E_{xc}\approx -\frac{3}{2}(\frac{3}{4\pi } )^{\frac{1}{3}}\int dr[(n^{\uparrow }(r)^{\frac{4}{3} }+(n^{\downarrow}(r))^{\frac{4}{3} }  ]    \to  n^{\uparrow }(r);n^{\downarrow}(r)\Leftrightarrow E_{xc}
$$

$$
V_{xc}^{\uparrow} =v+B^{\uparrow}=\frac{\delta E_{xc}[n^{\uparrow }(r),n^{\downarrow}(r)] }{\delta n^{\uparrow }(r)};V_{xc}^{\downarrow} =v+B^{\downarrow}=\frac{\delta E_{xc}[n^{\uparrow }(r),n^{\downarrow}(r)] }{\delta n^{\downarrow}(r)}
$$

$$
\begin{aligned}
\text{1.Guess-charge-density:} \, n^{\uparrow }(r),n^{\downarrow}(r),n{}(r)=n^{\uparrow }(r)+n^{\downarrow}(r) \\
\Downarrow \\
\text{2.Poisson-eq:} \, \nabla^2 V_{\text{Hatree}}(r) = -4 \pi n(r){} ; {}V_{xc}^{\uparrow,\downarrow} =v_{xc}(r) \pm B_{xc} ^{z}=\frac{\delta E_{xc}[n^{\uparrow }(r),n^{\downarrow}(r)] }{\delta n^{\uparrow,\downarrow}(r)}\\
\Downarrow \\
\text{3.KS-eq:} \left[ -\frac{ \hbar }{2m}\nabla^2 + V_{\text{SCF}}(r) + V_{\text{Hatree}}(r) +v_{xc} (r)\pm B_{xc}^{z}  \right] \Psi_{i}^{\uparrow,\downarrow} (r) = \varepsilon_{i}^{\uparrow,\downarrow}  \Psi_{i}^{\uparrow,\downarrow} (r) \\
\Downarrow \\
4.n_{\text{new}}(r) = \sum \left| \Psi_{i}^{\uparrow} (r) \right|^2+\sum \left| \Psi_{i}^{\downarrow} (r) \right|^2 \\
\Downarrow \\
5.n(r) = n_{\text{new}}(r) \vee n(r) \neq n_{\text{new}}(r)
\end{aligned}
$$
