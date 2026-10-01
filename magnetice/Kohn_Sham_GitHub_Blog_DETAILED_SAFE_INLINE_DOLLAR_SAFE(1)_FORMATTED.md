# Kohn–Sham equation: detailed derivation from the density variational principle

這份筆記的主線是：Hohenberg–Kohn 定理告訴我們 ground-state energy 可以視為 density functional，而且 ground-state density 使能量最小；但真正 interacting system 的 kinetic-energy functional $T[n]$ 很難直接寫出來。Kohn–Sham 方法因此建立一個 auxiliary non-interacting system，使它具有和真實 interacting system 相同的 ground-state density，再把難處集中到 exchange–correlation functional $E_{xc}[n]$ 中。

The main idea of these notes is that the Hohenberg–Kohn theorems allow the ground-state energy to be treated as a density functional and tell us that the ground-state density minimizes it. However, the kinetic-energy functional $T[n]$ of the interacting system is difficult to write explicitly. The Kohn–Sham method therefore introduces an auxiliary non-interacting system with the same ground-state density as the real interacting system, and collects the remaining unknown physics into the exchange–correlation functional $E_{xc}[n]$.

---

# 1. Start from the density energy functional

對固定 external potential $V(\mathbf r)$，能量泛函寫成

For a fixed external potential $V(\mathbf r)$, the energy functional is

$$ E_V[n]=T[n]+V_{ee}[n]+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r). $$

第二 Hohenberg–Kohn 定理告訴我們，ground-state density 是讓這個 functional 最小的 density。

The second Hohenberg–Kohn theorem tells us that the ground-state density is the density that minimizes this functional.

但是這個 minimization 不是完全自由的，因為總電子數 $N$ 必須固定。

However, this minimization is not completely unconstrained because the total number of electrons $N$ must remain fixed.

---

## 2. Electron-number constraint

總電子數由 density 積分得到：

The total number of electrons is obtained by integrating the density:

$$ \int d^{3}\mathbf r\,n(\mathbf r)=N. $$

如果 density 做一個小變化

If the density changes slightly,

$$ n(\mathbf r)\longrightarrow n(\mathbf r)+\delta n(\mathbf r), $$

那麼 electron number 的變化是

the corresponding change in the electron number is

$$ \delta N=\int d^{3}\mathbf r\,\delta n(\mathbf r). $$

因為電子數固定，

Because the electron number is fixed,

$$ \delta N=0. $$

所以允許的 density variation 必須滿足

Therefore, an allowed density variation must satisfy

$$ \int d^{3}\mathbf r\,\delta n(\mathbf r)=0. $$

也可以寫成 constraint functional：

This can also be written as a constraint functional:

$$ N[n]=\int d^{3}\mathbf r\,n(\mathbf r). $$

而我們要求

and we require

$$ N[n]=N. $$

---

## 3. Why a Lagrange multiplier is introduced

我們想 minimize $E_V[n]$，但同時又要滿足 $N[n]=N$。

We want to minimize $E_V[n]$, but at the same time we must satisfy the constraint $N[n]=N$.

因此引入 Lagrange multiplier $\mu$，定義新的 functional：

Therefore, introduce a Lagrange multiplier $\mu$ and define a new functional:

$$ L[n,\mu]=E_V[n]-\mu\left[\int d^{3}\mathbf r\,n(\mathbf r)-N\right]. $$

這樣 minimization 問題就從「有 constraint 的 minimization」轉成「對 $L$ 做 unconstrained variation」。

This converts the constrained minimization problem into an unconstrained variation of $L$.

ground state 必須滿足

At the ground state,

$$ \delta L=0. $$

---

## 4. Functional variation of $L[n,\mu]$

energy functional 的一階變化可以寫成

The first-order variation of the energy functional can be written as

$$ \delta E_V[n]=\int d^{3}\mathbf r\,\frac{\delta E_V[n]}{\delta n(\mathbf r)}\delta n(\mathbf r). $$

constraint term 的變化是

The variation of the constraint term is

$$ \delta\left[\int d^{3}\mathbf r\,n(\mathbf r)-N\right]=\int d^{3}\mathbf r\,\delta n(\mathbf r). $$

所以

Therefore,

$$ \delta L=\int d^{3}\mathbf r\,\frac{\delta E_V[n]}{\delta n(\mathbf r)}\delta n(\mathbf r)-\mu\int d^{3}\mathbf r\,\delta n(\mathbf r). $$

把兩項合在一起：

Combining the two terms,

$$ \delta L=\int d^{3}\mathbf r\left[\frac{\delta E_V[n]}{\delta n(\mathbf r)}-\mu\right]\delta n(\mathbf r). $$

因為 $\delta n(\mathbf r)$ 可以在各位置獨立改變，而 ground state 要求 $\delta L=0$，所以 integrand 必須為零：

Because $\delta n(\mathbf r)$ can vary independently at each position, while the ground state requires $\delta L=0$, the integrand must vanish:

$$ \frac{\delta E_V[n]}{\delta n(\mathbf r)}=\mu. $$

這就是 density minimization 的 Euler–Lagrange condition。

This is the Euler–Lagrange condition for minimizing the density functional.

---

## 5. Physical meaning of $\mu$

手寫筆記把 $\mu$ 理解成 chemical potential。

The handwritten notes interpret $\mu$ as the chemical potential.

由

From

$$ \frac{\delta E_V[n]}{\delta n(\mathbf r)}=\mu, $$

可以理解成：當系統增加一點電子密度時，能量的變化尺度由 $\mu$ 控制。

This means that when the electron density is changed slightly, the corresponding energy change is controlled by $\mu$.

在固定粒子數變分中，$\mu$ 是用來 enforce electron-number conservation 的 Lagrange multiplier；物理上它也對應加入或移除電子的能量尺度。

In the fixed-particle-number variation, $\mu$ is the Lagrange multiplier that enforces electron-number conservation. Physically, it is also the energy scale associated with adding or removing electrons.

---

## 6. Apply the Euler–Lagrange equation to the interacting functional

原本的 energy functional 是

The original energy functional is

$$ E_V[n]=T[n]+V_{ee}[n]+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r). $$

對 density 做 functional derivative：

Taking the functional derivative with respect to the density,

$$ \frac{\delta E_V[n]}{\delta n(\mathbf r)}=\frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}+V(\mathbf r). $$

因此 Euler–Lagrange equation 是

Therefore, the Euler–Lagrange equation is

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}+V(\mathbf r)=\mu. $$

也可以整理成

It can also be rearranged as

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}=\mu-V(\mathbf r). $$

到這一步看起來 ground-state problem 已經被寫成 density equation，但真正的困難是 $T[n]$ 和 interacting $V_{ee}[n]$ 的 explicit form 不知道。

At this point the ground-state problem has formally been written as an equation for the density, but the real difficulty is that the explicit forms of the interacting kinetic functional $T[n]$ and the electron-electron interaction functional $V_{ee}[n]$ are not known.

這就是為什麼需要 Kohn–Sham construction。

This is why the Kohn–Sham construction is introduced.

---

# 7. Kohn–Sham auxiliary non-interacting system

Kohn–Sham 方法建立一個 auxiliary system。

The Kohn–Sham method constructs an auxiliary system.

手寫筆記列出三個核心條件：

The handwritten notes list three central conditions:

1. 這個 auxiliary system 中的電子彼此不直接 interaction。

2. 系統可以用 single-electron orbitals $\phi_i(\mathbf r)$ 描述。

3. auxiliary system 的 ground-state density 必須和真實 interacting system 的 ground-state density 相同。

In English:

1. The electrons in the auxiliary system do not interact directly with each other.

2. The system can be described by single-electron orbitals $\phi_i(\mathbf r)$.

3. The auxiliary system must reproduce the same ground-state density as the real interacting system.

因此

Therefore,

$$ n_{\mathrm{KS}}(\mathbf r)=n_0(\mathbf r). $$

對 non-interacting orbitals，density 是

For non-interacting orbitals, the density is

$$ n(\mathbf r)=\sum_{i=1}^{N}\phi_i^{\ast}(\mathbf r)\phi_i(\mathbf r). $$

也就是

That is,

$$ n(\mathbf r)=\sum_{i=1}^{N}\lvert\phi_i(\mathbf r)\rvert^{2}. $$

這一步的目的，是用 orbitals 來建立一個可以明確計算的 kinetic energy。

The purpose is to introduce orbitals so that the kinetic energy can be written explicitly.

---

## 8. Kohn–Sham kinetic energy

對 non-interacting Kohn–Sham system，kinetic energy 可以直接由 orbitals 計算。

For the non-interacting Kohn–Sham system, the kinetic energy can be calculated directly from the orbitals.

按照手寫筆記在後面採用的 Rydberg-unit convention，

Using the Rydberg-unit convention adopted later in the handwritten notes,

$$ T_{\mathrm{KS}}[\{\phi_i\}]=\sum_{i=1}^{N}\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\left(-\nabla^{2}\right)\phi_i(\mathbf r). $$

這個 $T_{\mathrm{KS}}$ 是 auxiliary non-interacting system 的 kinetic energy，不等於真實 interacting system 的 $T[n]$。

This $T_{\mathrm{KS}}$ is the kinetic energy of the auxiliary non-interacting system. It is not equal to the kinetic energy $T[n]$ of the real interacting system.

兩者的差別之後會被放進 exchange–correlation functional。

The difference between them will later be included in the exchange–correlation functional.

---

# 9. Rewrite the total energy in Kohn–Sham form

Kohn–Sham energy functional 寫成

The Kohn–Sham energy functional is written as

$$ E[n]=T_{\mathrm{KS}}[n]+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

其中 $E_H[n]$ 是 classical Hartree electrostatic energy，而 $E_{xc}[n]$ 收集剩下沒有被前面幾項描述的部分。

Here, $E_H[n]$ is the classical Hartree electrostatic energy, while $E_{xc}[n]$ collects the remaining parts that are not described by the previous terms.

按照這份筆記使用的 Rydberg units，

Using the Rydberg units of these notes,

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

真實 interacting system 的能量仍然是

The energy of the real interacting system is

$$ E[n]=T[n]+V_{ee}[n]+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r). $$

比較兩個 expression：

Comparing the two expressions,

$$ T[n]+V_{ee}[n]=T_{\mathrm{KS}}[n]+E_H[n]+E_{xc}[n]. $$

所以 exchange–correlation energy 定義為

Therefore, the exchange–correlation energy is defined as

$$ E_{xc}[n]=T[n]-T_{\mathrm{KS}}[n]+V_{ee}[n]-E_H[n]. $$

這個式子很重要，因為它告訴我們 $E_{xc}$ 不只是 exchange 和 correlation 的 interaction energy。

This equation is important because it shows that $E_{xc}$ is not only an interaction correction.

它也包含真實 interacting kinetic energy 和 auxiliary non-interacting kinetic energy 的差：

It also contains the difference between the real interacting kinetic energy and the auxiliary non-interacting kinetic energy:

$$ T[n]-T_{\mathrm{KS}}[n]. $$

同時 interaction 部分包含

At the same time, the interaction correction contains

$$ V_{ee}[n]-E_H[n]. $$

也就是不能被 classical Hartree term 描述的 electron-electron physics。

That is the part of the electron-electron interaction that is not described by the classical Hartree term.

---

# 10. Density Euler equation in Kohn–Sham form

第二 Hohenberg–Kohn theorem 加上 electron-number constraint 給出

The second Hohenberg–Kohn theorem together with the electron-number constraint gives

$$ \frac{\delta E[n]}{\delta n(\mathbf r)}=\mu. $$

代入 Kohn–Sham decomposition：

Substituting the Kohn–Sham decomposition,

$$ \frac{\delta T_{\mathrm{KS}}[n]}{\delta n(\mathbf r)}+V(\mathbf r)+\frac{\delta E_H[n]}{\delta n(\mathbf r)}+\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}=\mu. $$

這裡出現一個問題：

A problem now appears:

$$ \frac{\delta T_{\mathrm{KS}}[n]}{\delta n(\mathbf r)}\;? $$

雖然 formal notation 寫成 $T_{\mathrm{KS}}[n]$，但實際上我們真正知道的是 orbital expression：

Although we write the formal notation $T_{\mathrm{KS}}[n]$, what we actually know explicitly is its orbital expression:

$$ T_{\mathrm{KS}}[\{\phi_i\}]=\sum_{i=1}^{N}\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\left(-\nabla^{2}\right)\phi_i(\mathbf r). $$

因此直接對 density 微分並不方便。

Therefore, directly differentiating it with respect to the density is not convenient.

手寫筆記的解法是：不要直接對 $n$ variation，而是把 energy functional 改寫成 orbital functional，再對 $\phi_i$ variation。

The solution in the handwritten notes is to rewrite the energy as an orbital functional and vary the orbitals $\phi_i$ directly.

---

# 11. Rewrite the energy as an orbital functional

利用

Using

$$ n(\mathbf r)=\sum_i\phi_i^{\ast}(\mathbf r)\phi_i(\mathbf r), $$

energy functional 可以寫成

the energy functional can be written as

$$ E[\{\phi_i\}]=\sum_i\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\left(-\nabla^{2}\right)\phi_i(\mathbf r)+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

按照 Rydberg units，

Using Rydberg units,

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

---

## 12. Why orthonormality constraints are needed

Kohn–Sham orbitals 代表不同的 single-electron states，所以要滿足 orthonormality：

The Kohn–Sham orbitals represent different single-electron states, so they must satisfy orthonormality:

$$ \int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\phi_j(\mathbf r)=\delta_{ij}. $$

因此在 minimize orbital functional 時，除了固定 electron number，也要維持不同 orbitals 的 orthonormality。

Therefore, when minimizing the orbital functional, we must preserve not only the electron number but also the orthonormality of the orbitals.

所以引入一組 Lagrange multipliers $\lambda_{ij}$：

Thus, introduce a set of Lagrange multipliers $\lambda_{ij}$:

$$ L=E[\{\phi_i\}]-\sum_{ij}\lambda_{ij}\left[\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\phi_j(\mathbf r)-\delta_{ij}\right]. $$

ground-state orbitals 必須讓 $L$ stationary：

The ground-state orbitals must make $L$ stationary:

$$ \frac{\delta L}{\delta\phi_i^{\ast}(\mathbf r)}=0. $$

接下來手寫筆記逐項計算每一個 term 的 functional derivative。

The handwritten notes then evaluate the functional derivative of every term separately.

---

# 13. Variation of the kinetic term

Kohn–Sham kinetic energy 是

The Kohn–Sham kinetic energy is

$$ T_{\mathrm{KS}}=\sum_i\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\left(-\nabla^{2}\right)\phi_i(\mathbf r). $$

對 $\phi_i^{\ast}(\mathbf r)$ 做 functional derivative：

Taking the functional derivative with respect to $\phi_i^{\ast}(\mathbf r)$,

$$ \frac{\delta T_{\mathrm{KS}}}{\delta\phi_i^{\ast}(\mathbf r)}=-\nabla^{2}\phi_i(\mathbf r). $$

所以 kinetic term 對 Kohn–Sham equation 的 contribution 就是

Thus, the kinetic contribution to the Kohn–Sham equation is

$$ -\nabla^{2}\phi_i(\mathbf r). $$

---

# 14. Variation of the external-potential term

external energy 是

The external-potential energy is

$$ E_{\mathrm{ext}}=\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r). $$

而 density 是

and the density is

$$ n(\mathbf r)=\sum_j\phi_j^{\ast}(\mathbf r)\phi_j(\mathbf r). $$

因此對 $\phi_i^{\ast}$ 的 variation，

Therefore, under variation with respect to $\phi_i^{\ast}$,

$$ \frac{\delta n(\mathbf r)}{\delta\phi_i^{\ast}(\mathbf r)}=\phi_i(\mathbf r). $$

所以

Thus,

$$ \frac{\delta E_{\mathrm{ext}}}{\delta\phi_i^{\ast}(\mathbf r)}=V(\mathbf r)\phi_i(\mathbf r). $$

這一步就是 chain rule：external energy 先依賴 density，而 density 再依賴 orbital。

This is an application of the chain rule: the external energy depends on the density, and the density depends on the orbital.

---

# 15. Variation of the Hartree energy

按照 Rydberg units，Hartree energy 是

Using Rydberg units, the Hartree energy is

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

對 density 做 variation 時，因為 $n(\mathbf r)n(\mathbf r')$ 裡兩個 density 都會變，所以會得到兩個完全相同的 contribution。

When the density is varied, both density factors in $n(\mathbf r)n(\mathbf r')$ change. Therefore, two identical contributions appear.

可以寫成

The variation can be written as

$$ \delta E_H=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{\delta n(\mathbf r)n(\mathbf r')+n(\mathbf r)\delta n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

交換第二項中的 dummy variables $\mathbf r$ 和 $\mathbf r'$，兩項相同：

After exchanging the dummy variables $\mathbf r$ and $\mathbf r'$ in the second term, the two terms are identical:

$$ \delta E_H=2\int d^{3}\mathbf r\,\delta n(\mathbf r)\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

因此

Therefore,

$$ \frac{\delta E_H[n]}{\delta n(\mathbf r)}=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

定義 Hartree potential：

Define the Hartree potential:

$$ V_H(\mathbf r)=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

所以

Thus,

$$ \frac{\delta E_H[n]}{\delta n(\mathbf r)}=V_H(\mathbf r). $$

再使用 chain rule：

Using the chain rule,

$$ \frac{\delta E_H[n]}{\delta\phi_i^{\ast}(\mathbf r)}=\frac{\delta E_H[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^{\ast}(\mathbf r)}. $$

由

From

$$ \frac{\delta n(\mathbf r)}{\delta\phi_i^{\ast}(\mathbf r)}=\phi_i(\mathbf r), $$

得到

we obtain

$$ \frac{\delta E_H[n]}{\delta\phi_i^{\ast}(\mathbf r)}=V_H(\mathbf r)\phi_i(\mathbf r). $$

---

# 16. Variation of the exchange–correlation energy

定義 exchange–correlation potential：

Define the exchange–correlation potential:

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

使用 chain rule：

Using the chain rule,

$$ \frac{\delta E_{xc}[n]}{\delta\phi_i^{\ast}(\mathbf r)}=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^{\ast}(\mathbf r)}. $$

因此

Therefore,

$$ \frac{\delta E_{xc}[n]}{\delta\phi_i^{\ast}(\mathbf r)}=V_{xc}(\mathbf r)\phi_i(\mathbf r). $$

---

# 17. Variation of the orthonormality constraint

constraint part 是

The constraint term is

$$ -\sum_{ij}\lambda_{ij}\left[\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\phi_j(\mathbf r)-\delta_{ij}\right]. $$

對 $\phi_i^{\ast}(\mathbf r)$ 做 variation：

Varying with respect to $\phi_i^{\ast}(\mathbf r)$,

$$ \frac{\delta}{\delta\phi_i^{\ast}(\mathbf r)}\left[-\sum_j\lambda_{ij}\int d^{3}\mathbf r\,\phi_i^{\ast}(\mathbf r)\phi_j(\mathbf r)\right]=-\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

$\delta_{ij}$ 本身不依賴 orbital，所以它的 variation 是零。

The term $\delta_{ij}$ does not depend on the orbitals, so its variation is zero.

---

# 18. Collect all terms

把 kinetic、external、Hartree、exchange–correlation 和 constraint contributions 全部加起來：

Adding the kinetic, external, Hartree, exchange–correlation, and constraint contributions,

$$ -\nabla^{2}\phi_i(\mathbf r)+V(\mathbf r)\phi_i(\mathbf r)+V_H(\mathbf r)\phi_i(\mathbf r)+V_{xc}(\mathbf r)\phi_i(\mathbf r)-\sum_j\lambda_{ij}\phi_j(\mathbf r)=0. $$

因此

Therefore,

$$ \left[-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

定義 Kohn–Sham single-particle Hamiltonian：

Define the Kohn–Sham single-particle Hamiltonian:

$$ \hat h_{\mathrm{KS}}=-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r). $$

所以

Thus,

$$ \hat h_{\mathrm{KS}}\phi_i=\sum_j\lambda_{ij}\phi_j. $$

---

# 19. Why the right-hand side initially mixes different orbitals

手寫筆記特別指出：在這一步，$\hat h_{\mathrm{KS}}$ 作用在某一個 orbital $\phi_i$ 上，結果不一定只沿著原來的 $\phi_i$。

The handwritten notes emphasize that at this stage, when $\hat h_{\mathrm{KS}}$ acts on one orbital $\phi_i$, the result does not necessarily point only along the original $\phi_i$.

它可以是 occupied orbital space 中不同 orbitals 的線性組合：

It can be a linear combination of different orbitals in the occupied-orbital space:

$$ \hat h_{\mathrm{KS}}\phi_i=\lambda_{i1}\phi_1+\lambda_{i2}\phi_2+\cdots. $$

原因是 orthonormality constraints 是一整組 matrix constraints，而不是每個 orbital 各自只有一個 scalar multiplier。

The reason is that the orthonormality constraints form a matrix of constraints rather than one independent scalar constraint for each orbital.

所以 $\lambda_{ij}$ 一開始是一個 matrix。

Therefore, $\lambda_{ij}$ initially forms a matrix.

---

# 20. Why $\lambda_{ij}$ can be diagonalized

手寫筆記指出 $\lambda$ 是 Hermitian matrix：

The handwritten notes state that $\lambda$ is a Hermitian matrix:

$$ \lambda_{ij}=\lambda_{ji}^{\ast}. $$

例如二維情況可以寫成

For a two-dimensional example,

$$ \lambda=\begin{pmatrix}a&b\cr b^{\ast}&c\end{pmatrix}. $$

任何 Hermitian matrix 都可以用 unitary transformation 對角化。

Any Hermitian matrix can be diagonalized by a unitary transformation.

令

Let

$$ U^{\dagger}U=I. $$

則可以選擇新的 orbital basis，使得

Then we can choose a new orbital basis such that

$$ U^{\dagger}\lambda U=\mathrm{diag}(\varepsilon_1,\varepsilon_2,\ldots). $$

在這個新的 orbital basis 中，

In this new orbital basis,

$$ \lambda_{ij}=\varepsilon_i\delta_{ij}. $$

所以原本的 coupled equation

Therefore, the original coupled equation

$$ \hat h_{\mathrm{KS}}\phi_i=\sum_j\lambda_{ij}\phi_j $$

可以變成 diagonal form：

can be written in diagonal form:

$$ \hat h_{\mathrm{KS}}\phi_i=\varepsilon_i\phi_i. $$

這就是標準 Kohn–Sham equation。

This is the standard Kohn–Sham equation.

---

# 21. Final Kohn–Sham equation

在這份筆記使用的 Rydberg units 中，

In the Rydberg units used in these notes,

$$ \left[-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

同時 density 由 occupied Kohn–Sham orbitals 重建：

At the same time, the density is reconstructed from the occupied Kohn–Sham orbitals:

$$ n(\mathbf r)=\sum_i\lvert\phi_i(\mathbf r)\rvert^{2}. $$

因此 Kohn–Sham 方法不是只解一次 equation，而是需要 self-consistency：orbitals 給出 density，density 決定 $V_H$ 和 $V_{xc}$，新的 potential 再決定新的 orbitals。

Therefore, the Kohn–Sham method is not a one-shot equation. It requires self-consistency: the orbitals give the density, the density determines $V_H$ and $V_{xc}$, and the updated potentials determine new orbitals.

---

# 22. Hartree units and Rydberg units

手寫筆記特別比較 Hartree units 和 Rydberg units，因為 kinetic term、Hartree energy 和 Hartree potential 的係數不同。

The handwritten notes explicitly compare Hartree units and Rydberg units because the coefficients of the kinetic term, Hartree energy, and Hartree potential are different.

## Hartree units

Kinetic operator:

$$ \hat T=-\frac{1}{2}\nabla^{2}. $$

Hartree energy:

$$ E_H[n]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

Hartree potential:

$$ V_H(\mathbf r)=\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

## Rydberg units

Kinetic operator:

$$ \hat T=-\nabla^{2}. $$

Hartree energy:

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

Hartree potential:

$$ V_H(\mathbf r)=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

因此前面推導中出現的 $-\nabla^{2}$ 和 Hartree potential 前面的 factor 2 都來自 Rydberg-unit convention。

Therefore, the $-\nabla^{2}$ kinetic operator and the factor 2 in the Hartree potential used above come from the Rydberg-unit convention.

---

# 23. What is inside $E_{xc}$

前面定義

Previously,

$$ E_{xc}[n]=T[n]-T_{\mathrm{KS}}[n]+V_{ee}[n]-E_H[n]. $$

因此

Therefore,

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

把 $E_{xc}$ 的兩部分分開：

Separating the two parts of $E_{xc}$,

$$ V_{xc}(\mathbf r)=\frac{\delta\left[T[n]-T_{\mathrm{KS}}[n]\right]}{\delta n(\mathbf r)}+\frac{\delta\left[V_{ee}[n]-E_H[n]\right]}{\delta n(\mathbf r)}. $$

手寫筆記把它們記成 kinetic part 和 interaction part：

The handwritten notes label them as a kinetic part and an interaction part:

$$ V_{xc}(\mathbf r)=V_{xc}^{\mathrm{kin}}(\mathbf r)+V_{xc}^{\mathrm{int}}(\mathbf r). $$

其中

where

$$ V_{xc}^{\mathrm{kin}}(\mathbf r)=\frac{\delta\left[T[n]-T_{\mathrm{KS}}[n]\right]}{\delta n(\mathbf r)}, $$

代表真實 interacting kinetic energy 與 auxiliary non-interacting kinetic energy 的差。

represents the difference between the real interacting kinetic energy and the auxiliary non-interacting kinetic energy.

而

and

$$ V_{xc}^{\mathrm{int}}(\mathbf r)=\frac{\delta\left[V_{ee}[n]-E_H[n]\right]}{\delta n(\mathbf r)}, $$

代表 electron-electron interaction 中不能被 classical Hartree term 描述的部分。

represents the part of the electron-electron interaction that is not described by the classical Hartree term.

---

# 24. Why Hartree–Fock appears next in the handwritten notes

手寫筆記接著寫 Hartree–Fock 兩電子例子，是為了把「Hartree direct term」和「exchange term」的物理來源分開看。

The handwritten notes next introduce a two-electron Hartree–Fock example in order to separate the physical origin of the Hartree direct term from the exchange term.

因為電子是 fermions，兩電子 wave function 必須在交換兩個電子時改變 sign。

Because electrons are fermions, a two-electron wave function must change sign when the two electrons are exchanged.

因此使用 antisymmetric two-electron wave function：

Therefore, use an antisymmetric two-electron wave function:

$$ \Phi(1,2)=\frac{1}{\sqrt{2}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

electron-electron interaction operator 是

The electron-electron interaction operator is

$$ \hat V_{ee}=\frac{1}{r_{12}}. $$

其中

where

$$ r_{12}=\lvert\mathbf r_1-\mathbf r_2\rvert. $$

---

# 25. Expectation value of the two-electron interaction

interaction energy 的 expectation value 是

The expectation value of the interaction energy is

$$ \left\langle\Phi\left\vert\hat V_{ee}\right\vert\Phi\right\rangle. $$

代入 antisymmetric wave function：

Substituting the antisymmetric wave function,

$$ \left\langle\Phi\left\vert\hat V_{ee}\right\vert\Phi\right\rangle=\frac{1}{2}\int d^{3}\mathbf r_1d^{3}\mathbf r_2\left[\phi_1^{\ast}(1)\phi_2^{\ast}(2)-\phi_2^{\ast}(1)\phi_1^{\ast}(2)\right]\frac{1}{r_{12}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

把括號展開會得到 direct terms 和 exchange terms。

Expanding the brackets gives direct terms and exchange terms.

利用兩個 direct terms 相同、兩個 exchange terms 也相同，可以整理成

Using the equality of the two direct terms and the equality of the two exchange terms, the result can be written as

$$ \left\langle\Phi\left\vert\hat V_{ee}\right\vert\Phi\right\rangle=\int d^{3}\mathbf r_1d^{3}\mathbf r_2\frac{\lvert\phi_1(1)\rvert^{2}\lvert\phi_2(2)\rvert^{2}}{r_{12}}-\int d^{3}\mathbf r_1d^{3}\mathbf r_2\frac{\phi_1^{\ast}(1)\phi_2^{\ast}(2)\phi_2(1)\phi_1(2)}{r_{12}}. $$

定義

Define

$$ J_{12}=\int d^{3}\mathbf r_1d^{3}\mathbf r_2\frac{\lvert\phi_1(1)\rvert^{2}\lvert\phi_2(2)\rvert^{2}}{r_{12}}, $$

以及

and

$$ K_{12}=\int d^{3}\mathbf r_1d^{3}\mathbf r_2\frac{\phi_1^{\ast}(1)\phi_2^{\ast}(2)\phi_2(1)\phi_1(2)}{r_{12}}. $$

所以

Therefore,

$$ \left\langle\Phi\left\vert\hat V_{ee}\right\vert\Phi\right\rangle=J_{12}-K_{12}. $$

---

## 26. Physical meaning of the direct and exchange terms

第一項 $J_{12}$ 是兩個電子 density 之間的 classical Coulomb repulsion。

The first term $J_{12}$ is the classical Coulomb repulsion between the two electron densities.

這就是手寫筆記中對 Hartree energy 的物理圖像。

This is the physical picture associated with the Hartree energy in the handwritten notes.

第二項 $K_{12}$ 來自 antisymmetric fermionic wave function 的 cross terms。

The second term $K_{12}$ comes from the cross terms generated by the antisymmetric fermionic wave function.

因為 total interaction energy 中它前面帶負號，

Because it appears with a minus sign in the total interaction energy,

$$ J_{12}-K_{12}, $$

所以 exchange contribution 會降低系統能量。

the exchange contribution lowers the system energy.

這就是為什麼手寫筆記接著寫「calculate exchange energy by uniform electron gas: LDA」：下一步要用 uniform electron gas 去得到 exchange energy 的 density dependence。

This is why the handwritten notes next state “calculate exchange energy by uniform electron gas: LDA”: the next step is to use the uniform electron gas to obtain the density dependence of the exchange energy.

---

# 27. Logic of the whole Kohn–Sham derivation

這份筆記的完整推導順序是：

The complete logic of the derivation is:

1. 從 Hohenberg–Kohn energy functional $E_V[n]$ 開始。
2. 因為總電子數固定，所以引入 electron-number constraint。
3. 用 Lagrange multiplier $\mu$ 得到 $\delta E/\delta n=\mu$。
4. 發現 interacting $T[n]$ 的 explicit density functional 很難直接處理。
5. 建立 non-interacting auxiliary Kohn–Sham system。
6. 要求 auxiliary system 和 real system 有相同 ground-state density。
7. 用 single-particle orbitals 寫出 explicit $T_{\mathrm{KS}}$。
8. 把 real-system energy 和 Kohn–Sham decomposition 比較，定義 $E_{xc}$。
9. 發現 $T_{\mathrm{KS}}$ 實際上是 orbital functional，因此改對 orbitals variation。
10. 為了保持 orbitals orthonormal，引入 matrix Lagrange multipliers $\lambda_{ij}$。
11. 分別對 kinetic、external、Hartree、exchange–correlation、orthonormality terms 做 functional derivative。
12. 得到 coupled equation $\hat h_{\mathrm{KS}}\phi_i=\sum_j\lambda_{ij}\phi_j$。
13. 因為 $\lambda$ 是 Hermitian，可以用 unitary transformation diagonalize。
14. 得到標準 Kohn–Sham equation $\hat h_{\mathrm{KS}}\phi_i=\varepsilon_i\phi_i$。
15. 比較 Hartree units 和 Rydberg units，理解前面係數的來源。
16. 再把 $E_{xc}$ 分成 kinetic correction 和 interaction correction。
17. 用 Hartree–Fock 兩電子例子看出 direct Hartree term 與 exchange term 的物理來源。
