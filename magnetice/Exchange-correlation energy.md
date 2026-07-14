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
