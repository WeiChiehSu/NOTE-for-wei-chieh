# LDA Exchange Energy from the Uniform Electron Gas

本筆記依照手寫內容整理 uniform electron gas 的 exchange energy 推導，最後得到 Local Density Approximation (LDA) 中的 exchange functional。整體流程是：plane wave -> Fermi sphere -> $n$ 與 $k_{F}$ 的關係 -> exchange matrix element -> 對所有 occupied states 求和 -> uniform electron gas 的 exchange energy -> LDA local approximation。

This note follows the handwritten derivation of the exchange energy of the uniform electron gas and its use in the Local Density Approximation (LDA). The logical chain is: plane wave -> Fermi sphere -> relation between $n$ and $k_{F}$ -> exchange matrix element -> sum over occupied states -> exchange energy of the uniform electron gas -> local LDA approximation.

從筆記中的自由電子能量 $\varepsilon_{\mathbf k}=k^{2}/2$ 與 Coulomb interaction $1/\lvert\mathbf r-\mathbf r'\rvert$ 可以看出，這一份推導使用 Hartree atomic units。

From the free-electron energy $\varepsilon_{\mathbf k}=k^{2}/2$ and the Coulomb interaction $1/\lvert\mathbf r-\mathbf r'\rvert$ used in the handwritten notes, this derivation is written in Hartree atomic units.

---

## 1. Plane waves and periodic boundary conditions

考慮體積為 $\Omega=L^{3}$ 的立方盒，使用 periodic boundary condition：

Consider a cubic box with volume $\Omega=L^{3}$ and periodic boundary conditions:

$$ \psi(x+L,y,z)=\psi(x,y,z). $$

單電子 orbital 使用 plane wave：

The single-electron orbital is represented by a plane wave:

$$ \phi_{\mathbf k}(\mathbf r)=\frac{1}{\sqrt{\Omega}}e^{i\mathbf k\cdot\mathbf r}. $$

加入 spin 後，單電子 wave function 寫成：

After introducing spin, the single-electron wave function is written as:

$$ \psi_{\mathbf k\sigma}(\mathbf r,s)=\frac{1}{\sqrt{\Omega}}e^{i\mathbf k\cdot\mathbf r}\chi_{\sigma}(s). $$

其中 $\chi_{\sigma}(s)$ 是 spin wave function，spin orthonormality 為：

Here $\chi_{\sigma}(s)$ is the spin wave function, with the orthonormality condition:

$$ \sum_{s}\chi_{\sigma}^{\ast}(s)\chi_{\sigma'}(s)=\delta_{\sigma\sigma'}. $$

plane wave 的 normalization 為：

The plane wave is normalized as:

$$ \int_{\Omega}d^{3}\mathbf r\,\lvert\phi_{\mathbf k}(\mathbf r)\rvert^{2}=1. $$

因為 $\lvert\phi_{\mathbf k}(\mathbf r)\rvert^{2}=1/\Omega$，所以 normalization coefficient 是 $1/\sqrt{\Omega}$。

Because $\lvert\phi_{\mathbf k}(\mathbf r)\rvert^{2}=1/\Omega$, the normalization coefficient is $1/\sqrt{\Omega}$.

不同 plane-wave states 也滿足 orthonormality：

Different plane-wave states also satisfy orthonormality:

$$ \int_{\Omega}d^{3}\mathbf r\,\phi_{\mathbf k}^{\ast}(\mathbf r)\phi_{\mathbf k'}(\mathbf r)=\delta_{\mathbf k,\mathbf k'}. $$

---

## 2. Quantization of momentum in a periodic box

由 periodic boundary condition：

From the periodic boundary condition:

$$ e^{ik_{x}(x+L)}=e^{ik_{x}x}. $$

因此：

Therefore:

$$ e^{ik_{x}L}=1=e^{i2\pi n_{x}}. $$

所以三個方向的 wave vector 都被量子化：

Thus, the three components of the wave vector are quantized:

$$ k_{x}=\frac{2\pi n_{x}}{L},\qquad k_{y}=\frac{2\pi n_{y}}{L},\qquad k_{z}=\frac{2\pi n_{z}}{L}. $$

也就是：

Equivalently:

$$ \mathbf k=\frac{2\pi}{L}(n_{x},n_{y},n_{z}). $$

相鄰 $k$ points 的間距為：

The spacing between neighboring $k$ points is:

$$ \Delta k_{x}=\Delta k_{y}=\Delta k_{z}=\frac{2\pi}{L}. $$

因此每一個 $k$ state 在 momentum space 中佔據的體積為：

Therefore, the volume occupied by one $k$ state in momentum space is:

$$ \Delta k^{3}=\Delta k_{x}\Delta k_{y}\Delta k_{z}=\left(\frac{2\pi}{L}\right)^{3}=\frac{(2\pi)^{3}}{\Omega}. $$

所以每單位 $k$-space volume 的 state density 為：

Thus, the density of states per unit volume in $k$ space is:

$$ \frac{1}{\Delta k^{3}}=\frac{\Omega}{(2\pi)^{3}}. $$

在 thermodynamic limit 中，$k$-point sum 可以轉成 integral：

In the thermodynamic limit, a sum over $k$ points becomes an integral:

$$ \sum_{\mathbf k}\rightarrow\frac{\Omega}{(2\pi)^{3}}\int d^{3}\mathbf k. $$

---

## 3. Electrons inside the Fermi sphere

自由電子的 single-particle energy 為：

The single-particle energy of a free electron is:

$$ \varepsilon_{\mathbf k}=\frac{k^{2}}{2},\qquad k=\lvert\mathbf k\rvert. $$

在 zero temperature ground state，電子由最低能量開始填滿 states，直到 Fermi wave vector $k_{F}$：

At zero temperature, the ground state is obtained by filling the lowest-energy states up to the Fermi wave vector $k_{F}$:

$$ \lvert\mathbf k\rvert\le k_{F}. $$

在 three-dimensional $k$ space 中，occupied states 因此形成一個 Fermi sphere。每一個 $\mathbf k$ state 可以放兩個不同 spin 的電子。

In three-dimensional $k$ space, the occupied states therefore form a Fermi sphere. Each $\mathbf k$ state can contain two electrons with opposite spin.

---

## 4. Relation between electron density and Fermi wave vector

電子密度定義為：

The electron density is defined as:

$$ n=\frac{N}{\Omega}. $$

對所有 occupied plane-wave states 求和，並包含 spin degeneracy 2：

Summing over all occupied plane-wave states and including the spin degeneracy of 2 gives:

$$ n=2\int_{\lvert\mathbf k\rvert\le k_{F}}\frac{d^{3}\mathbf k}{(2\pi)^{3}}. $$

使用 spherical coordinates：

Using spherical coordinates:

$$ d^{3}\mathbf k=k^{2}\sin\theta\,dk\,d\theta\,d\varphi. $$

因此：

Therefore:

$$ n=\frac{2}{(2\pi)^{3}}\int_{0}^{k_{F}}k^{2}dk\int_{0}^{\pi}\sin\theta\,d\theta\int_{0}^{2\pi}d\varphi. $$

角度積分給出 $4\pi$，所以：

The angular integrals give $4\pi$, so:

$$ n=\frac{k_{F}^{3}}{3\pi^{2}}. $$

因此 Fermi wave vector 與電子密度的關係是：

Therefore, the relation between the Fermi wave vector and the electron density is:

$$ k_{F}=(3\pi^{2}n)^{1/3}. $$

---

## 5. Exchange energy and the Coulomb Fourier transform

exchange energy 可以寫成所有 occupied states 的 exchange matrix elements：

The exchange energy can be written in terms of exchange matrix elements between occupied states:

$$ E_{x}=-\frac{1}{2}\sum_{i,j\in\mathrm{occ}}K_{ij}. $$

對兩個 single-particle states $i$ 和 $j$，exchange matrix element 為：

For two single-particle states $i$ and $j$, the exchange matrix element is:

$$ K_{ij}=\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\psi_{i}^{\ast}(\mathbf r)\psi_{j}^{\ast}(\mathbf r')\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}\psi_{j}(\mathbf r)\psi_{i}(\mathbf r'). $$

為了處理 $1/\lvert\mathbf r-\mathbf r'\rvert$，先計算 Coulomb potential 的 Fourier transform。

To handle $1/\lvert\mathbf r-\mathbf r'\rvert$, we first calculate the Fourier transform of the Coulomb potential.

令：

Let:

$$ V(R)=\frac{1}{R},\qquad R=\lvert\mathbf R\rvert. $$

Fourier transform 定義為：

The Fourier transform is defined as:

$$ V(\mathbf q)=\int d^{3}\mathbf R\,e^{-i\mathbf q\cdot\mathbf R}\frac{1}{R}. $$

因為 $1/R$ 具有 spherical symmetry，可以令 $\mathbf q$ 沿著 $z$ axis，因此：

Because $1/R$ has spherical symmetry, we choose $\mathbf q$ along the $z$ axis, so:

$$ \mathbf q\cdot\mathbf R=qR\cos\theta. $$

因此：

Therefore:

$$ V(q)=2\pi\int_{0}^{\infty}R^{2}dR\int_{0}^{\pi}\sin\theta\,d\theta\,\frac{e^{-iqR\cos\theta}}{R}. $$

令 $\mu=\cos\theta$，則 angular integral 為：

Let $\mu=\cos\theta$. The angular integral becomes:

$$ \int_{0}^{\pi}\sin\theta\,e^{-iqR\cos\theta}d\theta=\int_{-1}^{1}e^{-iqR\mu}d\mu=\frac{2\sin(qR)}{qR}. $$

所以：

Therefore:

$$ V(q)=\frac{4\pi}{q}\int_{0}^{\infty}\sin(qR)dR. $$

這個積分不能直接普通收斂，因此筆記中引入 convergence factor $e^{-\eta R}$：

This integral is not ordinarily convergent, so the handwritten notes introduce the convergence factor $e^{-\eta R}$:

$$ \int_{0}^{\infty}\sin(qR)dR=\lim_{\eta\rightarrow0^{+}}\int_{0}^{\infty}e^{-\eta R}\sin(qR)dR. $$

利用：

Using:

$$ \int_{0}^{\infty}e^{-\eta R}\sin(qR)dR=\frac{q}{q^{2}+\eta^{2}}, $$

得到：

we obtain:

$$ V(q)=\lim_{\eta\rightarrow0^{+}}\frac{4\pi}{q}\frac{q}{q^{2}+\eta^{2}}=\frac{4\pi}{q^{2}}. $$

所以 Coulomb interaction 的 inverse Fourier transform 為：

Therefore, the inverse Fourier transform of the Coulomb interaction is:

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}=\int\frac{d^{3}\mathbf q}{(2\pi)^{3}}\frac{4\pi}{q^{2}}e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}. $$

在 finite periodic volume $\Omega$ 中，integral 轉為 discrete sum：

In a finite periodic volume $\Omega$, the integral becomes a discrete sum:

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}=\frac{1}{\Omega}\sum_{\mathbf q}\frac{4\pi}{q^{2}}e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}. $$

---

## 6. Exchange matrix element for plane-wave states

令兩個 states 為 $(\mathbf k,\sigma)$ 與 $(\mathbf k',\sigma')$。exchange matrix element 為：

Let the two states be $(\mathbf k,\sigma)$ and $(\mathbf k',\sigma')$. Their exchange matrix element is:

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\psi_{\mathbf k\sigma}^{\ast}(\mathbf r)\psi_{\mathbf k'\sigma'}^{\ast}(\mathbf r')\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}\psi_{\mathbf k'\sigma'}(\mathbf r)\psi_{\mathbf k\sigma}(\mathbf r'). $$

spin 部分給出：

The spin part gives:

$$ \sum_{s}\chi_{\sigma}^{\ast}(s)\chi_{\sigma'}(s)=\delta_{\sigma\sigma'}. $$

因此只有相同 spin 的電子具有非零 exchange matrix element：

Therefore, only electrons with the same spin have a nonzero exchange matrix element.

將 plane waves 代入 spatial part：

Substituting the plane waves into the spatial part gives:

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\frac{\delta_{\sigma\sigma'}}{\Omega^{2}}\int d^{3}\mathbf r\int d^{3}\mathbf r'\,e^{-i\mathbf k\cdot\mathbf r}e^{-i\mathbf k'\cdot\mathbf r'}\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}e^{i\mathbf k'\cdot\mathbf r}e^{i\mathbf k\cdot\mathbf r'}. $$

定義 momentum difference：

Define the momentum difference:

$$ \mathbf Q=\mathbf k-\mathbf k'. $$

使用 finite-volume Coulomb expansion：

Using the finite-volume Coulomb expansion:

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}=\frac{1}{\Omega}\sum_{\mathbf q}\frac{4\pi}{q^{2}}e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}. $$

代入後，$\mathbf r$ 與 $\mathbf r'$ 的 exponential 可以分開：

After substitution, the exponentials involving $\mathbf r$ and $\mathbf r'$ separate:

$$ e^{-i\mathbf Q\cdot\mathbf r}e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}e^{i\mathbf Q\cdot\mathbf r'}=e^{i(\mathbf q-\mathbf Q)\cdot\mathbf r}e^{-i(\mathbf q-\mathbf Q)\cdot\mathbf r'}. $$

plane-wave orthonormality 使得只有 $\mathbf q=\mathbf Q$ 的項留下：

Plane-wave orthonormality leaves only the term with $\mathbf q=\mathbf Q$:

$$ \int_{\Omega}d^{3}\mathbf r\,e^{i(\mathbf q-\mathbf Q)\cdot\mathbf r}=\Omega\delta_{\mathbf q,\mathbf Q}. $$

因此 exchange matrix element 為：

Therefore, the exchange matrix element becomes:

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\delta_{\sigma\sigma'}\frac{4\pi}{\Omega\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

這個結果表示 exchange 只發生在 same-spin states 之間，而且 exchange strength 取決於 momentum difference $\lvert\mathbf k-\mathbf k'\rvert$。當兩個 $k$ states 很接近時，exchange matrix element 較大；當它們在 momentum space 中相距較遠時，exchange matrix element 較小。

This result shows that exchange occurs only between states with the same spin, and its strength depends on the momentum difference $\lvert\mathbf k-\mathbf k'\rvert$. When the two $k$ states are close in momentum space, the exchange matrix element is larger; when they are far apart, it is smaller.

---

## 7. Sum over all occupied states

exchange energy 為：

The exchange energy is:

$$ E_{x}=-\frac{1}{2}\sum_{\sigma,\sigma'}\sum_{\lvert\mathbf k\rvert\le k_{F}}\sum_{\lvert\mathbf k'\rvert\le k_{F}}\delta_{\sigma\sigma'}\frac{4\pi}{\Omega\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

spin sum 給出 factor 2：

The spin sum gives a factor of 2:

$$ \sum_{\sigma,\sigma'}\delta_{\sigma\sigma'}=2. $$

因此：

Therefore:

$$ E_{x}=-\frac{4\pi}{\Omega}\sum_{\lvert\mathbf k\rvert\le k_{F}}\sum_{\lvert\mathbf k'\rvert\le k_{F}}\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

在 thermodynamic limit：

In the thermodynamic limit:

$$ \Omega\rightarrow\infty,\qquad N\rightarrow\infty,\qquad \frac{N}{\Omega}=n. $$

將兩個 sums 轉成 integrals：

Convert the two sums into integrals:

$$ E_{x}=-\frac{4\pi}{\Omega}\left(\frac{\Omega}{(2\pi)^{3}}\right)^{2}\int_{\lvert\mathbf k\rvert\le k_{F}}d^{3}\mathbf k\int_{\lvert\mathbf k'\rvert\le k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

定義：

Define:

$$ I=\int_{\lvert\mathbf k\rvert\le k_{F}}d^{3}\mathbf k\int_{\lvert\mathbf k'\rvert\le k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

則：

Then:

$$ E_{x}=-\Omega\frac{4\pi}{(2\pi)^{6}}I. $$

因此 exchange energy per volume 為：

Therefore, the exchange energy per volume is:

$$ \frac{E_{x}}{\Omega}=-\frac{I}{16\pi^{5}}. $$

---

## 8. Evaluate the integral inside the Fermi sphere

由 spherical symmetry，可以固定 $\mathbf k$ 沿著 $z$ axis，並先對 $\mathbf k'$ 積分。

Because of spherical symmetry, we can choose $\mathbf k$ along the $z$ axis and first integrate over $\mathbf k'$.

定義：

Define:

$$ J(k)=\int_{\lvert\mathbf k'\rvert\le k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

令 $\mathbf k'$ 使用 spherical coordinates，$\theta$ 是 $\mathbf k$ 與 $\mathbf k'$ 之間的 angle。則：

Write $\mathbf k'$ in spherical coordinates, where $\theta$ is the angle between $\mathbf k$ and $\mathbf k'$. Then:

$$ \lvert\mathbf k-\mathbf k'\rvert^{2}=k^{2}+k'^{2}-2kk'\cos\theta. $$

因此：

Therefore:

$$ J(k)=2\pi\int_{0}^{k_{F}}k'^{2}dk'\int_{0}^{\pi}\frac{\sin\theta\,d\theta}{k^{2}+k'^{2}-2kk'\cos\theta}. $$

令 $u=\cos\theta$，則：

Let $u=\cos\theta$. Then:

$$ \int_{0}^{\pi}\frac{\sin\theta\,d\theta}{k^{2}+k'^{2}-2kk'\cos\theta}=\frac{1}{kk'}\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right). $$

所以：

Therefore:

$$ J(k)=\frac{2\pi}{k}\int_{0}^{k_{F}}k'\,dk'\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right). $$

再對 $\mathbf k$ 積分：

Now integrate over $\mathbf k$:

$$ I=\int_{\lvert\mathbf k\rvert\le k_{F}}d^{3}\mathbf k\,J(k). $$

因此：

Therefore:

$$ I=8\pi^{2}\int_{0}^{k_{F}}k\,dk\int_{0}^{k_{F}}k'\,dk'\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right). $$

---

## 9. Make the integral dimensionless

令 $k$ 和 $k'$ 相對於 $k_{F}$ 無因次化：

Scale $k$ and $k'$ by the Fermi wave vector:

$$ k=k_{F}x,\qquad k'=k_{F}y,\qquad 0\le x\le1,\qquad 0\le y\le1. $$

因此：

Therefore:

$$ I=8\pi^{2}k_{F}^{4}J_{0}. $$

其中：

where:

$$ J_{0}=\int_{0}^{1}x\,dx\int_{0}^{1}y\,dy\ln\left(\frac{x+y}{\lvert x-y\rvert}\right). $$

integrand 對交換 $x$ 與 $y$ 是 symmetric，因此可以只積分 square 的一半再乘 2：

The integrand is symmetric under exchange of $x$ and $y$, so we can integrate over half of the square and multiply by 2:

$$ J_{0}=2\int_{0}^{1}x\,dx\int_{0}^{x}y\,dy\ln\left(\frac{x+y}{x-y}\right). $$

令 $y=xt$，則 $dy=xdt$：

Let $y=xt$, so that $dy=xdt$:

$$ J_{0}=2\int_{0}^{1}x^{3}dx\int_{0}^{1}t\,dt\ln\left(\frac{1+t}{1-t}\right). $$

定義：

Define:

$$ A=\int_{0}^{1}t\ln\left(\frac{1+t}{1-t}\right)dt. $$

使用 power-series expansion：

Using the power-series expansion:

$$ \ln\left(\frac{1+t}{1-t}\right)=2\sum_{m=0}^{\infty}\frac{t^{2m+1}}{2m+1}. $$

因此：

Therefore:

$$ A=2\sum_{m=0}^{\infty}\frac{1}{2m+1}\int_{0}^{1}t^{2m+2}dt. $$

而：

Since:

$$ \int_{0}^{1}t^{2m+2}dt=\frac{1}{2m+3}, $$

所以：

we obtain:

$$ A=2\sum_{m=0}^{\infty}\frac{1}{(2m+1)(2m+3)}. $$

利用 telescoping form：

Using the telescoping form:

$$ \frac{2}{(2m+1)(2m+3)}=\frac{1}{2m+1}-\frac{1}{2m+3}, $$

得到：

we obtain:

$$ A=1. $$

因此：

Therefore:

$$ J_{0}=2\left(\int_{0}^{1}x^{3}dx\right)A=2\left(\frac{1}{4}\right)(1)=\frac{1}{2}. $$

所以：

Thus:

$$ I=8\pi^{2}k_{F}^{4}\left(\frac{1}{2}\right)=4\pi^{2}k_{F}^{4}. $$

---

## 10. Exchange energy of the uniform electron gas

代回 exchange energy per volume：

Substituting the result back into the exchange energy per volume:

$$ \frac{E_{x}}{\Omega}=-\frac{1}{16\pi^{5}}\left(4\pi^{2}k_{F}^{4}\right)=-\frac{k_{F}^{4}}{4\pi^{3}}. $$

每個電子的 exchange energy 定義為：

The exchange energy per electron is defined as:

$$ \varepsilon_{x}=\frac{E_{x}}{N}=\frac{E_{x}/\Omega}{N/\Omega}=\frac{E_{x}/\Omega}{n}. $$

因為：

Because:

$$ n=\frac{k_{F}^{3}}{3\pi^{2}}, $$

所以：

we obtain:

$$ \varepsilon_{x}=-\frac{3k_{F}}{4\pi}. $$

再使用：

Using:

$$ k_{F}=(3\pi^{2}n)^{1/3}, $$

得到 uniform electron gas 的 one-electron exchange energy：

we obtain the exchange energy per electron of the uniform electron gas:

$$ \varepsilon_{x}(n)=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}n^{1/3}. $$

exchange energy per volume 為：

The exchange energy per volume is:

$$ e_{x}(n)=n\varepsilon_{x}(n)=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}n^{4/3}. $$

uniform electron gas 的 total exchange energy 可以寫成：

The total exchange energy of the uniform electron gas can be written as:

$$ E_{x}=\Omega e_{x}(n)=N\varepsilon_{x}(n). $$

---

## 11. Local Density Approximation for exchange

對 non-uniform system，LDA 的想法是在每一個 position $\mathbf r$，把附近電子視為一個 density 等於 local density $n(\mathbf r)$ 的 uniform electron gas。

For a non-uniform system, LDA treats the neighborhood of each position $\mathbf r$ as a uniform electron gas with density equal to the local density $n(\mathbf r)$.

因此 local exchange energy per electron 為：

Therefore, the local exchange energy per electron is:

$$ \varepsilon_{x}(n(\mathbf r))=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}[n(\mathbf r)]^{1/3}. $$

local exchange energy density 為：

The local exchange energy density is:

$$ e_{x}(n(\mathbf r))=n(\mathbf r)\varepsilon_{x}(n(\mathbf r))=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}[n(\mathbf r)]^{4/3}. $$

最後對 real space 積分，得到 LDA exchange functional：

Finally, integrating over real space gives the LDA exchange functional:

$$ E_{x}^{\mathrm{LDA}}[n]=\int d^{3}\mathbf r\,n(\mathbf r)\varepsilon_{x}(n(\mathbf r)). $$

也就是：

Equivalently:

$$ E_{x}^{\mathrm{LDA}}[n]=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}\int d^{3}\mathbf r\,[n(\mathbf r)]^{4/3}. $$

這就是手寫筆記最後由 uniform electron gas exchange energy 導向 LDA exchange energy 的結果。

This is the final result in the handwritten notes: the exchange energy of the uniform electron gas is used locally to construct the LDA exchange functional for a non-uniform density.
