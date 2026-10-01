# Plane waves, Bloch theorem, reciprocal lattice, and energy cutoffs

這份筆記的主線是：晶體中的有效勢具有 lattice periodicity，因此 Hamiltonian 具有 lattice translational symmetry。從 translation operator 與 Hamiltonian 對易，可以得到 Bloch theorem；再把 Bloch wave 的 periodic part 用 reciprocal-lattice plane waves 展開，就得到實際 DFT code 中使用的 plane-wave basis。因為 reciprocal vectors 有無限多個，所以最後需要用 kinetic-energy cutoff 截斷 basis。筆記最後再把這個想法延伸到 charge density、`ecutwfc`、`ecutrho`，以及為什麼 pseudopotential 可以降低 plane-wave cutoff。

The main idea of these notes is that the effective potential in a crystal has lattice periodicity, so the Hamiltonian has lattice translational symmetry. From the commutation between the translation operator and the Hamiltonian, we obtain Bloch's theorem. The periodic part of a Bloch wave can then be expanded by reciprocal-lattice plane waves, which gives the plane-wave basis used in practical DFT codes. Because there are infinitely many reciprocal lattice vectors, the basis must be truncated by a kinetic-energy cutoff. The notes finally extend this idea to the charge density, `ecutwfc`, `ecutrho`, and the reason why pseudopotentials can reduce the required plane-wave cutoff.

---

## 1. Start from the Kohn–Sham Hamiltonian in a crystal

手寫筆記從 Kohn–Sham Hamiltonian 開始：

The handwritten notes start from the Kohn–Sham Hamiltonian:

$$ \hat H=-\frac{\hbar^{2}}{2m}\nabla^{2}+V_{\mathrm{eff}}(\mathbf r). $$

在晶體中，原子排列具有 lattice periodicity，所以有效勢也滿足

In a crystal, the atomic arrangement has lattice periodicity, so the effective potential satisfies

$$ V_{\mathrm{eff}}(\mathbf r+\mathbf R)=V_{\mathrm{eff}}(\mathbf r), $$

其中 $\mathbf R$ 是任意 lattice vector。

Here, $\mathbf R$ is any lattice vector.

這代表把位置整體平移一個完整 lattice vector 後，電子看到的 physical environment 不變。

This means that after translating the position by a complete lattice vector, the physical environment seen by the electron does not change.

因此可以預期 Hamiltonian 具有 translational symmetry。

Therefore, we expect the Hamiltonian to have translational symmetry.

---

## 2. Define the lattice translation operator

按照手寫筆記的 convention，定義 translation operator $\hat T_{\mathbf R}$：

Using the convention of the handwritten notes, define the translation operator $\hat T_{\mathbf R}$ by

$$ \hat T_{\mathbf R}\psi(\mathbf r)=\psi(\mathbf r+\mathbf R). $$

也就是說，$\hat T_{\mathbf R}$ 的作用是把 wave function 平移一個 lattice vector $\mathbf R$。

That is, $\hat T_{\mathbf R}$ shifts the wave function by one lattice vector $\mathbf R$.

接下來要比較兩種操作順序：

Next, compare two different operation orders:

第一種：先 translate，再讓 Hamiltonian 作用。

First: translate first, then apply the Hamiltonian.

第二種：先讓 Hamiltonian 作用，再 translate。

Second: apply the Hamiltonian first, then translate.

如果兩種結果完全相同，就代表 $\hat H$ 與 $\hat T_{\mathbf R}$ 對易。

If the two results are identical, then $\hat H$ and $\hat T_{\mathbf R}$ commute.

---

## 3. First translate, then apply the Hamiltonian

先做 translation：

First apply the translation:

$$ \hat T_{\mathbf R}\psi(\mathbf r)=\psi(\mathbf r+\mathbf R). $$

再讓 Hamiltonian 作用：

Then apply the Hamiltonian:

$$ \hat H\hat T_{\mathbf R}\psi(\mathbf r)=\left[-\frac{\hbar^{2}}{2m}\nabla^{2}+V_{\mathrm{eff}}(\mathbf r)\right]\psi(\mathbf r+\mathbf R). $$

所以

Thus,

$$ \hat H\hat T_{\mathbf R}\psi(\mathbf r)=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi(\mathbf r+\mathbf R)+V_{\mathrm{eff}}(\mathbf r)\psi(\mathbf r+\mathbf R). $$

這是第一種操作順序得到的結果。

This is the result from the first operation order.

---

## 4. First apply the Hamiltonian, then translate

先讓 Hamiltonian 作用在原本的 wave function：

First apply the Hamiltonian to the original wave function:

$$ \hat H\psi(\mathbf r)=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi(\mathbf r)+V_{\mathrm{eff}}(\mathbf r)\psi(\mathbf r). $$

接著把整個結果平移 $\mathbf R$：

Then translate the entire result by $\mathbf R$:

$$ \hat T_{\mathbf R}\hat H\psi(\mathbf r)=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi(\mathbf r+\mathbf R)+V_{\mathrm{eff}}(\mathbf r+\mathbf R)\psi(\mathbf r+\mathbf R). $$

利用晶格週期性

Using the lattice periodicity

$$ V_{\mathrm{eff}}(\mathbf r+\mathbf R)=V_{\mathrm{eff}}(\mathbf r), $$

得到

we obtain

$$ \hat T_{\mathbf R}\hat H\psi(\mathbf r)=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi(\mathbf r+\mathbf R)+V_{\mathrm{eff}}(\mathbf r)\psi(\mathbf r+\mathbf R). $$

這和前一節的結果完全相同。

This is exactly the same as the result in the previous section.

因此

Therefore,

$$ \hat H\hat T_{\mathbf R}=\hat T_{\mathbf R}\hat H. $$

也就是

That is,

$$ [\hat H,\hat T_{\mathbf R}]=0. $$

---

## 5. Physical meaning of the commutation relation

這個 commutation relation 的物理意義是：

The physical meaning of this commutation relation is:

如果把電子移動一個完整 lattice vector，系統的物理不會改變。

If an electron is moved by a complete lattice vector, the physics of the system does not change.

因此 Hamiltonian 具有 lattice translational symmetry。

Therefore, the Hamiltonian has lattice translational symmetry.

這一步是後面 Bloch theorem 的核心。

This is the key step leading to Bloch's theorem.

---

# 6. Common eigenstates of the Hamiltonian and translation operator

因為

Because

$$ [\hat H,\hat T_{\mathbf R}]=0, $$

所以 $\hat H$ 和 $\hat T_{\mathbf R}$ 可以選擇共同 eigenstates。

we can choose common eigenstates of $\hat H$ and $\hat T_{\mathbf R}$.

因此可以同時寫成

Thus,

$$ \hat H\psi(\mathbf r)=E\psi(\mathbf r), $$

以及

and

$$ \hat T_{\mathbf R}\psi(\mathbf r)=\lambda_{\mathbf R}\psi(\mathbf r). $$

根據 translation operator 的定義，

From the definition of the translation operator,

$$ \hat T_{\mathbf R}\psi(\mathbf r)=\psi(\mathbf r+\mathbf R). $$

所以

Therefore,

$$ \psi(\mathbf r+\mathbf R)=\lambda_{\mathbf R}\psi(\mathbf r). $$

這表示 wave function 平移一個 lattice vector 之後，最多只差一個 constant factor $\lambda_{\mathbf R}$。

This means that after translation by a lattice vector, the wave function differs only by a constant factor $\lambda_{\mathbf R}$.

---

## 7. Why the translation eigenvalue must be a phase factor

平移一個 lattice vector 不應改變電子出現的 probability density。

Translation by a lattice vector should not change the probability density of finding the electron.

所以

Therefore,

$$ \lvert\psi(\mathbf r+\mathbf R)\rvert^{2}=\lvert\psi(\mathbf r)\rvert^{2}. $$

又因為

Since

$$ \psi(\mathbf r+\mathbf R)=\lambda_{\mathbf R}\psi(\mathbf r), $$

所以

we have

$$ \lvert\lambda_{\mathbf R}\psi(\mathbf r)\rvert^{2}=\lvert\psi(\mathbf r)\rvert^{2}. $$

因此

Therefore,

$$ \lvert\lambda_{\mathbf R}\rvert^{2}=1. $$

所以

Thus,

$$ \lvert\lambda_{\mathbf R}\rvert=1. $$

模長等於 1 的 complex number 可以寫成 pure phase：

A complex number with magnitude 1 can be written as a pure phase:

$$ \lambda_{\mathbf R}=e^{i\theta_{\mathbf R}}. $$

因此

Therefore,

$$ \psi(\mathbf r+\mathbf R)=e^{i\theta_{\mathbf R}}\psi(\mathbf r). $$

也就是說，平移後 wave function 的 probability density 不變，但 phase 可以改變。

That is, the probability density is unchanged by translation, while the phase may change.

---

## 8. Translate once, twice, and many times

為了了解 phase $\theta_{\mathbf R}$ 和 translation distance 的關係，手寫筆記先看一維 lattice vector $a$。

To understand how the phase $\theta_{\mathbf R}$ depends on the translation distance, the handwritten notes first consider a one-dimensional lattice vector $a$.

平移一次：

Translate once:

$$ \hat T_{a}\psi=e^{i\theta_{a}}\psi. $$

平移兩次：

Translate twice:

$$ \hat T_{2a}\psi=e^{i\theta_{2a}}\psi. $$

但是

However,

$$ \hat T_{2a}=\hat T_{a}\hat T_{a}. $$

因此

Therefore,

$$ \hat T_{2a}\psi=\hat T_{a}\left(e^{i\theta_{a}}\psi\right)=e^{i\theta_{a}}\hat T_{a}\psi=e^{i2\theta_{a}}\psi. $$

所以

Thus,

$$ \theta_{2a}=2\theta_{a}. $$

同樣地，平移 $n$ 次後：

Similarly, after translating $n$ times,

$$ \theta_{na}=n\theta_{a}. $$

也就是 phase 和 translation distance 成正比。

Thus, the phase is proportional to the translation distance.

---

## 9. Introduce the wave vector $\mathbf k$

手寫筆記把這個 proportionality constant 記成 wave vector $\mathbf k$。

The handwritten notes denote this proportionality constant by the wave vector $\mathbf k$.

在一維中可以寫成

In one dimension,

$$ \theta_{a}=ka. $$

因此

Therefore,

$$ \theta_{na}=kna. $$

推廣到三維 lattice vector $\mathbf R$：

Generalizing to a three-dimensional lattice vector $\mathbf R$,

$$ \theta_{\mathbf R}=\mathbf k\cdot\mathbf R. $$

所以 translation eigenvalue 是

Therefore, the translation eigenvalue is

$$ \lambda_{\mathbf R}=e^{i\mathbf k\cdot\mathbf R}. $$

因此

Thus,

$$ \psi_{\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{\mathbf k}(\mathbf r). $$

這就是 Bloch theorem 的 translation form。

This is the translation form of Bloch's theorem.

---

# 10. What is $\mathbf k$?

手寫筆記接著問：$\mathbf k$ 到底代表什麼？

The handwritten notes next ask: what does $\mathbf k$ mean?

先看自由電子的一維 plane wave：

Consider a one-dimensional free-electron plane wave:

$$ \psi_{k}(x)=e^{ikx}. $$

momentum operator 是

The momentum operator is

$$ \hat p=-i\hbar\frac{d}{dx}. $$

讓它作用在 plane wave 上：

Applying it to the plane wave,

$$ \hat p e^{ikx}=-i\hbar\frac{d}{dx}e^{ikx}. $$

因為

Since

$$ \frac{d}{dx}e^{ikx}=ik e^{ikx}, $$

所以

we obtain

$$ \hat p e^{ikx}=\hbar k e^{ikx}. $$

因此

Therefore,

$$ p=\hbar k. $$

所以 $k$ 是和 momentum 對應的 wave vector。

Thus, $k$ is the wave vector associated with momentum.

在 crystal 中，Bloch state 的 $\mathbf k$ 也是用來標記 translational phase 的 quantum number。

In a crystal, the $\mathbf k$ of a Bloch state is also the quantum number that labels the translational phase.

---

# 11. Bloch form of the wave function

Bloch theorem 的 translation relation 是

The translation relation of Bloch's theorem is

$$ \psi_{\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{\mathbf k}(\mathbf r). $$

可以把 Bloch wave 改寫成

A Bloch wave can be written as

$$ \psi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{\mathbf k}(\mathbf r). $$

其中 $e^{i\mathbf k\cdot\mathbf r}$ 是 plane-wave phase，而 $u_{\mathbf k}(\mathbf r)$ 是 lattice-periodic function。

Here, $e^{i\mathbf k\cdot\mathbf r}$ is a plane-wave phase and $u_{\mathbf k}(\mathbf r)$ is a lattice-periodic function.

接下來要證明

The next step is to prove

$$ u_{\mathbf k}(\mathbf r+\mathbf R)=u_{\mathbf k}(\mathbf r). $$

---

## 12. Prove that $u_{\mathbf k}(\mathbf r)$ is periodic

由

From

$$ \psi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{\mathbf k}(\mathbf r), $$

可以寫成

we can write

$$ u_{\mathbf k}(\mathbf r)=e^{-i\mathbf k\cdot\mathbf r}\psi_{\mathbf k}(\mathbf r). $$

因此

Therefore,

$$ u_{\mathbf k}(\mathbf r+\mathbf R)=e^{-i\mathbf k\cdot(\mathbf r+\mathbf R)}\psi_{\mathbf k}(\mathbf r+\mathbf R). $$

再利用 Bloch theorem：

Using Bloch's theorem,

$$ \psi_{\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{\mathbf k}(\mathbf r). $$

所以

Therefore,

$$ u_{\mathbf k}(\mathbf r+\mathbf R)=e^{-i\mathbf k\cdot(\mathbf r+\mathbf R)}e^{i\mathbf k\cdot\mathbf R}\psi_{\mathbf k}(\mathbf r). $$

把 phase 合併：

Combining the phases,

$$ u_{\mathbf k}(\mathbf r+\mathbf R)=e^{-i\mathbf k\cdot\mathbf r}\psi_{\mathbf k}(\mathbf r). $$

因此

Thus,

$$ u_{\mathbf k}(\mathbf r+\mathbf R)=u_{\mathbf k}(\mathbf r). $$

所以 $u_{\mathbf k}$ 是 lattice-periodic function。

Therefore, $u_{\mathbf k}$ is a lattice-periodic function.

這一步非常重要，因為 periodic function 可以用 Fourier series 展開。

This step is very important because a periodic function can be expanded in a Fourier series.

---

# 13. One-dimensional Fourier series

先看一維 periodic function：

First consider a one-dimensional periodic function:

$$ u(x+a)=u(x). $$

它可以展開成 Fourier series：

It can be expanded as a Fourier series:

$$ u(x)=\sum_{n=-\infty}^{\infty}c_{n}e^{i\frac{2\pi n}{a}x}. $$

為什麼 basis function $e^{i2\pi nx/a}$ 本身也是 periodic？

Why is the basis function $e^{i2\pi nx/a}$ itself periodic?

因為

Because

$$ e^{i\frac{2\pi n}{a}(x+a)}=e^{i\frac{2\pi n}{a}x}e^{i2\pi n}. $$

而

and

$$ e^{i2\pi n}=1. $$

所以

Thus,

$$ e^{i\frac{2\pi n}{a}(x+a)}=e^{i\frac{2\pi n}{a}x}. $$

這就是 Fourier basis 能夠描述 periodic function 的原因。

This is why Fourier basis functions can describe a periodic function.

---

# 14. Extend the Fourier expansion to three dimensions

在三維中，我們希望用 plane waves

In three dimensions, we want to use plane waves

$$ e^{i\mathbf q\cdot\mathbf r} $$

來展開 periodic function。

to expand the periodic function.

為了讓 basis function 具有 lattice periodicity，必須要求

For the basis function to have lattice periodicity, we require

$$ e^{i\mathbf q\cdot(\mathbf r+\mathbf R)}=e^{i\mathbf q\cdot\mathbf r}. $$

把左邊展開：

Expanding the left-hand side,

$$ e^{i\mathbf q\cdot(\mathbf r+\mathbf R)}=e^{i\mathbf q\cdot\mathbf r}e^{i\mathbf q\cdot\mathbf R}. $$

所以 periodicity 要求

Therefore, periodicity requires

$$ e^{i\mathbf q\cdot\mathbf R}=1. $$

因此

Thus,

$$ \mathbf q\cdot\mathbf R=2\pi n. $$

所有滿足這個條件的 $\mathbf q$ 就是 reciprocal lattice vectors。

All vectors $\mathbf q$ satisfying this condition are reciprocal lattice vectors.

通常記成

They are usually denoted by

$$ \mathbf q=\mathbf G. $$

所以 reciprocal lattice vector 的定義條件是

Thus, the defining condition of a reciprocal lattice vector is

$$ e^{i\mathbf G\cdot\mathbf R}=1. $$

---

# 15. Expand the periodic part $u_{\mathbf k}$ with reciprocal lattice vectors

因為 $u_{\mathbf k}(\mathbf r)$ 是 lattice-periodic function，所以可以展開成

Because $u_{\mathbf k}(\mathbf r)$ is lattice periodic, it can be expanded as

$$ u_{\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{\mathbf k}(\mathbf G)e^{i\mathbf G\cdot\mathbf r}. $$

Fourier coefficient 可以寫成

The Fourier coefficient can be written as

$$ C_{\mathbf k}(\mathbf G)=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,u_{\mathbf k}(\mathbf r)e^{-i\mathbf G\cdot\mathbf r}. $$

這裡 $\Omega$ 可以取一個 periodic cell 的體積。

Here, $\Omega$ can be taken as the volume of one periodic cell.

---

# 16. Plane-wave expansion of the Bloch wave

Bloch wave 是

The Bloch wave is

$$ \psi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{\mathbf k}(\mathbf r). $$

代入 Fourier expansion：

Substituting the Fourier expansion,

$$ \psi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}\sum_{\mathbf G}C_{\mathbf k}(\mathbf G)e^{i\mathbf G\cdot\mathbf r}. $$

所以

Therefore,

$$ \psi_{\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$

這就是 plane-wave basis representation。

This is the plane-wave basis representation.

每一個 basis function 都有 wave vector

Each basis function has wave vector

$$ \mathbf k+\mathbf G. $$

---

## 17. Why a cutoff is necessary

理論上 reciprocal lattice vectors $\mathbf G$ 有無限多個：

In principle, there are infinitely many reciprocal lattice vectors $\mathbf G$:

$$ \mathbf G\rightarrow\text{infinitely many values}. $$

所以完整 Fourier expansion 需要無限多個 plane waves。

Therefore, the complete Fourier expansion requires infinitely many plane waves.

電腦不可能處理無限大的 basis。

A computer cannot handle an infinite basis.

因此實際計算必須設定 cutoff，只保留有限數目的 $\mathbf G$。

Therefore, practical calculations must introduce a cutoff and keep only a finite number of $\mathbf G$ vectors.

在 VASP 中這對應 `ENCUT`。

In VASP this corresponds to `ENCUT`.

在 Quantum ESPRESSO 中這對應 `ecutwfc`。

In Quantum ESPRESSO this corresponds to `ecutwfc`.

---

# 18. Why the cutoff is defined by kinetic energy

手寫筆記不是直接限制 $\mathbf G$ 的數量，而是用 plane-wave kinetic energy 來決定哪些 basis functions 要保留。

The handwritten notes do not directly limit the number of $\mathbf G$ vectors. Instead, they use the plane-wave kinetic energy to decide which basis functions are retained.

normalized plane-wave basis 可以寫成

A normalized plane-wave basis function can be written as

$$ \langle\mathbf r\vert\mathbf k+\mathbf G\rangle=\frac{1}{\sqrt{\Omega}}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$

kinetic-energy operator 是

The kinetic-energy operator is

$$ \hat T=-\frac{\hbar^{2}}{2m}\nabla^{2}. $$

讓它作用在 plane wave 上：

Applying it to the plane wave,

$$ \hat T e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$

所以這個 plane wave 的 kinetic energy 是

Therefore, the kinetic energy of this plane wave is

$$ E_{\mathrm{kin}}(\mathbf k+\mathbf G)=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}. $$

---

## 19. Define the wave-function cutoff

只保留滿足

Keep only plane waves satisfying

$$ \frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\leq E_{\mathrm{cut}}. $$

的 plane waves。

These are the retained plane waves.

如果

If

$$ \frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}>E_{\mathrm{cut}}, $$

那個 $\mathbf G$ 對應的 plane wave 就不放進 basis。

then the plane wave corresponding to that $\mathbf G$ is excluded from the basis.

所以 $E_{\mathrm{cut}}$ 就是 plane-wave basis 的 kinetic-energy cutoff。

Thus, $E_{\mathrm{cut}}$ is the kinetic-energy cutoff of the plane-wave basis.

---

# 20. Shape of the cutoff in reciprocal space

從 cutoff condition

From the cutoff condition

$$ \frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\leq E_{\mathrm{cut}}, $$

可以得到

we obtain

$$ \lvert\mathbf k+\mathbf G\rvert^{2}\leq\frac{2mE_{\mathrm{cut}}}{\hbar^{2}}. $$

所以

Thus,

$$ \lvert\mathbf k+\mathbf G\rvert\leq\sqrt{\frac{2mE_{\mathrm{cut}}}{\hbar^{2}}}. $$

這表示在 reciprocal space 中，保留的 plane waves 落在一個 sphere 裡。

This means that in reciprocal space, the retained plane waves lie inside a sphere.

如果用一個近似的最大 reciprocal magnitude $G_{\mathrm{max}}$ 表示 cutoff radius，可以寫成

If we denote the cutoff radius approximately by a maximum reciprocal magnitude $G_{\mathrm{max}}$,

$$ G_{\mathrm{max}}\approx\sqrt{\frac{2mE_{\mathrm{cut}}}{\hbar^{2}}}. $$

反過來

Conversely,

$$ E_{\mathrm{cut}}\approx\frac{\hbar^{2}G_{\mathrm{max}}^{2}}{2m}. $$

因此提高 $E_{\mathrm{cut}}$ 會增加 $G_{\mathrm{max}}$，也就是保留更多 plane waves。

Therefore, increasing $E_{\mathrm{cut}}$ increases $G_{\mathrm{max}}$, so more plane waves are included.

---

# 21. Why a larger cutoff gives a more complete Fourier expansion

從

From

$$ \psi_{\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}, $$

可以看到 $E_{\mathrm{cut}}$ 越高，就保留越多 $\mathbf G$。

we can see that a larger $E_{\mathrm{cut}}$ retains more $\mathbf G$ vectors.

因此 Fourier series 越完整，wave function 的形狀可以描述得更精細。

Therefore, the Fourier series becomes more complete and can represent finer features of the wave function.

這就是為什麼 plane-wave calculation 要做 cutoff convergence test。

This is why a plane-wave calculation requires a cutoff convergence test.

---

# 22. Relation between wave vector and wavelength

手寫筆記用一維 plane wave 幫助理解 cutoff 的物理圖像：

The handwritten notes use a one-dimensional plane wave to build a physical picture of the cutoff:

$$ \psi(x)=e^{iqx}. $$

如果一個 wavelength 是 $\lambda$，periodicity 要求

If one wavelength is $\lambda$, periodicity requires

$$ \psi(x+\lambda)=\psi(x). $$

所以

Thus,

$$ e^{iq(x+\lambda)}=e^{iqx}. $$

因此

Therefore,

$$ e^{iq\lambda}=1. $$

所以

Thus,

$$ q\lambda=2\pi. $$

得到

Hence,

$$ \lambda=\frac{2\pi}{\lvert q\rvert}. $$

對 plane-wave basis，

For the plane-wave basis,

$$ q=\lvert\mathbf k+\mathbf G\rvert. $$

因此

Therefore,

$$ \lambda=\frac{2\pi}{\lvert\mathbf k+\mathbf G\rvert}. $$

---

## 23. High spatial frequency and low spatial frequency

如果

If

$$ \lvert\mathbf k+\mathbf G\rvert $$

很大，那麼 wavelength 很短：

is large, the wavelength is short:

$$ \lambda\downarrow. $$

這對應 high spatial frequency。

This corresponds to a high spatial frequency.

如果

If

$$ \lvert\mathbf k+\mathbf G\rvert $$

很小，那麼 wavelength 很長：

is small, the wavelength is long:

$$ \lambda\uparrow. $$

這對應 low spatial frequency。

This corresponds to a low spatial frequency.

---

## 24. Why sharp functions need more plane waves

手寫筆記用 Fourier series 的圖像來理解：

The handwritten notes use the Fourier-series picture:

smooth function 的空間變化慢，所以用少數 long-wavelength components 就可以近似。

A smooth function changes slowly in space, so it can be approximated with only a few long-wavelength components.

例如

For example,

$$ f(x)\approx c_{0}+c_{1}\cos(Gx). $$

但是 sharp function 有快速空間變化，需要更多 short-wavelength, high-frequency components。

A sharp function has rapid spatial variation, so it requires more short-wavelength, high-frequency components.

例如要用更多 terms：

For example, more terms are needed:

$$ f(x)\approx c_{0}+c_{1}\cos(Gx)+c_{2}\cos(2Gx)+\cdots. $$

所以 function 越 sharp，需要的 $G_{\mathrm{max}}$ 越大，也就是需要更高的 $E_{\mathrm{cut}}$。

Therefore, the sharper the function, the larger the required $G_{\mathrm{max}}$, and hence the larger the required $E_{\mathrm{cut}}$.

---

# 25. The density also needs a Fourier cutoff

不只 wave function 要做 Fourier expansion，charge density 也需要。

Not only the wave function but also the charge density needs a Fourier expansion.

定義

Define

$$ \rho(\mathbf r)=\psi^{\ast}(\mathbf r)\psi(\mathbf r). $$

wave function 展開成

Expand the wave function as

$$ \psi(\mathbf r)=\sum_{\mathbf G}C_{\mathbf G}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$

它的 complex conjugate 是

Its complex conjugate is

$$ \psi^{\ast}(\mathbf r)=\sum_{\mathbf G'}C_{\mathbf G'}^{\ast}e^{-i(\mathbf k+\mathbf G')\cdot\mathbf r}. $$

相乘得到

Multiplying them,

$$ \rho(\mathbf r)=\sum_{\mathbf G,\mathbf G'}C_{\mathbf G'}^{\ast}C_{\mathbf G}e^{i(\mathbf G-\mathbf G')\cdot\mathbf r}. $$

注意 $\mathbf k$ 在 product 中被消掉。

Notice that $\mathbf k$ cancels in the product.

---

# 26. Define the density reciprocal vector $\mathbf Q$

定義

Define

$$ \mathbf Q=\mathbf G-\mathbf G'. $$

那麼 density 可以寫成

Then the density can be written as

$$ \rho(\mathbf r)=\sum_{\mathbf Q}\rho_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}. $$

其中 Fourier coefficient 可以從所有滿足 $\mathbf G-\mathbf G'=\mathbf Q$ 的 pair 加總得到：

The Fourier coefficient is obtained by summing over all pairs satisfying $\mathbf G-\mathbf G'=\mathbf Q$:

$$ \rho_{\mathbf Q}=\sum_{\mathbf G,\mathbf G'}C_{\mathbf G'}^{\ast}C_{\mathbf G},\qquad\mathbf G-\mathbf G'=\mathbf Q. $$

因為 density 是 lattice-periodic quantity，

Because the density is lattice periodic,

$$ \rho(\mathbf r+\mathbf R)=\rho(\mathbf r). $$

所以它也自然可以用 reciprocal lattice Fourier series 展開。

Therefore, it can naturally be expanded in reciprocal-lattice Fourier components.

---

# 27. Why the density cutoff can be larger than the wave-function cutoff

假設 wave-function basis 中最大的 wave vector magnitude 是

Suppose the largest wave-vector magnitude in the wave-function basis is

$$ k_{\mathrm{max}}. $$

density 來自 wave function 和它的 complex conjugate 的 product。

The density comes from the product of the wave function and its complex conjugate.

在極端情況下，一個 component 可以在 $+k_{\mathrm{max}}$，另一個可以在 $-k_{\mathrm{max}}$。

In the extreme case, one component can be at $+k_{\mathrm{max}}$ and another at $-k_{\mathrm{max}}$.

因此 difference wave vector 最大可以到

Therefore, the largest difference wave vector can be

$$ Q_{\mathrm{max}}=2k_{\mathrm{max}}. $$

這就是為什麼 density Fourier expansion 需要比 wave function 更高的 reciprocal-space cutoff。

This is why the density Fourier expansion requires a larger reciprocal-space cutoff than the wave-function expansion.

---

## 28. Relation between wave-function cutoff and density cutoff

wave-function cutoff 可以寫成

The wave-function cutoff can be written as

$$ E_{\mathrm{cut}}^{\mathrm{wfc}}=\frac{\hbar^{2}k_{\mathrm{max}}^{2}}{2m}. $$

density cutoff 則是

The density cutoff is

$$ E_{\mathrm{cut}}^{\rho}=\frac{\hbar^{2}Q_{\mathrm{max}}^{2}}{2m}. $$

利用

Using

$$ Q_{\mathrm{max}}=2k_{\mathrm{max}}, $$

得到

we obtain

$$ E_{\mathrm{cut}}^{\rho}=\frac{\hbar^{2}(2k_{\mathrm{max}})^{2}}{2m}. $$

因此

Therefore,

$$ E_{\mathrm{cut}}^{\rho}=4\frac{\hbar^{2}k_{\mathrm{max}}^{2}}{2m}. $$

也就是

That is,

$$ E_{\mathrm{cut}}^{\rho}=4E_{\mathrm{cut}}^{\mathrm{wfc}}. $$

這就是手寫筆記中把 Quantum ESPRESSO 的 `ecutrho` 和 `ecutwfc` 連起來的 Fourier-product 圖像。

This is the Fourier-product picture used in the handwritten notes to connect Quantum ESPRESSO `ecutrho` and `ecutwfc`.

---

# 29. Why the all-electron potential is difficult for plane waves

手寫筆記最後回到 nucleus 附近的 potential。

The handwritten notes finally return to the potential near a nucleus.

對 all-electron Coulomb potential，在 nucleus 附近具有類似

For an all-electron Coulomb potential, near the nucleus it behaves like

$$ V(r)\sim-\frac{Ze^{2}}{r}. $$

這個 potential 在 core region 變化非常 sharp。

This potential changes very sharply in the core region.

由前面的 Fourier 圖像可知，sharp spatial features 需要 high spatial frequencies。

From the Fourier picture developed above, sharp spatial features require high spatial frequencies.

所以如果直接描述 all-electron wave function，core region 會需要非常高的 $E_{\mathrm{cut}}$。

Therefore, directly representing an all-electron wave function would require a very large $E_{\mathrm{cut}}$ in the core region.

---

# 30. Curvature of the wave function near a strong potential

手寫筆記也從 Schrödinger equation 來理解這件事：

The handwritten notes also explain this from the Schrödinger equation:

$$ \left[-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\mathbf r)\right]\psi(\mathbf r)=E\psi(\mathbf r). $$

移項：

Rearranging,

$$ -\frac{\hbar^{2}}{2m}\nabla^{2}\psi(\mathbf r)=\left[E-V(\mathbf r)\right]\psi(\mathbf r). $$

因此

Therefore,

$$ \nabla^{2}\psi(\mathbf r)=\frac{2m}{\hbar^{2}}\left[V(\mathbf r)-E\right]\psi(\mathbf r). $$

所以當 nucleus 附近 $\lvert V-E\rvert$ 很大時，wave function 的 curvature 也會很大。

Thus, when $\lvert V-E\rvert$ is large near the nucleus, the curvature of the wave function also becomes large.

wave function 變得很 sharp，就需要更多 high-frequency plane waves 才能描述。

A sharply varying wave function requires more high-frequency plane waves.

這和前面的 Fourier argument 是同一件事。

This is the same physical idea as the Fourier argument above.

---

# 31. Why pseudopotentials and PAW help

為了避免直接描述 nucleus 附近非常 sharp 的 all-electron behavior，實際 plane-wave DFT 通常使用 pseudopotential 或 PAW。

To avoid representing the extremely sharp all-electron behavior near the nucleus directly, practical plane-wave DFT commonly uses pseudopotentials or PAW.

核心想法是讓 nucleus 附近需要直接用 plane waves 表示的 function 變得比較 smooth。

The central idea is to make the function that must be represented by plane waves smoother near the nucleus.

smooth function 需要的 high-frequency Fourier components 較少。

A smoother function requires fewer high-frequency Fourier components.

所以所需的 $E_{\mathrm{cut}}$ 可以降低。

Therefore, the required $E_{\mathrm{cut}}$ can be reduced.

這就是手寫筆記中「all-electron potential 很 sharp，所以 cutoff 很高；使用 pseudopotential 或 PAW 後可以降低 cutoff」的邏輯。

This is the logic in the handwritten notes: an all-electron potential is very sharp and requires a high cutoff, while pseudopotential or PAW treatment makes the problem smoother and allows a lower cutoff.

---

# 32. Fourier components of the potential scatter plane waves

手寫筆記最後再用 potential 的 Fourier expansion 解釋 high-$G$ component 為什麼會產生 high-frequency wave-function component。

The handwritten notes finally use the Fourier expansion of the potential to explain why a high-$G$ potential component produces a high-frequency component in the wave function.

把 potential 寫成

Write the potential as

$$ V(\mathbf r)=\sum_{\mathbf Q}V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}. $$

考慮一個 incoming plane wave

Consider an incoming plane wave

$$ e^{i\mathbf k\cdot\mathbf r}. $$

某一個 potential Fourier component $V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}$ 作用上去：

Apply one potential Fourier component $V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}$:

$$ V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}e^{i\mathbf k\cdot\mathbf r}=V_{\mathbf Q}e^{i(\mathbf k+\mathbf Q)\cdot\mathbf r}. $$

所以 potential 可以把 wave vector $\mathbf k$ scatter 到

Therefore, the potential can scatter a wave vector $\mathbf k$ into

$$ \mathbf k+\mathbf Q. $$

如果 $\mathbf Q$ 很大，就會產生很大的 final wave vector，也就是 high spatial frequency。

If $\mathbf Q$ is large, the final wave vector is large, corresponding to a high spatial frequency.

---

## 33. One-dimensional cosine example

手寫筆記用一維 cosine potential 做例子：

The handwritten notes use a one-dimensional cosine potential as an example:

$$ V(x)=V_{1}\cos(Qx). $$

利用

Using

$$ \cos(Qx)=\frac{1}{2}\left(e^{iQx}+e^{-iQx}\right), $$

所以

we have

$$ V(x)=\frac{V_{1}}{2}e^{iQx}+\frac{V_{1}}{2}e^{-iQx}. $$

讓它作用在 incoming plane wave $e^{ikx}$：

Applying it to an incoming plane wave $e^{ikx}$,

$$ V(x)e^{ikx}=\frac{V_{1}}{2}e^{i(k+Q)x}+\frac{V_{1}}{2}e^{i(k-Q)x}. $$

所以原本的 $k$ component 會被 potential coupling 到

Thus, the original $k$ component is coupled by the potential to

$$ k+Q $$

以及

and

$$ k-Q. $$

如果 $Q$ 很大，就會生成很高 frequency 的 wave-function components。

If $Q$ is large, very high-frequency wave-function components are generated.

因此 sharp potential 含有較大的 high-$Q$ Fourier components，也就需要更大的 plane-wave cutoff。

Therefore, a sharp potential contains larger high-$Q$ Fourier components and requires a larger plane-wave cutoff.

---

# 34. Logic of the whole derivation

這份手寫筆記的完整邏輯可以整理成：

The complete logic of the handwritten notes is:

1. 晶體有效勢滿足 $V_{\mathrm{eff}}(\mathbf r+\mathbf R)=V_{\mathrm{eff}}(\mathbf r)$。
2. 定義 lattice translation operator $\hat T_{\mathbf R}$。
3. 分別計算 $\hat H\hat T_{\mathbf R}\psi$ 和 $\hat T_{\mathbf R}\hat H\psi$。
4. 利用 potential periodicity 得到 $[\hat H,\hat T_{\mathbf R}]=0$。
5. 因為兩個 operators 對易，可以選共同 eigenstates。
6. translation eigenvalue 不改變 probability density，所以其 magnitude 必須等於 1。
7. 因此 translation eigenvalue 是 phase factor $e^{i\mathbf k\cdot\mathbf R}$。
8. 得到 Bloch theorem：$\psi_{\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{\mathbf k}(\mathbf r)$。
9. 用 free-electron plane wave 與 momentum operator 說明 $\mathbf k$ 的 wave-vector 意義。
10. 把 Bloch wave 寫成 $e^{i\mathbf k\cdot\mathbf r}u_{\mathbf k}(\mathbf r)$。
11. 證明 $u_{\mathbf k}$ 是 lattice-periodic function。
12. periodic function 可以用 Fourier series 展開。
13. 三維 periodic plane-wave basis 必須滿足 $e^{i\mathbf G\cdot\mathbf R}=1$，所以 $\mathbf G$ 是 reciprocal lattice vector。
14. 得到 $\psi_{\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}$。
15. 因為 $\mathbf G$ 有無限多個，所以實際計算必須截斷。
16. 用 kinetic energy $\hbar^{2}\lvert\mathbf k+\mathbf G\rvert^{2}/2m$ 定義 plane-wave cutoff。
17. $E_{\mathrm{cut}}$ 越高，保留的 $G_{\mathrm{max}}$ 越大，Fourier expansion 越完整。
18. 大 $\lvert\mathbf k+\mathbf G\rvert$ 對應短 wavelength 和 high spatial frequency。
19. sharp function 需要更多 high-frequency components，所以需要更高 cutoff。
20. density 是 wave function 和 complex conjugate 的 product，所以 Fourier difference vector 可以到 $Q_{\mathrm{max}}=2k_{\mathrm{max}}$。
21. 因此這份筆記得到 $E_{\mathrm{cut}}^{\rho}=4E_{\mathrm{cut}}^{\mathrm{wfc}}$ 的 Fourier-product 關係。
22. nucleus 附近 all-electron potential 很 sharp，wave function curvature 大，所以需要很高 cutoff。
23. pseudopotential 或 PAW 讓 core region 的 plane-wave representation 變 smooth，因此可以降低 cutoff。
24. potential Fourier component $\mathbf Q$ 會把 plane wave $\mathbf k$ scatter 到 $\mathbf k+\mathbf Q$，所以 sharp potential 中的大 $\mathbf Q$ component 會產生 high-frequency wave-function components。
