# Exchange energy in a uniform electron gas and the LDA exchange functional

這份筆記的目標不是直接背誦 LDA 的交換能公式，而是從均勻電子氣體的單電子平面波開始，一步一步推導出 exchange energy，最後再把均勻系統的結果用到非均勻電子密度 $n(\mathbf r)$ 上。

The purpose of these notes is not to simply memorize the LDA exchange formula. The idea is to start from the plane-wave states of a uniform electron gas, derive the exchange energy step by step, and finally use the uniform-gas result locally for a non-uniform density $n(\mathbf r)$.

整體邏輯是：

The logical chain is:

```text
plane wave
→ occupied electron states inside the Fermi sphere
→ relation between n and k_F
→ exchange matrix element
→ sum over all occupied states
→ exchange energy of the uniform electron gas
→ local-density approximation

```

---

## 1. Why plane waves are used for a uniform electron gas

均勻電子氣體沒有特別的原子位置，也沒有一個空間方向比其他方向更特殊。因此可以把電子放在一個體積為 $\Omega=L^{3}$ 的盒子中，並使用 periodic boundary condition。

A uniform electron gas has no special atomic position and no preferred direction in space. Therefore, we can place the electrons in a box of volume $\Omega=L^{3}$ and impose periodic boundary conditions.

例如在 $x$ 方向，

For example, in the $x$ direction,

$$ \psi(x+L,y,z)=\psi(x,y,z). $$

對這種具有平移對稱性的系統，單電子軌域自然可以選成 plane wave。

For a translationally invariant system, the natural single-electron orbitals are plane waves.

加入 spin 後，可以把單電子態寫成

Including spin, a single-electron state can be written as

$$ \psi_{\mathbf k\sigma}(\mathbf r,s)=\phi_{\mathbf k}(\mathbf r)\chi_{\sigma}(s)=\frac{1}{\sqrt{\Omega}}e^{i\mathbf k\cdot\mathbf r}\chi_{\sigma}(s). $$

其中 $\phi_{\mathbf k}(\mathbf r)$ 是空間部分，而 $\chi_{\sigma}(s)$ 是 spin wave function。

Here, $\phi_{\mathbf k}(\mathbf r)$ is the spatial part and $\chi_{\sigma}(s)$ is the spin wave function.

spin 只有兩種可能狀態，可以記成 $\uparrow$ 與 $\downarrow$。

There are two possible spin states, which can be denoted by $\uparrow$ and $\downarrow$.

spin wave functions 滿足正交條件：

The spin wave functions satisfy the orthonormality condition:

$$ \sum_{s}\chi_{\sigma}^{\ast}(s)\chi_{\sigma'}(s)=\delta_{\sigma\sigma'}. $$

這個 $\delta_{\sigma\sigma'}$ 之後會很重要，因為它會告訴我們 exchange 只發生在相同 spin 的電子之間。

This $\delta_{\sigma\sigma'}$ will become important later, because it tells us that the exchange term survives only for electrons with the same spin.

---

## 2. Normalization of the plane wave

plane wave 必須滿足 normalization。

The plane wave must be normalized.

$$ \int_{\Omega}d^{3}\mathbf r\,\lvert\phi_{\mathbf k}(\mathbf r)\rvert^{2}=1. $$

代入

Substituting

$$ \phi_{\mathbf k}(\mathbf r)=\frac{1}{\sqrt{\Omega}}e^{i\mathbf k\cdot\mathbf r}, $$

得到

we obtain

$$ \int_{\Omega}d^{3}\mathbf r\,\frac{1}{\Omega}e^{-i\mathbf k\cdot\mathbf r}e^{i\mathbf k\cdot\mathbf r}=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r=1. $$

因此 normalization coefficient 是 $1/\sqrt{\Omega}$。

Therefore, the normalization coefficient is $1/\sqrt{\Omega}$.

對不同的 $\mathbf k$ 與 $\mathbf k'$，plane waves 也滿足 orthonormality：

Plane waves with different $\mathbf k$ and $\mathbf k'$ also satisfy orthonormality:

$$ \int_{\Omega}d^{3}\mathbf r\,\phi_{\mathbf k}^{\ast}(\mathbf r)\phi_{\mathbf k'}(\mathbf r)=\delta_{\mathbf k,\mathbf k'}. $$

因為

because

$$ \int_{\Omega}d^{3}\mathbf r\,\phi_{\mathbf k}^{\ast}(\mathbf r)\phi_{\mathbf k'}(\mathbf r)=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,e^{i(\mathbf k'-\mathbf k)\cdot\mathbf r}. $$

只有當 $\mathbf k=\mathbf k'$ 時，積分才不會因相位互相抵消而變成零。

Only when $\mathbf k=\mathbf k'$ does the integral remain nonzero; otherwise the oscillating phases cancel.

---

## 3. Periodic boundary condition quantizes the momentum

現在把 periodic boundary condition 套到 plane wave 上。

Now apply the periodic boundary condition to the plane wave.

在 $x$ 方向，

In the $x$ direction,

$$ e^{ik_{x}(x+L)}=e^{ik_{x}x}. $$

因此

Therefore,

$$ e^{ik_{x}L}=1=e^{i2\pi n_{x}}. $$

所以允許的 $k_x$ 只能取

Thus, the allowed values of $k_x$ are

$$ k_{x}=\frac{2\pi}{L}n_{x}. $$

同理，

Similarly,

$$ k_{y}=\frac{2\pi}{L}n_{y},\qquad k_{z}=\frac{2\pi}{L}n_{z}. $$

因此相鄰兩個 $k$-points 的距離是

Therefore, the spacing between neighboring $k$-points is

$$ \Delta k_{x}=\Delta k_{y}=\Delta k_{z}=\frac{2\pi}{L}. $$

一個允許的 $k$-state 在 momentum space 中所佔的體積就是

The volume occupied by one allowed $k$-state in momentum space is therefore

$$ \Delta^{3}k=\Delta k_{x}\Delta k_{y}\Delta k_{z}=\left(\frac{2\pi}{L}\right)^{3}=\frac{(2\pi)^{3}}{\Omega}. $$

所以在 thermodynamic limit 中，

Therefore, in the thermodynamic limit,

$$ \sum_{\mathbf k}\longrightarrow\frac{\Omega}{(2\pi)^{3}}\int d^{3}\mathbf k. $$

這一步很重要，因為後面我們要把「所有 occupied states 的離散加總」改寫成 momentum-space integral。

This step is important because later we will convert the discrete sum over all occupied states into an integral over momentum space.

---

## 4. Electrons fill a Fermi sphere

對自由電子，在 Hartree atomic units 中，

For free electrons in Hartree atomic units,

$$ \varepsilon_{\mathbf k}=\frac{k^{2}}{2}. $$

在 $T=0$ 的基態中，電子會從最低能量開始依序填滿。

At $T=0$, the ground state is formed by filling the lowest-energy states first.

由於能量只依賴 $k=\lvert\mathbf k\rvert$，所以所有

Because the energy depends only on $k=\lvert\mathbf k\rvert$, all states satisfying

$$ \lvert\mathbf k\rvert\leq k_{F} $$

的狀態會被填滿。

are occupied.

在三維 $k$-space 中，這些 occupied states 形成一個球，因此叫做 Fermi sphere。

In three-dimensional $k$-space, these occupied states form a sphere, called the Fermi sphere.

每一個 $\mathbf k$-point 可以放兩個電子，一個 spin up，一個 spin down。

Each $\mathbf k$-point can contain two electrons, one spin up and one spin down.

---

## 5. Relation between the electron density $n$ and $k_{F}$

下一步要把 electron density $n$ 和 Fermi wave vector $k_{F}$ 連起來。

The next step is to connect the electron density $n$ with the Fermi wave vector $k_{F}$.

對均勻電子氣體，

For a uniform electron gas,

$$ n=\frac{N}{\Omega}. $$

從所有 occupied single-electron states 出發，

Starting from all occupied single-electron states,

$$ n=\sum_{\sigma}\sum_{\lvert\mathbf k\rvert\leq k_{F}}\lvert\psi_{\mathbf k\sigma}(\mathbf r,s)\rvert^{2}. $$

每個 spatial plane wave 的機率密度是 $1/\Omega$，所以

The probability density of each spatial plane wave is $1/\Omega$, so

$$ n=\frac{1}{\Omega}\sum_{\sigma}\sum_{\lvert\mathbf k\rvert\leq k_{F}}1. $$

spin sum 給出 factor 2：

The spin sum gives a factor of 2:

$$ n=\frac{2}{\Omega}\sum_{\lvert\mathbf k\rvert\leq k_{F}}1. $$

現在使用前面得到的 sum-to-integral relation：

Now use the sum-to-integral relation obtained above:

$$ n=2\int_{\lvert\mathbf k\rvert\leq k_{F}}\frac{d^{3}\mathbf k}{(2\pi)^{3}}. $$

因為 occupied region 是一個球，所以改用 spherical coordinates：

Because the occupied region is a sphere, use spherical coordinates:

$$ d^{3}\mathbf k=k^{2}\sin\theta\,dk\,d\theta\,d\phi. $$

因此

Therefore,

$$ n=\frac{2}{(2\pi)^{3}}\int_{0}^{k_{F}}k^{2}dk\int_{0}^{\pi}\sin\theta\,d\theta\int_{0}^{2\pi}d\phi. $$

角度積分給出

The angular integrals give

$$ \int_{0}^{\pi}\sin\theta\,d\theta=2,\qquad\int_{0}^{2\pi}d\phi=2\pi. $$

因此

Therefore,

$$ n=\frac{2}{(2\pi)^{3}}\frac{k_{F}^{3}}{3}(4\pi). $$

整理後得到

After simplification,

$$ n=\frac{k_{F}^{3}}{3\pi^{2}}. $$

所以

Thus,

$$ k_{F}=(3\pi^{2}n)^{1/3}. $$

這個關係非常重要，因為後面先把 exchange energy 寫成 $k_F$ 的函數，最後再利用這條式子把結果改寫成 density $n$ 的函數。

This relation is essential because we will first derive the exchange energy as a function of $k_F$, and then use this equation to rewrite the final result as a function of the density $n$.

---

## 6. Starting point of the exchange energy

對 Slater determinant，exchange energy 可以寫成 occupied orbitals 之間的 exchange matrix elements 的總和。

For a Slater determinant, the exchange energy can be written as a sum of exchange matrix elements between occupied orbitals.

$$ E_{x}=-\frac{1}{2}\sum_{i}^{\mathrm{occ}}\sum_{j}^{\mathrm{occ}}\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\psi_{i}^{\ast}(\mathbf r)\psi_{j}^{\ast}(\mathbf r')\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}\psi_{j}(\mathbf r)\psi_{i}(\mathbf r'). $$

我們真正需要處理的困難部分是 Coulomb kernel

The difficult part is the Coulomb kernel

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}. $$

它在 real space 裡和兩個座標 $\mathbf r$ 及 $\mathbf r'$ 綁在一起，不容易直接和 plane waves 一起積分。

In real space it couples the two coordinates $\mathbf r$ and $\mathbf r'$, which makes the plane-wave integrals inconvenient.

因此筆記下一步不是直接硬算 real-space integral，而是先把 Coulomb interaction 做 Fourier transform。

Therefore, instead of directly evaluating the real-space integral, the next step is to Fourier transform the Coulomb interaction.

---

## 7. Fourier transform of the Coulomb potential

令

Let

$$ \mathbf R=\mathbf r-\mathbf r'. $$

Coulomb potential 可以寫成

The Coulomb potential is

$$ V(\mathbf R)=\frac{1}{R}. $$

它的 Fourier transform 是

Its Fourier transform is

$$ V(\mathbf q)=\int d^{3}\mathbf R\,e^{-i\mathbf q\cdot\mathbf R}\frac{1}{R}. $$

因為 $1/R$ 具有 spherical symmetry，所以積分結果只會依賴 $q=\lvert\mathbf q\rvert$，不會依賴 $\mathbf q$ 的方向。

Because $1/R$ is spherically symmetric, the result depends only on $q=\lvert\mathbf q\rvert$, not on the direction of $\mathbf q$.

因此可以把 $\mathbf q$ 選在 $z$-axis 上：

Therefore, we can choose $\mathbf q$ along the $z$-axis:

$$ \mathbf q=(0,0,q). $$

這樣

Then,

$$ \mathbf q\cdot\mathbf R=qR\cos\theta. $$

用 spherical coordinates，

Using spherical coordinates,

$$ d^{3}\mathbf R=R^{2}\sin\theta\,dR\,d\theta\,d\phi. $$

所以

Thus,

$$ V(q)=\int_{0}^{\infty}R^{2}dR\int_{0}^{\pi}\sin\theta\,d\theta\int_{0}^{2\pi}d\phi\,e^{-iqR\cos\theta}\frac{1}{R}. $$

先做 $\phi$ 積分：

First perform the $\phi$ integral:

$$ V(q)=2\pi\int_{0}^{\infty}R\,dR\int_{0}^{\pi}\sin\theta\,e^{-iqR\cos\theta}d\theta. $$

令

Let

$$ \mu=\cos\theta,\qquad d\mu=-\sin\theta\,d\theta. $$

當 $\theta=0$ 時 $\mu=1$，當 $\theta=\pi$ 時 $\mu=-1$。

When $\theta=0$, $\mu=1$, and when $\theta=\pi$, $\mu=-1$.

因此

Therefore,

$$ \int_{0}^{\pi}\sin\theta\,e^{-iqR\cos\theta}d\theta=\int_{-1}^{1}e^{-iqR\mu}d\mu. $$

直接積分：

Integrating directly,

$$ \int_{-1}^{1}e^{-iqR\mu}d\mu=\frac{e^{-iqR}-e^{iqR}}{-iqR}. $$

利用

Using

$$ e^{ix}-e^{-ix}=2i\sin x, $$

得到

we obtain

$$ \int_{-1}^{1}e^{-iqR\mu}d\mu=\frac{2\sin(qR)}{qR}. $$

因此

Therefore,

$$ V(q)=2\pi\int_{0}^{\infty}R\,dR\,\frac{2\sin(qR)}{qR}. $$

整理為

This becomes

$$ V(q)=\frac{4\pi}{q}\int_{0}^{\infty}\sin(qR)dR. $$

---

## 8. Why a convergence factor is introduced

上面的積分

The integral

$$ \int_{0}^{\infty}\sin(qR)dR $$

不是普通意義下容易直接處理的收斂積分。

is not a normally convergent integral in the usual sense.

因此手寫筆記加入一個 convergence factor：

Therefore, the handwritten notes introduce a convergence factor:

$$ e^{-\eta R},\qquad\eta>0. $$

先計算

We first evaluate

$$ I(\eta)=\int_{0}^{\infty}e^{-\eta R}\sin(qR)dR, $$

最後再取

and then take the limit

$$ \eta\rightarrow0^{+}. $$

利用

Using

$$ \sin(qR)=\mathrm{Im}\left(e^{iqR}\right), $$

可以寫成

we can write

$$ I(\eta)=\mathrm{Im}\int_{0}^{\infty}e^{-(\eta-iq)R}dR. $$

因為 $\eta>0$，上限 $R\rightarrow\infty$ 時 exponential 會衰減。

Because $\eta>0$, the exponential decays as $R\rightarrow\infty$.

因此

Thus,

$$ \int_{0}^{\infty}e^{-(\eta-iq)R}dR=\frac{1}{\eta-iq}. $$

而

and

$$ \frac{1}{\eta-iq}=\frac{\eta+iq}{\eta^{2}+q^{2}}. $$

取 imaginary part：

Taking the imaginary part,

$$ I(\eta)=\frac{q}{\eta^{2}+q^{2}}. $$

最後令 $\eta\rightarrow0^{+}$：

Finally, taking $\eta\rightarrow0^{+}$,

$$ \int_{0}^{\infty}\sin(qR)dR=\frac{1}{q}. $$

因此 Coulomb potential 的 Fourier transform 為

Therefore, the Fourier transform of the Coulomb potential is

$$ V(q)=\frac{4\pi}{q^{2}}. $$

也就是

That is,

$$ \int d^{3}\mathbf R\,\frac{e^{-i\mathbf q\cdot\mathbf R}}{R}=\frac{4\pi}{q^{2}}. $$

---

## 9. Why the Coulomb interaction is easier in momentum space

Fourier inverse transform 給出

The inverse Fourier transform gives

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}=\int\frac{d^{3}\mathbf q}{(2\pi)^{3}}\frac{4\pi}{q^{2}}e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}. $$

這一步的物理與數學意義都很重要。

This step is important both physically and mathematically.

在 real space 中，

In real space,

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert} $$

同時依賴 $\mathbf r$ 和 $\mathbf r'$。

depends on $\mathbf r$ and $\mathbf r'$ together.

但做 Fourier transform 後，

After the Fourier transform,

$$ e^{i\mathbf q\cdot(\mathbf r-\mathbf r')}=e^{i\mathbf q\cdot\mathbf r}e^{-i\mathbf q\cdot\mathbf r'}. $$

因此 $\mathbf r$ 與 $\mathbf r'$ 的 dependence 被拆開，後面可以分別使用 plane-wave orthogonality。

Thus, the dependence on $\mathbf r$ and $\mathbf r'$ is separated, allowing the two integrals to be treated using plane-wave orthogonality.

這就是為什麼 exchange matrix element 在 momentum space 裡比在 real space 裡容易計算。

This is why the exchange matrix element is much easier to evaluate in momentum space than in real space.

---

## 10. Exchange matrix element between two plane-wave states

取兩個 occupied states：

Consider two occupied states:

$$ i=(\mathbf k,\sigma),\qquad j=(\mathbf k',\sigma'). $$

exchange matrix element 為

The exchange matrix element is

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\psi_{\mathbf k\sigma}^{\ast}(\mathbf r)\psi_{\mathbf k'\sigma'}^{\ast}(\mathbf r')\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}\psi_{\mathbf k'\sigma'}(\mathbf r)\psi_{\mathbf k\sigma}(\mathbf r'). $$

先處理 spin part。

First consider the spin part.

由 spin orthogonality，

From spin orthogonality,

$$ \sum_{s}\chi_{\sigma}^{\ast}(s)\chi_{\sigma'}(s)=\delta_{\sigma\sigma'}. $$

因此 exchange matrix element 會帶有

Therefore, the exchange matrix element contains

$$ \delta_{\sigma\sigma'}. $$

如果 $\sigma\neq\sigma'$，exchange matrix element 為零。

If $\sigma\neq\sigma'$, the exchange matrix element vanishes.

所以 exchange 只發生在相同 spin 的電子之間。

Thus, exchange occurs only between electrons with the same spin.

---

## 11. Spatial part of the exchange matrix element

現在代入 plane waves：

Now substitute the plane waves:

$$ \phi_{\mathbf k}(\mathbf r)=\frac{1}{\sqrt{\Omega}}e^{i\mathbf k\cdot\mathbf r}. $$

因此 spatial part 變成

The spatial part becomes

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\frac{\delta_{\sigma\sigma'}}{\Omega^{2}}\int d^{3}\mathbf r\int d^{3}\mathbf r'\,e^{-i\mathbf k\cdot\mathbf r}e^{-i\mathbf k'\cdot\mathbf r'}\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}e^{i\mathbf k'\cdot\mathbf r}e^{i\mathbf k\cdot\mathbf r'}. $$

把 exponent 合併：

Combine the exponentials:

$$ e^{-i\mathbf k\cdot\mathbf r}e^{i\mathbf k'\cdot\mathbf r}=e^{-i(\mathbf k-\mathbf k')\cdot\mathbf r}, $$

以及

and

$$ e^{-i\mathbf k'\cdot\mathbf r'}e^{i\mathbf k\cdot\mathbf r'}=e^{i(\mathbf k-\mathbf k')\cdot\mathbf r'}. $$

定義 momentum transfer：

Define the momentum transfer:

$$ \mathbf q=\mathbf k-\mathbf k'. $$

所以

Then,

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\frac{\delta_{\sigma\sigma'}}{\Omega^{2}}\int d^{3}\mathbf r\int d^{3}\mathbf r'\,e^{-i\mathbf q\cdot\mathbf r}\frac{1}{\lvert\mathbf r-\mathbf r'\rvert}e^{i\mathbf q\cdot\mathbf r'}. $$

---

## 12. Insert the Fourier representation of the Coulomb interaction

使用前面得到的

Using the result obtained above,

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}=\int\frac{d^{3}\mathbf Q}{(2\pi)^{3}}\frac{4\pi}{Q^{2}}e^{i\mathbf Q\cdot(\mathbf r-\mathbf r')}. $$

代入 exchange matrix element：

Substituting into the exchange matrix element,

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\frac{\delta_{\sigma\sigma'}}{\Omega^{2}}\int\frac{d^{3}\mathbf Q}{(2\pi)^{3}}\frac{4\pi}{Q^{2}}\int d^{3}\mathbf r\,e^{i(\mathbf Q-\mathbf q)\cdot\mathbf r}\int d^{3}\mathbf r'\,e^{-i(\mathbf Q-\mathbf q)\cdot\mathbf r'}. $$

現在兩個 real-space integrals 已經完全分開。

Now the two real-space integrals are completely separated.

plane-wave orthogonality 會要求

Plane-wave orthogonality imposes

$$ \mathbf Q=\mathbf q. $$

這就是 momentum selection condition。

This is the momentum selection condition.

因此最後只剩下 Coulomb Fourier component 在

Therefore, only the Coulomb Fourier component at

$$ \mathbf q=\mathbf k-\mathbf k' $$

的位置。

survives.

最後得到

The final exchange matrix element is

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}=\delta_{\sigma\sigma'}\frac{4\pi}{\Omega\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

---

## 13. Physical meaning of the exchange matrix element

這個結果直接告訴我們 exchange strength 和兩個電子的 momentum difference 有關：

This result directly shows that the exchange strength depends on the momentum difference between two electrons:

$$ K_{\mathbf k\sigma,\mathbf k'\sigma'}\propto\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

當 $\mathbf k$ 和 $\mathbf k'$ 很接近時，

When $\mathbf k$ and $\mathbf k'$ are close,

$$ \lvert\mathbf k-\mathbf k'\rvert $$

很小，因此 exchange matrix element 較大。

is small, so the exchange matrix element is stronger.

當兩個 momentum 相差很大時，exchange matrix element 就較弱。

When the two momenta are far apart, the exchange matrix element is weaker.

手寫筆記把這件事理解成兩個 plane waves 的 overlap 形成具有 wave vector

The handwritten notes interpret this through the overlap of two plane waves, which creates an oscillatory pattern with wave vector

$$ \mathbf q=\mathbf k-\mathbf k'. $$

因此 $\mathbf q$ 越小，兩個波的變化尺度越長，exchange contribution 也越強。

Thus, a smaller $\mathbf q$ corresponds to a longer spatial variation scale and a stronger exchange contribution.

---

## 14. Sum over all occupied states

現在要把所有 Fermi sphere 裡的 occupied states 都加起來。

We now sum over all occupied states inside the Fermi sphere.

exchange energy 為

The exchange energy is

$$ E_{x}=-\frac{1}{2}\sum_{\sigma,\sigma'}\sum_{\lvert\mathbf k\rvert\leq k_{F}}\sum_{\lvert\mathbf k'\rvert\leq k_{F}}K_{\mathbf k\sigma,\mathbf k'\sigma'}. $$

代入 exchange matrix element：

Substituting the exchange matrix element,

$$ E_{x}=-\frac{1}{2}\sum_{\sigma,\sigma'}\sum_{\lvert\mathbf k\rvert\leq k_{F}}\sum_{\lvert\mathbf k'\rvert\leq k_{F}}\delta_{\sigma\sigma'}\frac{4\pi}{\Omega\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

spin sum 中只有 $\sigma=\sigma'$ 的兩種情況留下來，所以

Only the two cases with $\sigma=\sigma'$ survive in the spin sum, so

$$ \sum_{\sigma,\sigma'}\delta_{\sigma\sigma'}=2. $$

因此

Therefore,

$$ E_{x}=-\frac{4\pi}{\Omega}\sum_{\lvert\mathbf k\rvert\leq k_{F}}\sum_{\lvert\mathbf k'\rvert\leq k_{F}}\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

在 thermodynamic limit 中，

In the thermodynamic limit,

$$ \sum_{\mathbf k}\longrightarrow\frac{\Omega}{(2\pi)^{3}}\int d^{3}\mathbf k. $$

所以

Therefore,

$$ E_{x}=-\frac{4\pi}{\Omega}\left(\frac{\Omega}{(2\pi)^{3}}\right)^{2}\int_{\lvert\mathbf k\rvert\leq k_{F}}d^{3}\mathbf k\int_{\lvert\mathbf k'\rvert\leq k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

整理 prefactor：

Collecting the prefactor,

$$ E_{x}=-\frac{\Omega}{16\pi^{5}}I, $$

其中

where

$$ I=\int_{\lvert\mathbf k\rvert\leq k_{F}}d^{3}\mathbf k\int_{\lvert\mathbf k'\rvert\leq k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

所以問題現在變成：如何計算這個六維積分 $I$。

The problem is now reduced to evaluating the six-dimensional integral $I$.

---

## 15. Reduce the six-dimensional integral

先定義

First define

$$ J(k)=\int_{\lvert\mathbf k'\rvert\leq k_{F}}d^{3}\mathbf k'\frac{1}{\lvert\mathbf k-\mathbf k'\rvert^{2}}. $$

那麼

Then,

$$ I=\int_{\lvert\mathbf k\rvert\leq k_{F}}d^{3}\mathbf k\,J(k). $$

由於 Fermi sphere 具有 spherical symmetry，而且 integrand 只依賴 $\lvert\mathbf k-\mathbf k'\rvert$，所以 $J$ 只依賴 $k=\lvert\mathbf k\rvert$，不依賴 $\mathbf k$ 的方向。

Because the Fermi sphere is spherically symmetric and the integrand depends only on $\lvert\mathbf k-\mathbf k'\rvert$, $J$ depends only on $k=\lvert\mathbf k\rvert$, not on the direction of $\mathbf k$.

因此可以把 $\mathbf k$ 選在 $z$-axis：

Therefore, choose $\mathbf k$ along the $z$-axis:

$$ \mathbf k=(0,0,k). $$

再把 $\mathbf k'$ 寫成 spherical coordinates：

Write $\mathbf k'$ in spherical coordinates:

$$ \mathbf k'=(k'\sin\theta\cos\phi,k'\sin\theta\sin\phi,k'\cos\theta). $$

則

Then,

$$ \lvert\mathbf k-\mathbf k'\rvert^{2}=k^{2}+k'^{2}-2kk'\cos\theta. $$

所以

Therefore,

$$ J(k)=\int_{0}^{k_{F}}k'^{2}dk'\int_{0}^{\pi}\sin\theta\,d\theta\int_{0}^{2\pi}d\phi\,\frac{1}{k^{2}+k'^{2}-2kk'\cos\theta}. $$

先做 $\phi$ 積分：

First perform the $\phi$ integral:

$$ J(k)=2\pi\int_{0}^{k_{F}}k'^{2}dk'\int_{0}^{\pi}\frac{\sin\theta\,d\theta}{k^{2}+k'^{2}-2kk'\cos\theta}. $$

---

## 16. Angular integral

令

Let

$$ u=\cos\theta,\qquad du=-\sin\theta\,d\theta. $$

則

Then,

$$ \int_{0}^{\pi}\frac{\sin\theta\,d\theta}{k^{2}+k'^{2}-2kk'\cos\theta}=\int_{-1}^{1}\frac{du}{k^{2}+k'^{2}-2kk'u}. $$

令

Define

$$ a=k^{2}+k'^{2},\qquad b=2kk'. $$

則

Then,

$$ \int\frac{du}{a-bu}=-\frac{1}{b}\ln(a-bu). $$

所以

Therefore,

$$ \int_{-1}^{1}\frac{du}{a-bu}=\frac{1}{b}\ln\left(\frac{a+b}{a-b}\right). $$

注意

Notice that

$$ a+b=(k+k')^{2}, $$

而

and

$$ a-b=(k-k')^{2}. $$

因此

Therefore,

$$ \int_{-1}^{1}\frac{du}{k^{2}+k'^{2}-2kk'u}=\frac{1}{2kk'}\ln\left(\frac{(k+k')^{2}}{(k-k')^{2}}\right). $$

利用

Using

$$ \ln\left(\frac{A^{2}}{B^{2}}\right)=2\ln\left(\frac{\lvert A\rvert}{\lvert B\rvert}\right), $$

得到

we obtain

$$ \int_{-1}^{1}\frac{du}{k^{2}+k'^{2}-2kk'u}=\frac{1}{kk'}\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right). $$

所以

Thus,

$$ J(k)=\frac{2\pi}{k}\int_{0}^{k_{F}}k'\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right)dk'. $$

---

## 17. Put $J(k)$ back into $I$

因為 $J(k)$ 只依賴 $k$，外層 $\mathbf k$-integral 也可以使用 spherical coordinates：

Since $J(k)$ depends only on $k$, the outer $\mathbf k$-integral can also be evaluated in spherical coordinates:

$$ I=4\pi\int_{0}^{k_{F}}k^{2}J(k)dk. $$

代入 $J(k)$：

Substituting $J(k)$,

$$ I=8\pi^{2}\int_{0}^{k_{F}}k\,dk\int_{0}^{k_{F}}k'\,dk'\ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right). $$

現在積分只剩兩個 scalar variables $k$ 和 $k'$，原來的六維積分已經被大幅簡化。

The original six-dimensional integral has now been reduced to a two-variable scalar integral over $k$ and $k'$.

---

## 18. Why dimensionless variables are introduced

下一步手寫筆記定義

The handwritten notes next define

$$ k=k_{F}x,\qquad k'=k_{F}y. $$

其中

with

$$ 0\leq x\leq1,\qquad0\leq y\leq1. $$

這樣做的目的，是把所有具有 dimension 的部分抽成 $k_{F}$ 的次方，剩下的積分就只是純數字。

The purpose is to factor out all dimensional dependence into a power of $k_F$, leaving only a dimensionless numerical integral.

由

From

$$ dk=k_{F}dx,\qquad dk'=k_{F}dy, $$

可得

we obtain

$$ k\,dk=k_{F}^{2}x\,dx,\qquad k'\,dk'=k_{F}^{2}y\,dy. $$

而 logarithm 中的 $k_F$ 會約掉：

The factor $k_F$ cancels inside the logarithm:

$$ \ln\left(\frac{k+k'}{\lvert k-k'\rvert}\right)=\ln\left(\frac{x+y}{\lvert x-y\rvert}\right). $$

因此

Therefore,

$$ I=8\pi^{2}k_{F}^{4}\int_{0}^{1}x\,dx\int_{0}^{1}y\,dy\ln\left(\frac{x+y}{\lvert x-y\rvert}\right). $$

定義 dimensionless integral

Define the dimensionless integral

$$ \mathcal J=\int_{0}^{1}x\,dx\int_{0}^{1}y\,dy\ln\left(\frac{x+y}{\lvert x-y\rvert}\right). $$

因此

Then,

$$ I=8\pi^{2}k_{F}^{4}\mathcal J. $$

---

## 19. Why the square is split into two triangles

積分區域是

The integration region is

$$ 0\leq x\leq1,\qquad0\leq y\leq1. $$

也就是 $x-y$ 平面上的一個 unit square。

This is a unit square in the $x-y$ plane.

但是 integrand 中有

However, the integrand contains

$$ \lvert x-y\rvert. $$

因此在 $y<x$ 和 $y>x$ 兩個區域中，absolute value 的形式不同。

Thus, the absolute value takes different forms in the regions $y<x$ and $y>x$.

同時 integrand

At the same time, the integrand

$$ f(x,y)=xy\ln\left(\frac{x+y}{\lvert x-y\rvert}\right) $$

在交換 $x$ 和 $y$ 後不變：

is symmetric under exchange of $x$ and $y$:

$$ f(x,y)=f(y,x). $$

因此 unit square 可以沿著 $y=x$ 分成上下兩個 triangle，而且兩邊的積分相同。

Therefore, the unit square can be split along $y=x$ into two triangles, and both contributions are equal.

所以

Thus,

$$ \mathcal J=2\int_{0}^{1}dx\int_{0}^{x}dy\,xy\ln\left(\frac{x+y}{x-y}\right). $$

這就是手寫筆記中畫 triangle 的原因。

This is why the handwritten notes draw and use the triangular integration region.

---

## 20. Substitute $y=xt$

在 lower triangle 中，

Inside the lower triangle,

$$ 0\leq y\leq x. $$

令

Let

$$ y=xt. $$

那麼

Then,

$$ dy=x\,dt, $$

而當 $y=0$ 時 $t=0$，當 $y=x$ 時 $t=1$。

When $y=0$, $t=0$, and when $y=x$, $t=1$.

同時

Also,

$$ x+y=x(1+t), $$

以及

and

$$ x-y=x(1-t). $$

所以

Therefore,

$$ \ln\left(\frac{x+y}{x-y}\right)=\ln\left(\frac{1+t}{1-t}\right). $$

而 measure 變成

The measure becomes

$$ xy\,dx\,dy=x(xt)\,dx\,(x\,dt)=x^{3}t\,dx\,dt. $$

因此

Therefore,

$$ \mathcal J=2\int_{0}^{1}x^{3}dx\int_{0}^{1}t\ln\left(\frac{1+t}{1-t}\right)dt. $$

現在 $x$ 和 $t$ 完全分離。

Now the $x$ and $t$ dependences are completely separated.

---

## 21. Evaluate the remaining logarithmic integral

先定義

Define

$$ A=\int_{0}^{1}t\ln\left(\frac{1+t}{1-t}\right)dt. $$

使用

Using

$$ \ln(1+t)=t-\frac{t^{2}}{2}+\frac{t^{3}}{3}-\frac{t^{4}}{4}+\cdots, $$

以及

and

$$ \ln(1-t)=-t-\frac{t^{2}}{2}-\frac{t^{3}}{3}-\frac{t^{4}}{4}-\cdots, $$

兩者相減：

Subtracting them,

$$ \ln\left(\frac{1+t}{1-t}\right)=2\left(t+\frac{t^{3}}{3}+\frac{t^{5}}{5}+\cdots\right). $$

可以寫成

This can be written as

$$ \ln\left(\frac{1+t}{1-t}\right)=2\sum_{m=0}^{\infty}\frac{t^{2m+1}}{2m+1}. $$

所以

Thus,

$$ A=2\sum_{m=0}^{\infty}\frac{1}{2m+1}\int_{0}^{1}t^{2m+2}dt. $$

而

and

$$ \int_{0}^{1}t^{2m+2}dt=\frac{1}{2m+3}. $$

因此

Therefore,

$$ A=2\sum_{m=0}^{\infty}\frac{1}{(2m+1)(2m+3)}. $$

利用

Using

$$ \frac{2}{(2m+1)(2m+3)}=\frac{1}{2m+1}-\frac{1}{2m+3}, $$

得到 telescoping series：

we obtain a telescoping series:

$$ A=\sum_{m=0}^{\infty}\left(\frac{1}{2m+1}-\frac{1}{2m+3}\right). $$

展開前幾項：

Writing the first few terms,

$$ A=\left(1-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{5}\right)+\left(\frac{1}{5}-\frac{1}{7}\right)+\cdots. $$

中間項互相抵消，因此

All intermediate terms cancel, so

$$ A=1. $$

---

## 22. Finish the dimensionless integral

因為

Since

$$ \int_{0}^{1}x^{3}dx=\frac{1}{4}, $$

所以

we obtain

$$ \mathcal J=2\left(\frac{1}{4}\right)(1)=\frac{1}{2}. $$

因此

Therefore,

$$ I=8\pi^{2}k_{F}^{4}\left(\frac{1}{2}\right). $$

得到

Hence,

$$ I=4\pi^{2}k_{F}^{4}. $$

---

## 23. Exchange energy per volume

前面有

Previously we obtained

$$ E_{x}=-\frac{\Omega}{16\pi^{5}}I. $$

代入

Substituting

$$ I=4\pi^{2}k_{F}^{4}, $$

得到

we get

$$ E_{x}=-\frac{\Omega}{16\pi^{5}}4\pi^{2}k_{F}^{4}. $$

因此

Therefore,

$$ \frac{E_{x}}{\Omega}=-\frac{k_{F}^{4}}{4\pi^{3}}. $$

這是 uniform electron gas 的 exchange energy density。

This is the exchange energy per volume of the uniform electron gas.

---

## 24. Exchange energy per electron

單電子 exchange energy 定義為

The exchange energy per electron is

$$ \varepsilon_{x}=\frac{E_{x}}{N}. $$

利用

Using

$$ n=\frac{N}{\Omega}, $$

可寫成

we can write

$$ \varepsilon_{x}=\frac{E_{x}/\Omega}{n}. $$

因此

Therefore,

$$ \varepsilon_{x}=-\frac{k_{F}^{4}}{4\pi^{3}}\frac{1}{n}. $$

又因為

Since

$$ n=\frac{k_{F}^{3}}{3\pi^{2}}, $$

所以

we obtain

$$ \varepsilon_{x}=-\frac{k_{F}^{4}}{4\pi^{3}}\frac{3\pi^{2}}{k_{F}^{3}}. $$

得到

Thus,

$$ \varepsilon_{x}=-\frac{3k_{F}}{4\pi}. $$

再代入

Substituting

$$ k_{F}=(3\pi^{2}n)^{1/3}, $$

得到

we obtain

$$ \varepsilon_{x}(n)=-\frac{3}{4\pi}(3\pi^{2}n)^{1/3}. $$

整理後

After simplification,

$$ \varepsilon_{x}(n)=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}n^{1/3}. $$

這就是 uniform electron gas 中每一個 electron 的 exchange energy。

This is the exchange energy per electron of the uniform electron gas.

---

## 25. Exchange energy per volume

每單位體積的 exchange energy 是

The exchange energy per unit volume is

$$ e_{x}(n)=n\varepsilon_{x}(n). $$

因此

Therefore,

$$ e_{x}(n)=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}n^{4/3}. $$

對真正 uniform 的系統，總 exchange energy 就是

For a truly uniform system, the total exchange energy is

$$ E_{x}=N\varepsilon_{x}(n). $$

也可以寫成

or equivalently,

$$ E_{x}=\Omega e_{x}(n). $$

---

## 26. From the uniform electron gas to LDA

真正的材料一般不是 uniform electron gas。

A real material is generally not a uniform electron gas.

電子密度會隨位置改變：

The electron density varies with position:

$$ n=n(\mathbf r). $$

LDA 的想法是：在每一個位置 $\mathbf r$，把附近的一小塊區域近似成一個具有相同 local density $n(\mathbf r)$ 的 uniform electron gas。

The idea of the local-density approximation is to treat a small region around each position $\mathbf r$ as if it were a uniform electron gas with the same local density $n(\mathbf r)$.

因此在每一個位置，可以直接使用 uniform electron gas 的 exchange energy per electron：

Therefore, at each point in space, we use the exchange energy per electron of a uniform electron gas evaluated at the local density:

$$ \varepsilon_{x}(n(\mathbf r))=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}[n(\mathbf r)]^{1/3}. $$

local exchange energy per volume 為

The local exchange energy per volume is

$$ e_{x}(\mathbf r)=n(\mathbf r)\varepsilon_{x}(n(\mathbf r)). $$

所以

Thus,

$$ e_{x}(\mathbf r)=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}[n(\mathbf r)]^{4/3}. $$

最後把每一個位置的 local contribution 積分起來：

Finally, integrate the local contribution over all space:

$$ E_{x}^{\mathrm{LDA}}[n]=\int d^{3}\mathbf r\,n(\mathbf r)\varepsilon_{x}(n(\mathbf r)). $$

因此

Therefore,

$$ E_{x}^{\mathrm{LDA}}[n]=-\frac{3}{4}\left(\frac{3}{\pi}\right)^{1/3}\int d^{3}\mathbf r\,[n(\mathbf r)]^{4/3}. $$

這就是手寫筆記最後得到的 LDA exchange functional。

This is the LDA exchange functional obtained at the end of the handwritten notes.

---

## 27. Logic of the whole derivation

這份推導中每一步的目的可以整理成：

The purpose of each step can be summarized as follows:

1. 使用 plane wave：因為 uniform electron gas 具有 translational symmetry。
2. 使用 periodic boundary condition：讓 momentum states 離散化並建立 $\sum_{\mathbf k}\rightarrow\int d^{3}\mathbf k$ 的關係。
3. 建立 Fermi sphere：因為 $T=0$ 時電子從最低 free-electron energy 開始填滿。
4. 推導 $n$ 與 $k_F$：最後才能把 exchange energy 從 $k_F$ 改寫成 density functional。
5. Fourier transform $1/R$：因為 real-space Coulomb kernel 同時耦合 $\mathbf r$ 和 $\mathbf r'$，momentum space 可以把兩個積分拆開。
6. 使用 spin orthogonality：得到 exchange 只存在於 same-spin electrons。
7. 使用 plane-wave orthogonality：得到 momentum selection condition，讓 exchange matrix element 化成 $1/\lvert\mathbf k-\mathbf k'\rvert^{2}$。
8. 對所有 occupied states 加總：得到整個 Fermi sea 的 exchange energy。
9. 利用 spherical symmetry：把原本的高維積分降成只依賴 scalar $k$ 和 $k'$ 的積分。
10. 使用 $x=k/k_F$ 與 $y=k'/k_F$：把 dimensional dependence 抽出成 $k_F^{4}$，剩下純數值積分。
11. 把 square 分成兩個 triangles：處理 $\lvert x-y\rvert$，並利用 $x\leftrightarrow y$ symmetry。
12. 得到 uniform electron gas 的 $\varepsilon_x(n)$：這是 LDA 的 local reference。
13. 把 $n$ 換成 $n(\mathbf r)$ 並積分全空間：得到 $E_x^{\mathrm{LDA}}[n]$。

In English:

1. Use plane waves because the uniform electron gas has translational symmetry.
2. Use periodic boundary conditions to quantize momentum and establish the sum-to-integral relation.
3. Fill a Fermi sphere because at $T=0$ electrons occupy the lowest free-electron states.
4. Derive the relation between $n$ and $k_F$ so that the final result can be written as a density functional.
5. Fourier transform $1/R$ because the real-space Coulomb kernel couples $\mathbf r$ and $\mathbf r'$, while momentum space separates the two integrals.
6. Use spin orthogonality to show that exchange survives only between equal-spin electrons.
7. Use plane-wave orthogonality to obtain the momentum selection condition and the factor $1/\lvert\mathbf k-\mathbf k'\rvert^{2}$.
8. Sum over all occupied states to obtain the exchange energy of the full Fermi sea.
9. Use spherical symmetry to reduce the high-dimensional integral to scalar integrals over $k$ and $k'$.
10. Introduce $x=k/k_F$ and $y=k'/k_F$ to factor out the dimensional dependence as $k_F^{4}$.
11. Split the unit square into two triangles to handle $\lvert x-y\rvert$ and use the symmetry under $x\leftrightarrow y$.
12. Obtain $\varepsilon_x(n)$ for the uniform electron gas, which serves as the local reference of LDA.
13. Replace $n$ by $n(\mathbf r)$ locally and integrate over all space to obtain $E_x^{\mathrm{LDA}}[n]$.
