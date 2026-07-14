# magnetic correction DFT(磁性修正DFT)

$$
Normal-density:n(r)=\sum \left \langle \psi  \right | \psi^{*}(r)\psi (r) \left | \psi  \right \rangle   
$$

$$
\Longrightarrow Spin-density-martix:n_{\alpha \beta } (r)=\sum_{\alpha }^{} \left \langle \psi  \right | \psi_{\beta  }^{*}(r)\psi _{\alpha }^{}(r) \left | \psi  \right \rangle [\alpha ,\beta =\uparrow ,\downarrow ]  
$$

$$
Normarl:\left | \psi(r)  \right \rangle \Longrightarrow Spin:\left | \psi (r)*  \right \rangle =\begin{pmatrix}
\psi_{\uparrow }(r)  & \\
\psi_{\downarrow } (r)  & 
\end{pmatrix}
$$

$$
Normarl:n(r)=\left \langle \psi(r)  | \psi(r)  \right \rangle  \Longrightarrow Spin{}martix:n_{\alpha \beta } (r)=\left | \psi (r)*  \right \rangle \left \langle \psi (r)* \right |   =
\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}
$$

$$
Normal:n(r)[scalar]\longrightarrow Spin:strengh(r)[scalar]+direction(r)[vector]
$$

$$
3d{}vector:V=v_{x} \widehat{x}+v_{y} \widehat{y} +v_{z} \widehat{z}\Longrightarrow 2X2{}martix:A=A_{0}I+\sigma _{x} a_{x}+\sigma _{y} a_{y}+\sigma _{z} a_{z} 
$$

$$
n_{\alpha \beta}(r)=\frac{1}{2}(n(r)I+\sigma .S(r))=total{}electron{}density+spin{}direction{}trend
$$

$$
\sigma .S(r)=\sigma _{x} .s_{x}+\sigma _{y} .s_{y}+\sigma _{z} .s_{z}=\begin{pmatrix}
 0 & 1\\
 1 & 0
\end{pmatrix}s_{x}+\begin{pmatrix}
0  &-i\\
i  & 0
\end{pmatrix}s_{y}+\begin{pmatrix}
1  & 0\\
0  & -1
\end{pmatrix}s_{z}
$$

$$
\Longrightarrow \sigma .S(r)=\begin{pmatrix}
 s_{z}  & s_{x}-is_{y}   \\
 s_{x}+is_{y}  & -s_{z} 
\end{pmatrix};n(r).I=\begin{pmatrix}
n  & 0 \\
0  & n
\end{pmatrix}
$$

$$
n_{\alpha \beta}(r)=\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}=\frac{1}{2}(n(r)I+\sigma .S(r))=\frac{1}{2} \begin{pmatrix}
 n(r)+s_{z}  & s_{x}-is_{y}   \\
 s_{x}+is_{y}  & n(r)-s_{z} 
\end{pmatrix}= \begin{pmatrix}
spin-up-density  & spin-direction-trend-to-x,y,z-axis\\
spin-up/down-mixing  & spin-down-density
\end{pmatrix}
$$

$$
Total{}electron{}number=Trace\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}=n_{\uparrow \uparrow } (r)+n_{\downarrow \downarrow} (r)=n(r)
$$

$$
n_{\uparrow \uparrow } (r),n_{\downarrow \downarrow} (r)=diagonal{}element
$$

$$
Local{}spin{}difference=n_{\uparrow \uparrow } (r)-n_{\downarrow \downarrow} (r)=\frac{1}{2}(n(r)+s_{z}))- \frac{1}{2}(n(r)-s_{z}))=s_{z} 
$$

$$
s_{z}\begin{cases}
s_{z}=0,n_{\uparrow \uparrow } (r)=n_{\downarrow \downarrow} (r)\Longrightarrow no-spin-trend \\
s_{z}>0,n_{\uparrow \uparrow } (r)>n_{\downarrow \downarrow} (r)\Longrightarrow spin-tend-to-spin-up \\
s_{z}<0,n_{\uparrow \uparrow } (r)\le n_{\downarrow \downarrow} (r)\Longrightarrow spin-tend-to-spin-down \\
\end{cases}
$$

$$
n_{\uparrow \downarrow } (r),n_{\downarrow \uparrow} (r)=off-diagonal{}element
$$

$$
off-diagonal{}element{}in{}z-base=
\begin{cases}
\left | \uparrow _{z}   \right \rangle= \begin{pmatrix}
1  & \\
0  &
\end{pmatrix}\Longrightarrow n=\left | \uparrow _{z}  \right \rangle \left \langle \uparrow _{z} \right | =\begin{pmatrix}
1  & \\
0  &
\end{pmatrix}\begin{pmatrix}
 1 &0
\end{pmatrix}=\begin{pmatrix}
1  & 0\\
0  & 0
\end{pmatrix}\\
\left | \downarrow  _{z}   \right \rangle= \begin{pmatrix}
0  & \\
1  &
\end{pmatrix}\Longrightarrow n=\left | \downarrow _{z}  \right \rangle \left \langle \downarrow _{z} \right | =\begin{pmatrix}
0  & \\
1  &
\end{pmatrix}\begin{pmatrix}
 0 &1
\end{pmatrix}=\begin{pmatrix}
0  & 0\\
0  & 1
\end{pmatrix}\\
\end{cases}\Longrightarrow off-diagonal{}element=0\Longrightarrow spin{}along{}z-axis
$$

$$
off-diagonal{}element{}in{}z-base=
\begin{cases}
\left | \uparrow _{x}   \right \rangle=\frac{1}{\sqrt{2} }  \begin{pmatrix}
1  & \\
1  &
\end{pmatrix}\Longrightarrow n=\left | \uparrow _{x}  \right \rangle \left \langle \uparrow _{x} \right | =\begin{pmatrix}
1  & \\
1  &
\end{pmatrix}\begin{pmatrix}
 1 &1
\end{pmatrix}=\frac{1}{2} \begin{pmatrix}
1  & 1\\
1  & 1
\end{pmatrix}\\
\left | \downarrow  _{y}   \right \rangle=\frac{1}{\sqrt{2} } \begin{pmatrix}
1  & \\
i  &
\end{pmatrix}\Longrightarrow n=\left | \downarrow _{y}  \right \rangle \left \langle \downarrow _{y} \right | =\begin{pmatrix}
1  & \\
i  &
\end{pmatrix}\begin{pmatrix}
 1 &-i
\end{pmatrix}=\frac{1}{2} \begin{pmatrix}
1  & -i\\
i  & 1
\end{pmatrix}\\
\end{cases}\Longrightarrow off-diagonal{}element\ne 0\Longrightarrow 
\begin{cases}
spin-tend-to-x-axis\longrightarrow real-part \\
spin-tend-to-y-axis\longrightarrow imaginary-part
\end{cases}
$$

$$
Postion:n_{\alpha \beta}(r)=\frac{1}{2}(n(r)I+\sigma .S(r))\to v(r)=v(r).I+\mu _{B} \sigma .B(r)=scalar{}potential+spin{}and{}magnetic{}coupling
$$

$$
Normal{}K-S{}equation:\left[ -\frac{\nabla^2 r}{2} + V_{\text{SCF}}(r) + V_{\text{Hatree}}(r) +V_{xc} (r) \right] \Psi(r) = \varepsilon \Psi(r)
$$

$$
\Downarrow
$$

$$
Magnetic{}K-S{}equation:\left[ (-\frac{ \hbar }{2m}\nabla^2+ V_{\text{Hatree}}(r)).I + V_{\text{SCF}}(r) +\frac{\delta E_{xc} }{\delta n(r) }   \right] 
\begin{pmatrix}
\varphi_{i}^{\uparrow }    & \\
\varphi_{i}^{\downarrow }   &
\end{pmatrix} = \varepsilon_{i}  
\begin{pmatrix}
\varphi_{i}^{\uparrow }    & \\
\varphi_{i}^{\downarrow }   &
\end{pmatrix}
$$

$$
E_{xc}= E_{xc}[n_{\uparrow }(r) ,n_{\downarrow }(r) ]\Longrightarrow related{}to{}spin-up/down{}density
$$


$$
\frac{\delta E_{xc} }{\delta n(r)} \to effective{}potential\to give{}diffrent{}energy{}for{}diffrent{}spin\to be{}self{}magnetic{}field{}B(r)
$$

$$
\frac{\delta E_{xc} }{\delta n(r)} =V_{xc}(r)=v_{xc}(r).I+\mu _{B} \sigma .B_{xc}(r)=scalar{}xc{}potential+self{}magnetic{}field
$$

$$
B_{xc}(r) =(B_{xc}^{x}(r),B_{xc}^{y}(r),B_{xc}^{z}(r))\to \sigma .B_{xc}(r)= \begin{pmatrix}
 0 & 1\\
 1 & 0
\end{pmatrix}B_{xc}^{x}(r)+\begin{pmatrix}
0  &-i\\
i  & 0
\end{pmatrix}B_{xc}^{y}(r)+\begin{pmatrix}
1  & 0\\
0  & -1
\end{pmatrix}B_{xc}^{z}(r)
$$

$$
\sigma .B_{xc}(r) =
\begin{pmatrix}
B_{xc}^{z}(r)  & B_{xc}^{x}(r)-iB_{xc}^{y}(r)\\
B_{xc}^{x}(r)+iB_{xc}^{y}(r)  & -B_{xc}^{z}(r)
\end{pmatrix}
$$

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
spin-density-martix:n_{\alpha \beta } (r)=\sum \varphi_{i}^{\alpha *}(r) \varphi_{i}^{\beta }(r)=
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)  & \varphi _{i}^{\downarrow }(r)
\end{pmatrix}
\begin{pmatrix}
\varphi _{i}^{\uparrow }(r)   & \\
\varphi _{i}^{\downarrow }(r)  &
\end{pmatrix}=
\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}
$$

$$
Total{}electron{}density=Trace\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}=n_{\uparrow \uparrow } (r)+n_{\downarrow \downarrow} (r)=n(r)
$$
