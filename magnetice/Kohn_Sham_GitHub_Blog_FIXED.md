# Kohn–Sham Equation

本筆記依照手寫內容整理 Kohn–Sham (K–S) 方程的推導。流程是：先從固定電子數下的能量變分開始，再建立與真實系統具有相同基態電子密度的非交互作用輔助系統，最後對 Kohn–Sham 軌域進行變分，得到 Kohn–Sham equation。

This note follows the handwritten derivation of the Kohn–Sham (K–S) equation. We start from energy minimization with a fixed electron number, construct a non-interacting auxiliary system with the same ground-state density as the real system, and finally vary the Kohn–Sham orbitals to obtain the Kohn–Sham equation.

---

## 1. Density functional and electron-number constraint

對固定外部勢 $V(\mathbf r)$，多電子系統的能量寫成電子密度的泛函：

For a fixed external potential $V(\mathbf r)$, the many-electron energy is written as a functional of the electron density:

$$ E_V[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^{3}\mathbf r. $$

基態電子密度需要讓總能量最小，但同時總電子數必須固定：

The ground-state density minimizes the total energy while the total electron number remains fixed:

$$ \int n(\mathbf r)d^{3}\mathbf r=N. $$

若電子密度發生微小變化：

If the electron density changes slightly:

$$ n(\mathbf r)\rightarrow n(\mathbf r)+\delta n(\mathbf r). $$

總電子數不能改變，因此：

The total electron number cannot change, so:

$$ \delta N=\int \delta n(\mathbf r)d^{3}\mathbf r=0. $$

引入 Lagrange multiplier $\mu$，把電子數守恆加入能量泛函：

Introduce a Lagrange multiplier $\mu$ to impose the electron-number constraint:

$$ L[n,\mu]=E_V[n]-\mu\left[\int n(\mathbf r)d^{3}\mathbf r-N\right]. $$

基態需要滿足：

At the ground state:

$$ \frac{\delta L}{\delta n(\mathbf r)}=0. $$

因此：

Therefore:

$$ \frac{\delta E_V[n]}{\delta n(\mathbf r)}=\mu. $$

這是固定電子數下的 Euler–Lagrange 條件。$\mu$ 可以理解為 chemical potential。

This is the Euler–Lagrange condition at fixed electron number. The quantity $\mu$ can be understood as the chemical potential.

由能量泛函：

From the energy functional:

$$ E_V[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^{3}\mathbf r, $$

可得到：

we obtain:

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}+V(\mathbf r)=\mu. $$

因此：

Therefore:

$$ \frac{\delta T[n]}{\delta n(\mathbf r)}+\frac{\delta V_{ee}[n]}{\delta n(\mathbf r)}=\mu-V(\mathbf r). $$

---

## 2. Kohn–Sham auxiliary system

真實多電子系統的能量為：

The energy of the real many-electron system is:

$$ E[n]=T[n]+V_{ee}[n]+\int V(\mathbf r)n(\mathbf r)d^{3}\mathbf r. $$

困難在於真實多電子系統的 $T[n]$ 和 $V_{ee}[n]$ 並不容易直接寫成簡單的電子密度泛函。

The difficulty is that the exact $T[n]$ and $V_{ee}[n]$ of the interacting many-electron system are not easy to write as simple explicit density functionals.

Kohn–Sham theory 建立一個 auxiliary non-interacting system。手寫筆記中的條件是：

Kohn–Sham theory introduces an auxiliary non-interacting system. In the handwritten notes, this auxiliary system satisfies:

1. 電子彼此不直接交互作用。 / The electrons do not directly interact with each other.
2. 系統可以由 single-electron orbitals $\phi_i(\mathbf r)$ 描述。 / The system can be described by single-electron orbitals $\phi_i(\mathbf r)$.
3. 輔助系統和真實系統具有相同的 ground-state density。 / The auxiliary system has the same ground-state density as the real system.

因此電子密度寫成：

Therefore, the electron density is written as:

$$ n(\mathbf r)=\sum_{i=1}^{N}\lvert\phi_i(\mathbf r)\rvert^{2}. $$

在手寫筆記採用的 Rydberg-unit 表示下，非交互作用 Kohn–Sham kinetic energy 為：

Using the Rydberg-unit convention of the handwritten notes, the non-interacting Kohn–Sham kinetic energy is:

$$ T_{KS}[\{\phi_i\}]=\sum_{i=1}^{N}\int d^{3}\mathbf r\,\phi_i^{*}(\mathbf r)(-\nabla^{2})\phi_i(\mathbf r). $$

Kohn–Sham total energy 寫成：

The Kohn–Sham total energy is written as:

$$ E[n]=T_{KS}[n]+\int V(\mathbf r)n(\mathbf r)d^{3}\mathbf r+E_H[n]+E_{xc}[n]. $$

在 Rydberg units 中，Hartree energy 為：

In Rydberg units, the Hartree energy is:

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

比較真實系統與 Kohn–Sham 輔助系統：

Comparing the real system with the Kohn–Sham auxiliary system:

$$ T[n]+V_{ee}[n]=T_{KS}[n]+E_H[n]+E_{xc}[n]. $$

因此 exchange–correlation energy 定義為：

Therefore, the exchange–correlation energy is defined as:

$$ E_{xc}[n]=T[n]-T_{KS}[n]+V_{ee}[n]-E_H[n]. $$

手寫筆記後面也使用 $W[n]$ 表示電子–電子交互作用能，因此可寫成 $W[n]\equiv V_{ee}[n]$。

Later in the handwritten notes, $W[n]$ is also used for the electron–electron interaction energy, so we may write $W[n]\equiv V_{ee}[n]$.

---

## 3. Orbital functional and orthonormality constraint

由 Hohenberg–Kohn 第二定理，在固定電子數下：

From the second Hohenberg–Kohn theorem, at fixed electron number:

$$ \frac{\delta E[n]}{\delta n(\mathbf r)}=\mu. $$

因此：

Therefore:

$$ \frac{\delta T_{KS}[n]}{\delta n(\mathbf r)}+V(\mathbf r)+\frac{\delta E_H[n]}{\delta n(\mathbf r)}+\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}=\mu. $$

但是 $T_{KS}$ 是由 orbitals $\phi_i(\mathbf r)$ 表示，而不是直接由 $n(\mathbf r)$ 表示，因此改成對 orbital functional 做變分。

However, $T_{KS}$ is expressed through the orbitals $\phi_i(\mathbf r)$ rather than directly through $n(\mathbf r)$, so we vary an orbital functional instead.

$$ E[\{\phi_i\}]=\sum_i\int d^{3}\mathbf r\,\phi_i^{*}(\mathbf r)(-\nabla^{2})\phi_i(\mathbf r)+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

電子密度仍由 Kohn–Sham orbitals 給出：

The density is still determined by the Kohn–Sham orbitals:

$$ n(\mathbf r)=\sum_i\lvert\phi_i(\mathbf r)\rvert^{2}. $$

不同 orbitals 需要滿足 orthonormality：

The orbitals must satisfy the orthonormality condition:

$$ \int d^{3}\mathbf r\,\phi_i^{*}(\mathbf r)\phi_j(\mathbf r)=\delta_{ij}. $$

因此引入 Lagrange multipliers $\lambda_{ij}$：

Therefore, introduce Lagrange multipliers $\lambda_{ij}$:

$$ L=E[\{\phi_i\}]-\sum_{ij}\lambda_{ij}\left[\int d^{3}\mathbf r\,\phi_i^{*}(\mathbf r)\phi_j(\mathbf r)-\delta_{ij}\right]. $$

基態軌域需要讓能量最小，因此：

The ground-state orbitals must minimize the energy, so:

$$ \frac{\delta L}{\delta\phi_i^{*}(\mathbf r)}=0. $$

---

## 4. Functional derivative of each term

### 4.1 Non-interacting kinetic energy

Kohn–Sham kinetic term 的變分為：

The variation of the Kohn–Sham kinetic term is:

$$ \frac{\delta T_{KS}}{\delta\phi_i^{*}(\mathbf r)}=-\nabla^{2}\phi_i(\mathbf r). $$

### 4.2 External potential

External-potential energy 為：

The external-potential energy is:

$$ E_{ext}=\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r). $$

因為：

Because:

$$ n(\mathbf r)=\sum_i\phi_i^{*}(\mathbf r)\phi_i(\mathbf r), $$

所以：

we obtain:

$$ \frac{\delta n(\mathbf r)}{\delta\phi_i^{*}(\mathbf r)}=\phi_i(\mathbf r). $$

因此：

Therefore:

$$ \frac{\delta E_{ext}}{\delta\phi_i^{*}(\mathbf r)}=V(\mathbf r)\phi_i(\mathbf r). $$

### 4.3 Hartree energy

在 Rydberg units 中：

In Rydberg units:

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

對密度變分時，因為兩個 density factors 是對稱的，所以會產生 factor 2：

When varying the density, the two symmetric density factors produce a factor of 2:

$$ \frac{\delta E_H[n]}{\delta n(\mathbf r)}=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

定義 Hartree potential：

Define the Hartree potential:

$$ V_H(\mathbf r)=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

使用 chain rule：

Using the chain rule:

$$ \frac{\delta E_H[n]}{\delta\phi_i^{*}(\mathbf r)}=\frac{\delta E_H[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^{*}(\mathbf r)}=V_H(\mathbf r)\phi_i(\mathbf r). $$

### 4.4 Exchange–correlation energy

定義 exchange–correlation potential：

Define the exchange–correlation potential:

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

使用 chain rule：

Using the chain rule:

$$ \frac{\delta E_{xc}[n]}{\delta\phi_i^{*}(\mathbf r)}=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}\frac{\delta n(\mathbf r)}{\delta\phi_i^{*}(\mathbf r)}=V_{xc}(\mathbf r)\phi_i(\mathbf r). $$

### 4.5 Orthonormality constraint

Orthonormality constraint 的變分給出：

The variation of the orthonormality constraint gives:

$$ \frac{\delta}{\delta\phi_i^{*}(\mathbf r)}\left[-\sum_j\lambda_{ij}\int d^{3}\mathbf r\,\phi_i^{*}(\mathbf r)\phi_j(\mathbf r)\right]=-\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

把所有項加起來，並令 $\delta L/\delta\phi_i^{*}=0$：

Adding all terms and imposing $\delta L/\delta\phi_i^{*}=0$:

$$ -\nabla^{2}\phi_i(\mathbf r)+V(\mathbf r)\phi_i(\mathbf r)+V_H(\mathbf r)\phi_i(\mathbf r)+V_{xc}(\mathbf r)\phi_i(\mathbf r)-\sum_j\lambda_{ij}\phi_j(\mathbf r)=0. $$

因此：

Therefore:

$$ \left[-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\sum_j\lambda_{ij}\phi_j(\mathbf r). $$

定義 Kohn–Sham Hamiltonian：

Define the Kohn–Sham Hamiltonian:

$$ \hat h_{KS}=-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r). $$

所以：

Thus:

$$ \hat h_{KS}\phi_i=\sum_j\lambda_{ij}\phi_j. $$

---

## 5. Diagonalization of the Lagrange-multiplier matrix

$\lambda_{ij}$ 是 Hermitian matrix：

$\lambda_{ij}$ is a Hermitian matrix:

$$ \lambda_{ij}=\lambda_{ji}^{*}. $$

因此可以利用 unitary transformation 將它對角化：

Therefore, it can be diagonalized by a unitary transformation:

$$ U^{\dagger}U=I. $$

$$ U^{\dagger}\lambda U=\varepsilon. $$

選擇 diagonal orbital basis 後：

After choosing the diagonal orbital basis:

$$ \lambda_{ij}=\varepsilon_i\delta_{ij}. $$

因此原本彼此耦合的 orbital equations 變成獨立的 single-electron eigenvalue equations：

The originally coupled orbital equations become independent single-electron eigenvalue equations:

$$ \left[-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

這就是 Kohn–Sham equation。

This is the Kohn–Sham equation.

---

## 6. Hartree units and Rydberg units

手寫筆記中特別比較 Hartree units 和 Rydberg units。為避免 GitHub Markdown table 把公式中的絕對值符號誤認成欄位分隔符，這裡不用表格，改成分開列出公式。

The handwritten notes explicitly compare Hartree units and Rydberg units. To avoid GitHub Markdown tables interpreting mathematical absolute-value symbols as table separators, the formulas are listed separately instead of being placed in a table.

### Hartree units

Kinetic operator:

$$ \hat T=-\frac{1}{2}\nabla^{2}. $$

Hartree energy:

$$ E_H[n]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

Hartree potential:

$$ V_H(\mathbf r)=\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

### Rydberg units

Kinetic operator:

$$ \hat T=-\nabla^{2}. $$

Hartree energy:

$$ E_H[n]=\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

Hartree potential:

$$ V_H(\mathbf r)=2\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

因此前面推導中的 $-\nabla^{2}$ 與 Hartree potential 前的 factor 2 都是 Rydberg-unit convention。

Therefore, the $-\nabla^{2}$ kinetic operator and the factor 2 in the Hartree potential used above follow the Rydberg-unit convention.

---

## 7. Physical meaning of the exchange–correlation term

Exchange–correlation energy 定義為：

The exchange–correlation energy is defined as:

$$ E_{xc}[n]=T[n]-T_{KS}[n]+W[n]-E_H[n]. $$

其中 $W[n]\equiv V_{ee}[n]$。

Here, $W[n]\equiv V_{ee}[n]$.

因此：

Therefore:

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}[n]}{\delta n(\mathbf r)}. $$

依照手寫筆記，可把它理解成 kinetic contribution 和 interaction contribution：

Following the handwritten notes, it can be understood as a kinetic contribution and an interaction contribution:

$$ V_{xc}=V_{xc}^{\mathrm{kin}}+V_{xc}^{\mathrm{int}}. $$

Kinetic contribution：

Kinetic contribution:

$$ V_{xc}^{\mathrm{kin}}=\frac{\delta\left(T[n]-T_{KS}[n]\right)}{\delta n}. $$

它代表真實 interacting system 和 Kohn–Sham auxiliary system 之間的 kinetic-energy difference。

It represents the kinetic-energy difference between the real interacting system and the Kohn–Sham auxiliary system.

Interaction contribution：

Interaction contribution:

$$ V_{xc}^{\mathrm{int}}=\frac{\delta\left(W[n]-E_H[n]\right)}{\delta n}. $$

它代表普通 Hartree mean-field 無法描述的 electron–electron exchange and correlation effects。

It represents the electron–electron exchange and correlation effects that are not described by the ordinary Hartree mean field.

---

## 8. Two-electron Hartree–Fock picture

對兩個 fermions，總波函數需要具有交換反對稱性：

For two fermions, the total wave function must be antisymmetric under particle exchange:

$$ \Phi(1,2)=\frac{1}{\sqrt{2}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

兩電子 Coulomb interaction 為：

The Coulomb interaction between the two electrons is:

$$ \hat V_{ee}=\frac{1}{r_{12}}. $$

因此 interaction energy expectation value 為：

Therefore, the expectation value of the interaction energy is:

$$ \langle\Phi\lvert\hat V_{ee}\rvert\Phi\rangle=\frac{1}{2}\int d\mathbf r_1d\mathbf r_2\left[\phi_1^{*}(1)\phi_2^{*}(2)-\phi_2^{*}(1)\phi_1^{*}(2)\right]\frac{1}{r_{12}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

展開後可以分成 direct Coulomb term 和 exchange term：

After expansion, it separates into a direct Coulomb term and an exchange term:

$$ \langle\Phi\lvert\hat V_{ee}\rvert\Phi\rangle=\int d\mathbf r_1d\mathbf r_2\frac{\lvert\phi_1(1)\rvert^{2}\lvert\phi_2(2)\rvert^{2}}{r_{12}}-\int d\mathbf r_1d\mathbf r_2\,\phi_1^{*}(1)\phi_2(1)\frac{1}{r_{12}}\phi_2^{*}(2)\phi_1(2). $$

簡寫為：

This can be written as:

$$ \langle\Phi\lvert\hat V_{ee}\rvert\Phi\rangle=J_{12}-K_{12}. $$

其中 $J_{12}$ 是 direct Coulomb contribution，對應兩個電子密度之間的 classical Coulomb repulsion；$K_{12}$ 是由 fermionic antisymmetry 產生的 exchange contribution。

Here, $J_{12}$ is the direct Coulomb contribution corresponding to the classical Coulomb repulsion between the two electron densities, while $K_{12}$ is the exchange contribution generated by fermionic antisymmetry.

手寫筆記最後指出，可以利用 uniform electron gas 計算 exchange energy，進一步建立 LDA。

Finally, the handwritten notes point toward calculating the exchange energy using the uniform electron gas, which leads to LDA.

$$ \text{uniform electron gas}\rightarrow E_x[n]\rightarrow\text{LDA}. $$

---

## 9. Final Kohn–Sham equation

整個推導最後得到：

The derivation finally gives:

$$ \left[-\nabla^{2}+V(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

電子密度由 occupied Kohn–Sham orbitals 給出：

The electron density is obtained from the occupied Kohn–Sham orbitals:

$$ n(\mathbf r)=\sum_{i\in\mathrm{occ}}\lvert\phi_i(\mathbf r)\rvert^{2}. $$

Kohn–Sham DFT 的核心概念是：使用一組 non-interacting single-electron orbitals，重現真實 interacting many-electron system 的 ground-state electron density，而複雜的 many-body effects 被集中到 $E_{xc}[n]$ 或 $V_{xc}(\mathbf r)$ 中。

The central idea of Kohn–Sham DFT is to use a set of non-interacting single-electron orbitals to reproduce the ground-state electron density of the real interacting many-electron system, while the complicated many-body effects are collected into $E_{xc}[n]$ or $V_{xc}(\mathbf r)$.
