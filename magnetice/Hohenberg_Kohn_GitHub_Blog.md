# Hohenberg–Kohn Theorems

## 1. Density as the basic variable in DFT

DFT 使用電子密度 $n(\mathbf r)$ 來描述系統的基態。

In density functional theory (DFT), the ground state is described using the electron density $n(\mathbf r)$.

電子密度可以寫成

The electron density can be written as

$$
n(\mathbf r)=\left\langle \Psi \left|\sum_i \delta(\mathbf r-\mathbf r_i)\right| \Psi \right\rangle .
$$

對一個含有 $N$ 個電子的系統，也可以寫成

For an $N$-electron system, it can also be written as

$$
n(\mathbf r)
=
N\int
\left|\Psi(\mathbf r,\mathbf r_2,\ldots,\mathbf r_N)\right|^2
\,d^3r_2\cdots d^3r_N .
$$

因此

Therefore,

$$
\int n(\mathbf r)\,d^3r=N,
$$

也就是電子密度對整個空間積分後等於系統中的總電子數。

which means that integrating the electron density over all space gives the total number of electrons.

---

## 2. External potential

外部勢能算符可以寫成

The external-potential operator can be written as

$$
\hat V_{\mathrm{ext}}
=
\sum_i V(\mathbf r_i).
$$

它的期望值為

Its expectation value is

$$
\left\langle \Psi\left|\hat V_{\mathrm{ext}}\right|\Psi\right\rangle
=
\left\langle \Psi\left|
\sum_i V(\mathbf r_i)
\right|\Psi\right\rangle
=
\int V(\mathbf r)n(\mathbf r)\,d^3r.
$$

因此，外部勢能的貢獻可以直接寫成外部勢 $V(\mathbf r)$ 與電子密度 $n(\mathbf r)$ 的積分。

Therefore, the contribution from the external potential can be written directly as an integral of the external potential $V(\mathbf r)$ and the electron density $n(\mathbf r)$.

---

# First Hohenberg–Kohn Theorem

第一 Hohenberg–Kohn 定理指出：基態電子密度 $n_0(\mathbf r)$ 可以唯一決定外部勢 $V(\mathbf r)$，最多只差一個加法常數 $C$。

The first Hohenberg–Kohn theorem states that the ground-state density $n_0(\mathbf r)$ uniquely determines the external potential $V(\mathbf r)$, up to an additive constant $C$.

$$
n_0(\mathbf r)
\Longleftrightarrow
V(\mathbf r)+C.
$$

由於外部勢決定 Hamiltonian，而 Hamiltonian 又決定基態波函數，因此

Since the external potential determines the Hamiltonian, and the Hamiltonian determines the ground-state wave function,

$$
V(\mathbf r)
\rightarrow
\hat H
\rightarrow
\Psi_0
\rightarrow
\text{ground-state physics}.
$$

換句話說，若知道基態電子密度，就能決定基態的所有物理量。

In other words, once the ground-state density is known, all ground-state physical properties are determined.

---

## 3. Proof of the first Hohenberg–Kohn theorem by contradiction

假設存在兩個不同的外部勢 $V(\mathbf r)$ 和 $V'(\mathbf r)$，但是它們產生相同的基態電子密度

Assume that two different external potentials $V(\mathbf r)$ and $V'(\mathbf r)$ produce the same ground-state density

$$
n(\mathbf r)=n'(\mathbf r).
$$

對應的 Hamiltonian 為

The corresponding Hamiltonians are

$$
\hat H
=
\hat T+\hat V_{ee}+\hat V_{\mathrm{ext}},
$$

$$
\hat H'
=
\hat T+\hat V_{ee}+\hat V'_{\mathrm{ext}}.
$$

其中

where

$$
\hat V_{\mathrm{ext}}
=
\sum_i V(\mathbf r_i),
\qquad
\hat V'_{\mathrm{ext}}
=
\sum_i V'(\mathbf r_i).
$$

令 $\Psi$ 與 $\Psi'$ 分別是 $\hat H$ 與 $\hat H'$ 的真實基態，對應能量為 $E$ 與 $E'$。

Let $\Psi$ and $\Psi'$ be the true ground states of $\hat H$ and $\hat H'$, with ground-state energies $E$ and $E'$, respectively.

根據量子力學的變分原理，對 Hamiltonian $\hat H$ 而言，任何不是其真實基態的試探波函數，其能量期望值都高於真實基態能量。因此

According to the quantum-mechanical variational principle, for the Hamiltonian $\hat H$, the expectation value obtained from any trial wave function other than its true ground state must be higher than the true ground-state energy. Therefore,

$$
E
<
\left\langle \Psi'\left|\hat H\right|\Psi'\right\rangle .
$$

因為

Since

$$
\hat H
=
\hat H'
+
\left(\hat V_{\mathrm{ext}}-\hat V'_{\mathrm{ext}}\right),
$$

所以

we obtain

$$
\begin{aligned}
\left\langle \Psi'\left|\hat H\right|\Psi'\right\rangle
&=
\left\langle \Psi'\left|\hat H'\right|\Psi'\right\rangle
+
\left\langle \Psi'\left|
\hat V_{\mathrm{ext}}-\hat V'_{\mathrm{ext}}
\right|\Psi'\right\rangle\\
&=
E'
+
\left\langle \Psi'\left|
\hat V_{\mathrm{ext}}-\hat V'_{\mathrm{ext}}
\right|\Psi'\right\rangle .
\end{aligned}
$$

而

and

$$
\begin{aligned}
\left\langle \Psi'\left|
\hat V_{\mathrm{ext}}-\hat V'_{\mathrm{ext}}
\right|\Psi'\right\rangle
&=
\left\langle \Psi'\left|
\sum_i\left[V(\mathbf r_i)-V'(\mathbf r_i)\right]
\right|\Psi'\right\rangle\\
&=
\int d^3r\,n'(\mathbf r)
\left[V(\mathbf r)-V'(\mathbf r)\right].
\end{aligned}
$$

因為假設 $n'(\mathbf r)=n(\mathbf r)$，所以

Because we assumed $n'(\mathbf r)=n(\mathbf r)$,

$$
E
<
E'
+
\int d^3r\,n(\mathbf r)
\left[V(\mathbf r)-V'(\mathbf r)\right].
\tag{1}
$$

交換兩個系統，以同樣的方法得到

By exchanging the two systems and applying the same argument,

$$
E'
<
E
+
\int d^3r\,n(\mathbf r)
\left[V'(\mathbf r)-V(\mathbf r)\right].
\tag{2}
$$

將式 $(1)$ 與式 $(2)$ 相加

Adding Eqs. $(1)$ and $(2)$ gives

$$
E+E'
<
E'+E.
$$

這是一個矛盾。

This is a contradiction.

因此，兩個真正不同的外部勢不能產生完全相同的基態電子密度。

Therefore, two genuinely different external potentials cannot produce exactly the same ground-state density.

所以基態電子密度 $n_0(\mathbf r)$ 可以決定外部勢 $V(\mathbf r)$，最多只差一個常數。

Thus, the ground-state density $n_0(\mathbf r)$ determines the external potential $V(\mathbf r)$ up to an additive constant.

---

## 4. Why can the potentials differ by a constant?

若

If

$$
V'(\mathbf r)=V(\mathbf r)+C,
$$

則

then

$$
\hat V'_{\mathrm{ext}}
=
\sum_i\left[V(\mathbf r_i)+C\right]
=
\hat V_{\mathrm{ext}}+NC.
$$

因此

Therefore,

$$
\hat H'
=
\hat H+NC.
$$

若

If

$$
\hat H\Psi=E\Psi,
$$

則

then

$$
(\hat H+NC)\Psi
=
(E+NC)\Psi.
$$

也就是說，加上一個常數只會讓整個能量做整體平移，不會改變波函數與電子密度。

This means that adding a constant only shifts the total energy by an overall constant and does not change the wave function or the electron density.

---

## 5. Consequence of the first theorem: ground-state quantities are density functionals

第一 Hohenberg–Kohn 定理給出

The first Hohenberg–Kohn theorem gives

$$
n_0(\mathbf r)
\rightarrow
V(\mathbf r)
\rightarrow
\hat H
\rightarrow
\Psi_0.
$$

因此所有基態物理量都可以寫成電子密度的泛函

Therefore, all ground-state physical quantities can be written as functionals of the electron density,

$$
A=A[n_0].
$$

基態能量為

The ground-state energy is

$$
E_0
=
\left\langle \Psi_0\left|
\hat T+\hat V_{ee}
\right|\Psi_0\right\rangle
+
\int d^3r\,V(\mathbf r)n_0(\mathbf r).
$$

由於 $\Psi_0$ 由 $n_0$ 決定，因此動能與電子－電子交互作用能也可以視為電子密度的泛函：

Since $\Psi_0$ is determined by $n_0$, the kinetic and electron–electron interaction energies can also be regarded as functionals of the density:

$$
E_0
=
T[n_0]
+
V_{ee}[n_0]
+
\int d^3r\,V(\mathbf r)n_0(\mathbf r).
$$

---

# Second Hohenberg–Kohn Theorem

第二 Hohenberg–Kohn 定理指出：對任何允許的試探電子密度 $n(\mathbf r)$，能量泛函都不會低於真實基態密度 $n_0(\mathbf r)$ 所對應的基態能量。

The second Hohenberg–Kohn theorem states that for any allowed trial electron density $n(\mathbf r)$, the energy functional cannot be lower than the ground-state energy obtained from the true ground-state density $n_0(\mathbf r)$.

$$
E_V[n]
\ge
E_V[n_0]
=
E_0.
$$

這可以視為從波函數的量子力學變分原理，轉換成電子密度的變分原理。

This can be viewed as transforming the quantum-mechanical variational principle for wave functions into a variational principle for the electron density.

---

## 6. From the wave-function variational principle to the density variational principle

在量子力學中

In quantum mechanics,

$$
\hat H
=
\hat T+\hat V_{ee}+\hat V_{\mathrm{ext}},
$$

且真實基態滿足

and the true ground state satisfies

$$
\hat H\Psi_0=E_0\Psi_0.
$$

對任何試探波函數 $\Psi$，變分原理給出

For any trial wave function $\Psi$, the variational principle gives

$$
\left\langle \Psi\left|\hat H\right|\Psi\right\rangle
\ge
E_0.
$$

根據第一 Hohenberg–Kohn 定理，可以定義電子密度的能量泛函

Using the first Hohenberg–Kohn theorem, we can define the energy functional of the electron density as

$$
E_V[n]
=
T[n]
+
V_{ee}[n]
+
\int d^3r\,V(\mathbf r)n(\mathbf r).
$$

考慮一個試探電子密度 $n(\mathbf r)$，需要滿足

Consider a trial density $n(\mathbf r)$ satisfying

$$
n(\mathbf r)\ge 0,
$$

以及電子數守恆

and particle-number conservation,

$$
\int d^3r\,n(\mathbf r)=N.
$$

令這個電子密度對應的波函數為 $\Psi[n]$，則

Let the wave function corresponding to this density be $\Psi[n]$. Then

$$
E_V[n]
=
\left\langle \Psi[n]\left|
\hat T+\hat V_{ee}
\right|\Psi[n]\right\rangle
+
\left\langle \Psi[n]\left|
\hat V_{\mathrm{ext}}
\right|\Psi[n]\right\rangle.
$$

由於

Since

$$
\left\langle \Psi[n]\left|
\hat V_{\mathrm{ext}}
\right|\Psi[n]\right\rangle
=
\int d^3r\,V(\mathbf r)n(\mathbf r),
$$

所以

we have

$$
E_V[n]
=
\left\langle \Psi[n]\left|\hat H\right|\Psi[n]\right\rangle.
$$

再使用量子力學的變分原理

Using the quantum-mechanical variational principle again,

$$
\left\langle \Psi[n]\left|\hat H\right|\Psi[n]\right\rangle
\ge
\left\langle \Psi_0\left|\hat H\right|\Psi_0\right\rangle
=
E_0.
$$

因此

Therefore,

$$
E_V[n]
\ge
E_V[n_0]
=
E_0.
$$

也就是：任意試探電子密度所算出的能量，都不會低於真正的基態能量；當 $n(\mathbf r)=n_0(\mathbf r)$ 時，能量取得最小值。

That is, the energy calculated from any trial density cannot be lower than the true ground-state energy. The minimum is reached when $n(\mathbf r)=n_0(\mathbf r)$.

---

## 7. Summary

第一 Hohenberg–Kohn 定理：

First Hohenberg–Kohn theorem:

$$
n_0(\mathbf r)
\Longrightarrow
V(\mathbf r)+C
\Longrightarrow
\hat H
\Longrightarrow
\Psi_0
\Longrightarrow
\text{all ground-state properties}.
$$

第二 Hohenberg–Kohn 定理：

Second Hohenberg–Kohn theorem:

$$
E_V[n]
\ge
E_V[n_0]
=
E_0.
$$

因此，DFT 可以把原本以多體波函數為基本變數的量子力學問題，轉換成以電子密度 $n(\mathbf r)$ 為基本變數的問題。

Therefore, DFT transforms the many-body quantum-mechanical problem, originally formulated in terms of the many-electron wave function, into a problem formulated in terms of the electron density $n(\mathbf r)$.
