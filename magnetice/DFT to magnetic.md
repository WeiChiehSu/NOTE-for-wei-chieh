# Density Functional Theory (密度泛函理論)

想要得到材料的電子性質,需要計算材料中的薛丁格方程式:

To obtain the electronic properties of a material, it is necessary to solve the Schrödinger equation for the material:

$$
H\Psi (r)=\varepsilon \Psi (r)
$$

$$
H =-\sum_{a=1 }^{k} \frac{\nabla^{2} _{R_{a}  }  } {2m_{a}} +\sum_{a=1 }^{k} \sum_{b>a }^{k} \frac{Z_{a}Z_{b} }{R_{ab}}-\sum_{i=1}^{n} \frac{\nabla^{2} _{r_{i}  }  } {2} +\sum_{i=1 }^{n} \sum_{j>i }^{n} \frac{1 }{r_{ij}}+ \sum_{i=1 }^{n} \sum_{a=1 }^{k} \frac{Z_{a} }{r_{ia}}
$$

$$
其中 \Psi (r)為N個電子波函數的乘積:
$$

$$
where{}\Psi(r){}is{}the{}product{}of{}the{}wavefunctions{}of{}the{}N{}electrons.
$$

$$
\Psi (r)=\psi _{1}(r) \psi _{2}(r)\psi _{3}(r).....
$$

這個方程式非常複雜,計算的成本非常高,近乎無法計算.

This equation is highly complex and extremely computationally expensive, making it nearly impossible to solve directly.

但在1964年,Hohenberg和Kohn發現了材料的基態電荷密度決定了材料基態的能量和波函數的性質,這表示我們可以用一個具有3個維度的電荷密度波函數來解薛丁格方程式,而不需要解有3N個變量的電子波函數,這讓計算複雜材料的電子能帶成為了可行,這便是密度泛函理論.

However, in 1964, Hohenberg and Kohn discovered that the ground-state electron density of a material uniquely determines the ground-state energy and wavefunction properties of the system. This means that the Schrödinger equation can be solved using the electron density, which depends on only three spatial variables, rather than the many-electron wavefunction with 3N variables. This breakthrough made it feasible to compute the electronic structure of complex materials and formed the foundation of density functional theory (DFT).

$$
\begin{aligned}
H \Psi(r) &= \varepsilon(\psi_{1}, \psi_{2}, \psi_{3}, \ldots) \, \Psi(r) \\
\Downarrow \\
H \Psi(r) &= \varepsilon[n(r)] \, \Psi(r)
\end{aligned}
$$

考慮絕熱近似和單電子近似後,材料的哈密頓量可改寫為下列的形式:

Under the adiabatic approximation and the single-electron approximation, the Hamiltonian of the material can be rewritten in the following form:

$$
-\sum_{a=1 }^{k} \frac{\nabla^{2} _{R_{a}  }  } {2m_{a}} +\sum_{a=1 }^{k} \sum_{b>a }^{k} \frac{Z_{a}Z_{b} }{R_{ab}}-\sum_{i=1}^{n} \frac{\nabla^{2} _{r_{i}  }  } {2} +\sum_{i=1 }^{n} \sum_{j>i }^{n} \frac{1 }{r_{ij}}+ \sum_{i=1 }^{n} \sum_{a=1 }^{k} \frac{Z_{a} }{r_{ia}}\Longrightarrow -\frac{\nabla^{2}r }{2}+V_{SCF}(r)+V_{Hatree}(r)
$$

這個公式被稱為Kohn–Sham equation,描述在「有效單電子勢」下，電子如何運動,其第一項為電子動能,第二項為電子和原子核間的勢能項,第三項為Hatree項:

This equation is called the Kohn–Sham equation, which describes how electrons move under an "effective single-electron potential." The first term represents the kinetic energy of the electrons, the second term represents the potential energy between the electrons and the atomic nuclei, and the third term is the Hartree term:

$$
V_{Hatree}(r)=e^{2} \int \frac{n(r_{i}) }{\left | r-r_{i} \right | } d^{3} r_{i}
$$

Hatree項代表單個電子和由全部電子組成的電荷密度間產生的庫倫排斥.


The Hartree term represents the Coulomb repulsion between a single electron and the charge density formed by all electrons.

$$
\frac{\delta E_{XC} }{\delta n(r)} = V_{xc} (r)
$$1

XC項為交換-關聯能,這項用一個勢能來近似電子感受到的交換能和關聯勢能,這在常規DFT中是一個定值.

The XC term means the exchange-correlation energy. This term uses a potential to approximate the exchange energy and correlation potential felt by electrons. In conventional DFT, this is a fixed value.

DFT的數值計算方式如下:

The numerical procedure of DFT is as follows:

$$
\begin{aligned}
\text{1.Guess-charge-density:} \, n(r) \\
\Downarrow \\
\text{2.Poisson-eq:} \, \nabla^2 V_{\text{Hatree}}(r) = -4 \pi n(r){} ; {}\frac{\delta E_{XC} }{\delta n(r)} = V_{xc} (r)\\
\Downarrow \\
\text{3.KS-eq:} \left[ -\frac{ \hbar }{2m}\nabla^2 + V_{\text{SCF}}(r) + V_{\text{Hatree}}(r) +V_{xc} (r) \right] \Psi(r) = \varepsilon \Psi(r) \\
\Downarrow \\
4.n_{\text{new}}(r) = \sum \left| \Psi(r) \right|^2 \\
\Downarrow \\
5.n(r) = n_{\text{new}}(r) \vee n(r) \neq n_{\text{new}}(r)
\end{aligned}
$$

$$
第1步為猜一個初始電子密度:解電子系統的Kohn–Sham{}equation,需要知道電子密度n(r)才能算出有效勢,問題是：一開始根本不知道真實的n(r)，所以只好先猜一個初始電子密度.
$$

$$
Step{}1{}is{}to{}guess{}an{}initial{}electron{}density:{}to{}solve{}the{}Kohn–Sham{}equation{}for{}the{}electronic{}system,{}the{}electron{}density{}n(r){}is{}required{}to{}compute{}the{}effective{}potential.{}However,{}the{}true{}n(r){}is{}not{}known{}at{}the{}beginning,{}so{}one{}must{}first{}make{}an{}initial{}guess{}for{}the{}electron{}density.
$$

$$
第2步為解Poisson{}equation:電子密度會產生庫倫靜電場,這步便是從目前的電子密度n(r)去計算Hartree勢,得到電子-電子之間的平均排斥作用.
$$

$$
Step{}2{}is{}to{}solve{}the{}Poisson{}equation:{}the{}electron{}density{}generates{}a{}Coulomb{}electrostatic{}field.{}In{}this{}step,{}the{}Hartree{}potential{}is{}calculated{}from{}the{}current{}electron{}density{}n(r),{}yielding{}the{}average{}electron–electron{}repulsive{}interaction.
$$

$$
第3步為解Kohn–Sham{}equation:得到Hartree勢後,便知道了系統的Hamiltonian,使用數值方法（例如:plane-wave 展開、基組展開、數值對角化)找到Hamiltonian的eigenvalue和eigenstate.
$$

$$
Step{}3{}is{}to{}solve{}the{}Kohn–Sham{}equation:{}once{}the{}Hartree{}potential{}is{}obtained,{}the{}Hamiltonian{}of{}the{}system{}is{}known.{}Numerical{}methods{}(such{}as{}plane-wave{}expansion,{}basis{}set{}expansion,{}or{}numerical{}diagonalization){}are{}then{}used{}to{}obtain{}the{}eigenvalues{}and{}eigenstates{}of{}the{}Hamiltonian.
$$

$$
第4步為更新電子密度:電子密度就是所有電子波函數的平方和,用解出來的eigenstate重新計算,得到新的電子密度.
$$

$$
Step{}4{}is{}to{}update{}the{}electron{}density:{}the{}electron{}density{}is{}the{}sum{}of{}the{}squared{}magnitudes{}of{}all{}electron{}wavefunctions.{}It{}is{}recalculated{}using{}the{}obtained{}eigenstates{}to{}produce{}a{}new{}electron{}density.
$$

$$
第5步為檢查收斂:如果新算出的電子密度 n_{\text{new}}(r) 和之前猜的n(r) 一致 -> 就找到一個「自洽」解;如果不一致,就把 n_{\text{new}}(r) 當作新的密度,再回到第2步重複計算，直到收斂
$$

$$
Step{}5{}is{}to{}check{}for{}convergence:{}if{}the{}newly{}calculated{}electron{}density{}n_{\text{new}}(r){}is{}consistent{}with{}the{}previously{}guessed{}n(r),{}then{}a{}self-consistent{}solution{}has{}been{}found.{}If{}they{}are{}not{}consistent,{}n_{\text{new}}(r){}is{}used{}as{}the{}new{}electron{}density,{}and{}the{}procedure{}returns{}to{}Step{}2{}and{}repeats{}until{}convergence{}is{}achieved.
$$

使用密度泛函理論(DFT),我們可以得到材料的基態電荷密度,以此解出材料的基態能量和基態波函數,我們也可以對DFT理論延伸,考慮對材料引入微擾時,材料的性質將產生甚麼樣的變化,這理論被稱為密度泛函微擾理論(DFPT).

Using density functional theory (DFT), we can obtain the ground-state electron density of a material, from which the ground-state energy and ground-state wavefunctions can be determined. The DFT framework can also be extended to consider how the properties of a material change when a perturbation is introduced. This extension is known as density functional perturbation theory (DFPT).

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
Normarl:n(r)=\left \langle \psi(r)  | \psi(r)  \right \rangle  \Longrightarrow Spin{}martix:n_{\alpha \beta } (r)=\left \langle \psi (r)*  | \psi (r)*  \right \rangle =\begin{pmatrix}
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
