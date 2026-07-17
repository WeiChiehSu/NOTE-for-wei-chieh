# Exchange-correlation energy

$$
When{}electron{}at{}r,The{}probility{}of{}other{}electron{}near{}r{}will{}decrease{}\Longrightarrow The{}place{}of{}near{}r{}lose{}some{}electron{}density\Longrightarrow Like{}hole
$$

$$
hole{}reason:
\begin{cases}
  & exchange:wave-antisymmetry\longrightarrow same-spin-can't-approach \\
  & correlation:electron-repulsion\to Hatree-potential
\end{cases}
$$

$$
n_{xc}(r,r')=n(r')\int_{0}^{1}d\lambda[g_{n}(r,r',\lambda)-1 ]\Longrightarrow The{}place{}of{}near{}r'{}lose{}electron{}density=electron{}density{}at{}r'\times The{}probility{}of{}other{}electron{}near{}r
$$

$$
g_{n}(r,r',\lambda)
\begin{cases}
  & g_{n}\le1\Longrightarrow decrease-electron-density\Longrightarrow hole  &  \\
  & g_{n}=1\Longrightarrow no-special-effect &  \\
  & g_{n}> 1\Longrightarrow increase-electron-density & 
\end{cases}
$$

$$
E_{xc}[n(r)]=\frac{1}{2}\int drn(r)\int dr'\frac{n_{xc}(r,r') }{\left | r-r' \right | }  \Longrightarrow all{}potentail{}detween{}electron{}and{}hole=all{}elecron{}density\times lose{}electron(hole){}density\Longrightarrow negative{}value
$$

$$
hole{}rule
\begin{cases}
  & hole-related-to-distance-with-electron-in-center \\
  & \int dr'n_{xc}(r,r')=-1\Longrightarrow all-hole-density=lose-one-electron
\end{cases}
$$

$$
LDA{}approximation:elecron-density{}near{}r\to hole{}density{}from{}uniform{}electron{}gas\Longrightarrow n_{xc}^{LDA}(r,r')=n(r')h_{0}(\left | r-r' \right |;n(r))   
$$

$$
2\times 2{}spin-martix\to E_{xc}:n_{\uparrow }(r),n_{\downarrow}(r)(colinear)   
$$

$$
E_{xc} [n_{\uparrow }(r),n_{\downarrow}(r)]=\int drn(r)\varepsilon_{xc}(n_{\uparrow }(r),n_{\downarrow}(r))
$$

$$
LSDA:n_{\uparrow },n_{\downarrow};GGA:n_{\uparrow }+ \nabla n_{\uparrow }  ,n_{\downarrow}+\nabla n_{\downarrow }:Meta-GGA:n_{\uparrow }+ \nabla n_{\uparrow }+\tau _{\uparrow }   ,n_{\downarrow}+\nabla n_{\downarrow }+\tau _{\downarrow }
$$

# LDA uniform electron gas exchange energy

$$
\varepsilon_{xc}[n(r)]= \varepsilon_{x}[n(r)]+\varepsilon_{c}[n(r)]=exchange+corrleation
$$

$$
exchange\to antisymmetry
$$

$$
antisymmetry\Longrightarrow \psi (1,2)=\frac{1}{\sqrt{2} } [\phi_{1}(1) \phi_{2}(2)-\phi_{2}(1)\phi_{1}(2)]
$$

$$
V_{ee}=\frac{1}{r_{12}}\Longrightarrow \left \langle \psi \right |V_{ee}\left | \psi  \right \rangle  =\frac{1}{2}\int dr_{1}dr_{2}  [\phi_{1}^{\star } (1) \phi_{2}^{\star }(2)-\phi_{2}^{\star }(1)\phi_{1}^{\star }(2)]\frac{1}{r_{12}}[\phi_{1}(1) \phi_{2}(2)-\phi_{2}(1)\phi_{1}(2)] 
$$

$$
(1):\frac{1}{2}\int dr_{1}dr_{2}\phi_{1}^{\star } (1) \phi_{2}^{\star }(2)\frac{1}{r_{12}}\phi_{1}(1) \phi_{2}(2)=\int dr_{1}dr_{2}\left | \phi_{1}^{\star } (1)  \right | \frac{1}{r_{12} } \left | \phi_{2}^{\star } (2)  \right |=J_{12}(corrleation{}between{}A{}and{}B) 
$$

$$
(4):\frac{1}{2}\int dr_{1}dr_{2}\phi_{2}^{\star } (1) \phi_{1}^{\star }(2)\frac{1}{r_{12}}\phi_{2}(1) \phi_{1}(2)=\int dr_{1}dr_{2}\left | \phi_{2}^{\star } (1)  \right | \frac{1}{r_{12} } \left | \phi_{1}^{\star } (2)  \right |=J_{21}\Longrightarrow J_{21}=J_{12}\Longrightarrow Total=2J_{12} 
$$

$$
(2):\frac{1}{2}\int dr_{1}dr_{2}\phi_{1}^{\star } (1) \phi_{2}^{\star }(2)\frac{1}{r_{12}}\phi_{2}(1) \phi_{1}(2)=\int dr_{1}dr_{2}[\phi_{1}^{\star } (1) \phi_{2}(1)]\frac{1}{r_{12}}[\phi_{2}^{\star }(2) \phi_{1}(2)]=K_{12}\Longrightarrow exchange{}between{}1{}and{}2
$$

$$
(3):\frac{1}{2}\int dr_{1}dr_{2}\phi_{2}^{\star } (1) \phi_{1}^{\star }(2)\frac{1}{r_{12}}\phi_{1}(1) \phi_{2}(2)=\int dr_{1}dr_{2}[\phi_{2}^{\star } (1) \phi_{1}(1)]\frac{1}{r_{12}}[\phi_{1}^{\star }(2) \phi_{2}(2)]=K_{21}\Longrightarrow K_{21}^{\star }=K_{12}\Longrightarrow K_{21}\Longrightarrow total=2K_{12}
$$

$$
\Longrightarrow \left \langle \psi \right |V_{ee}\left | \psi  \right \rangle =J_{12}-K_{12}=corrleation(increase)-exchange(decrease)
$$
