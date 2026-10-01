# Kohn–Sham Equation

本筆記整理 Kohn–Sham (K–S) 方程的基本想法：先從 Hohenberg–Kohn 第二定理的變分條件出發，再建立一個與真實系統具有相同基態電子密度的非交互作用輔助系統，最後對單電子軌域進行變分，得到 Kohn–Sham 方程。

This note summarizes the basic idea of the Kohn–Sham (K–S) equation. We start from the variational condition of the second Hohenberg–Kohn theorem, construct an auxiliary non-interacting system with the same ground-state electron density as the real system, and finally perform the variation with respect to the single-electron orbitals.

---

## 1. Density functional and the electron-number constraint

對固定外部勢 $V(\mathbf r)$，多電子系統的能量可以寫成電子密度的泛函：

For a fixed external potential $V(\mathbf r)$, the many-electron energy can be written as a functional of the electron density:

$$ E_V[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^3\mathbf r. $$

基態能量對應於在固定電子數條件下，使 $E_V[n]$ 最小的電子密度。

The ground state corresponds to the electron density that minimizes $E_V[n]$ while keeping the total electron number fixed.

$$ \int n(\mathbf r)d^3\mathbf r=N. $$

若電子密度發生微小變化

If the density changes slightly,

$$ n(\mathbf r)\rightarrow n(\mathbf r)+\delta n(\mathbf r), $$

因為總電子數不能改變，所以

because the total number of electrons must remain unchanged,

$$ \delta N=\int \delta n(\mathbf r)d^3\mathbf r=0. $$

因此需要在能量最小化中加入電子數守恆的限制條件。引入 Lagrange multiplier $\mu$：

Therefore, the electron-number constraint must be included in the minimization. We introduce a Lagrange multiplier $\mu$:

$$ L[n,\mu]=E_V[n]-\mu\left[\int n(\mathbf r)d^3\mathbf r-N\right]. $$

在基態，對電子密度的變分必須為零：

At the ground state, the variation with respect to the density must vanish:

$$ \frac{\delta L}{\delta n(\mathbf r)}=0. $$

因此

Therefore,

$$ \frac{\delta E_V[n]}{\delta n(\mathbf r)}=\mu. $$

這就是 Euler–Lagrange 條件。$\mu$ 在物理上可以理解為 chemical potential：在電子數發生微小改變時，系統能量的變化率。

This is the Euler–Lagrange condition. Physically, $\mu$ can be understood as the chemical potential: the change of the system energy when the electron number changes slightly.

由

From

$$ E_V[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^3\mathbf r, $$

可以得到

we obtain

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}+V(\mathbf r)=\mu. $$

因此

Therefore,

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}=\mu-V(\mathbf r). $$

---

## 2. Why introduce the Kohn–Sham auxiliary system?

真實多電子系統的能量可以寫成

The energy of the real many-electron system can be written as

$$ E[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^3\mathbf r. $$

困難在於真實的動能 $T[n]$ 與電子–電子交互作用 $V_{ee}[n]$ 並不知道如何精確地寫成電子密度 $n(\mathbf r)$ 的簡單泛函。

The difficulty is that the exact kinetic energy $T[n]$ and electron–electron interaction $V_{ee}[n]$ are not known as simple explicit functionals of the density $n(\mathbf r)$.

Kohn–Sham theory 因此建立一個輔助的非交互作用系統。這個系統需要滿足：

Kohn–Sham theory therefore introduces an auxiliary non-interacting system. The auxiliary system is required to satisfy:

1. 電子彼此不直接交互作用。 / The electrons do not directly interact with each other.
2. 系統可以由單電子軌域 $\phi_i(\mathbf r)$ 描述。 / The system can be described by single-electron orbitals $\phi_i(\mathbf r)$.
3. 輔助系統和真實系統具有相同的基態電子密度。 / The auxiliary system has the same ground-state density as the real system.

$$ n(\mathbf r)=n_0(\mathbf r). $$

對非交互作用系統，電子密度為

For the non-interacting system, the electron density is

$$ n(\mathbf r)=\sum_{i=1}^{N}|\phi_i(\mathbf r)|^2. $$

非交互作用電子的 Kohn–Sham 動能寫成

The Kohn–Sham kinetic energy of the non-interacting electrons is written as

$$ T_{KS}[\{\phi_i\}]=\sum_{i=1}^{N}\int d^3\mathbf r\,\phi_i^*(\mathbf r)(-\nabla^2)\phi_i(\mathbf r). $$

上式對應筆記中採用的 Rydberg-unit 形式；Hartree units 與 Rydberg units 的差別會在後面列出。

The expression above follows the Rydberg-unit form used in the handwritten notes. The difference between Hartree and Rydberg units is listed later.

Kohn–Sham 系統的總能量可以寫成

The total energy in Kohn–Sham theory can be written as

$$ E[n]=T_{KS}[n]+\int V(\mathbf r)n(\mathbf r)d^3\mathbf r+E_H[n]+E_{xc}[n]. $$

在筆記使用的 Rydberg-unit 表示法中，Hartree energy 寫成

In the Rydberg-unit convention used in the notes, the Hartree energy is written as

$$ E_H[n]=\int d^3\mathbf r\int d^3\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{|\mathbf r-\mathbf r'|}. $$

將 Kohn–Sham 能量和真實系統能量比較：

Comparing the Kohn–Sham energy with the real-system energy,

$$ T[n]+V_{ee}[n]=T_{KS}[n]+E_H[n]+E_{xc}[n]. $$

因此 exchange–correlation energy 定義為

Therefore, the exchange–correlation energy is defined as

$$ E_{xc}[n]=T[n]-T_{KS}[n]+V_{ee}[n]-E_H[n]. $$

其中包含兩類 Kohn–Sham 簡化系統沒有精確描述的物理：真實系統和輔助系統之間的動能差，以及 Hartree 項不能描述的電子–電子交換與關聯效應。

It contains two kinds of physics that are not described exactly by the simple Kohn–Sham auxiliary system: the kinetic-energy difference between the real and auxiliary systems, and the exchange–correlation part of the electron–electron interaction that is not described by the Hartree term.

---

## 3. Variational condition in Kohn–Sham theory

由 Hohenberg–Kohn 第二定理，在固定電子數下：

From the second Hohenberg–Kohn theorem, with fixed electron number,

$$ \frac{\delta E[n]}{\delta n(\mathbf r)}=\mu. $$

因此

Therefore,

$$ \frac{\delta T_{KS}[n]}{\delta n(\mathbf r)}+V(\mathbf r)+\frac{\delta E_H[n]}{\delta n(\mathbf r)}+\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}=\mu. $$

問題是 $T_{KS}$ 並不是直接用 $n(\mathbf r)$ 表示，而是由軌域 $\phi_i(\mathbf r)$ 表示，所以直接計算 $\delta T_{KS}/\delta n$ 並不方便。

The problem is that $T_{KS}$ is not written directly in terms of $n(\mathbf r)$; it is written in terms of the orbitals $\phi_i(\mathbf r)$. Therefore, directly evaluating $\delta T_{KS}/\delta n$ is inconvenient.

因此改成對 orbital energy functional 進行變分：

Therefore, we perform the variation using an orbital energy functional:

$$ E[\{\phi_i\}]=\sum_i\int d^3\mathbf r\,\phi_i^*(\mathbf r)(-\nabla^2)\phi_i(\mathbf r)+\int d^3\mathbf r\,V(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

電子密度仍然由軌域給出：

The density is still determined by the orbitals:

$$ n(\mathbf r)=\sum_i|\phi_i(\mathbf r)|^2. $$

不同的單電子軌域需要滿足正交歸一條件：

The single-electron orbitals must satisfy the orthonormality condition:

$$ \int d^3\mathbf r\,\phi_i^*(\mathbf r)\phi_j(\mathbf r)=\delta_{ij}. $$

因此再次引入 Lagrange multipliers $\lambda_{ij}$：

We therefore introduce Lagrange multipliers $\lambda_{ij}$:

$$ L=E[\{\phi_i\}]-\sum_{ij}\lambda_{ij}\left[\int d^3\mathbf r\,\phi_i^*(\mathbf r)\phi_j(\mathbf r)-\delta_{ij}\right]. $$

基態軌域需要讓能量最小，因此

The ground-state orbitals must minimize the energy, so

$$ \frac{\delta L}{\delta\phi_i^*(\mathbf r)}=0. $$

---

## 4. Functional derivative of each term

### (1) Non-interacting kinetic energy

對 Kohn–Sham 動能做變分：

For the Kohn–Sham kinetic energy,

$$ \frac{\delta T_{KS}}{\delta\phi_i^*(\mathbf r)}=-\nabla^2\phi_i(\mathbf r). $$

### (2) External potential

外部勢能為

The external-potential energy is

$$ E_{ext}=\int d^3\mathbf r\,V(\mathbf r)n(\mathbf r). $$

因為

Because

$$ n(\mathbf r)=\sum_i\phi_i^*(\mathbf r)\phi_i(\mathbf r), $$

所以

we obtain

$$ \frac{\delta n(\mathbf r)}{\delta\phi_i^*(\mathbf r)}=\phi_i(\mathbf r), $$

進而得到

and therefore

$$ \frac{\delta E_{ext}}{\delta\phi_i^*(\mathbf r)}=V(\mathbf r)\phi_i(\mathbf r). $$

### (3) Hartree energy

在筆記採用的 Rydberg-unit 表示中：

Using the Rydberg-unit convention of the notes,

$$ E_H[n]=\int d^3\mathbf r\int d^3\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{|\mathbf r-\mathbf r'|}. $$

對密度變分後，兩個對稱項給出

After varying the density, the two symmetric terms give

$$ \frac{\delta E_H[n]}{\delta n(\mathbf r)}=2\int d^3\mathbf r'\frac{n(\mathbf r')}{|\mathbf r-\mathbf r'|}. $$

定義 Hartree potential：

Define the Hartree potential:

$$ V_H(\mathbf r)=2\int d^3\mathbf r'\frac{n(\mathbf r')}{|\mathbf r-\mathbf r'|}. $$

使用 chain rule：

Using the chain rule,

$$ \frac{\delta E_H[n]}{\delta\phi_i^*(\mathbf r)}=\frac{\delta E_H[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^*(\mathbf r)}=V_H(\mathbf r)\phi_i(\mathbf r). $$

### (4) Exchange–correlation energy

定義 exchange–correlation potential：

Define the exchange–correlation potential:

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

使用 chain rule：

Using the chain rule,

$$ \frac{\delta E_{xc}[n]}{\delta\phi_i^*(\mathbf r)}=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^*(\mathbf r)}=V_{xc}(\mathbf r)\phi_i(\mathbf r). $$

### (5) Orthonormality constraint

正交歸一限制項的變分給出

The variation of the orthonormality constraint gives

$$ \frac{\delta}{\delta\phi_i^*(\mathbf r)}\left[-\sum_j\lambda_{ij}\int d^3\mathbf r\,\phi_i^*(\mathbf r)\phi_j(\mathbf r)\right]=-\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

把所有項加起來並令 $\delta L/\delta\phi_i^*=0$：

Adding all terms and imposing $\delta L/\delta\phi_i^*=0$ gives

$$ -\nabla^2\phi_i(\mathbf r)+V(\mathbf r)\phi_i(\mathbf r)+V_H(\mathbf r)\phi_i(\mathbf r)+V_{xc}(\mathbf r)\phi_i(\mathbf r)-\sum_j\lambda_{ij}\phi_j(\mathbf r)=0. $$

因此

Therefore,

$$ \left[-\nabla^2+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

定義 Kohn–Sham Hamiltonian：

Define the Kohn–Sham Hamiltonian:

$$ \hat h_{KS}=-\nabla^2+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r). $$

所以

Thus,

$$ \hat h_{KS}\phi_i=\sum_j\lambda_{ij}\phi_j. $$

---

## 5. Diagonalizing the Lagrange-multiplier matrix

$\lambda_{ij}$ 是 Hermitian matrix：

$\lambda_{ij}$ is a Hermitian matrix:

$$ \lambda_{ij}=\lambda_{ji}^*. $$

因此可以利用 unitary transformation 將它對角化：

Therefore, it can be diagonalized by a unitary transformation:

$$ U^\dagger U=I. $$

$$ U^\dagger\lambda U=\varepsilon. $$

對角化之後

After diagonalization,

$$ \lambda_{ij}=\varepsilon_i\delta_{ij}. $$

所以原本耦合的軌域方程可以改寫成彼此獨立的單電子本徵值方程：

The originally coupled orbital equations can then be rewritten as independent single-electron eigenvalue equations:

$$ \left[-\nabla^2+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

這就是 Kohn–Sham equation。

This is the Kohn–Sham equation.

---

## 6. Hartree units and Rydberg units

手寫筆記中特別比較了 Hartree units 與 Rydberg units。兩種單位下，動能、Hartree energy 與 Hartree potential 的係數不同。

The handwritten notes explicitly compare Hartree units and Rydberg units. The coefficients of the kinetic term, Hartree energy, and Hartree potential are different in the two unit systems.

| Term | Hartree units | Rydberg units |
|---|---|---|
| Kinetic energy | $-\frac{1}{2}\nabla^2$ | $-\nabla^2$ |
| Hartree energy | $\frac{1}{2}\int d^3\mathbf r\int d^3\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{|\mathbf r-\mathbf r'|}$ | $\int d^3\mathbf r\int d^3\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{|\mathbf r-\mathbf r'|}$ |
| Hartree potential | $\int d^3\mathbf r'\frac{n(\mathbf r')}{|\mathbf r-\mathbf r'|}$ | $2\int d^3\mathbf r'\frac{n(\mathbf r')}{|\mathbf r-\mathbf r'|}$ |

因此，前面推導中出現的 $-\nabla^2$ 和 $2\int n(\mathbf r')/|\mathbf r-\mathbf r'|$ 是 Rydberg-unit 表示法。

Therefore, the $-\nabla^2$ kinetic operator and the factor $2$ in the Hartree potential used above correspond to the Rydberg-unit convention.

---

## 7. Physical meaning of the exchange–correlation term

Exchange–correlation energy 定義為

The exchange–correlation energy is defined as

$$ E_{xc}[n]=T[n]-T_{KS}[n]+V_{ee}[n]-E_H[n]. $$

因此

Therefore,

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

可以將它分成兩部分：

It can be separated into two contributions:

$$ V_{xc}=V_{xc}^{kin}+V_{xc}^{int}. $$

其中動能部分為

The kinetic contribution is

$$ V_{xc}^{kin}=\frac{\delta\left(T[n]-T_{KS}[n]\right)}{\delta n}. $$

它代表真實交互作用系統與 Kohn–Sham 非交互作用輔助系統之間的動能差。

It represents the kinetic-energy difference between the real interacting system and the non-interacting Kohn–Sham auxiliary system.

交互作用部分為

The interaction contribution is

$$ V_{xc}^{int}=\frac{\delta\left(V_{ee}[n]-E_H[n]\right)}{\delta n}. $$

它包含 Hartree mean-field 無法描述的電子–電子交換與關聯效應。

It contains the electron–electron exchange and correlation effects that cannot be described by the Hartree mean-field term.

---

## 8. Two-electron Hartree–Fock picture

對兩個 fermions，波函數必須具有交換反對稱性。可以寫成

For two fermions, the wave function must be antisymmetric under particle exchange:

$$ \Phi(1,2)=\frac{1}{\sqrt{2}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

兩電子之間的 Coulomb interaction 為

The Coulomb interaction between the two electrons is

$$ \hat V_{ee}=\frac{1}{r_{12}}. $$

因此交互作用能的期望值為

The expectation value of the interaction energy is

$$ \langle\Phi|\hat V_{ee}|\Phi\rangle=\frac{1}{2}\int d\mathbf r_1d\mathbf r_2\left[\phi_1^*(1)\phi_2^*(2)-\phi_2^*(1)\phi_1^*(2)\right]\frac{1}{r_{12}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

展開後可以分成 direct Coulomb term 與 exchange term：

After expansion, it can be separated into a direct Coulomb term and an exchange term:

$$ \langle\Phi|\hat V_{ee}|\Phi\rangle=\int d\mathbf r_1d\mathbf r_2\frac{|\phi_1(1)|^2|\phi_2(2)|^2}{r_{12}}-\int d\mathbf r_1d\mathbf r_2\,\phi_1^*(1)\phi_2(1)\frac{1}{r_{12}}\phi_2^*(2)\phi_1(2). $$

簡寫為

This can be written as

$$ \langle\Phi|\hat V_{ee}|\Phi\rangle=J_{12}-K_{12}. $$

其中 $J_{12}$ 是兩個電子密度之間的 classical Coulomb repulsion，對應 Hartree contribution；$K_{12}$ 是由 fermionic antisymmetry 產生的 exchange contribution，並降低同自旋電子的交互作用能。

Here, $J_{12}$ is the classical Coulomb repulsion between the two electron densities and corresponds to the Hartree contribution. $K_{12}$ is the exchange contribution generated by fermionic antisymmetry, and it lowers the interaction energy for same-spin electrons.

最後，筆記指出 exchange energy 可以利用 uniform electron gas 近似，進而建立 LDA。

Finally, the notes point toward evaluating the exchange energy using the uniform electron gas, which leads to the LDA approximation.

$$ \text{uniform electron gas}\rightarrow E_x[n]\rightarrow \text{LDA}. $$

---

## 9. Final Kohn–Sham equation

整個推導最後得到

The derivation finally gives

$$ \left[-\nabla^2+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

電子密度由所有 occupied Kohn–Sham orbitals 給出：

The electron density is obtained from the occupied Kohn–Sham orbitals:

$$ n(\mathbf r)=\sum_i^{occ}|\phi_i(\mathbf r)|^2. $$

因此 Kohn–Sham DFT 的核心概念是：用一組非交互作用單電子軌域建立與真實交互作用多電子系統相同的基態電子密度，而真正複雜的 many-body physics 被集中到 $E_{xc}[n]$ 或 $V_{xc}(\mathbf r)$ 中。

Therefore, the central idea of Kohn–Sham DFT is to use a set of non-interacting single-electron orbitals to reproduce the ground-state density of the real interacting many-electron system, while the complicated many-body physics is collected into $E_{xc}[n]$ or $V_{xc}(\mathbf r)$.
